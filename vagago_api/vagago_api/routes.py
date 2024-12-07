from flask import Blueprint, jsonify
from flask_apispec import doc

hello_blueprint = Blueprint("hello", __name__)


@hello_blueprint.route("/hello", methods=["GET"])
@doc(
    description="Endpoint for hello world.",
    tags=["Hello"],
)
def say_hello():
    """Hello World route.

    responses:
      200:
        description: Hello World sentence.
        content:
          application/json:
            example:
              message: "Hello, World!"
    """
    return jsonify({"message": "Hello, World!"})
