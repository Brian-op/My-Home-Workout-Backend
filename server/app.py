from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from server.models import db
from server.config import Config

from server.controllers.auth_controller import auth_bp
from server.controllers.user_controller import user_bp
from server.controllers.workout_controller import workout_bp


migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)

    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(workout_bp, url_prefix='/api/workouts')

    @app.route('/')
    def home():
        return {'message': 'Home Workout API is running '}

    return app
