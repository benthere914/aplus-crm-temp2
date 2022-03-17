from .db import db
from sqlalchemy.dialects.postgresql import JSON

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), primary_key=False, nullable=False)
    last_name = db.Column(db.String(255), primary_key=False, nullable=False)
    address = db.Column(JSON, primary_key=False, nullable=False)
    meta_data = db.Column(JSON, primary_key=False, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "meta_data": self.meta_data,
        }

