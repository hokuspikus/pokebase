from django.db import models
from django.contrib.auth.models import User

TYPES = (
    ("nor", "normal"),
    ("fig", "fighting"),
    ("fly", "flying"),
    ("gro", "ground"),
    ("roc", "rock"),
    ("bug", "bug"),
    ("gho", "ghost"),
    ("ste", "steel"),
    ("fir", "fire"),
    ("wat", "water"),
    ("gra", "grass"),
    ("ele", "electric"),
    ("psy", "psychic"),
    ("ice", "ice"),
    ("dra", "dragon"),
    ("fai", "fairy"),
    ("dar", "dark"),
)

TEAMS = (
    ("yel", "Instinct"),
    ("blu", "Mystic"),
    ("red", "Valor"),
)
# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=32, unique=True)
    pokedex_number = models.IntegerField(unique=True)
    type = models.CharField(max_length=4, choices=TYPES)
    second_type = models.CharField(max_length=4, choices=TYPES, null=True, blank=True)
    evolves_from = models.ForeignKey("Pokemon", on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True)
    image_shiny = models.ImageField(null=True)
    fast_attack = models.ForeignKey("FastAttack", on_delete=models.DO_NOTHING, null=True)
    charged_attack = models.ForeignKey("ChargedAttack", on_delete=models.DO_NOTHING, null=True, related_name="primary_attack")
    second_charged_attack = models.ForeignKey("ChargedAttack", on_delete=models.DO_NOTHING, null=True, related_name="secondary_attack")


class FastAttack(models.Model):
    name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=4, choices=TYPES)
    power = models.IntegerField()


class ChargedAttack(models.Model):
    name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=4, choices=TYPES)
    power = models.IntegerField()


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    team = models.CharField(max_length=4, choices=TEAMS)
    pokemon = models.ManyToManyField("Pokemon", through="TrainerPokemon")


class TrainerPokemon(models.Model):
    trainer = models.ForeignKey("Trainer", on_delete=models.CASCADE)
    pokemon = models.ForeignKey("Pokemon", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    is_shiny = models.BooleanField()




