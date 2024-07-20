import pytest

from src.core.genre.domain.genre import Genre

class TestGenre:

    def test_create_genre(self):
        genre = Genre('Action')
        assert genre.name == 'Action'
        assert genre.id is not None

    def test_create_genre_with_description(self):
        genre = Genre('Action', 'Action movies')
        assert genre.name == 'Action'
        assert genre.description == 'Action movies'
        assert genre.id is not None

    def test_create_genre_with_inactive_status(self):
        genre = Genre('Action', 'Action movies', False)
        assert genre.name == 'Action'
        assert genre.description == 'Action movies'
        assert genre.is_active is False
        assert genre.id is not None
    
    def test_create_genre_with_long_name(self):
        with pytest.raises(ValueError, match="Genre name is too long \(max 255 characters\)"):
            Genre('A' * 256)

    def test_create_genre_without_name(self):
        with pytest.raises(ValueError, match="Genre name is required"):
            Genre('')

    def test_genre_str_representation(self):
        genre = Genre('Action', 'Action movies')
        assert str(genre) != 'Action - Action movies (True)'

    def test_genre_repr_representation(self):
        genre = Genre('Action', 'Action movies')
        assert repr(genre) == 'Action - Action movies (True)'

class TestGenreActivation:

    def test_deactivate_genre(self):
        genre = Genre('Action')
        genre.deactivate()
        assert genre.is_active is False

    def test_activate_genre(self):
        genre = Genre('Action', is_active=False)
        genre.activate()
        assert genre.is_active is True

class TestGenreUpdate:

    def test_update_genre(self):
        genre = Genre('Action')
        genre.update('Adventure', 'Adventure movies')
        assert genre.name == 'Adventure'
        assert genre.description == 'Adventure movies'
        assert genre.id is not None

    def test_update_genre_with_long_name(self):
        genre = Genre('Action')
        with pytest.raises(ValueError, match="Genre name is too long \(max 255 characters\)"):
            genre.update('A' * 256, 'Adventure movies')

    def test_update_genre_without_name(self):
        genre = Genre('Action')
        with pytest.raises(ValueError, match="Genre name is required"):
            genre.update('', 'Adventure movies')

class TestGenreEquality:

    def test_genre_equality(self):
        genre1 = Genre(name='Action', id='123e4567-e89b-12d3-a456-426614174000')
        genre2 = Genre(name='Action', id='123e4567-e89b-12d3-a456-426614174000')
        assert genre1 == genre2

    def test_genre_inequality(self):
        genre1 = Genre('Action')
        genre2 = Genre('Adventure')
        assert genre1 != genre2

    def test_genre_equality_with_different_instances(self):
        genre1 = Genre('Action')
        genre2 = Genre('Action')
        assert genre1 != 'Action'
        assert genre1 != genre2



