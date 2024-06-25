from fastapi import FastAPI

app = FastAPI()

books = [
    {"author": "George Orwell", "title": "1984", "category": "Dystopian"},
    {"author": "Harper Lee", "title": "To Kill a Mockingbird", "category": "Classic"},
    {"author": "J.K. Rowling", "title": "Harry Potter and the Sorcerer's Stone", "category": "Fantasy"},
    {"author": "J.R.R. Tolkien", "title": "The Hobbit", "category": "Fantasy"},
    {"author": "F. Scott Fitzgerald", "title": "The Great Gatsby", "category": "Classic"},
    {"author": "Mary Shelley", "title": "Frankenstein", "category": "Gothic"},
    {"author": "Jane Austen", "title": "Pride and Prejudice", "category": "Romance"},
    {"author": "Mark Twain", "title": "Adventures of Huckleberry Finn", "category": "Adventure"},
    {"author": "Ernest Hemingway", "title": "The Old Man and the Sea", "category": "Literary Fiction"},
    {"author": "Isaac Asimov", "title": "Foundation", "category": "Science Fiction"}
]

@app.get('/v1/get-message')
async def first_api():
  return { 'message' : 'Hello World From FastAPI'}

@app.get('/v1/get-books')
async def get_books():
  return books

# Path Parameters
@app.get('/v1/get-books/{book_title}')
async def get_books_path_param(book_title: str):
  for book in books:
    if book.get('title').casefold() == book_title.casefold():
      return book
  return { 'message': 'No book found!' }

# Query Parameters
@app.get('/v1/books')
async def get_books_query_param(category: str): # category -> query parameter
  books_to_return = []
  for book in books:
    if book.get('category').casefold() == category.casefold():
      books_to_return.append(book)
  return books_to_return

# Query Parameter and Path Parameter
@app.get('/v1/books/{book_author}')
async def get_books_query_path_param(book_author: str, category: str): # category -> query parameter
  books_to_return = []
  for book in books:
    if book.get('author').casefold() == book_author.casefold() and \
      book.get('category').casefold() == category.casefold():
      books_to_return.append(book)
  return books_to_return
