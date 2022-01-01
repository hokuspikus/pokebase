from django.db.models import Q
from django.shortcuts import render
from django.views import View
from pokesite.models import Trainer, Pokemon, TYPES
# Create your views here.


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
        if poke_second_type == "":
            trainer = Trainer.objects.get(id=trainer_id)
            types = TYPES
            filtered_pokemon = Pokemon.objects.filter(Q(type=poke_type) &
                                                      Q(second_type=poke_type)).order_by('pokedex_number')
            ctx = {
                "trainer": trainer,
                "filtered": filtered_pokemon,
                "types": types,
                "chosen": poke_type
            }
        else:
            trainer = Trainer.objects.get(id=trainer_id)
            types = TYPES
            filtered_pokemon = Pokemon.objects.filter(Q(type=poke_type) & Q(second_type=poke_second_type) |
                                                      Q(type=poke_second_type) & Q(second_type=poke_type)).order_by(
                                                      'pokedex_number'),
            ctx = {
                "trainer": trainer,
                "filtered": filtered_pokemon,
                "types": types,
                "chosen": poke_type,
                "second_chosen": poke_second_type
            }
        return render(request, "trainer_add.html", ctx)
