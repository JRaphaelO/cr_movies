from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, TypeVar
from uuid import UUID

from src import config
from src.core._shared.application.base_use_case import BaseUseCase
from src.core.genre.domain.genre_repository import GenreRepository

@dataclass
class ListGenreRequest:
    order_by: str = 'name'
    current_page: int = 1

@dataclass
class GenreOutput:
    id: UUID
    name: str
    description: str
    is_active: bool

@dataclass
class ListOutputMeta:
    current_page: int
    per_page: int = config.DEFAULT_PAGE_SIZE
    total_pages: int = 0
    total: int = 0

T = TypeVar('T')

@dataclass
class ListOutput(Generic[T], ABC):
    data: list[T] = field(default_factory=list)
    meta: ListOutputMeta = field(default_factory=ListOutputMeta)

@dataclass
class ListGenreResponse(ListOutput[GenreOutput]):
    pass

class ListGenre(BaseUseCase):
    def __init__(self, genre_repository: GenreRepository):
        self.genre_repository = genre_repository

    def execute(self, listGenreRequest: ListGenreRequest):
        genres = self.genre_repository.list()

        ordered_genres = sorted(genres, key=lambda genre: getattr(genre, listGenreRequest.order_by))
        page_offset = (listGenreRequest.current_page - 1) * config.DEFAULT_PAGE_SIZE
        genres_page = ordered_genres[page_offset:page_offset + config.DEFAULT_PAGE_SIZE]
        total_pages = (len(ordered_genres) / config.DEFAULT_PAGE_SIZE)  if (len(ordered_genres) % config.DEFAULT_PAGE_SIZE == 0) else (len(ordered_genres) // config.DEFAULT_PAGE_SIZE) + 1
        return ListGenreResponse(
            data=sorted(
                [GenreOutput(id=genre.id, name=genre.name, description=genre.description, is_active=genre.is_active) for genre in genres_page],
                key=lambda genre: genre.name
            ),
            meta=ListOutputMeta(
                current_page=listGenreRequest.current_page,
                per_page=config.DEFAULT_PAGE_SIZE,
                total = len(ordered_genres),
                total_pages= total_pages
            ),
        )