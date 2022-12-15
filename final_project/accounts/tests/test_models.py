from django.core.exceptions import ValidationError
from django.test import TestCase

from final_project.accounts.models import Account


class AccountModelTests(TestCase):
    # 3A - Arrange, Act, Assert
    #     Setup,    Do,   Check Result
    def test_account_save__when_first_name_is_valid__expect_correct_result(self):
        # Arrange
        account = Account(
            first_name='Ivan',
            last_name='Ivanov',
            username='ivan',
            email='ivan.ivanov@gmail.com',
            phone_number='1234567890',
            password='SomePassword123'

        )

        # Act
        account.full_clean()  # Call this for validation
        account.save()

        # Assert
        self.assertIsNotNone(account.pk)

    def test_account_save__when_first_name_has_invalid_length__expect_exception(self):
        # Arrange
        account = Account(
            first_name='IvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvanIvan',
            last_name='Ivanov',
            username='ivan',
            email='ivan.ivanov@gmail.com',
            phone_number='1234567890',
            password='SomePassword123'

        )


        # Assert & Act
        with self.assertRaises(ValidationError) as context:
            account.full_clean()  # Call this for validation
            account.save()

        self.assertIsNotNone(context.exception)

    def test_account_save__when_account_is_superuser__expect_correct_result(self):
        # Arrange
        account = Account(
            first_name='Ivan',
            last_name='Ivanov',
            username='ivan',
            email='ivan.ivanov@gmail.com',
            phone_number='1234567890',
            password='SomePassword123'

        )

        account.is_admin = True
        account.is_active = True
        account.is_staff = True
        account.is_superadmin = True

        # Act
        account.full_clean()  # Call this for validation
        account.save()

        # Assert
        self.assertTrue(account.is_admin)
        self.assertTrue(account.is_active)
        self.assertTrue(account.is_staff)
        self.assertTrue(account.is_superadmin)