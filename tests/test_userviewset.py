import json
import pdb

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from core.posting.factories import UserFactory
from core.posting.models import User, ProfilePicture
from rest_framework.authtoken.models import Token


class TestUserViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = User.objects.create(username='test_user', email='test@example.com', birthday='2001-01-01')
        self.user.set_password('test_password')
        self.user.save()
        self.profile_picture = ProfilePicture.objects.create(user=self.user)
        # print(f'{self.user.username} {self.user.email}')

    def test_get_user(self):
        response = self.client.get(reverse('account-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_data = json.loads(response.content)

        self.assertEqual(user_data[0]['username'], self.user.username)

    def test_signup_default_profile_picture(self):
        url = reverse('account-list')
        data = {
            'complete_name': 'John Doe',
            'email': 'johndoe@example.com',
            'birthday': '1990-01-01',
            'username': 'johndoe',
            'password': 'password123',
        }
        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.content[])

        user = User.objects.get(email='johndoe@example.com')
        profile_pic = ProfilePicture.objects.create(user=user)

        self.assertEqual(user.profile_picture.profile_picture.url, '/media/default_profile_picture/default_profile_picture.png')


    def test_edit_user(self):
        
        pdb.set_trace()
        # self.client.login()
        

        data = {
            'username': 'new_username',
            'birthday': self.user.birthday,
            'email': self.user.email,
            'complete_name': 'Mateus Diniz'
        }

        response = self.client.put('/posting/account/'+ str(self.user.pk) +'/', data=data, format='multipart')

        user_profi_pic, created = ProfilePicture.objects.get_or_create(user=self.user)
        user_profi_pic.profile_picture.name = 'path/to/new_profile_picture.jpg'
        user_profi_pic.save()

        pdb.set_trace()

        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, reverse('user'))

        updated_user = User.objects.get(pk=self.user.pk)


        self.assertEqual(updated_user.username, 'new_username')
        pdb.set_trace()
        self.assertEqual(updated_user.profile_picture.profile_picture.name, 'path/to/new_profile_picture.jpg')


