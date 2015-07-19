import os


base = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base, 'app.db')
WTF_CSRF_ENABLED = True
SECRET_KEY = 'somesecret'
