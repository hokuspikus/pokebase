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


def populate_pokedex_semimanually():
    Pokemon.objects.create(name="Burmy", pokedex_number=412, type="bug")
    Pokemon.objects.create(name="Wormadam", pokedex_number=413, type="bug", second_type="gra")
    Pokemon.objects.create(name="Cherrim", pokedex_number=421, type="gra")
    Pokemon.objects.create(name="Shellos", pokedex_number=422, type="wat")
    Pokemon.objects.create(name="Gastrodon", pokedex_number=423, type="wat", second_type="gro")
    Pokemon.objects.create(name="Giratina", pokedex_number=487, type="gho", second_type="dra")
    Pokemon.objects.create(name="Shaymin", pokedex_number=492, type="gra", second_type="fly")
    Pokemon.objects.create(name="Basculin", pokedex_number=550, type="wat")
    Pokemon.objects.create(name="Darmanitan", pokedex_number=555, type="fir")
    Pokemon.objects.create(name="Deerling", pokedex_number=585, type="nor", second_type="gra")
    Pokemon.objects.create(name="Sawsbuck", pokedex_number=586, type="nor", second_type="gra")
    Pokemon.objects.create(name="Tornadus", pokedex_number=641, type="fly")
    Pokemon.objects.create(name="Thundurus", pokedex_number=642, type="ele", second_type="fly")
    Pokemon.objects.create(name="Landorus", pokedex_number=645, type="gro", second_type="fly")
    Pokemon.objects.create(name="Keldeo", pokedex_number=647, type="wat", second_type="fig")
    Pokemon.objects.create(name="Meloetta", pokedex_number=648, type="nor", second_type="psy")
    Pokemon.objects.create(name="Furfrou", pokedex_number=676, type="nor")
    Pokemon.objects.create(name="Pumpkaboo", pokedex_number=710, type="gho", second_type="gra")
    Pokemon.objects.create(name="Gourgeist", pokedex_number=711, type="gho", second_type="gra")
    Pokemon.objects.create(name="Hoopa", pokedex_number=720, type="psy", second_type="dar")


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


def change_attacks_to_pokemon(pokedex_number, charged_attack, fast_attack):
    poke = Pokemon.objects.get(pokedex_number=pokedex_number)
    poke.charged_attack = ChargedAttack.objects.get(name=charged_attack)
    poke.fast_attack = FastAttack.objects.get(name=fast_attack)
    poke.save()


def set_default_attacks_to_manually_entered_pokemon():
    change_attacks_to_pokemon(412, "Struggle", "Tackle")
    change_attacks_to_pokemon(413, "Bug Buzz", "Bug Bite")
    change_attacks_to_pokemon(421, "Dazzling Gleam", "Razor Leaf")
    change_attacks_to_pokemon(422, "Water Pulse", "Mud Slap")
    change_attacks_to_pokemon(423, "Water Pulse", "Mud Slap")
    change_attacks_to_pokemon(487, "Dragon Claw", "Dragon Breath")
    change_attacks_to_pokemon(492, "Energy Ball", "Zen Headbutt")
    change_attacks_to_pokemon(550, "Aqua Jet", "Tackle")
    change_attacks_to_pokemon(555, "Overheat", "Tackle",)
    change_attacks_to_pokemon(585, "Energy Ball", "Tackle")
    change_attacks_to_pokemon(586, "Megahorn", "Feint Attack")
    change_attacks_to_pokemon(641, "Grass Knot", "Bite")
    change_attacks_to_pokemon(642, "Sludge Wave", "Bite")
    change_attacks_to_pokemon(645, "Earthquake", "Mud Shot")
    change_attacks_to_pokemon(647, "Aqua Jet", "Poison Jab")
    change_attacks_to_pokemon(648, "Psyshock", "Quick Attack")
    change_attacks_to_pokemon(676, "Surf", "Take Down")
    change_attacks_to_pokemon(710, "Grass Knot", "Astonish")
    change_attacks_to_pokemon(711, "Seed Bomb", "Hex")
    change_attacks_to_pokemon(720, "Shadow Ball", "Confusion")


def set_images():
    for i in range(1, 721):
        poke = Pokemon.objects.get(pokedex_number=i)
        poke.image = f'images/{i}.png'
        poke.save()

