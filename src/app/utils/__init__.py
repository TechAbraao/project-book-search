from dotenv import load_dotenv
import os
from src.app.utils.GoogleBooksAPI import GoogleBooksAPI

load_dotenv()
API_KEY = os.getenv("GOOGLE_BOOK_API_KEY")

api_google_books = GoogleBooksAPI(API_KEY)

