from flask_restful import Resource
from flask import request
from models.my_workouts import My_Workout
from models.db import db


class MyWorkout(Resource):
    def get(self):
        data = My_Workout.find_all()
        results = [u.json() for u in data]
        return results

    def post(self):
        data = request.get_json()
        myWorkout = My_Workout(**data)
        myWorkout.create()
        return myWorkout.json()


class MyWorkoutById(Resource):
    def put(self, id):
        data = request.get_json()
        myWorkout = My_Workout.find_by_id(id)
        for key in data:
            setattr(myWorkout, key, data[key])
        db.session.commit()
        return myWorkout.json()

    def delete(self, id):
        bacterium = My_Workout.find_by_id(id)
        bacterium.delete()
        return {"msg": "Workout deleted!"}


class WorkoutByUser(Resource):
    def get(self, user_id):
        data = My_Workout.find_by_user(user_id)
        myWorkouts = [u.json() for u in data]
        return myWorkouts.json()


class WorkoutByWorkoutType(Resource):
    def get(self, workout_id):
        data = My_Workout.find_by_workout(workout_id)
        myWorkouts = [u.json() for u in data]
        return myWorkouts.json()
