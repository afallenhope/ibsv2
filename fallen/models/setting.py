# -*- coding: utf-8 -*-
from datetime import datetime

from fallen.models.base_model import BaseModel, db


class Setting(db.Model, BaseModel):
    __tablename__ = "settings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    value = db.Column(db.String(25), unique=False, nullable=False)
    active = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Setting %r>' % self.name
