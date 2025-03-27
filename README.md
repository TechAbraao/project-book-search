<h1 align="center"> 📖 Book Search | Your favorite book is here! 📖 </h1>
<div align="center">
  <img src="public/wallpaper.png" width="100%">
</div>

## 💡 Technologies

<div align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/Python-black?style=for-the-badge&logo=Python&logoSize=60"> 
  <img alt="Static Badge" src="https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=Flask&logoSize=60"> 
  <img alt="Static Badge" src="https://img.shields.io/badge/Jinja2-black?style=for-the-badge&logo=Jinja&logoColor=red&logoSize=60">
  <img alt="Static Badge" src="https://img.shields.io/badge/SQLAlchemy-black?style=for-the-badge&logo=SQLAlchemy&logoColor=red&logoSize=60">
  <img alt="Static Badge" src="https://img.shields.io/badge/CSS-black?style=for-the-badge&logo=CSS3&logoSize=60"> 
  <img alt="Static Badge" src="https://img.shields.io/badge/HTML-black?style=for-the-badge&logo=HTML5&logoSize=60"> 
  <img alt="Static Badge" src="https://img.shields.io/badge/Google Books API-black?style=for-the-badge&logo=googlecloud&logoSize=60">
  <img alt="Static Badge" src="https://img.shields.io/badge/SQLite-black?style=for-the-badge&logo=sqlite&logoSize=60">
</div>

## 📌 Getting Started

### 🔧 Pre-requisites

- An IDE of your choice
- Python installed on your system (recommended version: 3.8+)
- Google Books API Secret Key ([How to get one?](https://developers.google.com/books/docs/v1/using))

### 1️⃣ Clone this repository

```bash
git clone https://github.com/TechAbraao/project-book-search.git
```

### 2️⃣ Enter the project directory

```bash
cd project-book-search
```

### 3️⃣ Create or activate the Virtual Environment [OPTIONAL]

- **Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows:**
  ```powershell
  python -m venv venv
  venv\Scripts\activate
  ```

### 4️⃣ Install all dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure the `.env` file

Rename the `.env.example` file to `.env` and edit the environment variables accordingly:

```bash
FLASK_APP=src.app.app
FLASK_RUN_HOST=<host>
FLASK_RUN_PORT=<port>
DEBUG=True
GOOGLE_BOOK_API_KEY=<your_google_books_api_key>
```

### 6️⃣ Run the application
If you are on a Unix system:
```bash
chmod +x run.sh
./run.sh
```
Or by Flask:
```bash
flask run
```

### 7️⃣ Access in browser

```bash
http://<FLASK_RUN_HOST>:<FLASK_RUN_PORT>
```

