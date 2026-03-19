from book import Book
import sqlite3
import os.path

db_path = os.path.join(os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))), 'books.db')

def setup_db():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists books(
            title TEXT,
            pages INTEGER
        )
        ''')

setup_db()

def add_book(book):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO books VALUES (?, ?)", (book.title, book.pages))
        return c.lastrowid
    
# add_book(Book("Test", 1))
# add_book(Book("Test2", 119))

def get_books():
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("SELECT * FROM books").fetchall()
        return [Book(book[0], book[1]) for book in result]
    
# data = get_books()
# print(data)

def get_book_by_title(title):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchone()
        if result:
            return Book(result[0], result[1])
        return None
    
# data = get_book_by_title("Test")
# print(data)

def delete_book_by_title(title):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("DELETE FROM books WHERE title = ?", (title,))

def delete_book(book):
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        result = c.execute("DELETE FROM books WHERE title = ? AND pages = ?", (book.title, book.pages))

# delete_book_by_title("Test")
