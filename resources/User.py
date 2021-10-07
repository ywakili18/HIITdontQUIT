from flask_restful import Resource
from flask import request
from models.user import User
from models.db import db


class User(Resource):
    def get(self):
        data = User.find_all()
        results = [u.json() for u in data]
        return results

    def post(self):
        data = request.get_json()
        user = User(**data)
        user.create()
        return user.json()


class UserById(Resource):
    def put(self, id):
        data = request.get_json()
        user = User.find_by_id(id)
        for key in data:
            setattr(user, key, data[key])
        db.session.commit()
        return user.json()

    def delete(self, id):
        bacterium = User.find_by_id(id)
        bacterium.delete()
        return {"msg": "User deleted!"}
