from django.db import models
from django.contrib.auth.models import User

TYPES = (
    ("nor", "Normal"),
    ("fig", "Fighting"),
    ("fly", "Flying"),
    ("gro", "Ground"),
    ("roc", "Rock"),
    ("bug", "Bug"),
    ("gho", "Ghost"),
    ("ste", "Steel"),
    ("fir", "Fire"),
    ("wat", "Water"),
    ("gra", "Grass"),
    ("ele", "Electric"),
    ("psy", "Psychic"),
    ("ice", "Ice"),
    ("dra", "Dragon"),
    ("fai", "Fairy"),
    ("dar", "Dark"),
    ("poi", "Poison"),
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
    evolves_from = models.ForeignKey("Pokemon", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    image_shiny = models.ImageField(blank=True, null=True)
    fast_attack = models.ForeignKey("FastAttack", on_delete=models.DO_NOTHING, blank=True, null=True,
                                    related_name="default_primary")
    charged_attack = models.ForeignKey("ChargedAttack", on_delete=models.DO_NOTHING, blank=True, null=True,
                                       related_name="default_secondary")

    def __str__(self):
        return f"{self.name} #{self.pokedex_number}"


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
    is_shiny = models.BooleanField(default=False)
    fast_attack = models.ForeignKey("FastAttack", on_delete=models.DO_NOTHING, blank=True, null=True)
    charged_attack = models.ForeignKey("ChargedAttack", on_delete=models.DO_NOTHING, blank=True, null=True,
                                       related_name="default")
    second_charged_attack = models.ForeignKey("ChargedAttack", on_delete=models.DO_NOTHING, blank=True, null=True,
                                              related_name="optional")
