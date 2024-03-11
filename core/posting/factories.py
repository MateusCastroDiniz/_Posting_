from .models import *
import factory


class UserFactory(factory.django.DjangoModelFactory):
    complete_name = factory.Faker('name')
    username = factory.Faker('name')
    email = factory.LazyAttribute(lambda x: "%s@exemple.com" % x.complete_name.split(' ')[0])
    birthday = factory.Faker('date_of_birth')

    class Meta:
        model = User

    def __str__(self):
        return self.username


class PostFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    text_content = factory.Faker('text')

    class Meta:
        model = Post


class CommentFactory(factory.django.DjangoModelFactory):
    content = factory.Faker('text')
    post = factory.SubFactory(PostFactory)
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = Comment


class RelationFactory(factory.django.DjangoModelFactory):
    follower = factory.SubFactory(UserFactory)
    followed = factory.SubFactory(UserFactory)

    class Meta:
        model = Relation

