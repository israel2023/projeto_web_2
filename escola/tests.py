from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        # Teste de login bem-sucedido
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)

        # Verifique se o usuário está logado
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)

        # Teste de logout bem-sucedido
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  
        # Verifique se é redirecionado para a página de login após o logout

        # Verifique se o usuário está desconectado
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_access_restricted_page(self):
        # Teste se um usuário não autenticado é redirecionado para a página de login
        response = self.client.get('/restricted/')
        self.assertEqual(response.status_code, 302)  
        # Verifique se é redirecionado para a página de login

        # Faça login primeiro
        self.client.login(username=self.username, password=self.password)

        # Teste se um usuário autenticado pode acessar a página restrita
        response = self.client.get('/restricted/')
        self.assertEqual(response.status_code, 200)
        # Verifique se a resposta é 200 OK
