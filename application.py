from flask import Flask
from App_be.controller.users_CRUD import users_crud
from App_be.controller.model_CRUD import model_crud


application = Flask(__name__,)
application.register_blueprint(users_crud)
application.register_blueprint(model_crud)


if __name__ == "__main__":
    application.run(host='0.0.0.0', threaded=True)
