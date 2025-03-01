from faker import Faker
import requests

class ApiGoogleBooks:
    def __init__(self, key):
        self.key = key

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
            title = volume_info.get("title")
            description = volume_info.get("description") or "Descrição não encontrada"
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
        else:
            print(f"Erro na requisição. Código de status: {res.status_code}")
            return None