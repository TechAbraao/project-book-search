from faker import Faker
import requests

class GoogleBooksAPI:
    def __init__(self, key):
        self.key = key
        self.lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def catchBook(self, query):
        URL = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={self.key}'
        response = requests.get(URL)
        res = response.json()

        for item in res["items"]:
            volume_info = item.get("volumeInfo", {})
            title = volume_info.get("title")
            description = volume_info.get("description")
            authors = volume_info.get("authors", [])
            categories = volume_info.get("categories", [])
            image = volume_info.get("imageLinks", {}).get("thumbnail", None)
            data = {
                "title": title,
                "description": description,
                "authors": authors,
                "categories": categories,
                "image": image,
            }

        return data

    def catchIdBook(self, query):
        id_list = []
        URL = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={self.key}&maxResults=30'
        response = requests.get(URL)
        res = response.json()
        for item in res["items"]:
            _id = item["id"]
            id_list.append(_id)
        return id_list

    def random_id(self, list_id):
        fake = Faker()
        random_index = fake.random_int(min=0, max=len(list_id) - 1)
        return list_id[random_index]

    def idForVolume(self, volume_id):
        URL = f"https://www.googleapis.com/books/v1/volumes/{volume_id}?key={self.key}"
        res = requests.get(URL)
        if res.status_code == 200:
            res = res.json()
            volume_info = res.get("volumeInfo", {})
            title = volume_info.get("title") or self.lorem_ipsum
            description = volume_info.get("description") or self.lorem_ipsum
            authors = volume_info.get("authors", []) or self.lorem_ipsum
            categories = volume_info.get("categories", []) or self.lorem_ipsum
            image = volume_info.get("imageLinks", {}).get("thumbnail", None)
            data = {
                "id": volume_id,
                "title": title,
                "description": description,
                "authors": authors,
                "categories": categories,
                "image": image,
            }
            return data
        else:
            print(f"Erro na requisição. Código de status: {res.status_code}")
            return None

    def searchByName(self, book_name):
        URL = f"https://www.googleapis.com/books/v1/volumes?q={book_name}&key={self.key}&maxResults=1"
        response = requests.get(URL)
        res = response.json()

        for item in res["items"]:
            volume_info = item.get("volumeInfo", {})
            volume_id = item.get("id")
            title = volume_info.get("title")
            description = volume_info.get("description")
            authors = volume_info.get("authors", [])
            categories = volume_info.get("categories", [])
            image = volume_info.get("imageLinks", {}).get("thumbnail", None)
            data = {
                "id": volume_id,
                "title": title,
                "description": description,
                "authors": authors,
                "categories": categories,
                "image": image,
            }
            return data

def get_books_by_genre(api, genre="Humor", num_books=6):

    list_all = api.catchIdBook(genre)

    if not list_all:
        return []

    ids = [api.random_id(list_all) for _ in range(num_books)]
    books = [api.idForVolume(book_id) for book_id in ids]

    return books