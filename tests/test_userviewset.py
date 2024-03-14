# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from core.posting.models import User
# from core.posting.factories import UserFactory
#
#
# class UserViewSetTestCase(APITestCase):
#
#     client = APIClient()
#
#     def setUp(self):
#         self.user = UserFactory()
#         self.list_url = reverse('account-list')
#         self.detail_url = reverse('account-detail', kwargs={'pk': self.user.pk})
#
#
#     # def test_list(self):
#     #     response = self.client.get(self.list_url)
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(len(response.data), 1)  # Verifica se apenas um usuário está na lista
#
#     def test_retrieve(self):
#         response = self.client.get(self.detail_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['username'], self.user.username)  # Verifica se os dados do usuário estão corretos
#
#         import pdb
#         pdb.set_trace()
#
#     def test_create(self):
#         data = {'complete_name': 'Novo Usuário', 'username': 'novo_usuario', 'email': 'novo_usuario@example.com',
#                 'birthday': '1990-01-01'}
#         response = self.client.post(self.list_url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 2)  # Verifica se o usuário foi criado no banco de dados
#         import pdb
#         pdb.set_trace()
#
#     def test_update(self):
#         data = {'complete_name': 'Usuário Atualizado', 'username': 'usuario_atualizado',
#                 'email': 'usuario_atualizado@example.com', 'birthday': '1990-01-01'}
#         response = self.client.put(self.detail_url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.complete_name, 'Usuário Atualizado')  # Verifica se o usuário foi atualizado
#
#         import pdb
#         pdb.set_trace()
#
#     def test_partial_update(self):
#         data = {'email': 'novo_email@example.com'}
#         response = self.client.patch(self.detail_url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.user.refresh_from_db()
#         self.assertEqual(self.user.email,
#                          'novo_email@example.com')  # Verifica se a atualização parcial foi bem-sucedida
#         import pdb
#         pdb.set_trace()
#
#     def test_delete(self):
#         response = self.client.delete(self.detail_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(
#             User.objects.filter(pk=self.user.pk).exists())  # Verifica se o usuário foi removido do banco de dados
#         import pdb
#         pdb.set_trace()
