# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.urls import reverse
# from core.posting.models import Post
# from core.posting.factories import *

# class PostViewSetTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = UserFactory()
#         self.client.force_authenticate(user=self.user)

#     def test_create_post_with_image(self):
#         """
#         Testa se um post com imagem é criado corretamente.
#         """
#         # Define os dados do post
#         post_data = {
#             'text_content': 'Conteúdo do post',
#             # Aqui você deve substituir 'path/para/sua/imagem.jpg' pelo caminho da imagem que você deseja testar
#             'image_content': open('media/default-profile_pictures/default_profile_picture.png', 'rb'),
#         }

#         # Faz uma solicitação POST para criar o post
#         response = self.client.post(reverse('create_post'), post_data, format='multipart')

#         # Verifica se o código de status da resposta é 201 CREATED
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
#         import pdb
#         pdb.set_trace()
#         # Verifica se o post foi criado no banco de dados
#         self.assertTrue(Post.objects.filter(text_content='Conteúdo do post', author=self.user).exists())
