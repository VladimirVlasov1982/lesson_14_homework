import sqlite3


class Movies:

    def connection_base(self, sqlite_query: str) -> list[dict]:
        """
        Подключается к БД и получает результат запроса в виде списка словарей
        :param sqlite_query:
        :return:
        """
        with sqlite3.connect('netflix.db') as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute(sqlite_query)
            result = cursor.fetchall()
            result_list = []
            for title in result:
                res_dict = dict(title)
                result_list.append(res_dict)
            return result_list

    def get_by_title(self, title: str) -> list[dict]:
        """
        Получает самый свежий фильм по названию
        :param title:
        :return: list[dict]
        """
        sqlite_query = f"""
                            SELECT title, country, release_year, listed_in AS genre, description 
                            FROM netflix
                            WHERE title LIKE '%{title}%'
                            ORDER BY release_year DESC
                            LIMIT 1
        """
        result = self.connection_base(sqlite_query)
        return result

    def get_by_range(self, first_year: int, second_year: int) -> list[dict]:
        """
        Возвращает название фильма и год в заданном периоде
        :param first_year:
        :param second_year:
        :return: list[dict]
        """
        sqlite_query = f"""
                        SELECT title, release_year
                        FROM netflix
                        WHERE release_year BETWEEN {first_year} AND {second_year}
                        LIMIT 100
        """
        result = self.connection_base(sqlite_query)
        return result

    def get_by_rating(self, rating: str) -> list[dict]:
        """
        Возвращает фильмы в зависимости от рейтинга
        :param rating:
        :return: list[dict]
        """
        sqlite_query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating != ''
                    AND rating IN ({rating})
        """
        result = self.connection_base(sqlite_query)
        return result

    def get_by_genre(self, genre: str) -> list[dict]:
        """
        Возвращает 10 самых свежих фильмов по искомому жанру
        :param genre:
        :return: list[dict]
        """
        sqlite_querty = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY release_year DESC
                    LIMIT 10
        """
        result = self.connection_base(sqlite_querty)
        return result
