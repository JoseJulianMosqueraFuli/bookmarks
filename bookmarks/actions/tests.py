from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from actions.models import Action
from actions.utils import create_action


class ActionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", password="password"
        )
        self.target = "Target object"

    def test_create_action(self):
        """Test creating a new action"""
        create_action(self.user, "followed", self.target)
        self.assertEqual(Action.objects.count(), 1)
        action = Action.objects.first()
        self.assertEqual(action.user, self.user)
        self.assertEqual(action.verb, "followed")
        self.assertEqual(action.target, self.target)

    def test_avoid_duplicate_actions(self):
        """Test that duplicate actions are not created"""
        create_action(self.user, "followed", self.target)
        create_action(self.user, "followed", self.target)
        self.assertEqual(Action.objects.count(), 1)

    def test_action_time_limit(self):
        """Test actions are not created within 60 second limit"""
        created = timezone.now() - timezone.timedelta(seconds=59)
        with self.settings(TIME_ZONE="UTC"):
            action = Action.objects.create(
                user=self.user, verb="followed", target=self.target, created=created
            )

        create_action(self.user, "followed", self.target)
        self.assertEqual(Action.objects.count(), 1)
        self.assertEqual(Action.objects.first().id, action.id)
