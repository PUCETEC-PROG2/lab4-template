import pytest
from pokemon import Pokemon, ElectricPokemon, WaterPokemon, FirePokemon
from trainer import Trainer

@pytest.fixture
def ash():
    return Trainer(1, "Ash", "Ketchum", 10, 5)

@pytest.fixture
def pikachu(ash):
    return ElectricPokemon(1, "Pikachu", 6.0, 0.4, ash)

@pytest.fixture
def squirtle():
    return WaterPokemon(2, "Squirtle", 9.0, 0.5, Trainer(2, "Misty", "Waterflower", 15, 4))

@pytest.fixture
def charmander():
    return FirePokemon(3, "Charmander", 8.5, 0.6, Trainer(3, "Brock", "Rock", 14, 3))

def test_pokemon_trainer_type(pikachu):
    assert isinstance(pikachu.trainer, Trainer), "El atributo 'trainer' no es de tipo 'Trainer' en el Pokémon Pikachu"

def test_pokemon_attack_method(pikachu):
    assert pikachu.attack() == "Pikachu lanzó un ataque eléctrico!", "El método 'attack' del Pokémon Pikachu no devuelve el mensaje esperado"

def test_water_pokemon_trainer_type(squirtle):
    assert isinstance(squirtle.trainer, Trainer), "El atributo 'trainer' no es de tipo 'Trainer' en el Pokémon Squirtle"

def test_water_pokemon_attack_method(squirtle):
    assert squirtle.attack() == "Squirtle lanzó un ataque acuático!", "El método 'attack' del Pokémon Squirtle no devuelve el mensaje esperado"

def test_fire_pokemon_trainer_type(charmander):
    assert isinstance(charmander.trainer, Trainer), "El atributo 'trainer' no es de tipo 'Trainer' en el Pokémon Charmander"

def test_fire_pokemon_attack_method(charmander):
    assert charmander.attack() == "Charmander lanzó un ataque de fuego!", "El método 'attack' del Pokémon Charmander no devuelve el mensaje esperado"
