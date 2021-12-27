# Generated by Django 3.2.10 on 2021-12-19 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargedAttack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('type', models.CharField(choices=[('nor', 'normal'), ('fig', 'fighting'), ('fly', 'flying'), ('gro', 'ground'), ('roc', 'rock'), ('bug', 'bug'), ('gho', 'ghost'), ('ste', 'steel'), ('fir', 'fire'), ('wat', 'water'), ('gra', 'grass'), ('ele', 'electric'), ('psy', 'psychic'), ('ice', 'ice'), ('dra', 'dragon'), ('fai', 'fairy'), ('dar', 'dark')], max_length=4)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FastAttack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('type', models.CharField(choices=[('nor', 'normal'), ('fig', 'fighting'), ('fly', 'flying'), ('gro', 'ground'), ('roc', 'rock'), ('bug', 'bug'), ('gho', 'ghost'), ('ste', 'steel'), ('fir', 'fire'), ('wat', 'water'), ('gra', 'grass'), ('ele', 'electric'), ('psy', 'psychic'), ('ice', 'ice'), ('dra', 'dragon'), ('fai', 'fairy'), ('dar', 'dark')], max_length=4)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('pokedex_number', models.IntegerField(unique=True)),
                ('type', models.CharField(choices=[('nor', 'normal'), ('fig', 'fighting'), ('fly', 'flying'), ('gro', 'ground'), ('roc', 'rock'), ('bug', 'bug'), ('gho', 'ghost'), ('ste', 'steel'), ('fir', 'fire'), ('wat', 'water'), ('gra', 'grass'), ('ele', 'electric'), ('psy', 'psychic'), ('ice', 'ice'), ('dra', 'dragon'), ('fai', 'fairy'), ('dar', 'dark')], max_length=4)),
                ('second_type', models.CharField(blank=True, choices=[('nor', 'normal'), ('fig', 'fighting'), ('fly', 'flying'), ('gro', 'ground'), ('roc', 'rock'), ('bug', 'bug'), ('gho', 'ghost'), ('ste', 'steel'), ('fir', 'fire'), ('wat', 'water'), ('gra', 'grass'), ('ele', 'electric'), ('psy', 'psychic'), ('ice', 'ice'), ('dra', 'dragon'), ('fai', 'fairy'), ('dar', 'dark')], max_length=4, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('image_shiny', models.ImageField(null=True, upload_to='')),
                ('charged_attack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='primary_attack', to='pokesite.chargedattack')),
                ('evolves_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokesite.pokemon')),
                ('fast_attack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pokesite.fastattack')),
                ('second_charged_attack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='secondary_attack', to='pokesite.chargedattack')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('team', models.CharField(choices=[('yel', 'Instinct'), ('blu', 'Mystic'), ('red', 'Valor')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=32, null=True)),
                ('is_shiny', models.BooleanField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokesite.pokemon')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokesite.trainer')),
            ],
        ),
        migrations.AddField(
            model_name='trainer',
            name='pokemon',
            field=models.ManyToManyField(through='pokesite.TrainerPokemon', to='pokesite.Pokemon'),
        ),
        migrations.AddField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]