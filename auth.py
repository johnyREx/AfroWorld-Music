# auth.py
from flask_login import UserMixin

class User(UserMixin, db.Model):
    # Add methods for user authentication (e.g., password hashing, login/logout functions)
