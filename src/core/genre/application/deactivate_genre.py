from src.core.genre.application.exceptions import InvalidGenre, NotFoundGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.domain.genre_repository import GenreRepository


class DeactivateeGenre:

    def __init__(self, genre_repository: GenreRepository):
        self.genre_repository = genre_repository

    def execute(self, genre_id: str) -> Genre:
        genre = self.genre_repository.find_by_id(genre_id)

        if not genre:
            raise NotFoundGenre("Genre not found")

        try:
            genre.deactivate()
            self.genre_repository.update(genre)
        except InvalidGenre as err:
            raise InvalidGenre(err)