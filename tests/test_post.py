from core.posting.factories import PostFactory, UserFactory
import pytest

@pytest.fixture
def post_creation():
    return PostFactory(text_content='Pipoca quente na manteiga',
                       author=UserFactory(first_name='Mateus', last_name='Diniz', username='Mateuso'))

@pytest.mark.django_db
def test_post_creation(post_creation):
    assert post_creation.text_content == 'Pipoca quente na manteiga'
    assert post_creation.author.username == 'Mateuso'
    assert post_creation.author.email == 'Mateus@exemple.com'
