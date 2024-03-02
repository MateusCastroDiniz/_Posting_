from core.posting.factories import ProfileFactory
import pytest

@pytest.fixture
def profile_creation():
    return ProfileFactory(username='Matednz')

@pytest.mark.django_db
def test_profile_creation(profile_creation):
    assert profile_creation.username == 'Matednz'