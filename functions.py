from flask import jsonify, json
import sqlite3


def get_actor_from_cast(name_one: str, name_two: str) -> list:
    """
    Получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки cast
    и возвращает список тех, кто играет с ними в паре больше 2 раз.
    :param name_one:
    :param name_two:
    :return: list
    """

    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"""
                        SELECT "cast"
                        FROM netflix
                        WHERE "cast" LIKE '%{name_one}%' AND "cast" LIKE '%{name_two}%'
                        GROUP BY "cast"
        """
        cursor.execute(sqlite_query)
        result_query = cursor.fetchall()
        all_actors = []
        for actor in result_query:
            all_actors.extend(actor[0].split(', '))
        finaly_list = []
        for actor in all_actors:
            if all_actors.count(actor.strip()) >= 2 and actor not in finaly_list and actor not in (name_one, name_two):
                finaly_list.append(actor.strip())
        return finaly_list


def get_movie_by_type_year_genre(type: str, year: int, genre: str) -> str:
    """
    Принимает тип картины (фильм или сериал), год выпуска и ее жанр.
    Получает на выходе список названий картин с их описаниями в JSON.
    :param type: str
    :param year: int
    :param genre: str
    :return: str
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        sqlite_query = f"""
                        SELECT title, description
                        FROM netflix
                        WHERE type = '{type}' AND release_year = {year} AND listed_in = '{genre}'
        """
        cursor.execute(sqlite_query)
        result_query = cursor.fetchall()
        result = []
        for title in result_query:
            movie_dict = dict(title)
            result.append(movie_dict)
        return json.dumps(result, ensure_ascii=False, indent=4)
