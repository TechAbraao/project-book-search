from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__)

data_card = [
    {
        "title": "Python para Iniciantes",
        "author": "Abraão Santos",
        "gender": "Computação",
        "synopsis": "Este livro é um guia completo para quem quer aprender Python desde o início, com explicações claras e exercícios práticos."
    },
    {
        "title": "Algoritmos em Python",
        "author": "Cláudia Oliveira",
        "gender": "Computação",
        "synopsis": "Aprenda os principais algoritmos de programação e como implementá-los eficientemente em Python."
    },
    {
        "title": "Estruturas de Dados",
        "author": "Carlos Silva",
        "gender": "Computação",
        "synopsis": "Um livro focado em ensinar as principais estruturas de dados e como usá-las para otimizar o desempenho dos programas."
    },
    {
        "title": "Inteligência Artificial com Python",
        "author": "Ricardo Souza",
        "gender": "Computação",
        "synopsis": "Explore os fundamentos da inteligência artificial, machine learning e deep learning, usando a linguagem Python."
    },
    {
        "title": "Desenvolvimento Web com Flask",
        "author": "Larissa Pereira",
        "gender": "Desenvolvimento Web",
        "synopsis": "Este livro é uma introdução ao desenvolvimento de aplicações web com o framework Flask, utilizando Python para backend."
    },
    {
        "title": "Ciência de Dados com Python",
        "author": "Eduardo Mendes",
        "gender": "Ciência de Dados",
        "synopsis": "Descubra como usar Python para análise de dados, visualização e aprendizado de máquinas para explorar grandes volumes de informações."
    }
]

@home.route("/")
def home_page():
    try:
        return render_template("pages/template/template.html", titulo="Book Search", data_card=data_card)
    except TemplateNotFound:
        abort(404)
