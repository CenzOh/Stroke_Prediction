from flask import Flask
from App_be.controller.users_CRUD import users_crud
from App_be.controller.model_CRUD import model_crud
from App_be.controller.home.home import home_actions
from App_be.controller.user.user import user_actions
from App_be.config import application

application.register_blueprint(users_crud)
application.register_blueprint(model_crud)
application.register_blueprint(home_actions)
application.register_blueprint(user_actions)


if __name__ == "__main__":
    application.run(host='0.0.0.0', threaded=True, debug=True)
