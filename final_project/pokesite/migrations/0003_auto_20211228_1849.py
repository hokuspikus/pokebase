# Generated by Django 3.2.10 on 2021-12-28 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokesite', '0002_alter_pokemon_evolves_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='second_charged_attack',
        ),
        migrations.AddField(
            model_name='trainerpokemon',
            name='charged_attack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='charged_attack', to='pokesite.chargedattack'),
        ),
        migrations.AddField(
            model_name='trainerpokemon',
            name='fast_attack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pokesite.fastattack'),
        ),
        migrations.AddField(
            model_name='trainerpokemon',
            name='second_charged_attack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='alternative_attack', to='pokesite.chargedattack'),
        ),
        migrations.AlterField(
            model_name='chargedattack',
            name='type',
            field=models.CharField(choices=[('nor', 'Normal'), ('fig', 'Fighting'), ('fly', 'Flying'), ('gro', 'Ground'), ('roc', 'Rock'), ('bug', 'Bug'), ('gho', 'Ghost'), ('ste', 'Steel'), ('fir', 'Fire'), ('wat', 'Water'), ('gra', 'Grass'), ('ele', 'Electric'), ('psy', 'Psychic'), ('ice', 'Ice'), ('dra', 'Dragon'), ('fai', 'Fairy'), ('dar', 'Dark'), ('poi', 'Poison')], max_length=4),
        ),
        migrations.AlterField(
            model_name='fastattack',
            name='type',
            field=models.CharField(choices=[('nor', 'Normal'), ('fig', 'Fighting'), ('fly', 'Flying'), ('gro', 'Ground'), ('roc', 'Rock'), ('bug', 'Bug'), ('gho', 'Ghost'), ('ste', 'Steel'), ('fir', 'Fire'), ('wat', 'Water'), ('gra', 'Grass'), ('ele', 'Electric'), ('psy', 'Psychic'), ('ice', 'Ice'), ('dra', 'Dragon'), ('fai', 'Fairy'), ('dar', 'Dark'), ('poi', 'Poison')], max_length=4),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='second_type',
            field=models.CharField(blank=True, choices=[('nor', 'Normal'), ('fig', 'Fighting'), ('fly', 'Flying'), ('gro', 'Ground'), ('roc', 'Rock'), ('bug', 'Bug'), ('gho', 'Ghost'), ('ste', 'Steel'), ('fir', 'Fire'), ('wat', 'Water'), ('gra', 'Grass'), ('ele', 'Electric'), ('psy', 'Psychic'), ('ice', 'Ice'), ('dra', 'Dragon'), ('fai', 'Fairy'), ('dar', 'Dark'), ('poi', 'Poison')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('nor', 'Normal'), ('fig', 'Fighting'), ('fly', 'Flying'), ('gro', 'Ground'), ('roc', 'Rock'), ('bug', 'Bug'), ('gho', 'Ghost'), ('ste', 'Steel'), ('fir', 'Fire'), ('wat', 'Water'), ('gra', 'Grass'), ('ele', 'Electric'), ('psy', 'Psychic'), ('ice', 'Ice'), ('dra', 'Dragon'), ('fai', 'Fairy'), ('dar', 'Dark'), ('poi', 'Poison')], max_length=4),
        ),
        migrations.AlterField(
            model_name='trainerpokemon',
            name='is_shiny',
            field=models.BooleanField(default=False),
        ),
    ]
