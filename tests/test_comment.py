from core.posting.factories import *
import pytest

@pytest.fixture
def create_comment():
    return CommentFactory(content='Pipoca quente na manteiga?', created_by=UserFactory(username='Corvo'),
                          post=PostFactory(text_content='Pipoca quente na manteiga!',
                                           author=UserFactory(username='Pica pau')))

@pytest.mark.django_db
def test_comment_created(create_comment):
    assert create_comment.content == 'Pipoca quente na manteiga?'

@pytest.mark.django_db
def test_comment_reference(create_comment):
    assert create_comment.post.author.username == 'Pica pau'

@pytest.mark.django_db
def test_comment_username(create_comment):
    assert create_comment.created_by.username == 'Corvo'
