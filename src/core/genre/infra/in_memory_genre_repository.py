from src.core.genre.domain.genre_repository import GenreRepository
from src.core.genre.domain.genre import Genre


class InMemoryGenreRepository(GenreRepository):
    def __init__(self, genres: list[Genre] = None):
        self.genres: list[Genre] = genres or []

    def save(self, genre: Genre):
        self.genres.append(genre)

    def list(self) -> list[Genre]:
        return self.genres
    
    def update(self, genre: Genre):
        for idx, genre_item in enumerate(self.genres):
            if genre_item.id == genre.id:
                self.genres[idx] = genre
                break

    def find_by_name(self, name: str) -> Genre:
        return next((genre for genre in self.genres if genre.name == name), None)
    
    def find_by_id(self, id: int) -> Genre:
        return next((genre for genre in self.genres if genre.id == id), None)