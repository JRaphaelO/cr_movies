from unittest.mock import create_autospec
import pytest

from src.core.genre.application.list_genre import GenreOutput, ListGenre, ListGenreRequest, ListGenreResponse, ListOutputMeta
from src.core.genre.domain.genre import Genre
from src.core.genre.domain.genre_repository import GenreRepository
from src.core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestListGenre:

    @pytest.fixture
    def genre_action(self) -> Genre:
        return Genre(name='Action', description='Action Movies', is_active=True)
    
    @pytest.fixture
    def genre_comedy(self) -> Genre:
        return Genre(name='Comedy', description='Comedy Movies', is_active=True)

    @pytest.fixture
    def genre_drama(self) -> Genre:
        return Genre(name='Drama', description='Drama Movies', is_active=False)
    
    @pytest.fixture
    def mock_empty_genre_repository(self) -> GenreRepository:
        repository = create_autospec(GenreRepository)
        repository.list.return_value = []
        return repository
    
    @pytest.fixture
    def mock_populated_genre_repository(self, genre_action, genre_comedy, genre_drama) -> GenreRepository:
        repository = create_autospec(GenreRepository)
        repository.list.return_value = [genre_action, genre_comedy, genre_drama]
        return repository

    def test_when_no_genres_then_return_empty_list(self, mock_empty_genre_repository):
        list_genre = ListGenre(mock_empty_genre_repository)
        response = list_genre.execute(ListGenreRequest())
        assert response  == ListGenreResponse(
            data=[], meta=ListOutputMeta(current_page=1, total_pages=0, per_page=2)
        )
    
    def test_when_genres_then_return_sorted_list(self, mock_populated_genre_repository, genre_action, genre_comedy, genre_drama):
        list_genre = ListGenre(mock_populated_genre_repository)
        response = list_genre.execute(ListGenreRequest())
        assert response == ListGenreResponse(
            data=[
                GenreOutput(id=genre_action.id, name=genre_action.name, description=genre_action.description, is_active=genre_action.is_active),
                GenreOutput(id=genre_comedy.id, name=genre_comedy.name, description=genre_comedy.description, is_active=genre_comedy.is_active)
            ],
            meta=ListOutputMeta(current_page=1, per_page=2, total_pages=2, total=3)
        )

    def test_fetch_page_without_elements(self, mock_populated_genre_repository: GenreRepository) -> None:
        listGenre = ListGenre(mock_populated_genre_repository)
        response = listGenre.execute(ListGenreRequest(current_page=3))

        assert response == ListGenreResponse(
            data=[],
            meta=ListOutputMeta(
                current_page=3,
                per_page=2,
                total_pages=2,
                total=3
            ),
        )
        