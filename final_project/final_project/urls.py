"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pokesite.views import BaseShowcase, TrainerAdd, PokemonDetails, PokemonBattle, PokemonBattleDetails, ChooseBattle, ToBeDone, \
                            SignUp, Login, CreateTrainer, Pokedex
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseShowcase.as_view(), name="main_page"),
    path('trainer/<trainer_name>/', TrainerAdd.as_view(), name="trainer"),
    path('pokedex/<pokemon_name>/', PokemonDetails.as_view(), name="pokemon_details"),
    path('trainer/<trainer_name>/battle/', ChooseBattle.as_view(), name="choose_battle"),
    path('trainer/<trainer_name>/battle/<pokemon_name>/details/', PokemonBattleDetails.as_view(), name="pokemon_battle_details"),
    path('trainer/<trainer_name>/battle/<pokemon_name>/', PokemonBattle.as_view(), name="pokemon_battle"),
    path('pokedex', Pokedex.as_view(), name="pokedex"),
    path('not-available-yet/', ToBeDone.as_view(), name="to_be_done"),
    path('register/', SignUp.as_view(), name="registration"),
    path('login/', Login.as_view(), name="login"),
    path('create-trainer/', CreateTrainer.as_view(), name="create_trainer"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
