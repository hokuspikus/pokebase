from django.core.management.base import BaseCommand
from ._private import set_default_fast_attacks, set_default_charged_attacks, default_attacks


class Command(BaseCommand):
    help = 'Sets default attacks for every Pokemon'

    def handle(self, *args, **options):
        set_default_fast_attacks(default_attacks)
        set_default_charged_attacks(default_attacks)
        self.stdout.write(self.style.SUCCESS("Default attacks set"))
