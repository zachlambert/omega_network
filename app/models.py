from datetime import datetime
from app import db


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    birth_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'birth_date': self.birth_date.isoformat() + 'Z'}
        return data
