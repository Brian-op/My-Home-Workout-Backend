from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .workout import Workout
from .exercise import Exercise
from .workout_exercise import WorkoutExercise
