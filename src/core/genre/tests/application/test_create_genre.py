import pytest

from src.core.genre.application.create_genre import CreateGenre, CreateGenreRequest
from src.core.genre.domain.genre import Genre
from src.core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository

class TestCreateGenre:

    def test_create_genre_with_data(self):
        data = CreateGenreRequest(name='Action', description='Action description')
        createGenre = CreateGenre(InMemoryGenreRepository())
        response = createGenre.execute(data)

        assert response.id is not None

    def test_create_genre_without_data(self):
        data = CreateGenreRequest(name='')
        createGenre = CreateGenre(InMemoryGenreRepository())

        with pytest.raises(Exception, match="Genre name is required"):
            createGenre.execute(data)

    def test_create_genre_with_long_name(self):
        data = CreateGenreRequest(name='a'*256)
        createGenre = CreateGenre(InMemoryGenreRepository())

        with pytest.raises(Exception, match="Genre name is too long \(max 255 characters\)"):
            createGenre.execute(data)

    def test_create_genre_with_existing_name(self):
        data = CreateGenreRequest(name='Action')
        genre = Genre('Action')
        createGenre = CreateGenre(InMemoryGenreRepository([genre]))

        with pytest.raises(Exception, match="Genre already exists"):
            createGenre.execute(data)

    def test_create_genre_with_inactive_status(self):
        data = CreateGenreRequest(name='Action', is_active=False)
        createGenre = CreateGenre(InMemoryGenreRepository())
        response = createGenre.execute(data)

        assert response.id is not None
