from dataclasses import dataclass
from uuid import UUID

from src.core._shared.application.base_use_case import BaseUseCase
from src.core.genre.application.exceptions import InvalidGenre, NotFoundGenre
from src.core.genre.domain.genre_repository import GenreRepository

@dataclass
class UpdateGenreRequest:
    id: UUID
    name: str = ''
    description: str = ''

@dataclass
class UpdateGenreResponse:
    id: UUID

class UpdateGenre(BaseUseCase):
    def __init__(self, genre_repository: GenreRepository):
        self.genre_repository = genre_repository

    def execute(self, update_genre_request: UpdateGenreRequest):
        genre = self.genre_repository.find_by_id(update_genre_request.id)
        if not genre:
            raise NotFoundGenre("Genre not found")
        
        if not update_genre_request.name and not update_genre_request.description:
            raise InvalidGenre("Genre Name or Description is required to update")

        try:
            name = update_genre_request.name or genre.name
            description = update_genre_request.description or genre.description
            genre.update(name, description)

            self.genre_repository.update(genre)

        except ValueError as err:
            raise InvalidGenre(err)