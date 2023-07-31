from .models import Action


def create_action(user, verb, target=None):
    action = Action(user=user, verb=verb, targe=target)
    action.save()
