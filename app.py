from dotenv import load_dotenv

load_dotenv()

from flask import Flask
from config import Config
from extensions import db, ma

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

# Import Routes
from routes.book_routes import book_bp
from routes.member_routes import member_bp
from routes.borrow_routes import borrow_bp
from routes.analytics_routes import analytics_bp
from routes.upload_routes import upload_bp

# Register Blueprints
app.register_blueprint(book_bp)
app.register_blueprint(member_bp)
app.register_blueprint(borrow_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(upload_bp)

@app.route('/')
def home():
    return "LibTrack API Running Successfully"

# Import Models
from models.book import Book
from models.member import Member
from models.borrow_record import BorrowRecord
from models.audit_log import AuditLog

# Create Tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)