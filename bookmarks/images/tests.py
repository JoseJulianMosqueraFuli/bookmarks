from django.test import TestCase
from django.urls import reverse

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


class ImageListViewTests(TestCase):
    def test_paginate_images(self):
        # Create lots of test images
        num_images = 10
        for i in range(num_images):
            Image.objects.create(
                title="Test %d" % i, url="https://example.com/", user=user
            )

        response = self.client.get("/images/")
        self.assertEqual(response.status_code, 200)

        # Check paginator context variable
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["images"]), 4)  # 4 per page


class ImageDetailViewTests(TestCase):
    def test_image_likes(self):
        user = get_user_model().objects.create_user(username="test", password="pass")
        image = Image.objects.create(
            title="Test", url="https://example.com/", user=user
        )
        response = self.client.post("/images/1/like/", {"id": image.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(image.users_like.count(), 1)
        self.assertTrue(user in image.users_like.all())


class ImageCreateViewTests(TestCase):
    def test_image_create_view(self):
        # Login as user
        self.client.login(username="user", password="password")

        # Send POST request
        response = self.client.post(
            reverse("image_create"),
            {"title": "Test Title", "url": "https://test.com/image.jpg"},
        )

        # Check redirect to detail page
        image = Image.objects.get(title="Test Title")
        self.assertRedirects(response, image.get_absolute_url())

        # Check new image created
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.first().title, "Test Title")


class ImageRankingViewTests(TestCase):
    def test_ranking_view(self):
        # Add test ranking data
        r.zadd("image_ranking", {1: 10, 2: 30, 3: 20})  # id: ranking score

        response = self.client.get(reverse("image_ranking"))
        self.assertEqual(response.status_code, 200)

        # Check ranking order
        first_id = response.context["most_viewed"][0].id
        self.assertEqual(first_id, 2)

        second = response.context["most_viewed"][1].id
        self.assertEqual(second, 3)
