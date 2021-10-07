from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db

from models.my_workouts import My_Workout
from models.user import User
from models.workout_names import Workout_Name

from resources.My_Workouts import MyWorkout, MyWorkoutById, WorkoutByUser, WorkoutByWorkoutType
from resources.User import User, UserById
from resources.Workout_Names import WorkoutName, WorkoutNameById

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/hiit"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(MyWorkout, '/myworkouts')
api.add_resource(MyWorkoutById, '/myworkouts/id/<int:id>')
api.add_resource(WorkoutByUser, '/myworkouts/user/<int:user_id>')
api.add_resource(WorkoutByWorkoutType, '/myworkouts/workouts/<int:workout_id>')

api.add_resource(User, '/users')
api.add_resource(UserById, '/users/<int:id>')

api.add_resource(WorkoutName, '/workoutname')
api.add_resource(WorkoutNameById, '/workoutname/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
