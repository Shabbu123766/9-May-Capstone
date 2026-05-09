#  LibTrack API Platform

A Flask-based Smart Library & Book Inventory Management System.

This project provides REST APIs for:

* Book Management
* Member Management
* Borrow/Return Operations
* Inventory Tracking
* CSV Upload
* Analytics
* Audit Logging
* Unit Testing
* Docker Support
* CI/CD using GitHub Actions

---

#  Features

##  Book Management

* Add Books
* View Books
* Update Books
* Delete Books

##  Member Management

* Add Members
* View Members
* Update Members
* Delete Members

##  Borrow & Return System

* Borrow Books
* Return Books
* Automatic Inventory Update

##  CSV Upload

* Upload books using CSV files

##  Analytics

* Total Books
* Borrowed Books
* Available Books

##  Audit Logs

* Tracks system operations

##  Unit Testing

* API testing using unittest

##  CI/CD

* GitHub Actions workflow for automated testing

##  Docker Support

* Dockerized Flask application

---

#  Technologies Used

| Technology       | Purpose                |
| ---------------- | ---------------------- |
| Python           | Backend Language       |
| Flask            | Web Framework          |
| Flask SQLAlchemy | ORM                    |
| MySQL            | Main Database          |
| SQLite           | CI/CD Testing Database |
| Pandas           | CSV Processing         |
| Postman          | API Testing            |
| GitHub Actions   | CI/CD                  |
| Docker           | Containerization       |
| unittest         | Unit Testing           |

---

#  Useful Links

## Flask Documentation

[https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

## SQLAlchemy Documentation

[https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)

## Docker Documentation

[https://docs.docker.com/](https://docs.docker.com/)

## GitHub Actions Documentation

[https://docs.github.com/en/actions](https://docs.github.com/en/actions)

## Postman

[https://www.postman.com/](https://www.postman.com/)


#  Project Structure

```bash
LibTrack API Platform
│
├── models
│   ├── book.py
│   ├── member.py
│   ├── borrow_record.py
│   └── audit_log.py
│
├── routes
│   ├── book_routes.py
│   ├── member_routes.py
│   ├── borrow_routes.py
│   ├── analytics_routes.py
│   └── upload_routes.py
│
├── tests
│   └── test_books.py
│
├── uploads
│   └── books.csv
│
├── .github
│   └── workflows
│       └── python-app.yml
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---


## 2️ Navigate to Project Folder

```bash
cd libtrack-api-platform
```

---

## 3️ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️ Configure Database

Create `.env` file:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost/libtrack
```

---

## 6️ Run Flask Server

```bash
python app.py
```

#  CSV Upload Format

Example `books.csv`:

```csv
title,author,isbn,category,quantity
Python Basics,James,1111,Programming,10
Flask Guide,John,2222,Web Development,5
Java Fundamentals,Smith,3333,Programming,8
```

---

#  Running Unit Tests

```bash
python -m unittest tests/test_books.py
```

---

#  Docker Setup

## Build Docker Image

```bash
docker build -t libtrack .
```

---

## Run Docker Container

```bash
docker run -p 5000:5000 libtrack
```

---

## Stop Docker Container

```bash
docker ps
docker stop <container_id>
```

---

#  CI/CD Pipeline

GitHub Actions automatically:

* Installs dependencies
* Runs unit tests
* Verifies application build

Workflow file:

```text
.github/workflows/python-app.yml
```


#  Author

Shabbu Parveen
