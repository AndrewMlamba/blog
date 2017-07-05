# import random
# from django.utils import timezone

import factory
from factory.django import DjangoModelFactory
from faker import Faker

from . import models

fake = Faker()


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = models.Author

    name = factory.Faker('name')


class PostsFactory(DjangoModelFactory):
    class Meta:
        model = models.Post

    author = factory.SubFactory(AuthorFactory)
    title = factory.lazy_attribute(lambda n: ' '.join(fake.words(nb=3)).title())
    text = factory.Faker('paragraph')
    created_date = factory.Faker('date_time_this_year')
    published_date = factory.Faker('date_time')
