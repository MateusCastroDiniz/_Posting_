import pytest
from core.posting.factories import *

@pytest.fixture
def create_relation():
    return RelationFactory(follower=UserFactory(username='mateuso'), followed=UserFactory(username='bozonaro'))


@pytest.mark.django_db
def test_relation_created(create_relation):
    assert create_relation.followed.username == 'bozonaro'