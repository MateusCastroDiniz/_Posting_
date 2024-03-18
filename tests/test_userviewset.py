import json
import pdb

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from core.posting.factories import UserFactory
from core.posting.models import User

class TestUserViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = User.objects.create(username='test_user', email='test@example.com', birthday='2001-01-01')
        self.user.set_password('test_password')
        self.user.save()


    def test_get_user(self):
        response = self.client.get(reverse('account-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = json.loads(response.content)

        # self.assertEqual(user_data[0], self.user.username)

    def test_signup_default_avatar(self):
        url = reverse('signup')
        data = {
            'complete_name': 'John Doe',
            'email': 'johndoe@example.com',
            'birthday': '1990-01-01',
            'username': 'johndoe',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='johndoe@example.com').exists())

        user = User.objects.get(email='johndoe@example.com')

        self.assertEqual(user.avatar.url, '/media/default-avatars/default-avatar.png')
        import pdb;
        pdb.set_trace()

    def test_edit_user(self):

        self.client.login(username='test_user', password='test_password')

        data = {
            'username': 'new_username',
            'avatarUpload': 'path/to/new_avatar.jpg'
        }

        response = self.client.post(reverse('user_edit'), data=data, format='multipart')

        pdb.set_trace()

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user'))

        updated_user = User.objects.get(pk=self.user.pk)


        self.assertEqual(updated_user.username, 'new_username')
        self.assertEqual(updated_user.avatar.path,
                         'path/to/new_avatar.jpg')


