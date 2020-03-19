from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from application.config import configuration
from application.manage import Database


db = None
jwt = None


def create_app(config):  

    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(configuration[config])

    # Initialize api
    api = Api(app=app,
              title='My Diary',
              doc='/api/v1/documentation',
              description='My Diary is a online journal where users can write down \
                          their thoughts and feelings')

    global jwt
    jwt = JWTManager(app)
    jwt._set_error_handler_callbacks(api)

    from application.views import blacklist
    """
    Returns True if the token has been blacklisted or False otherwise.

    This decorator sets the callback function that will 
    be called when a protected endpoint 
    is accessed.
    """

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in blacklist

    """ make db variable visible across all methods and classes """
    global db
    db = Database(app.config)

    from application.views.entry_views import api as entries
    from application.views.user_views import api as user
    api.add_namespace(entries, path='/api/v1')
    api.add_namespace(user, path='/api/v1')

    """ Create database tables """
    db.create_all()
    # db.drop_all()
    return app
