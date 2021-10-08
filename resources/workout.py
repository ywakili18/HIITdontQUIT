from models.db import db
from models.workout import Workout
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Workouts(Resource):
    def get(self):
        workouts = Workout.find_all()
        return workouts

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        workout = Workout(**params)
        workout.create()
        return workout.json(), 201


class WorkoutDetail(Resource):
    def get(self, workout_id):
        workout = Workout.query.options(
            joinedload('user', 'category')).filter_by(id=workout_id).first()
        return workout.json()

    def put(self, workout_id):
        data = request.get_json()
        workout = Workout.find_by_id(workout_id)
        for key in data:
            setattr(workout, key, data[key])
        db.session.commit()
        return workout.json()

    def delete(self, workout_id):
        workout = Workout.find_by_id(workout_id)
        if not workout:
            return {"msg": "Not found"}, 404
        db.session.delete(workout)
        db.session.commit()
        return {"msg": "Workout Deleted", "payload": workout_id}
