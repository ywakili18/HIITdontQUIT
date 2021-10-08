from datetime import datetime
from models.db import db


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship(
        'User', backref=db.backref('comment_users', lazy=True))

    def __init__(self, duration, user_id, name):
        self.duration = duration
        self.user_id = user_id
        self.name = name

    def json(self):
        return {"id": self.id, "duration": self.duration, "name": self.name, "user_id": self.user_id, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        workouts = Workout.query.all()
        return [w.json() for w in workouts]

    @classmethod
    def find_by_id(cls, workout_id):
        return Workout.query.filter_by(id=workout_id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()
