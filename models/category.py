from datetime import datetime
from models.db import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __init__(self, name, type, user_id):
        self.name = name
        self.type = type
        self.user_id = user_id

    def json(self):
        return {"id": self.id, "name": self.name, "type": self.type, "user_id": self.user_id, "created_at": str(self.created_at), "updated_at": str(self.updated_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        categories = Category.query.all()
        return [c.json() for c in categories]

    @classmethod
    def find_by_id(cls, id):
        return Category.query.filter_by(id=id).first()

    @classmethod
    def delete(cls, self):
        db.session.delete(self)
        db.session.commit()
