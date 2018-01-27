from datetime import datetime

from fallen.models.base_model import BaseModel, db


class User(db.Model, BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    active = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username
