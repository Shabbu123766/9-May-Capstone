from extensions import db

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100))

    author = db.Column(db.String(100))

    isbn = db.Column(db.String(100))

    category = db.Column(db.String(100))

    quantity = db.Column(db.Integer)

    available_quantity = db.Column(db.Integer)

    shelf_location = db.Column(db.String(50))