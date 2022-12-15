from django.contrib.auth import get_user, get_user_model
from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import reverse

from final_project.accounts.forms import RegisterForm
from final_project.accounts.models import Account, UserProfile
import json


UserModel = get_user_model()

class TestView(TestCase):

    def setUp(self):
        # self.client = Client()
        self.register_user_url = reverse('register_user')
        self.login_user_url = reverse('login_user')

    def test_register_user_GET(self):
        response = self.client.get(self.register_user_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_user_POST_creates_new_user(self):
        first_name = 'Ivan'
        last_name = 'Ivanov'
        phone_number = '1234567890'
        email = 'test@gmail.com'
        password = 'MyTestPassword123'
        username = 'test'

        user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                           password=password)

        user.phone_number = phone_number
        self.assertEqual(Account.objects.first().first_name, 'Ivan')

        # response = self.client.post(self.register_user_url, {
        #     'first_name': 'Peter',
        #     'last_name': 'Petrov',
        #     'phone_number': '0987654321',
        #     'email': 'peter@gmail.com',
        #     'password': 'TestPassword123',
        #     'username': 'peter',
        # })

        self.assertEqual(Account.objects.first().first_name, 'Ivan')

    def test_login_user_GET(self):
        response = self.client.get(self.login_user_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')







