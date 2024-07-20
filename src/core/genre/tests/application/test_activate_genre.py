import pytest

from src.core.genre.application.activate_genre import ActivateGenre
from src.core.genre.application.exceptions import InvalidGenre, NotFoundGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestActivateGenre:

    def test_activate_genre(self):
        genre = Genre(name='Action', description='Action Movies', is_active=False)
        activateGenre = ActivateGenre(InMemoryGenreRepository([genre]))
        
        activateGenre.execute(genre.id)

        assert genre.is_active == True

    def test_activate_genre_not_found(self):
        activateGenre = ActivateGenre(InMemoryGenreRepository())

        with pytest.raises(NotFoundGenre):
            activateGenre.execute('1')
        