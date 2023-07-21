from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="images_created",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    url = models.ImageField(max_length=2000)
    image = models.ImageField(upload_to="images_uploaded")
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "image"
        indexes = [
            models.Index(fields=["-created"]),
        ]
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def generate_unique_slug_on_save(self):
        if not self.slug:
            self.slug = slugify(self.title)

    def save(self, *args, **kwargs):
        self.generate_unique_slug_on_save()
        super().save(*args, **kwargs)
