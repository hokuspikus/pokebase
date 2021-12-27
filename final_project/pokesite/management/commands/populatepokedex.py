from django.core.management.base import BaseCommand
from ._private import populate_pokedex, pokemon


class Command(BaseCommand):
    help = 'Populates Pokedex with every Pokemon'

    def handle(self, *args, **options):
        populate_pokedex(pokemon)
        self.stdout.write(self.style.SUCCESS("Pokedex entries complete"))
