import pytest
from core.posting.factories import UserFactory

@pytest.fixture
def user_creation():
    return UserFactory(birthday='2004-04-06', username='Mateuso')

@pytest.mark.django_db
def test_user_creation(user_creation):
    assert user_creation.birthday == '2004-04-06'
    assert user_creation.username == 'Mateuso'
