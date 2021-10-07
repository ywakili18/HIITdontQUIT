from flask_restful import Resource
from flask import request
from models.workout_names import Workout_Name
from models.db import db


class WorkoutName(Resource):
    def get(self):
        data = Workout_Name.find_all()
        results = [u.json() for u in data]
        return results

    def post(self):
        data = request.get_json()
        workoutName = Workout_Name(**data)
        workoutName.create()
        return workoutName.json()


class WorkoutNameById(Resource):
    def put(self, id):
        data = request.get_json()
        workoutName = Workout_Name.find_by_id(id)
        for key in data:
            setattr(workoutName, key, data[key])
        db.session.commit()
        return workoutName.json()

    def delete(self, id):
        bacterium = Workout_Name.find_by_id(id)
        bacterium.delete()
        return {"msg": "Workout deleted!"}
