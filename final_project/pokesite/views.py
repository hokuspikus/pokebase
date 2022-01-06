from django.db.models import Q
from django.shortcuts import render
from django.views import View
from pokesite.models import Trainer, Pokemon, TYPES
from pokesite.management.commands._private import default_attacks


class BaseShowcase(View):
    def get(self, request):
        return render(request, "base.html")


class TrainerAdd(View):
    def get(self, request, trainer_id):
        trainer = Trainer.objects.get(id=trainer_id)
        types = TYPES
        ctx = {
            "trainer": trainer,
            "types": types
        }
        return render(request, "trainer_add.html", ctx)

    def post(self, request, trainer_id):
        poke_type = request.POST.get('type')
        poke_second_type = request.POST.get('second_type')
        trainer = Trainer.objects.get(id=trainer_id)
        types = TYPES
        if poke_second_type == "":
            filtered_pokemon = Pokemon.objects.filter(Q(type=poke_type) |
                                                      Q(second_type=poke_type)).order_by('pokedex_number')
            ctx = {
                "trainer": trainer,
                "filtered": filtered_pokemon,
                "types": types,
                "chosen": poke_type
            }
        elif poke_type == "":
            filtered_pokemon = Pokemon.objects.filter(Q(type=poke_second_type) | Q(second_type=poke_second_type)).order_by('pokedex_number')
            ctx = {
                "trainer": trainer,
                "filtered": filtered_pokemon,
                "types": types,
                "chosen": poke_second_type
            }
        else:
            filtered_pokemon = Pokemon.objects.filter(Q(type=poke_type, second_type=poke_second_type) | Q(type=poke_second_type, second_type=poke_type)).order_by('pokedex_number')
            ctx = {
                "trainer": trainer,
                "filtered": filtered_pokemon,
                "types": types,
                "chosen": poke_type,
                "second_chosen": poke_second_type
            }
        return render(request, "trainer_add.html", ctx)


class PokemonDetails(View):
    def get(self, request, pokemon_name):
        pokemon = Pokemon.objects.get(name__iexact=pokemon_name)
        fast_attacks = []
        charged_attacks = []
        for item in default_attacks:
            if item['pokemon_id'] == pokemon.pokedex_number:
                for attack in item['fast_moves']:
                    if attack not in fast_attacks:
                        fast_attacks.append(attack)
                for attack in item['charged_moves']:
                    if attack not in charged_attacks:
                        charged_attacks.append(attack)
        return render(request, "pokemon_details.html", {"pokemon": pokemon, "fast_attacks": fast_attacks, "charged_attacks": charged_attacks})
