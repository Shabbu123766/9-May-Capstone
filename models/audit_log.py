from extensions import db
from datetime import datetime

class AuditLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    action = db.Column(db.String(200))

    timestamp = db.Column(db.DateTime, default=datetime.utcnow)