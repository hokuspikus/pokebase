from django.core.management.base import BaseCommand
from ._private import populate_fast_attacks, populate_charged_attacks, fast_attacks, charged_attacks


class Command(BaseCommand):
    help = 'Populates DB with every existing fast and charged move'

    def handle(self, *args, **options):
        populate_fast_attacks(fast_attacks)
        populate_charged_attacks(charged_attacks)
        self.stdout.write(self.style.SUCCESS("Transfer complete"))
