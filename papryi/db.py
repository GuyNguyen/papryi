import sqlite3

from contextlib import closing
from typing_extensions import LiteralString


class DB:
    def __init__(self, database: str = "papryi.db"):
        self.database = database

        with closing(sqlite3.connect(database)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS library (
                        isbn PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        copies TINYINT DEFAULT 1
                    )
                    """
                )
                connection.commit()

    def insert_row(self, values: tuple[str, str, str, int]) -> None:
        query: LiteralString = """
            INSERT INTO library (isbn, title, author, copies)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(isbn) DO UPDATE SET
                    copies = copies + 1
            """

        with closing(sqlite3.connect(self.database)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query, values)
                connection.commit()

    def delete_row(self, isbn: tuple[str]) -> None:
        query: LiteralString = """
            DELETE FROM library WHERE isbn = (?)
            """

        with closing(sqlite3.connect(self.database)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query, isbn)
                connection.commit()

    def update_row(self) -> None:
        pass

    def select_row(self) -> list[str]:
        query: LiteralString = """
            SELECT * FROM library
            """

        with closing(sqlite3.connect(self.database)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(query)

                return cursor.fetchall()


if __name__ == "__main__":
    db = DB()
    db.insert_row(("978-1-61039-415-4", "The Hacked World Order", "Adam Segal", 1))
    # db.delete_row(("978-1-61039-415-4",))
    fetch = db.select_row()
    print(fetch)
