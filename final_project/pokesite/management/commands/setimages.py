from django.core.management.base import BaseCommand
from ._private import set_images


class Command(BaseCommand):
    help = 'Set an image for every Pokemon'

    def handle(self, *args, **options):
        set_images()
        self.stdout.write(self.style.SUCCESS("Images are set"))
