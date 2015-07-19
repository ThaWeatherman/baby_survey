from app import db


class User(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        '''all users are active'''
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        '''return true if user is authenticated'''
        return self.authenticated

    def is_anonymous(self):
        '''no anonymous users supported'''
        return False


class Guess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    eyes = db.Column(db.String)
    hair = db.Column(db.String)
    name = db.Column(db.String)
    length = db.Column(db.Float)
    weight = db.Column(db.Float)
    user = db.Column(db.String, db.ForeignKey('user.email'))
