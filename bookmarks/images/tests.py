from django.test import TestCase
from django.contrib.auth import get_user_model

from images.models import Image
from images.forms import ImageCreateForm


class ImageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="password"
        )
        self.image = Image.objects.create(
            title="Test", url="https://example.com/test.jpg", user=self.user
        )

    def test_image_creation(self):
        self.assertEqual(self.image.title, "Test")
        self.assertEqual(self.image.url, "https://example.com/test.jpg")
        self.assertEqual(self.image.user, self.user)

    def test_valid_form(self):
        form_data = {"title": "Valid", "url": "https://valid.com/image.jpg"}
        form = ImageCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {"title": "Invalid"}
        form = ImageCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
