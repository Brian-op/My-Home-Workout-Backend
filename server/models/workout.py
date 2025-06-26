from server.models import db

class Workout (db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key= True)
    title= db.Column(db.String(50), nullable=False)
    date= db.Column(db.Date, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)

    workout_exercises = db.relationship('WorkoutExercise', back_populates = 'workout', cascade ='all, delete')

    
    def __repr__(self):
        return f'<Workout {self.name}>'