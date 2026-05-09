from flask import Blueprint, request, jsonify
from extensions import db
from models.book import Book

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['POST'])
def add_book():

    data = request.json

    book = Book(
        title=data['title'],
        author=data['author'],
        isbn=data['isbn'],
        category=data['category'],
        quantity=data['quantity'],
        available_quantity=data['available_quantity'],
        shelf_location=data['shelf_location']
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({"message": "Book added successfully"})


@book_bp.route('/books', methods=['GET'])
def get_books():

    books = Book.query.all()

    result = []

    for book in books:
        result.append({
            "id": book.id,
            "title": book.title
        })

    return jsonify(result)

# Update Book
@book_bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):

    book = Book.query.get(id)

    if not book:
        return jsonify({"message": "Book not found"})

    data = request.json

    book.title = data['title']
    book.author = data['author']
    book.category = data['category']

    db.session.commit()

    return jsonify({"message": "Book updated successfully"})


# Delete Book
@book_bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):

    book = Book.query.get(id)

    if not book:
        return jsonify({"message": "Book not found"})

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully"})