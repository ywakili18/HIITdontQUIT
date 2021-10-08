from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import user, category, workout
from resources import User, category, workout

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/hiit"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(User.Users, '/users')
api.add_resource(User.UserDetail, '/users/<int:user_id>')
api.add_resource(category.Categories, '/categories')
api.add_resource(category.CategoryDetail, '/categories/<int:category_id>')
api.add_resource(workout.Workouts, '/comments')
api.add_resource(workout.WorkoutDetail, '/comments/<int:workout_id>')

if __name__ == '__main__':
    app.run(debug=True)
