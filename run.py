# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps import db, create_app
from apps.views import views as views_blueprint
from flask_login import LoginManager
from apps.models import Coach, Player, Exercise, WorkoutRoutine
from apps.accounts import accounts
import warnings
from sqlalchemy.exc import SAWarning
app = create_app()

warnings.filterwarnings('ignore', category=SAWarning, message='.*relationship .* will copy column .*')


app.register_blueprint(accounts, url_prefix='/accounts')  # Register the blueprint with a URL prefix
app.register_blueprint(views_blueprint)

login_manager = LoginManager(app)
login_manager.login_view = 'accounts.accounts_auth_signin'


@login_manager.user_loader
def load_user(user_id):
    return Coach.query.get(int(user_id)) or Player.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0', port=5000)


    """ 
     # Monday workout (Workout Group 1)
        monday_workout_group1 = WorkoutRoutine(day='Monday', workout_group=1)
        db.session.add(monday_workout_group1)

        monday_exercises_group1 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group1),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=monday_workout_group1),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=monday_workout_group1),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=monday_workout_group1),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group1)
        ]
        db.session.add_all(monday_exercises_group1)

        # Wednesday workout (Workout Group 1)
        wednesday_workout_group1 = WorkoutRoutine(day='Wednesday', workout_group=1)
        db.session.add(wednesday_workout_group1)

        wednesday_exercises_group1 = [
            Exercise(name='Tricep Pushdown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=2-LAMcpzODU', workout_routine=wednesday_workout_group1),
            Exercise(name='Lateral Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=3VcKaXpzqRo', workout_routine=wednesday_workout_group1),
            Exercise(name='Shoulder Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group1),
            Exercise(name='Dumbbell Row', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=pYcpY20QaE8', workout_routine=wednesday_workout_group1),
            Exercise(name='Bench Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rT7DgCr-3pg&t=65s', workout_routine=wednesday_workout_group1)
        ]
        db.session.add_all(wednesday_exercises_group1)

        # Friday workout (Workout Group 1)
        friday_workout_group1 = WorkoutRoutine(day='Friday', workout_group=1)
        db.session.add(friday_workout_group1)

        friday_exercises_group1 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group1),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=friday_workout_group1),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=friday_workout_group1),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=friday_workout_group1),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group1)
        ]
        db.session.add_all(friday_exercises_group1)

        db.session.commit()



       # Monday workout (Workout Group 2)
        monday_workout_group2 = WorkoutRoutine(day='Monday', workout_group=2)
        db.session.add(monday_workout_group2)

        monday_exercises_group2 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group2),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=monday_workout_group2),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=monday_workout_group2),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=monday_workout_group2),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group2)
        ]
        db.session.add_all(monday_exercises_group2)

        # Wednesday workout (Workout Group 2)
        wednesday_workout_group2 = WorkoutRoutine(day='Wednesday', workout_group=2)
        db.session.add(wednesday_workout_group2)

        wednesday_exercises_group2 = [
            Exercise(name='Tricep Pushdown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=2-LAMcpzODU', workout_routine=wednesday_workout_group2),
            Exercise(name='Lateral Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=3VcKaXpzqRo', workout_routine=wednesday_workout_group2),
            Exercise(name='Shoulder Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group2),
            Exercise(name='Dumbbell Row', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=pYcpY20QaE8', workout_routine=wednesday_workout_group2),
            Exercise(name='Bench Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rT7DgCr-3pg&t=65s', workout_routine=wednesday_workout_group2)
        ]
        db.session.add_all(wednesday_exercises_group2)

        # Friday workout (Workout Group 2)
        friday_workout_group2 = WorkoutRoutine(day='Friday', workout_group=2)
        db.session.add(friday_workout_group2)

        friday_exercises_group2 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group2),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=friday_workout_group2),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=friday_workout_group2),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=friday_workout_group2),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group2)
        ]
        db.session.add_all(friday_exercises_group2)

        db.session.commit()


        # Monday workout (Workout Group 3)
        monday_workout_group3 = WorkoutRoutine(day='Monday', workout_group=3)
        db.session.add(monday_workout_group3)

        monday_exercises_group3 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group3),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=monday_workout_group3),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=monday_workout_group3),
            Exercise(name='Weighted Step Ups', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=9ZknEYboBOQ', workout_routine=monday_workout_group3),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group3)
        ]
        db.session.add_all(monday_exercises_group3)

        # Wednesday workout (Workout Group 3)
        wednesday_workout_group3 = WorkoutRoutine(day='Wednesday', workout_group=3)
        db.session.add(wednesday_workout_group3)

        wednesday_exercises_group3 = [
            Exercise(name='Tricep Pushdown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=2-LAMcpzODU', workout_routine=wednesday_workout_group3),
            Exercise(name='Lateral Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=3VcKaXpzqRo', workout_routine=wednesday_workout_group3),
            Exercise(name='Shoulder Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group3),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group3),
            Exercise(name='Bench Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rT7DgCr-3pg&t=65s', workout_routine=wednesday_workout_group3)
        ]
        db.session.add_all(wednesday_exercises_group3)

        # Friday workout (Workout Group 3)
        friday_workout_group3 = WorkoutRoutine(day='Friday', workout_group=3)
        db.session.add(friday_workout_group3)

        friday_exercises_group3 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group3),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=friday_workout_group3),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=friday_workout_group3),
            Exercise(name='Weighted Step Ups', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=9ZknEYboBOQ', workout_routine=friday_workout_group3),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group3)
        ]
        db.session.add_all(friday_exercises_group3)

        db.session.commit()



        # Monday workout (Workout Group 4)
        monday_workout_group4 = WorkoutRoutine(day='Monday', workout_group=4)
        db.session.add(monday_workout_group4)

        monday_exercises_group4 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group4),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=monday_workout_group4),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=monday_workout_group4),
            Exercise(name='Weighted Step Ups', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=9ZknEYboBOQ', workout_routine=monday_workout_group4),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group4)
        ]
        db.session.add_all(monday_exercises_group4)

        # Wednesday workout (Workout Group 4)
        wednesday_workout_group4 = WorkoutRoutine(day='Wednesday', workout_group=4)
        db.session.add(wednesday_workout_group4)

        wednesday_exercises_group4 = [
            Exercise(name='Hammer Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=zC3nLlEvin4', workout_routine=wednesday_workout_group4),
            Exercise(name='Lateral Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=3VcKaXpzqRo', workout_routine=wednesday_workout_group4),
            Exercise(name='Shoulder Press', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group4),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group4),
            Exercise(name='Bench Press', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=rT7DgCr-3pg&t=65s', workout_routine=wednesday_workout_group4)
        ]
        db.session.add_all(wednesday_exercises_group4)

        # Friday workout (Workout Group 4)
        friday_workout_group4 = WorkoutRoutine(day='Friday', workout_group=4)
        db.session.add(friday_workout_group4)

        friday_exercises_group4 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group4),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=friday_workout_group4),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=friday_workout_group4),
            Exercise(name='Weighted Step Ups', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=9ZknEYboBOQ', workout_routine=friday_workout_group4),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group4)
        ]
        db.session.add_all(friday_exercises_group4)

        db.session.commit()


        # Monday workout (Workout Group 5)
        monday_workout_group5 = WorkoutRoutine(day='Monday', workout_group=5)
        db.session.add(monday_workout_group5)

        monday_exercises_group5 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group5),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=monday_workout_group5),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=monday_workout_group5),
            Exercise(name='Weighted Step Ups', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=9ZknEYboBOQ', workout_routine=monday_workout_group5),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group5)
        ]
        db.session.add_all(monday_exercises_group5)

        # Wednesday workout (Workout Group 5)
        wednesday_workout_group5 = WorkoutRoutine(day='Wednesday', workout_group=5)
        db.session.add(wednesday_workout_group5)

        wednesday_exercises_group5 = [
            Exercise(name='Hammer Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=zC3nLlEvin4', workout_routine=wednesday_workout_group5),
            Exercise(name='Lateral Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=3VcKaXpzqRo', workout_routine=wednesday_workout_group5),
            Exercise(name='Shoulder Press', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group5),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group5),
            Exercise(name='Bench Press', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=rT7DgCr-3pg&t=65s', workout_routine=wednesday_workout_group5)
        ]
        db.session.add_all(wednesday_exercises_group5)

        # Friday workout (Workout Group 5)
        friday_workout_group5 = WorkoutRoutine(day='Friday', workout_group=5)
        db.session.add(friday_workout_group5)

        friday_exercises_group5 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group5),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=friday_workout_group5),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=friday_workout_group5),
            Exercise(name='Weighted Step Ups', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=9ZknEYboBOQ', workout_routine=friday_workout_group5),
            Exercise(name='Calf Raises', sets=3, reps=20, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group5)
        ]
        db.session.add_all(friday_exercises_group5)

        db.session.commit()

        
        # Monday workout (Workout Group 6)
        monday_workout_group6 = WorkoutRoutine(day='Monday', workout_group=6)
        db.session.add(monday_workout_group6)

        monday_exercises_group6 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group6),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=monday_workout_group6),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=monday_workout_group6),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=monday_workout_group6),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group6)
        ]
        db.session.add_all(monday_exercises_group6)

        # Wednesday workout (Workout Group 6)
        wednesday_workout_group6 = WorkoutRoutine(day='Wednesday', workout_group=6)
        db.session.add(wednesday_workout_group6)

        wednesday_exercises_group6 = [
            Exercise(name='Front Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=3VcKaXpzqRo', workout_routine=wednesday_workout_group6),
            Exercise(name='Shoulder Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group6),
            Exercise(name='Seated Cable Rows', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=GZbfZ033f74&t=15s', workout_routine=wednesday_workout_group6),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group6),
            Exercise(name='Incline Bench Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=DbFgADa2PL8', workout_routine=wednesday_workout_group6)
        ]
        db.session.add_all(wednesday_exercises_group6)

        # Friday workout (Workout Group 6)
        friday_workout_group6 = WorkoutRoutine(day='Friday', workout_group=6)
        db.session.add(friday_workout_group6)

        friday_exercises_group6 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group6),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=friday_workout_group6),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=friday_workout_group6),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=friday_workout_group6),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group6)
        ]
        db.session.add_all(friday_exercises_group6)

        db.session.commit()

        
        # Monday workout (Workout Group 7)
        monday_workout_group7 = WorkoutRoutine(day='Monday', workout_group=7)
        db.session.add(monday_workout_group7)

        monday_exercises_group7 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group7),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=monday_workout_group7),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=monday_workout_group7),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=monday_workout_group7),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group7)
        ]
        db.session.add_all(monday_exercises_group7)

        # Wednesday workout (Workout Group 7)
        wednesday_workout_group7 = WorkoutRoutine(day='Wednesday', workout_group=7)
        db.session.add(wednesday_workout_group7)

        wednesday_exercises_group7 = [
            Exercise(name='Front Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=-t7fuZ0KhDA', workout_routine=wednesday_workout_group7),
            Exercise(name='Shoulder Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group7),
            Exercise(name='Seated Cable Rows', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=GZbfZ033f74&t=15s', workout_routine=wednesday_workout_group7),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group7),
            Exercise(name='Incline Bench Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=DbFgADa2PL8', workout_routine=wednesday_workout_group7)
        ]
        db.session.add_all(wednesday_exercises_group7)

        # Friday workout (Workout Group 7)
        friday_workout_group7 = WorkoutRoutine(day='Friday', workout_group=7)
        db.session.add(friday_workout_group7)

        friday_exercises_group7 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group7),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=friday_workout_group7),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=friday_workout_group7),
            Exercise(name='Bulgarian Split Squats', sets=3, reps=10, tutorial_link='https://www.youtube.com/shorts/uODWo4YqbT8', workout_routine=friday_workout_group7),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group7)
        ]
        db.session.add_all(friday_exercises_group7)

        db.session.commit()


        db.session.commit()
        # Monday workout (Workout Group 8)
        monday_workout_group8 = WorkoutRoutine(day='Monday', workout_group=8)
        db.session.add(monday_workout_group8)

        monday_exercises_group8 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group8),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=monday_workout_group8),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=monday_workout_group8),
            Exercise(name='Deadlift', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=monday_workout_group8),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group8)
        ]
        db.session.add_all(monday_exercises_group8)

        # Wednesday workout (Workout Group 8)
        wednesday_workout_group8 = WorkoutRoutine(day='Wednesday', workout_group=8)
        db.session.add(wednesday_workout_group8)

        wednesday_exercises_group8 = [
            Exercise(name='Front Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=-t7fuZ0KhDA', workout_routine=wednesday_workout_group8),
            Exercise(name='Shoulder Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group8),
            Exercise(name='Seated Cable Rows', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=GZbfZ033f74&t=15s', workout_routine=wednesday_workout_group8),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group8),
            Exercise(name='Incline Bench Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=DbFgADa2PL8', workout_routine=wednesday_workout_group8)
        ]
        db.session.add_all(wednesday_exercises_group8)

        # Friday workout (Workout Group 8)
        friday_workout_group8 = WorkoutRoutine(day='Friday', workout_group=8)
        db.session.add(friday_workout_group8)

        friday_exercises_group8 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group8),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=friday_workout_group8),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=friday_workout_group8),
            Exercise(name='Deadlift', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=friday_workout_group8),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group8)
        ]
        db.session.add_all(friday_exercises_group8)

        db.session.commit()


        # Monday workout (Workout Group 9)
        monday_workout_group9 = WorkoutRoutine(day='Monday', workout_group=9)
        db.session.add(monday_workout_group9)

        monday_exercises_group9 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group9),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=monday_workout_group9),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=monday_workout_group9),
            Exercise(name='Deadlift', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=monday_workout_group9),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group9)
        ]
        db.session.add_all(monday_exercises_group9)

        # Wednesday workout (Workout Group 9)
        wednesday_workout_group9 = WorkoutRoutine(day='Wednesday', workout_group=9)
        db.session.add(wednesday_workout_group9)

        wednesday_exercises_group9 = [
            Exercise(name='Front Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=-t7fuZ0KhDA', workout_routine=wednesday_workout_group9),
            Exercise(name='Shoulder Press', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group9),
            Exercise(name='Seated Cable Rows', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=GZbfZ033f74&t=15s', workout_routine=wednesday_workout_group9),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group9),
            Exercise(name='Incline Bench Press', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=DbFgADa2PL8', workout_routine=wednesday_workout_group9)
        ]
        db.session.add_all(wednesday_exercises_group9)

        # Friday workout (Workout Group 9)
        friday_workout_group9 = WorkoutRoutine(day='Friday', workout_group=9)
        db.session.add(friday_workout_group9)

        friday_exercises_group9 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group9),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=friday_workout_group9),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=friday_workout_group9),
            Exercise(name='Deadlift', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=friday_workout_group9),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group9)
        ]
        db.session.add_all(friday_exercises_group9)

        db.session.commit()


        # Monday workout (Workout Group 10)
        monday_workout_group10 = WorkoutRoutine(day='Monday', workout_group=10)
        db.session.add(monday_workout_group10)

        monday_exercises_group10 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=monday_workout_group10),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=monday_workout_group10),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=monday_workout_group10),
            Exercise(name='Deadlift', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=monday_workout_group10),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=monday_workout_group10)
        ]
        db.session.add_all(monday_exercises_group10)

        # Wednesday workout (Workout Group 10)
        wednesday_workout_group10 = WorkoutRoutine(day='Wednesday', workout_group=10)
        db.session.add(wednesday_workout_group10)

        wednesday_exercises_group10 = [
            Exercise(name='Front Raises', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=-t7fuZ0KhDA', workout_routine=wednesday_workout_group10),
            Exercise(name='Shoulder Press', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=qEwKCR5JCog', workout_routine=wednesday_workout_group10),
            Exercise(name='Seated Cable Rows', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=GZbfZ033f74&t=15s', workout_routine=wednesday_workout_group10),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=wednesday_workout_group10),
            Exercise(name='Incline Bench Press', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=DbFgADa2PL8', workout_routine=wednesday_workout_group10)
        ]
        db.session.add_all(wednesday_exercises_group10)

        # Friday workout (Workout Group 10)
        friday_workout_group10 = WorkoutRoutine(day='Friday', workout_group=10)
        db.session.add(friday_workout_group10)

        friday_exercises_group10 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=friday_workout_group10),
            Exercise(name='Broad Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=c6Etg7bpFfI', workout_routine=friday_workout_group10),
            Exercise(name='Box Jumps', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=hxldG9FX4j4', workout_routine=friday_workout_group10),
            Exercise(name='Deadlift', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=friday_workout_group10),
            Exercise(name='Calf Raises', sets=3, reps=30, tutorial_link='https://www.youtube.com/watch?v=3UWi44yN-wM', workout_routine=friday_workout_group10)
        ]
        db.session.add_all(friday_exercises_group10)

        db.session.commit()

        # Monday workout (Workout Group 11)
        monday_workout_group11 = WorkoutRoutine(day='Monday', workout_group=11)
        db.session.add(monday_workout_group11)

        monday_exercises_group11 = [
            Exercise(name='Wrist Curl', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qMtmHwaCmYI', workout_routine=monday_workout_group11),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=monday_workout_group11),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=monday_workout_group11),
            Exercise(name='Back Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=ph3pddpKzzw', workout_routine=monday_workout_group11),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=monday_workout_group11)
        ]
        db.session.add_all(monday_exercises_group11)

        # Wednesday workout (Workout Group 11)
        wednesday_workout_group11 = WorkoutRoutine(day='Wednesday', workout_group=11)
        db.session.add(wednesday_workout_group11)

        wednesday_exercises_group11 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=wednesday_workout_group11),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=wednesday_workout_group11),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=wednesday_workout_group11),
            Exercise(name='Leg Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=oujca3_Shgw', workout_routine=wednesday_workout_group11),
            Exercise(name='Dumbbell Lunges', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=D7KaRcUTQeE', workout_routine=wednesday_workout_group11)
        ]
        db.session.add_all(wednesday_exercises_group11)

        # Friday workout (Workout Group 11)
        friday_workout_group11 = WorkoutRoutine(day='Friday', workout_group=11)
        db.session.add(friday_workout_group11)

        friday_exercises_group11 = [
            Exercise(name='Wrist Curl', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qMtmHwaCmYI', workout_routine=friday_workout_group11),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=friday_workout_group11),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=friday_workout_group11),
            Exercise(name='Back Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=ph3pddpKzzw', workout_routine=friday_workout_group11),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=friday_workout_group11)
        ]
        db.session.add_all(friday_exercises_group11)

        db.session.commit()

        # Monday workout (Workout Group 12)
        monday_workout_group12 = WorkoutRoutine(day='Monday', workout_group=12)
        db.session.add(monday_workout_group12)

        monday_exercises_group12 = [
            Exercise(name='Wrist Curl', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qMtmHwaCmYI', workout_routine=monday_workout_group12),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=monday_workout_group12),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=monday_workout_group12),
            Exercise(name='Back Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=ph3pddpKzzw', workout_routine=monday_workout_group12),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=monday_workout_group12)
        ]
        db.session.add_all(monday_exercises_group12)

        # Wednesday workout (Workout Group 12)
        wednesday_workout_group12 = WorkoutRoutine(day='Wednesday', workout_group=12)
        db.session.add(wednesday_workout_group12)

        wednesday_exercises_group12 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=wednesday_workout_group12),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=wednesday_workout_group12),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=wednesday_workout_group12),
            Exercise(name='Leg Press', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=oujca3_Shgw', workout_routine=wednesday_workout_group12),
            Exercise(name='Dumbbell Lunges', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=D7KaRcUTQeE', workout_routine=wednesday_workout_group12)
        ]
        db.session.add_all(wednesday_exercises_group12)

        # Friday workout (Workout Group 12)
        friday_workout_group12 = WorkoutRoutine(day='Friday', workout_group=12)
        db.session.add(friday_workout_group12)

        friday_exercises_group12 = [
            Exercise(name='Wrist Curl', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qMtmHwaCmYI', workout_routine=friday_workout_group12),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=friday_workout_group12),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=friday_workout_group12),
            Exercise(name='Back Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=ph3pddpKzzw', workout_routine=friday_workout_group12),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=friday_workout_group12)
        ]
        db.session.add_all(friday_exercises_group12)

        db.session.commit()

       # Monday workout (Workout Group 13)
        monday_workout_group13 = WorkoutRoutine(day='Monday', workout_group=13)
        db.session.add(monday_workout_group13)

        monday_exercises_group13 = [
            Exercise(name='Wrist Curl', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qMtmHwaCmYI', workout_routine=monday_workout_group13),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=monday_workout_group13),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=monday_workout_group13),
            Exercise(name='Back Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=ph3pddpKzzw', workout_routine=monday_workout_group13),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=monday_workout_group13)
        ]
        db.session.add_all(monday_exercises_group13)

        # Wednesday workout (Workout Group 13)
        wednesday_workout_group13 = WorkoutRoutine(day='Wednesday', workout_group=13)
        db.session.add(wednesday_workout_group13)

        wednesday_exercises_group13 = [
            Exercise(name='Squats', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=wednesday_workout_group13),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=wednesday_workout_group13),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=wednesday_workout_group13),
            Exercise(name='Deadlift', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=wednesday_workout_group13),
            Exercise(name='Dumbbell Lunges', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=D7KaRcUTQeE', workout_routine=wednesday_workout_group13)
        ]
        db.session.add_all(wednesday_exercises_group13)

        # Friday workout (Workout Group 13)
        friday_workout_group13 = WorkoutRoutine(day='Friday', workout_group=13)
        db.session.add(friday_workout_group13)

        friday_exercises_group13 = [
            Exercise(name='Wrist Curl', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=qMtmHwaCmYI', workout_routine=friday_workout_group13),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=friday_workout_group13),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=friday_workout_group13),
            Exercise(name='Back Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=ph3pddpKzzw', workout_routine=friday_workout_group13),
            Exercise(name='Lat Pulldown', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=friday_workout_group13)
        ]
        db.session.add_all(friday_exercises_group13)

        db.session.commit()


        # Monday workout (Workout Group 14)
        monday_workout_group14 = WorkoutRoutine(day='Monday', workout_group=14)
        db.session.add(monday_workout_group14)

        monday_exercises_group14 = [
            Exercise(name='Bicep Curls', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=sAq_ocpRh_I', workout_routine=monday_workout_group14),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=monday_workout_group14),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=monday_workout_group14),
            Exercise(name='Dumbbell Row', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=pYcpY20QaE8', workout_routine=monday_workout_group14),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=monday_workout_group14)
        ]
        db.session.add_all(monday_exercises_group14)

        # Wednesday workout (Workout Group 14)
        wednesday_workout_group14 = WorkoutRoutine(day='Wednesday', workout_group=14)
        db.session.add(wednesday_workout_group14)

        wednesday_exercises_group14 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=wednesday_workout_group14),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=wednesday_workout_group14),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=wednesday_workout_group14),
            Exercise(name='Deadlift', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=wednesday_workout_group14),
            Exercise(name='Dumbbell Lunges', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=D7KaRcUTQeE', workout_routine=wednesday_workout_group14)
        ]
        db.session.add_all(wednesday_exercises_group14)

        # Friday workout (Workout Group 14)
        friday_workout_group14 = WorkoutRoutine(day='Friday', workout_group=14)
        db.session.add(friday_workout_group14)

        friday_exercises_group14 = [
            Exercise(name='Bicep Curls', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=sAq_ocpRh_I', workout_routine=friday_workout_group14),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=friday_workout_group14),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=friday_workout_group14),
            Exercise(name='Dumbbell Row', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=pYcpY20QaE8', workout_routine=friday_workout_group14),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=friday_workout_group14)
        ]
        db.session.add_all(friday_exercises_group14)

        db.session.commit()

       # Monday workout (Workout Group 15)
        monday_workout_group15 = WorkoutRoutine(day='Monday', workout_group=15)
        db.session.add(monday_workout_group15)

        monday_exercises_group15 = [
            Exercise(name='Bicep Curls', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=sAq_ocpRh_I', workout_routine=monday_workout_group15),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=monday_workout_group15),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=monday_workout_group15),
            Exercise(name='Dumbbell Row', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=pYcpY20QaE8', workout_routine=monday_workout_group15),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=monday_workout_group15)
        ]
        db.session.add_all(monday_exercises_group15)

        # Wednesday workout (Workout Group 15)
        wednesday_workout_group15 = WorkoutRoutine(day='Wednesday', workout_group=15)
        db.session.add(wednesday_workout_group15)

        wednesday_exercises_group15 = [
            Exercise(name='Squats', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=nFAscG0XUNY', workout_routine=wednesday_workout_group15),
            Exercise(name='Leg Extensions', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=YyvSfVjQeL0', workout_routine=wednesday_workout_group15),
            Exercise(name='Leg Curls', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=1Tq3QdYUuHs', workout_routine=wednesday_workout_group15),
            Exercise(name='Deadlift', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=n454SpMZRt8', workout_routine=wednesday_workout_group15),
            Exercise(name='Dumbbell Lunges', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=D7KaRcUTQeE', workout_routine=wednesday_workout_group15)
        ]
        db.session.add_all(wednesday_exercises_group15)

        # Friday workout (Workout Group 15)
        friday_workout_group15 = WorkoutRoutine(day='Friday', workout_group=15)
        db.session.add(friday_workout_group15)

        friday_exercises_group15 = [
            Exercise(name='Bicep Curls', sets=3, reps=6, tutorial_link='https://www.youtube.com/watch?v=sAq_ocpRh_I', workout_routine=friday_workout_group15),
            Exercise(name='Pull Ups', sets=3, reps=10, tutorial_link='https://www.youtube.com/watch?v=Es_psmnCn20', workout_routine=friday_workout_group15),
            Exercise(name='Face Pull', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=rep-qVOkqgk', workout_routine=friday_workout_group15),
            Exercise(name='Dumbbell Row', sets=3, reps=12, tutorial_link='https://www.youtube.com/watch?v=pYcpY20QaE8', workout_routine=friday_workout_group15),
            Exercise(name='Lat Pulldown', sets=3, reps=8, tutorial_link='https://www.youtube.com/watch?v=X5n55mMqSUs', workout_routine=friday_workout_group15)
        ]
        db.session.add_all(friday_exercises_group15)

        db.session.commit()

        



         """