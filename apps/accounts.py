# Flask modules
from flask   import render_template, request, redirect,flash,session,url_for,Blueprint
from jinja2  import TemplateNotFound
from flask_login import login_user, login_required, current_user, logout_user

# App modules
from . import db  # Import the db object from the current package
from .models import Coach, Player ,Exercise,PlayerWorkout,WorkoutRoutine,Match
import random
import string
from werkzeug.security import generate_password_hash, check_password_hash


accounts = Blueprint('accounts', __name__)

#methods for creating hashed passwords
def generate_coach_code():
    characters = string.ascii_uppercase + string.digits
    code_length = 6
    return ''.join(random.choice(characters) for _ in range(code_length))

def generate_player_code():
    characters = string.ascii_letters + string.digits
    code_length = 8
    return ''.join(random.choice(characters) for _ in range(code_length))


#sign up route
@accounts.route('/auth-signup/',methods=['GET', 'POST'])
def accounts_auth_signup():
  if request.method == 'POST':
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        new_email = request.form['new_email']
        role = request.form['role']

        existing_coach = Coach.query.filter_by(CoachEmail=new_email).first()
        existing_player = Player.query.filter_by(PlayerEmail=new_email).first()

        if existing_coach or existing_player:
            flash('Email already in use. Please choose another.')
        elif new_password != confirm_password:
            flash('Passwords do not match. Please re-enter.')
        else:
            hashed_password = generate_password_hash(new_password)
            if role == 'coach':
                coach_code = generate_coach_code()
                new_coach = Coach(CoachName=new_username, CoachEmail=new_email, CoachCode=coach_code, CoachPasswordHash=hashed_password)
                new_coach.set_password(new_password)
                db.session.add(new_coach)

            elif role == 'player':
                new_player = Player(PlayerName=new_username, PlayerEmail=new_email, CoachCode=None, PlayerPasswordHash=hashed_password)
                new_player.set_password(new_password)
                db.session.add(new_player)
                
            else:
                flash('Invalid role.')
                return redirect('/accounts/auth-signup/')

            
            db.session.commit()

            flash('Signup successful! You can now log in.')
            return redirect('/accounts/auth-signin/')

  return render_template('accounts/auth-signup.html')

#Sign in route
@accounts.route('/auth-signin/', methods=['GET', 'POST'])
def accounts_auth_signin():
    
  if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        coach = Coach.query.filter_by(CoachName=username).first()
        player = Player.query.filter_by(PlayerName=username).first()

        if coach and coach.check_password(password):
            session['user_id'] = coach.CoachID
            session['user_type'] = 'coach'  
            login_user(coach)
            return redirect('/')
        elif player and player.check_password(password):
            session['user_id'] = player.PlayerID
            session['user_type'] = 'player'  
            login_user(player) 
            return redirect('/')
        else:
            flash('Wrong username or password!')
            return redirect('/accounts/auth-signin/')
  return render_template('accounts/auth-signin.html')

#reset password (for signed out user )
@accounts.route('/accounts/auth-reset-password/', methods=['GET', 'POST'])
def accounts_auth_reset_password():
    if request.method == 'POST':
        email = request.form['email']
        
        coach = Coach.query.filter_by(CoachEmail=email).first()
        player = Player.query.filter_by(PlayerEmail=email).first()
        
        if coach or player:
            session['reset_email'] = email
            return redirect('/accounts/auth-password-reset-confirm/')
        else:
            flash('Email not found. Please enter a valid email address.')
    return render_template('accounts/auth-reset-password.html', segment='auth_reset_password', parent='accounts')

@accounts.route('/auth-password-reset-confirm/' , methods=['GET', 'POST'])
def accounts_auth_password_reset_confirm():
  
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']
        
        if new_password == confirm_new_password:
            email = session.get('reset_email')  
            
            if email:
                coach = Coach.query.filter_by(CoachEmail=email).first()
                player = Player.query.filter_by(PlayerEmail=email).first()
                
                if coach:
                    hashed_password = generate_password_hash(new_password)
                    coach.CoachPasswordHash = hashed_password
                elif player:
                    hashed_password = generate_password_hash(new_password)
                    player.PlayerPasswordHash = hashed_password

                db.session.commit()
                session.pop('reset_email', None)
                return redirect('/accounts/auth-password-reset-complete/')
                
            else:
                flash('Email not found in the session.')
        else:
            flash('Passwords do not match.')


    return render_template('accounts/auth-password-reset-confirm.html', segment='auth_password_reset_confirm', parent='accounts')

@accounts.route('/auth-password-reset-complete/')
def accounts_auth_password_reset_complete():
  return render_template('accounts/auth-password-reset-complete.html', segment='auth_password_reset_complete', parent='accounts')

#change password (for logged in user )
@accounts.route('/accounts/auth-change-password/', methods=['GET', 'POST'])
def accounts_auth_change_password():
  
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    coach = Coach.query.get(user_id)
    player = Player.query.get(user_id)

    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_new_password = request.form['confirm_new_password']

        if (coach and coach.check_password(current_password)) or (player and player.check_password(current_password)):
            if new_password == confirm_new_password:
                hashed_password = generate_password_hash(new_password)
                if coach:
                    coach.CoachPasswordHash = hashed_password
                elif player:
                    player.PlayerPasswordHash = hashed_password
                db.session.commit()
                return redirect('/accounts/auth-password-change-done/')
            else:
                flash('New passwords do not match.')
        else:
            flash('Incorrect current password.')
    return render_template('accounts/auth-change-password.html', segment='auth_change_password', parent='accounts')

@accounts.route('/auth-password-change-done/' ,methods=['GET', 'POST'])
def accounts_auth_password_change_done():
  return render_template('accounts/auth-password-change-done.html', segment='auth_password_change_done', parent='accounts')

#Log out

@accounts.route('/accounts/logout/')
def accounts_logout():
    session.pop('user_id', None)  # Remove the user's session data
    flash('You have been logged out.')  # Optionally show a logout message
    return redirect('/accounts/auth-signin/')  # Redirect the user to the login page


#Delete account

@accounts.route('/accounts/delete_account/',methods=['GET', 'POST'])
def accounts_delete_account():
    if 'user_id' not in session:
        return redirect('/accounts/auth-signin/')

    user_id = session['user_id']
    coach = Coach.query.get(user_id)
    player = Player.query.get(user_id)
    existing_workouts = PlayerWorkout.query.filter_by(player_id=player.PlayerID).all()
    existing_matches = Match.query.filter_by(player_id=player.PlayerID).all()

    if request.method == 'POST':
        if existing_matches:
            # Delete the existing player matches
            for existing_match in existing_matches:
                db.session.delete(existing_match)   
                db.session.commit()

        if existing_workouts:
            for existing_workout in existing_workouts:
                db.session.delete(existing_workout)
            db.session.commit()  # Commit all workout deletions before deleting the player

        db.session.delete(coach or player)
        db.session.commit()
        session.pop('user_id', None)
        flash('Account deleted successfully!')
        return redirect('/')

    return render_template('accounts/delete_account.html', coach=coach, player=player,segment='delete_account', parent='accounts')

 