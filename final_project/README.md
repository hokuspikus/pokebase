###Simple site to help Pokemon trainers with theory-crafting
####but more importantly to let me pass my final test :)

###Technologies used:
+ Python 3.9
+ Django 3.2.10
+ POSTGRESQL

The idea is to make a site that allows anyone interested in Pokemon battles 
to prepare themselves. Algorythms used are meant to be as accurate as in 
PokemonGO, obviously they will get better and better with every day of 
improvement.

For populating Database please use following commands after migrations in this specific order:
+ python3 manage.py populateattacks
+ python3 manage.py populatepokedex
+ python3 manage.py setdefaultattacks

These work thank to wonderful https://pogoapi.net/documentation/ site!