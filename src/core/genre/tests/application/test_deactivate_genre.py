import pytest

from src.core.genre.application.activate_genre import ActivateGenre
from src.core.genre.application.deactivate_genre import DeactivateeGenre
from src.core.genre.application.exceptions import InvalidGenre, NotFoundGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestDeactivateGenre:

    def test_deactivate_genre(self):
        genre = Genre(name='Action', description='Action Movies', is_active=True)
        deactivateGenre = DeactivateeGenre(InMemoryGenreRepository([genre]))
        
        deactivateGenre.execute(genre.id)

        assert genre.is_active == False

    def test_activate_genre_not_found(self):
        deactivateGenre = DeactivateeGenre(InMemoryGenreRepository())

        with pytest.raises(NotFoundGenre):
            deactivateGenre.execute('1')
        