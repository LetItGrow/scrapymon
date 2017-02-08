from flask_login import UserMixin

from flask_boilerplate import db


class User(db.Model, UserMixin):
    """Table users in database."""

    __tablename__ = 'users'

    uid = db.Column(db.String(64), primary_key=True)
    pwd = db.Column(db.String(64))

    def __init__(self, uid, pwd):
        """Initialize user."""
        self.uid = uid
        self.pwd = pwd

    def get_id(self):
        """Get user uid."""
        return self.uid
