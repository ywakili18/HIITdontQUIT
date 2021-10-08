from models.db import db
from models.category import Category
from flask_restful import Resource
from flask import request


class Categories(Resource):
    def get(self):
        categories = Category.find_all()
        return categories

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        content = Category(**params)
        content.create()
        return content.json(), 201


class CategoryDetail(Resource):
    def get(self, category_id):
        category = Category.query.options().filter_by(id=category_id).first()
        return category.json()

    def put(self, category_id):
        data = request.get_json()
        category = Category.find_by_id(category_id)
        for key in data:
            setattr(category, key, data[key])
        db.session.commit()
        return category.json()

    def delete(self, category_id):
        category = Category.find_by_id(category_id)
        if not category:
            return {"msg": "Not found"}, 404
        db.session.delete(category)
        db.session.commit()
        return {"msg": "Category Deleted", "payload": category_id}
