from server.models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User (db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique= True)
    password_hash = db.Column (db.String(150), nullable= False)

    workouts = db.relationship('Workout', backref = 'user', cascade = 'all, delete-orphan')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    def to_dict(self):
        return{
            "id":self.id,
            "username":self.username,
            "email":self.email
        }
