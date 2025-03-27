from flask import jsonify
from src.app.utils import api_google_books


# GET


# POST
def FindingBook(book_name):
    if not book_name or "message" not in book_name:
        return jsonify({"message": "Nenhum dado enviado ou campo 'message' ausente"}), 400

    book_name = book_name["message"]

    try:
        book_result = api_google_books.searchByName(book_name)
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar livro: {str(e)}"}), 500

    print(book_result)

    return book_result