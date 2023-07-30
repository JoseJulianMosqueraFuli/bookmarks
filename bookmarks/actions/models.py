from django.db import models


class Action(models.Model):
    user = models.ForeignKey(
        "auth.User",
        related_name="action",
        on_delete=models.CASCADE,
    )
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
        ]
        ordering = ["-created"]
