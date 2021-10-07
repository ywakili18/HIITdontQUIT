from datetime import datetime
from models.db import db


class Workout_Name(db.Model):
    __tablename__ = 'workout_name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)

    def __init__(self, content):
        self.content = content

    def json(self):
        return {"id": self.id, "content": self.content, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        workout_names = Workout_Name.query.all()
        return [w.json() for w in workout_names]
