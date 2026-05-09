from flask import Blueprint, request, jsonify
from extensions import db
from models.book import Book
from models.borrow_record import BorrowRecord
from datetime import datetime

borrow_bp = Blueprint('borrow_bp', __name__)

# Borrow Book API
@borrow_bp.route('/borrow', methods=['POST'])
def borrow_book():

    data = request.json

    # Find book
    book = Book.query.get(data['book_id'])

    if not book:
        return jsonify({"message": "Book not found"}), 404

    # Check availability
    if book.available_quantity <= 0:
        return jsonify({"message": "Book unavailable"}), 400

    # Create borrow record
    borrow = BorrowRecord(
        book_id=data['book_id'],
        member_id=data['member_id'],
        status="BORROWED"
    )

    # Reduce inventory
    book.available_quantity -= 1

    db.session.add(borrow)
    db.session.commit()

    return jsonify({"message": "Book borrowed successfully"})


# Return Book API
@borrow_bp.route('/return/<int:id>', methods=['PUT'])
def return_book(id):

    # Find borrow record
    borrow = BorrowRecord.query.get(id)

    if not borrow:
        return jsonify({"message": "Borrow record not found"}), 404

    # Update borrow status
    borrow.status = "RETURNED"
    borrow.return_date = datetime.utcnow()

    # Find related book safely
    book = Book.query.get(borrow.book_id)

    if book:
        book.available_quantity += 1

    db.session.commit()

    return jsonify({"message": "Book returned successfully"})