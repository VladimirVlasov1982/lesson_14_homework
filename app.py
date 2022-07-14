import json

from flask import Flask, jsonify
from utils import Movies

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


my_movie = Movies()

@app.route('/')
def page_main():
    return "Главная страничка"


@app.route('/movie/<title>')
def page_search(title):
    # Фильмы по названию
    result = my_movie.get_by_title(title)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/movie/<int:first_year>/to/<int:second_year>')
def page_range_year(first_year, second_year):
    # Фильмы в диапозоне
    result = my_movie.get_by_range(first_year, second_year)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/rating/children')
def page_children_rating():
    # Детские фильмы
    rating = "'G'"
    result = my_movie.get_by_rating(rating)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/rating/family')
def page_family_rating():
    # Фильмы для семьи
    rating = "'G', 'PG', 'PG-13'"
    result = my_movie.get_by_rating(rating)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/rating/adult')
def page_adult_rating():
    # Фильмы для взрослой возрастной категории
    rating = "'R', 'NC-17'"
    result = my_movie.get_by_rating(rating)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


@app.route('/genre/<genre>')
def page_genre_name(genre):
    # Фильмы по жанру
    result = my_movie.get_by_genre(genre)
    return app.response_class(
        json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json")


if __name__ == "__main__":
    app.run(debug=True)
