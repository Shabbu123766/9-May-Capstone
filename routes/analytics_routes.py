from flask import Blueprint, jsonify
from models.book import Book
from models.borrow_record import BorrowRecord

analytics_bp = Blueprint('analytics_bp', __name__)

@analytics_bp.route('/analytics', methods=['GET'])
def analytics():

    total_books = Book.query.count()

    borrowed_books = BorrowRecord.query.filter_by(status="BORROWED").count()

    available_books = total_books - borrowed_books

    return jsonify({
        "total_books": total_books,
        "borrowed_books": borrowed_books,
        "available_books": available_books
    })