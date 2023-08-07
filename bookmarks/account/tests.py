from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from account.models import Profile, Contact


class RegisterViewTests(TestCase):
    def test_register_page(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/register.html")

    def test_register_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "testuser",
                "email": "test@example.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        user = get_user_model().objects.last()
        self.assertEqual(user.username, "testuser")
        self.assertRedirects(response, reverse("register_done"))


class LoginViewTests(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_login(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="testpass123"
        )
        response = self.client.post(
            reverse("login"), {"username": "testuser", "password": "testpass123"}
        )
        self.assertRedirects(response, reverse("dashboard"))


class UserFollowViewTests(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="user1", password="pass123"
        )
        self.user2 = get_user_model().objects.create_user(
            username="user2", password="pass123"
        )

    def test_follow_user(self):
        self.client.login(username="user1", password="pass123")
        response = self.client.post(
            reverse("user_follow"), {"id": self.user2.id, "action": "follow"}
        )
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(response.status_code, 200)
