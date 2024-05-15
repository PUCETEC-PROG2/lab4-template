import importlib.util
import pytest

@pytest.fixture
def pokemon_module():
    spec = importlib.util.find_spec("pokemon")
    assert spec is not None, "\n\n***********     ERROR: El módulo 'pokemon' no existe    *************\
                \n\n***********     Crea el archivo pokemon.py, con eso será suficiente"
    return importlib.import_module("pokemon")

def test_module_exist(pokemon_module):
    assert pokemon_module is not None, "\n\n***********     ERROR: El módulo 'pokemon' no existe    *************"

def test_electric_pokemon_subclass_exists(pokemon_module):
    assert hasattr(pokemon_module, "ElectricPokemon"), "\n\n***********     La subclase 'ElectricPokemon' no existe en el módulo 'pokemon' *******\
                            \n***********     Asegúrate de crear la subclase\n"

def test_water_pokemon_subclass_exists(pokemon_module):
    assert hasattr(pokemon_module, "WaterPokemon"), "\n\n***********     La subclase 'WaterPokemon' no existe en el módulo 'pokemon' *******\
                            \n***********     Asegúrate de crear la subclase\n"

def test_fire_pokemon_subclass_exists(pokemon_module):
    assert hasattr(pokemon_module, "FirePokemon"), "\n\n***********     La subclase 'FirePokemon' no existe en el módulo 'pokemon' *******\
                            \n***********     Asegúrate de crear la subclase\n"