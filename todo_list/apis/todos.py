from bson import ObjectId
from flask import request, make_response, jsonify
from flask_restx import Namespace, Resource
from marshmallow.exceptions import ValidationError

from database.mongodb import db
from todo_list.schemas.todos import TODODetailSchema, TODOBaseSchema

todos_ns = Namespace("todos")


@todos_ns.route("/")
class TODOResource(Resource):
    def get(self):
        """
        List all TODOs
        """
        todos = db("todo_service")["todos"].find({})
        return TODODetailSchema().dump(todos, many=True)

    def post(self):
        """
        Create a new TODO
        """
        payload = request.get_json()
        try:
            data = TODOBaseSchema().load(payload)
            db("todo_service")["todos"].insert_one(data)
        except ValidationError as e:
            return make_response(jsonify(message=e.messages), 400)

        return TODODetailSchema().dump(data)


@todos_ns.route("/<string:tid>/")
class TODODetailResource(Resource):
    def put(self, tid):
        """
        Update a TODO
        """
        todo = db("todo_service")["todos"].find_one({"_id": ObjectId(tid)})
        if not todo:
            return make_response(jsonify(message=f"Todo with id {tid} not found"), 404)

        payload = request.get_json()
        try:
            data = TODOBaseSchema().load(payload)
            db("todo_service")["todos"].update_one({"_id": ObjectId(tid)}, {"$set": data})
        except ValidationError as e:
            return make_response(jsonify(message=e.messages), 400)

        return TODODetailSchema().dump(data)

    def delete(self, tid):
        """
        Delete TODO
        """
        todo = db("todo_service")["todos"].find_one({"_id": ObjectId(tid)})
        if not todo:
            return make_response(jsonify(message=f"Todo with id {tid} not found"), 404)
        db("todo_service")["todos"].delete_one({"_id": ObjectId(tid)})
        return {"message": f"Deleted todo {tid}"}
