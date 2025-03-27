import os
from src.app import create_app
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = create_app()
CORS(app)

if __name__ == "__main__":
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 5000))
    app.run(host=HOST, port=PORT, debug=True)
