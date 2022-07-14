from flask import jsonify
import sqlite3


def get_actor_from_cast(name_one, name_two):

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



def get_movie_by_type_year_genre(type, year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = f"""
                        SELECT title, description
                        FROM netflix
                        WHERE type = '{type}' AND release_year = {year} AND listed_in = '{genre}'
                        GROUP BY title
        """
        cursor.execute(sqlite_query)
        result_query = cursor.fetchall()
        result = []
        for title in result_query:
            movie_dict = {}
            (movie_dict['title'], movie_dict['description']) = title
            result.append(movie_dict)
        return result

print(get_actor_from_cast('Rose McIver', 'Ben Lamb'))