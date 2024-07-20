from uuid import uuid4
import pytest

from src.core.genre.application.exceptions import InvalidGenre, NotFoundGenre
from src.core.genre.application.update_genre import UpdateGenre, UpdateGenreRequest
from src.core.genre.domain.genre import Genre
from src.core.genre.infra.in_memory_genre_repository import InMemoryGenreRepository


class TestUpdateGenre:

    @pytest.fixture
    def genre_action(self) -> Genre:
        return Genre(name='Action', description='Action Movies', is_active=True)

    def test_when_genre_not_found_then_raise_exception(self, genre_action: Genre):
        update_genre = UpdateGenre(InMemoryGenreRepository([genre_action]))
        with pytest.raises(NotFoundGenre):
            update_genre.execute(UpdateGenreRequest(id=uuid4()))

    def test_when_genre_found_then_update_genre(self, genre_action: Genre):
        update_genre = UpdateGenre(InMemoryGenreRepository([genre_action]))
        update_genre.execute(UpdateGenreRequest(id=genre_action.id, name='New Action', description='New Action Movies'))

        assert genre_action.name == 'New Action'
        assert genre_action.description == 'New Action Movies'

    def test_when_genre_found_and_name_empty_then_update_genre(self, genre_action: Genre):
        update_genre = UpdateGenre(InMemoryGenreRepository([genre_action]))
        update_genre.execute(UpdateGenreRequest(id=genre_action.id, description='New Action Movies'))

        assert genre_action.name == 'Action'
        assert genre_action.description == 'New Action Movies'

    def test_when_genre_found_and_description_empty_then_update_genre(self, genre_action: Genre):
        update_genre = UpdateGenre(InMemoryGenreRepository([genre_action]))
        update_genre.execute(UpdateGenreRequest(id=genre_action.id, name='New Action'))

        assert genre_action.name == 'New Action'
        assert genre_action.description == 'Action Movies'

    def test_when_genre_found_and_name_and_description_empty_then_raise_exception(self, genre_action: Genre):
        update_genre = UpdateGenre(InMemoryGenreRepository([genre_action]))
        with pytest.raises(InvalidGenre):
            update_genre.execute(UpdateGenreRequest(id=genre_action.id))

    def test_when_genre_found_and_name_too_long_then_raise_exception(self, genre_action: Genre):
        update_genre = UpdateGenre(InMemoryGenreRepository([genre_action]))
        with pytest.raises(InvalidGenre):
            update_genre.execute(UpdateGenreRequest(id=genre_action.id, name='a' * 256))
