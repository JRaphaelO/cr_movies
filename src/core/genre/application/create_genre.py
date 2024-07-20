from dataclasses import dataclass
from uuid import UUID

from src.core._shared.application.base_use_case import BaseUseCase
from src.core.genre.application.exceptions import InvalidGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.domain.genre_repository import GenreRepository

@dataclass
class CreateGenreRequest:
    name: str
    description: str = ''
    is_active: bool = True

@dataclass
class CreateGenreResponse:
    id: str


class CreateGenre(BaseUseCase):
    def __init__(self, genre_repository: GenreRepository):
        self.genre_repository = genre_repository

    def execute(self, createGenreRequest: CreateGenreRequest) -> CreateGenreResponse:
        try:
            name, description, is_active = createGenreRequest.__dict__.values()

            genre = self.genre_repository.find_by_name(name)
            if genre:
                raise ValueError("Genre already exists")

            genre = Genre(
                name=name,
                description=description,
                is_active=is_active
            )
        except ValueError as err:
            raise InvalidGenre(err)
        
        self.genre_repository.save(genre)
        return CreateGenreResponse(id=str(genre.id))

