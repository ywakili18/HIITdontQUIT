from datetime import datetime
from models.db import db


class My_Workout(db.Model):
    __tablename__ = 'my_workouts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey(
        'workout_name.id'), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    workout_names = db.relationship(
        'My_Workout', backref=db.backref('my_workouts', lazy=True))
    users = db.relationship(
        'User', backref=db.backref('users', lazy=True))

    def __init__(self, user_id, workout_id, duration):
        self.user_id = user_id
        self.workout_id = workout_id
        self.duration = duration

    def json(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "workout_id": self.workout_id,
                "duration": self.duration,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
                }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return My_Workout.query.all()

    @classmethod
    def find_by_id(cls, id):
        return My_Workout.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_user(cls, user_id):
        return My_Workout.query.filter_by(user_id=user_id)

    @classmethod
    def find_by_workout(cls, workout_id):
        return My_Workout.query.filter_by(workout_id=workout_id)
