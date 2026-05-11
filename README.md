[README_flask.md](https://github.com/user-attachments/files/27611541/README_flask.md)
# Flask Student Manager

A simple full-stack web application for managing a student list, built with Flask and SQLite.

## What it does

- Add students by name
- View all students in a table
- Delete individual students
- Data is stored persistently in a SQLite database

## Stack

- Python, Flask
- SQLite (via Python's built-in sqlite3)
- HTML, Bootstrap 5
- Jinja2 templating

## Project Structure

```
flask_sqlite_project/
├── app.py              # Flask routes
├── database.py         # SQLite CRUD operations
└── templates/
    └── index.html      # Bootstrap UI with Jinja2 template
```

## Run locally

```bash
pip install flask
python app.py
```

Then open http://127.0.0.1:5000 in your browser.
