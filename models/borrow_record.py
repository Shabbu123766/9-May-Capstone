from extensions import db
from datetime import datetime

class BorrowRecord(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer)

    member_id = db.Column(db.Integer)

    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)

    return_date = db.Column(db.DateTime)

    status = db.Column(db.String(20))