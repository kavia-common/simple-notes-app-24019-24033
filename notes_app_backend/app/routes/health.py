from flask_smorest import Blueprint
from flask.views import MethodView
from http import HTTPStatus

blp = Blueprint("Health", "health", url_prefix="/", description="Health check route")

@blp.route("/")
class HealthCheck(MethodView):
    """
    Liveness probe endpoint.
    """

    @blp.response(HTTPStatus.OK)
    @blp.doc(summary="Health check", description="Returns a simple status payload indicating the API is healthy.")
    def get(self):
        return {"message": "Healthy"}
