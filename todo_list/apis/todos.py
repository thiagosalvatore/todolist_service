from flask_restx import Namespace, Resource

todos_ns = Namespace("todos")


@todos_ns.route("/")
class TODOResource(Resource):
    def get(self):
        """
        List all TODOs
        """
        return {"message": "List all TODOs"}

    def post(self):
        """
        Create a new TODO
        """
        return {"message": "Create a new TODO"}


@todos_ns.route("/<string:tid>/")
class TODODetailResource(Resource):
    def put(self, tid):
        """
        Update a TODO
        """
        return {"message": f"Update todo {tid}"}

    def delete(self, tid):
        """
        Delete TODO
        """
        return {"message": f"Delete todo {tid}"}
