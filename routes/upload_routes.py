from flask import Blueprint, request, jsonify
import pandas as pd
import os

from extensions import db
from models.book import Book

upload_bp = Blueprint('upload_bp', __name__)

UPLOAD_FOLDER = "uploads"

@upload_bp.route('/upload', methods=['POST'])
def upload_csv():

    # Check file exists
    if 'file' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400

    file = request.files['file']

    # Check filename
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(filepath)

    # Read CSV
    df = pd.read_csv(filepath)

    # Insert into database
    for index, row in df.iterrows():

        book = Book(
            title=row['title'],
            author=row['author'],
            isbn=str(row['isbn']),
            category=row['category'],
            quantity=int(row['quantity']),
            available_quantity=int(row['quantity']),
            shelf_location="A1"
        )

        db.session.add(book)

    db.session.commit()

    return jsonify({"message": "CSV uploaded successfully"})