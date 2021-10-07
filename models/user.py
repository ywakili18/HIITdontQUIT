from datetime import datetime
from models.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight_now = db.Column(db.Integer, nullable=False)
    goal_weight = db.Column(db.Integer, nullable=False)
    height_in_inches = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)

    def __init__(self, email, password, first_name, last_name, age, weight_now, goal_weight, height_in_inches):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight_now = weight_now
        self.goal_weight = goal_weight
        self.height_in_inches = height_in_inches

    def json(self):
        return {"id": self.id,
                "email": self.email,
                "password": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
                "weight_now": self.weight_now,
                "goal_weight": self.goal_weight,
                "height_in_inches": self.height_in_inches,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return User.query.all()

    @classmethod
    def find_by_id(cls, id):
        return User.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()
