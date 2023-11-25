from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import User


class CustomUserTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="user@email.com",
            password="testpass123",
        )
        self.assertEqual(user.email, "user@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            email="user@email.com",
            password="testpass123",
        )
        self.assertEqual(admin_user.email, "user@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
