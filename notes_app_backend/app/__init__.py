from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

from .routes.health import blp as health_blp
from .routes.notes import blp as notes_blp

# Initialize Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False

# CORS - open for demo; restrict in production
CORS(app, resources={r"/*": {"origins": "*"}})

# OpenAPI / Swagger configuration
app.config["API_TITLE"] = "Notes API - Ocean Professional"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# Theme metadata (informational for consumers)
app.config["API_DESCRIPTION"] = (
    "A modern, clean RESTful API for managing notes. "
    "Follows the Ocean Professional theme with clear endpoint organization."
)

# Initialize API and register blueprints
api = Api(app)
api.register_blueprint(health_blp)
api.register_blueprint(notes_blp)
