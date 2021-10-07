from datetime import datetime

from sqlalchemy.orm import backref
from models.db import db


class Workout_Name(db.Model):
    __tablename__ = 'workout_name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    workout_names = db.relationship(
        'My_Workout', cascade="all", backref=db.backref('my_workouts', lazy=True))

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def json(self):
        return {"id": self.id,
                "name": self.name,
                "type": self.type,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
                }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Workout_Name.query.all()

    @classmethod
    def find_by_id(cls, id):
        return Workout_Name.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()
