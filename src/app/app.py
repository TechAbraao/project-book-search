from src.app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == "__main__":
    PORT = os.getenv("HOST")
    HOST = os.getenv("PORT")
    app.run(port=4040, debug=True)