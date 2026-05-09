import unittest
import json

from app import app

class LibraryTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # Test Home API
    def test_home(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    # Test Add Book
    def test_add_book(self):

        data = {
            "title": "Python Basics",
            "author": "James",
            "isbn": "9999",
            "category": "Programming",
            "quantity": 5,
            "available_quantity": 5,
            "shelf_location": "A1"
        }

        response = self.client.post(
            '/books',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    # Test Get Books
    def test_get_books(self):

        response = self.client.get('/books')

        self.assertEqual(response.status_code, 200)

    # Test Add Member
    def test_add_member(self):

        data = {
            "name": "Ali",
            "email": "ali@test.com",
            "department": "CS",
            "phone": "9999999999"
        }

        response = self.client.post(
            '/members',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    # Test Borrow Book
    def test_borrow_book(self):

        # Add Book
        book_data = {
            "title": "Test Book",
            "author": "Author",
            "isbn": "7777",
            "category": "Programming",
            "quantity": 5,
            "available_quantity": 5,
            "shelf_location": "A1"
        }

        self.client.post(
            '/books',
            data=json.dumps(book_data),
            content_type='application/json'
        )

        # Get latest book
        books_response = self.client.get('/books')

        books = json.loads(books_response.data)

        book_id = books[-1]['id']

        # Add Member
        member_data = {
            "name": "Ali",
            "email": "ali@test.com",
            "department": "CS",
            "phone": "9999999999"
        }

        self.client.post(
            '/members',
            data=json.dumps(member_data),
            content_type='application/json'
        )

        # Get latest member
        members_response = self.client.get('/members')

        members = json.loads(members_response.data)

        member_id = members[-1]['id']

        # Borrow Book
        borrow_data = {
            "book_id": book_id,
            "member_id": member_id
        }

        response = self.client.post(
            '/borrow',
            data=json.dumps(borrow_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    # Test Return Book
    def test_return_book(self):

        response = self.client.put('/return/1')

        self.assertEqual(response.status_code, 200)

    # Test Analytics
    def test_analytics(self):

        response = self.client.get('/analytics')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()