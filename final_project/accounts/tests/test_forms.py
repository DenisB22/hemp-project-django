from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.test import TestCase

from final_project.accounts.forms import RegisterForm
from final_project.accounts.models import Account


class AccountRegisterFormTests(TestCase):
    def test_account_register_form_password_equal_confirm_password__expect_correct_result(self):
        data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'email': 'ivan.ivanov@gmail.com',
            'phone_number': '1234567890',
            'password': 'SomePassword123',
            'confirm_password': 'SomePassword123'
        }

        form = RegisterForm(data)

        self.assertTrue(form.is_valid())

    def test_account_register_form_password_not_equal_confirm_password__expect_correct_result(self):
        data = {
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'email': 'ivan.ivanov@gmail.com',
            'phone_number': '1234567890',
            'password': 'SomePassword123',
            'confirm_password': 'NotEqualPassword123'
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())

