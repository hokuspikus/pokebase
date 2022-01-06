from django.core.management.base import BaseCommand
from ._private import populate_pokedex, pokemon, populate_pokedex_semimanually


class Command(BaseCommand):
    help = 'Populates Pokedex with every Pokemon having regular form'

    def handle(self, *args, **options):
        populate_pokedex_semimanually()
        populate_pokedex(pokemon[:854])
        self.stdout.write(self.style.SUCCESS("Pokedex entries complete"))
