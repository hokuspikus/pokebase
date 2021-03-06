from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from pokesite.models import Trainer, Pokemon, TYPES
from pokesite.constant import CURRENT_MOVES, full_off, full_def, balanced, calculate_damage_effectiveness
from pokesite.forms import UserForm, LoginForm


class BaseShowcase(View):
    def get(self, request):
        return render(request, "base.html")


class TrainerAdd(View):
    def get(self, request, trainer_name):
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        types = TYPES
        ctx = {
            "trainer": trainer,
            "types": types
        }
        return render(request, "trainer_add.html", ctx)

    def post(self, request, trainer_name):
        poke_type = request.POST.get('type')
        poke_second_type = request.POST.get('second_type')
        trainer = Trainer.objects.get(name__iexact=trainer_name)
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
        type_effectiveness = []
        for type in TYPES:
            type_effectiveness.append((calculate_damage_effectiveness(type[1], pokemon), type[1]))
        very_resistant = []
        resistant = []
        weak = []
        very_weak = []
        for type in type_effectiveness:
            if type[0] < 0.4:
                very_resistant.append(type[1])
            elif 0.4 <= type[0] < 1:
                resistant.append(type[1])
            elif 1 < type[0] < 2:
                weak.append(type[1])
            elif type[0] >= 2:
                very_weak.append(type[1])
        for item in CURRENT_MOVES:
            if item['pokemon_id'] == pokemon.pokedex_number:
                for attack in item['fast_moves']:
                    if attack not in fast_attacks:
                        fast_attacks.append(attack)
                for attack in item['charged_moves']:
                    if attack not in charged_attacks:
                        charged_attacks.append(attack)
        return render(request, "pokemon_details.html", {"pokemon": pokemon, "fast_attacks": fast_attacks, "charged_attacks": charged_attacks,
                                                        "very_weak": very_weak, "weak": weak, "resistant": resistant, "very_resistant": very_resistant})


class PokemonBattleDetails(View):
    def get(self, request, pokemon_name, trainer_name):
        battle_pokemon = Pokemon.objects.get(name__iexact=pokemon_name)
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        ctx = {"trainer": trainer, "battle": battle_pokemon}
        return render(request, "trainer_battle_details.html", ctx)

    def post(self, request, pokemon_name, trainer_name):
        battle_pokemon = Pokemon.objects.get(name__iexact=pokemon_name)
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        mode = request.POST.get("mode")
        ctx = {"trainer": trainer, "battle": battle_pokemon}
        if mode == "offensive":
            suggestion_offensive = full_off(trainer.pokemon.all(), battle_pokemon)
            ctx["suggestion"] = suggestion_offensive
            return render(request, "trainer_battle_details.html", ctx)
        if mode == "defensive":
            suggestion_defensive = full_def(trainer.pokemon.all(), battle_pokemon)
            ctx["suggestion"] = suggestion_defensive
            return render(request, "trainer_battle_details.html", ctx)
        if mode == "balanced":
            suggestion_balanced = balanced(trainer.pokemon.all(), battle_pokemon)
            ctx["suggestion"] = suggestion_balanced
            return render(request, "trainer_battle_details.html", ctx)


class PokemonBattle(View):
    def get(self, request, pokemon_name, trainer_name):
        battle_pokemon = Pokemon.objects.get(name__iexact=pokemon_name)
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        ctx = {"trainer": trainer, "battle": battle_pokemon}
        return render(request, "trainer_battle.html", ctx)

    def post(self, request, pokemon_name, trainer_name):
        battle_pokemon = Pokemon.objects.get(name__iexact=pokemon_name)
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        mode = request.POST.get("mode")
        ctx = {"trainer": trainer, "battle": battle_pokemon}
        if mode == "offensive":
            suggestion_offensive = full_off(trainer.pokemon.all(), battle_pokemon)
            ctx["suggestion"] = suggestion_offensive
            return render(request, "trainer_battle.html", ctx)
        if mode == "defensive":
            suggestion_defensive = full_def(trainer.pokemon.all(), battle_pokemon)
            ctx["suggestion"] = suggestion_defensive
            return render(request, "trainer_battle.html", ctx)
        if mode == "balanced":
            suggestion_balanced = balanced(trainer.pokemon.all(), battle_pokemon)
            ctx["suggestion"] = suggestion_balanced
            return render(request, "trainer_battle.html", ctx)


class ChooseBattle(View):
    def get(self, request, trainer_name):
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        ctx = {"trainer": trainer}
        return render(request, "choose_battle.html", ctx)

    def post(self, request, trainer_name):
        trainer = Trainer.objects.get(name__iexact=trainer_name)
        to_search = request.POST.get("name")
        if to_search.isdigit():
            filtered = Pokemon.objects.filter(pokedex_number__contains=to_search).order_by('pokedex_number')
        else:
            filtered = Pokemon.objects.filter(name__icontains=to_search).order_by('pokedex_number')
        ctx = {"trainer": trainer, "filtered": filtered}
        return render(request, "choose_battle.html", ctx)


class ToBeDone(View):
    def get(self, request):
        return render(request, "to_be_done.html")


class SignUp(View):
    def get(self, request):
        user_form = UserForm()
        return render(request, "sign_up.html", {"user_form": user_form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if password == repeat_password:
                User.objects.create_user(username=username, email=email, password=password)
                message = "Your account has been created"
                return render(request, "sign_up.html", {"user_form": form, "message": message})
        else:
            error = "Passwords are not the same"
            return render(request, "sign_up.html", {"user_form": form, "error": error})


class Login(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {"login_form": login_form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("create_trainer")
            else:
                error = "Wrong username or password"
                return render(request, 'login.html', {"login_form": form, "error": error})
        else:
            error = "Something is wrong with your credentials"
            return render(request, 'login.html', {"login_form": form, "error": error})


class CreateTrainer(View):
    def get(self, request):
        return render(request, 'create_trainer.html')


class Pokedex(View):
    def get(self, request):
        pokedex = Pokemon.objects.all().order_by('pokedex_number')
        return render(request, 'pokedex.html', {"pokedex": pokedex})
