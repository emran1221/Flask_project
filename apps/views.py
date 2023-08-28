# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect,flash,session,url_for,Blueprint
from jinja2  import TemplateNotFound
from flask_login import login_user, login_required, current_user, logout_user
from sqlalchemy import func

# App modules
from . import db  # Import the db object from the current package
from .models import Coach, Player ,Exercise,PlayerWorkout, PlayerWorkoutLog,WorkoutRoutine,Match

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime, timedelta


views = Blueprint('views', __name__)



# App main route + generic routing
@views.route('/', defaults={'path': 'index.html'})



@views.route('/',methods=['GET', 'POST'])
def index():
    
    if 'user_id' in session:
        user_type = session.get('user_type')
        if user_type == 'coach':
            return redirect('/pages/coachindex/')  
        elif user_type == 'player':
            player_id = session['user_id']
            player = Player.query.get(player_id)
    
            if player.Position is None or player.Finishing is None or player.Shooting is None or player.Rebounding is None:
                return redirect('/pages/player_form/')  
            ######################player dashboard code
            request.form.get('join_coach')
            if 'join_coach' in request.form:
              coach_code = request.form['coach_code']
              new_coach = Coach.query.filter_by(CoachCode=coach_code).first()

              if new_coach:
                player.CoachCode = coach_code
                db.session.commit()
                flash('Joined coach successfully!')
                return redirect('/') 
              
            if 'mark_day_done' in request.form:
                # Mark today's workouts as done
                if 'user_id' in session:
                    player_id = session['user_id']
                    current_date = date.today()
                    workout_logs = PlayerWorkoutLog.query.filter_by(player_id=player_id, date=current_date).all()
                    for workout_log in workout_logs:
                        workout_log.is_done = True

                    db.session.commit()
                    flash("Today's workouts marked as done!")

            all_my_workouts = PlayerWorkoutLog.query.filter_by(player_id=player_id).all()
            
            # Calculate the next workout day
            today = date.today()  # Get today's date without the time

            # Get the closest upcoming workout date from PlayerWorkoutLog
            closest_workout_date = db.session.query(func.min(PlayerWorkoutLog.date)).filter(PlayerWorkoutLog.date >= today).scalar()

            print(closest_workout_date)
            if closest_workout_date:
                # Calculate the corresponding day for the closest workout date
                next_workout_day = closest_workout_date.strftime('%A')
            else:
                next_workout_day = None


            
            # Get upcoming workouts
            workouts = player.get_upcoming_workouts()
            coach = Coach.query.filter_by(CoachCode=player.CoachCode).first()
            
            # Calculate if workouts are available and completed for today
            # Get the player's workout logs for today
            workout_logs_today = PlayerWorkoutLog.query.filter_by(player_id=player.PlayerID, date=today).all()
            
            workouts_available = any(
                workout_log.date == today for workout_log in workout_logs_today
            ) 
            print("Workouts available:", workouts_available)

            workouts_completed = all(workout_log.is_done for workout_log in workout_logs_today)

            


            return render_template( 'pages/index.html', segment='index', parent='dashboard',player=player, coach=coach,workouts=workouts, day=next_workout_day,workouts_available=workouts_available, workouts_completed=workouts_completed,all_my_workouts=all_my_workouts)
            
        else:
            return "Unauthorized", 401
    return redirect('/accounts/auth-signin/')
  


#dashboard for coach
@views.route('/pages/coachindex/',methods=['GET', 'POST'])
def pages_coach_index():
    if 'user_id' in session:
        coach_id = session.get('user_id')
        coach = Coach.query.get(coach_id)
        enrolled_players = Player.query.filter_by(CoachCode=coach.CoachCode).all()
        return render_template('pages/coachindex.html',segment='index', parent='dashboard', coach=coach, enrolled_players=enrolled_players)
    else:
        flash('Please log in as a coach.')
        return redirect('/accounts/auth-signin/')
        #end coach dashboard code


#player_details_coach
@views.route('/pages/player_details_coach/<int:player_id>',methods=['GET', 'POST'])
def pages_player_details_coach(player_id):
    if 'user_id' in session and session.get('user_type') == 'coach':
        coach_id = session['user_id']
        coach = Coach.query.get(coach_id)
        player = Player.query.get(player_id)
        all_workouts = PlayerWorkoutLog.query.filter_by(player_id=player_id).all()

        if request.method == 'POST':
            feedback_text = request.form.get('feedback')

            # Update the player's feedback field
            player.CoachFeedback = feedback_text
            db.session.commit()
            return redirect('/pages/coachindex/')
        days = ['Monday', 'Wednesday', 'Friday']
        player_workouts = {day: [] for day in days}
        for day in days:
            workouts_for_day = player.get_workouts_for_day(day)
            player_workouts[day] = workouts_for_day

        return render_template('pages/player_details_coach.html',segment='index', parent='dashboard', coach=coach, player=player,player_workouts=player_workouts,all_workouts=all_workouts)

            
    else:
            flash('Please log in as a coach.')
            return redirect('/accounts/auth-signin/')
    
 
# End player_details_code



#edit_player_workouts
@views.route('/pages/edit_player_workouts/<int:player_id>', methods=['GET', 'POST'])
def pages_edit_player_workouts(player_id):
    if 'user_id' in session and session.get('user_type') == 'coach':
        coach_id = session['user_id']
        coach = Coach.query.get(coach_id)
        player = Player.query.get(player_id)
        exercises = Exercise.query.all()  # Fetch exercises from the database

        if request.method == 'POST':
            for field_name, value in request.form.items():
                if field_name.startswith('workout_'):
                    parts = field_name.split('_')
                    workout_id = parts[1]
                    # Extract and process the rest of the form data
                    player_workout = PlayerWorkout.query.get(workout_id)
                    if player_workout:
                        exercise_name = request.form.get("workout_" + workout_id + "_name")
                        sets = request.form.get("workout_" + workout_id + "_sets")
                        reps = request.form.get("workout_" + workout_id + "_reps")
                        tutorial_link = request.form.get(workout_id + '_link')

                        # Update the player workout with the new exercise name, sets, and reps
                        player_workout.exercise_name = exercise_name
                        player_workout.sets = sets
                        player_workout.reps = reps
                        player_workout.tutorial_link = tutorial_link
                        db.session.commit()
            flash('Player workouts updated successfully.')
            return redirect(url_for('views.pages_coach_index'))

        # Get the player's workouts for display
        days = ['Monday', 'Wednesday', 'Friday']
        player_workouts = {day: [] for day in days}
        for day in days:
            workouts_for_day = player.get_workouts_for_day(day)
            player_workouts[day] = workouts_for_day

        return render_template('pages/edit_player_workouts.html', segment='index', parent='dashboard', coach=coach, player=player, player_workouts=player_workouts, exercises=exercises)
    else:
        flash('Please log in as a coach.')
        return redirect('/accounts/auth-signin/')
# End player_details_coade


# Pages
@views.route('/pages/player_form/', methods=['GET', 'POST'])
def pages_player_form():
    if 'user_id' in session and session.get('user_type') == 'player':
        player_id = session['user_id']
        player = Player.query.get(player_id)

        
        if request.method == 'POST':
            existing_workouts = PlayerWorkout.query.filter_by(player_id=player.PlayerID).all()
            all_my_workouts = PlayerWorkoutLog.query.filter_by(player_id=player_id).all()

            if existing_workouts:
            # Delete the existing personalized workout
                for existing_workout in existing_workouts:
                    db.session.delete(existing_workout)   
                    db.session.commit()
                
                for myworkout in all_my_workouts:
                    db.session.delete(myworkout)
                    db.session.commit()
            position = request.form['position']
            finishing = int(request.form['finishing'])
            shooting = int(request.form['shooting'])
            rebounding = int(request.form['rebounding'])

           
            player.Position = position
            player.Finishing = finishing
            player.Shooting = shooting
            player.Rebounding = rebounding
            position = player.Position

            skills = {
                'Finishing': player.Finishing,
                'Shooting': player.Shooting,
                'Rebounding': player.Rebounding
            }
            
            def generate_workout(position, lowest_skill, equal_skills, rebounding_tied_with_highest, skills):
                workout_types = {
                    'Point Guard': ['1', '6', '11'],
                    'Shooting Guard': ['2', '7', '12'],
                    'Small Forward': ['3', '8', '13'],
                    'Power Forward': ['4', '9', '14'],
                    'Center': ['5', '10', '15']
                }
                finishing_skill = skills['Finishing']
                shooting_skill = skills['Shooting']
                
                workout_type = None
                if equal_skills or rebounding_tied_with_highest:
                    # Prioritize Finishing or Shooting for equal skills or tied with Rebounding
                    workout_type = workout_types[position][0]
                else:
                    # Determine the lowest-rated skill and select corresponding workout
                    if 'Finishing' in lowest_skill:
                        workout_type = workout_types[position][0]
                    elif 'Shooting' in lowest_skill:
                        workout_type = workout_types[position][0]
                    elif 'Rebounding' in lowest_skill:
                        if finishing_skill > shooting_skill:
                            workout_type = workout_types[position][2]
                        elif finishing_skill < shooting_skill:
                            workout_type = workout_types[position][1]
                        else:
                            workout_type = workout_types[position][1]###### We can change this based on what is more important shooting or finishing 
                return workout_type
                
            # Determine the highest-rated skill(s) and lowest-rated skill
            highest_rated_skills = [skill for skill, rating in skills.items() if rating == max(skills.values())]
            lowest_rated_skill = min(skills, key=skills.get)

            # Check if all skills are rated equally
            equal_skills = len(set(skills.values())) == 1

            # Check if Rebounding is tied with the highest-rated skill
            rebounding_tied_with_highest = 'Rebounding' in highest_rated_skills

            # Generate the workout using the generate_workout function
            workout = generate_workout(position, [lowest_rated_skill], equal_skills, rebounding_tied_with_highest, skills)

            player.Position = position
            player.Finishing = finishing
            player.Shooting = shooting
            player.Rebounding = rebounding
            player.Workout_code = workout

            db.session.commit()
            workout_routines = WorkoutRoutine.query.filter_by(workout_group=workout).all()

            # Create PlayerWorkout entries for each workout routine
            for workout_routine in workout_routines:
                for exercise in workout_routine.exercises:
                    tutorial_link = exercise.tutorial_link
                    player_workout = PlayerWorkout(
                        player_id=player.PlayerID,
                        workout_routine_id=workout_routine.id,
                        exercise_name=exercise.name,
                        sets=exercise.sets,
                        reps=exercise.reps
                    )
                    db.session.add(player_workout)
            
        
            db.session.commit()
            # Calculate the next Monday from today
            today = date.today()  # Get today's date without the time

            # Calculate the next Monday from today
            days_ahead = (0 - today.weekday()) % 7
            next_monday = today + timedelta(days=days_ahead)

            # Define the mapping from string days to integer days (0=Monday, 1=Tuesday, etc.)
            day_mapping = {
                'Monday': 0,
                'Tuesday': 1,
                'Wednesday': 2,
                'Thursday': 3,
                'Friday': 4,
                'Saturday': 5,
                'Sunday': 6
            }

            # Populate PlayerWorkoutLog for the next 4 weeks
            for _ in range(4):
                for workout_routine in workout_routines:
                    # Calculate the workout date based on the workout day
                    workout_day = workout_routine.day
                    days_until_workout = (day_mapping[workout_day] - next_monday.weekday()) % 7
                    workout_date = next_monday + timedelta(days=days_until_workout)
                    player_workout_log = PlayerWorkoutLog(
                        player_id=player.PlayerID,
                        workout_routine_id=workout_routine.id,
                        date=workout_date,
                        is_done=False  # Workouts are initially not done
                    )
                    db.session.add(player_workout_log)

                # Move to the next week
                next_monday += timedelta(days=7)

            db.session.commit()
            flash('Profile details updated successfully!')

            return redirect('/')
    return render_template('pages/player_form.html', segment='form_elements', player = player)

@views.route('/pages/match_statistics/' , methods=['GET', 'POST'])
def pages_match_statistics():
    if 'user_id' in session:
        player_id = session['user_id']
        player = Player.query.get(player_id)
        if player.Position is None or player.Finishing is None or player.Shooting is None or player.Rebounding is None:
            return redirect('/pages/player_form/')  
        if 'submit_match' in request.form:
               match_number = len(player.matches) + 1
               assists = int(request.form['assists'])
               points = int(request.form['points'])
               rebounds = int(request.form['rebounds'])
               new_match = Match(match_number=match_number, assists=assists, points=points, rebounds=rebounds)
               player.matches.append(new_match)
               db.session.commit()
               return render_template( 'pages/match_statistics.html', segment='match_statistics', parent='form_components',player=player)


    return render_template('pages/match_statistics.html', segment='match_statistics',player=player)



#player profile
@views.route('/pages/profile/')
def pages_profile():
  
    if 'user_id' in session:
        user_type = session.get('user_type')
        if user_type == 'coach':
            return redirect('/pages/coachprofile/')
        elif user_type == 'player':
            player_id = session['user_id']
            player = Player.query.get(player_id)
    
            if player.Position is None or player.Finishing is None or player.Shooting is None or player.Rebounding is None:
                return redirect('/pages/player_form/')  
            coach = Coach.query.filter_by(CoachCode=player.CoachCode).first()
            
            
            return render_template( 'pages/profile.html', segment='profile', parent='dashboard',player=player, coach=coach)
    return redirect('/accounts/auth-signin/')

@views.route('/pages/coachprofile/')
def pages_coach_profile():
    if 'user_id' in session:
        user_type = session.get('user_type')
        coach_id = session['user_id']
        coach = Coach.query.get(coach_id)
        return render_template( 'pages/coachprofile.html', segment='profile', parent='dashboard',coach=coach)
    return redirect('/accounts/auth-signin/')



# add template filter
def replace_value(value, arg):
  return value.replace(arg, ' ').title()
views.add_app_template_filter(replace_value, name='replace_value')
