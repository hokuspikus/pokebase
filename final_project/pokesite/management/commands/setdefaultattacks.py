from django.core.management.base import BaseCommand
from ._private import set_default_fast_attacks, set_default_charged_attacks, default_attacks, set_default_attacks_to_manually_entered_pokemon


class Command(BaseCommand):
    help = 'Sets default attacks for every Pokemon'

    def handle(self, *args, **options):
        set_default_fast_attacks(default_attacks[:853])
        set_default_charged_attacks(default_attacks[:853])
        set_default_attacks_to_manually_entered_pokemon()
        self.stdout.write(self.style.SUCCESS("Default attacks set"))
