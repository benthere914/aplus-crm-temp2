from .db import db
from sqlalchemy.dialects.postgresql import JSON

class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    customer = db.Column(JSON, primary_key=False, nullable=False)
    client = db.Column(JSON, primary_key=False, nullable=False)
    appliance = db.Column(JSON, primary_key=False, nullable=False)
    meta_data = db.Column(JSON, primary_key=False, nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "customer": self.customer,
            "client": self.client,
            "appliance": self.appliance,
            "meta_data": self.meta_data,
        }

