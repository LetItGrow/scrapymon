from flask_template import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """Table users in database."""

    __tablename__ = 'userse'

    id = db.Column(db.String(255), primary_key=True)
    pwd = db.Column(db.String(255))

    def __init__(self, id, pwd):
        """Initialize user."""
        self.id = id
        self.pwd = pwd

    def get_id(self):
        """Get user ID."""
        return self.id

