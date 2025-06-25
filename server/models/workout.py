from server.models import db

class Workout (db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key= True)
    title= db.Column(db.String(50), nullable=False)
    date= db.Column(db.Date, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

    workout_exercises = db.relationship ('WorkoutExercise'), backref = 'workout', cascade =('all, delete-orphan')

    def to_dict(self):
        return{
            "id": self.id,
            "title": self.title,
            "date": self.date.isoformat(),
            "user_id": self.user_id,
            "exercises": [workex.to_dict() for workex in self.workout_exercises]
        }