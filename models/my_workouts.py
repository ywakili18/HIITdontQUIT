from datetime import datetime
from models.db import db


class My_Workout(db.Model):
    __tablename__ = 'my_workouts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey(
        'workout_names.id'), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

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
