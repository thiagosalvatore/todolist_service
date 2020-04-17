from flask import Blueprint
from flask_restx import Api

from todo_list.apis.todos import todos_ns

todo_list_bp = Blueprint("todo_list_api", __name__)

api = Api(todo_list_bp)

api.add_namespace(todos_ns)
