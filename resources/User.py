from flask import request
from flask_restful import Resource
from models.user import User
from models.db import db


class Users(Resource):
    def get(self):
        users = User.find_all()
        return [u.json() for u in users]

    def post(self):
        data = request.get_json()
        user = User(**data)
        user.create()
        return user.json(), 201


class UserDetail(Resource):
    def get(self, user_id):
        user = User.query.options().filter_by(id=user_id).first()
        return user.json()

    def put(self, user_id):
        data = request.get_json()
        user = User.find_by_id(user_id)
        for key in data:
            setattr(user, key, data[key])
        db.session.commit()
        return user.json()

    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {"msg": "user not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"msg": "User Deleted", "payload": user_id}
