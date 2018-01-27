from flask_dance.consumer.backend.sqla import OAuthConsumerMixin

from fallen.models.base_model import db


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.Relationship(User)
