import json
from urllib.request import urlopen
from pokesite.models import TYPES, Pokemon, FastAttack, ChargedAttack

with urlopen("https://pogoapi.net/api/v1/pokemon_types.json") as poketypes:
    source = poketypes.read()

pokemon = json.loads(source)


def shorten_type(type):
    for i in TYPES:
        if type in i:
            return i[0]


def populate_pokedex(my_dict):
    for poke in my_dict:
        if poke['form'] == "Normal":
            pokemon_name = poke['pokemon_name']
            pokedex_number = poke['pokemon_id']
            pokemon_type_base = poke['type'][0]
            pokemon_type = shorten_type(pokemon_type_base)
            if len(poke['type']) > 1:
                pokemon_second_type_base = poke['type'][1]
                pokemon_second_type = shorten_type(pokemon_second_type_base)
                Pokemon.objects.create(name=pokemon_name, pokedex_number=pokedex_number, type=pokemon_type,
                                       second_type=pokemon_second_type)
            else:
                Pokemon.objects.create(name=pokemon_name, pokedex_number=pokedex_number, type=pokemon_type)


with urlopen("https://pogoapi.net/api/v1/fast_moves.json") as fasts:
    source2 = fasts.read()

fast_attacks = json.loads(source2)


def populate_fast_attacks(my_dict):
    for attack in my_dict:
        name = attack['name']
        power = attack['power']
        attack_type = shorten_type(attack['type'])
        FastAttack.objects.create(name=name, power=power, type=attack_type)


with urlopen("https://pogoapi.net/api/v1/charged_moves.json") as chargeds:
    source3 = chargeds.read()

charged_attacks = json.loads(source3)


def populate_charged_attacks(my_dict):
    for attack in my_dict:
        name = attack['name']
        power = attack['power']
        attack_type = shorten_type(attack['type'])
        ChargedAttack.objects.create(name=name, power=power, type=attack_type)


with urlopen("https://pogoapi.net/api/v1/current_pokemon_moves.json") as current_attacks:
    source4 = current_attacks.read()

default_attacks = json.loads(source4)


def set_default_fast_attacks(my_dict):
    for entry in my_dict:
        if entry['form'] == "Normal":
            if len(entry['fast_moves']) >= 1:
                fast_move = entry['fast_moves'][0]
                pokedex_number = entry['pokemon_id']
                poke = Pokemon.objects.get(pokedex_number=pokedex_number)
                default_fast_move = FastAttack.objects.get(name=fast_move)
                poke.fast_attack = default_fast_move
                poke.save()
            else:
                pass


def set_default_charged_attacks(my_dict):
    for entry in my_dict:
        if entry['form'] == "Normal":
            if len(entry['charged_moves']) >= 1:
                charged_move = entry['charged_moves'][0]
                pokedex_number = entry['pokemon_id']
                poke = Pokemon.objects.get(pokedex_number=pokedex_number)
                default_charged_move = ChargedAttack.objects.get(name=charged_move)
                poke.charged_attack = default_charged_move
                poke.save()
            else:
                pass
