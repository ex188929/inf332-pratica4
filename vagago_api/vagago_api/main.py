from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from vagago_api.routes import hello_blueprint


def create_app():
    # Inicializando o aplicativo Flask
    app = Flask(__name__)

    # Registrando as rotas
    app.register_blueprint(hello_blueprint)

    # Configurando Flask-APISpec
    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title="Vagago API",
                version="0.0.1",
                openapi_version="3.0.0",
                plugins=[MarshmallowPlugin()],
            ),
            "APISPEC_SWAGGER_UI_URL": "/swagger/",  # URL para o Swagger UI
            "APISPEC_SWAGGER_UI_PATH": "/",  # Caminho da interface Swagger
        }
    )

    docs = FlaskApiSpec(app)
    docs.register_existing_resources()  # Registra os recursos automaticamente

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
