from dotenv import load_dotenv
import os
from src.app.utils.api_google_books import ApiGoogleBooks

load_dotenv()
API_KEY = os.getenv("GOOGLE_BOOK_API_KEY")

api_google_books = ApiGoogleBooks(API_KEY)

