from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    username = "user"
    password = "1234"

    help = f"Create user with username={username} and password={password}"

    def handle(self, *args, **options):
        if not User.objects.filter(username=self.username).exists():
            User.objects.create_user(username=self.username, password=self.password)
            print(
                f'User with username="{self.username}" and password="{self.password}" created succesfully'
            )
        else:
            print(f'User with username="{self.username}" has already been created')
