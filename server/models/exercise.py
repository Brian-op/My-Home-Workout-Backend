from server.models import db

class Exercise (db.Model):
    __tablename__= 'exercises'

    id= db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable =True)
    description = db.Column(db.String)

    workout_exercise = db.relationship('WorkoutExercise', back_populates='exercise', cascade= 'all, delete')

    def __repr__(self):
        return f"<Exercise {self.name}>"