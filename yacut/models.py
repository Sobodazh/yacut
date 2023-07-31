from datetime import datetime
from random import choices
from string import ascii_letters, digits

from flask import url_for

from yacut import db

COUNT_OF_RANDOM = 6


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('cut_redirect',
                               short=self.short,
                               _external=True))

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])


def get_unique_short_id():
    while True:
        short_id = ''.join(choices(ascii_letters + digits, k=COUNT_OF_RANDOM))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id