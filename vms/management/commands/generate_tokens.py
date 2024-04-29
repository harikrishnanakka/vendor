from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from vms.utils import generate_token

class Command(BaseCommand):
    help = 'Generate tokens for users'

    def handle(self, *args, **options):
        username = input("Enter username: ")
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            self.stdout.write(self.style.ERROR(f"User '{username}' does not exist."))
            return

        # Generate a token for the user
        try:
            token = generate_token(user)
            self.stdout.write(self.style.SUCCESS(f"Token generated for user {user.username}: {token}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred during token generation: {e}"))
