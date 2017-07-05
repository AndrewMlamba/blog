from django.test import TestCase
from django.utils import timezone

from posts import factories


class PostModelTests(TestCase):
    def setUp(self):
        self.author = factories.AuthorFactory()

    def test_post_creation(self):
        post = factories.PostsFactory()
        self.assertIn(self.author.name, str(post))

    def test_post_has_correct_created_date(self):
        post = factories.PostsFactory()
        now = timezone.now()
        naive = now.replace(tzinfo=None)
        self.assertLess(post.created_date, naive)

    def test_publish(self):
        now = timezone.now()
        post = factories.PostsFactory()
        naive = now.replace(tzinfo=None)
        self.assertEquals(post.published_date, naive)
