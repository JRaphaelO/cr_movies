from src.core.genre.domain.genre_repository import GenreRepository
from src.core.genre.domain.genre import Genre


class InMemoryGenreRepository(GenreRepository):
    def __init__(self, genres: list[Genre] = None):
        self.genres: list[Genre] = genres or []

    def save(self, genre: Genre):
        self.genres.append(genre)

    def find_by_name(self, name: str) -> Genre:
        return next((genre for genre in self.genres if genre.name == name), None)