from django.core.exceptions import ValidationError
from django.test import TestCase
from apps.users.models import User


USER_NAME = 'test_user'
USER_PASSWORD = 'pass@123'
USER_EMAIL = 'admin@mail.ru'

SUPERUSER_NAME = 'test_superuser'
SUPERUSER_PASSWORD = 'superpass@123'
SUPERUSER_EMAIL = 'superadmin@mail.ru'


class UserTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username=USER_NAME, email=USER_EMAIL, password=USER_PASSWORD)
        self.super_user = User.objects.create_superuser(
            username=SUPERUSER_NAME,
            email=SUPERUSER_PASSWORD,
            password=SUPERUSER_EMAIL
        )

    def test_simple_user(self):
        """Проверка создания простого пользователя"""
        user = User.objects.filter(username=self.user.username, email=self.user.email).first()
        self.assertEqual(user, self.user)
        self.assertNotEqual(user.password, USER_PASSWORD)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_active, True)

    def test_super_user(self):
        """Проверка создания суперпользователя"""
        super_user = User.objects.filter(username=self.super_user.username, email=self.super_user.email).first()
        self.assertEqual(super_user, self.super_user)
        self.assertNotEqual(super_user.password, SUPERUSER_PASSWORD)
        self.assertEqual(super_user.is_staff, True)
        self.assertEqual(super_user.is_superuser, True)
        self.assertEqual(super_user.is_active, True)

    def test_user_without_email(self):
        """Проверка создания без почты"""
        with self.assertRaises(TypeError):
            User.objects.create_user(
                username=USER_NAME + '1',
                password=USER_PASSWORD,
            )

    def test_user_without_username(self):
        """Проверка создания без юзернейма"""

        with self.assertRaises(TypeError):
            user = User.objects.create_superuser(
                email='1' + USER_EMAIL,
                password=USER_PASSWORD,
            )
