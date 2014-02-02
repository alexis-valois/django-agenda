from django.test import TestCase, Client
from django.contrib.auth.models import User

class StatusTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_public(self):
        urls = [
            {'url': '/accounts/login/', 'status': 200, 'template': 'registration/login.html'},
            {'url': '/accounts/logout/', 'status': 302, 'template': 'registration/login.html'},
            {'url': '/accounts/profile/', 'status': 302, 'template': 'registration/login.html'},
        ]
        for elem in urls:
            response = self.client.get(elem['url'])
            self.assertEquals(response.status_code, elem['status'])

            response = self.client.get(elem['url'], follow=True)
            self.assertEquals(response.template_name, elem['template'])

    def generate_user(self, username):
        response = self.client.post('/user/create_account/', {
            'username': username,
            'password1': 'trytoguess',
            'password2': 'trytoguess',
        }, follow=True)
        return response

    def test_create_user(self):
        response = self.generate_user(username="johntest")
        self.assertEquals(response.template_name, ['user/succes.html'])
        user = User.objects.get(username="johntest")
        self.assertEquals(user.username, 'johntest')


    def test_login(self):
        self.generate_user(username='randomguy')
        response = self.client.post('/accounts/login/', {
            'username': 'randomguy',
            'password': 'trytoguess',
        }, follow=True)
        self.assertEquals(response.template_name, ['registration/profile.html'])
