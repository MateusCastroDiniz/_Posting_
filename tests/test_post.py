from core.posting.factories import PostFactory, ProfileFactory, UserFactory
import pytest

@pytest.fixture
def post_creation():
    return PostFactory(text_content='Pipoca quente na manteiga',
                       author=ProfileFactory(username='Mateuso',
                                             email=UserFactory(first_name='Mateus',
                                                               last_name='Diniz')))

@pytest.mark.django_db
def test_post_creation(post_creation):
    assert post_creation.text_content == 'Pipoca quente na manteiga'
    assert post_creation.author.username == 'Mateuso'
    assert post_creation.author.email.email == 'Mateus@exemple.com'
