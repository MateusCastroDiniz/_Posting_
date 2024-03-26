import pytest
from core.posting.factories import UserFactory, ProfilePictureFactory

@pytest.fixture
def user_creation():
    user = UserFactory(birthday='2004-04-06', username='Mateuso')
    ProfilePictureFactory(user=user)
    return user 
    



@pytest.mark.django_db
def test_user_creation(user_creation):
    assert user_creation.birthday == '2004-04-06'
    assert user_creation.username == 'Mateuso'
    assert user_creation.profile_picture.profile_picture.url == '/media/default_profile_picture/default_profile_picture.png'
