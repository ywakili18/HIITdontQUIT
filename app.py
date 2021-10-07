from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import user, workout_names, my_workouts
# from resources import workout_names

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/hiit"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# api.add_resource(user.Users, '/users')
# api.add_resource(user.UserDetail, '/users/<int:user_id>')
# api.add_resource(post.Posts, '/posts')
# api.add_resource(post.PostDetail, '/posts/<int:post_id>')
# api.add_resource(comment.Comments, '/comments')
if __name__ == '__main__':
    app.run()
