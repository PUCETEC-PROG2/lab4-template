import importlib.util
import pytest

@pytest.fixture
def trainer_module():
    spec = importlib.util.find_spec("trainer")
    assert spec is not None, "\n***** El módulo 'trainer' no existe. *********\
                        \n*****    Crea el archivo trainer.py. *****\n"
    return importlib.import_module("trainer")

@pytest.fixture
def pokemon_module():
    spec = importlib.util.find_spec("pokemon")
    assert spec is not None, "\n\n***********     ERROR: El módulo 'pokemon' no existe    *************\
                \n\n***********     Crea el archivo pokemon.py, con eso será suficiente"
    return importlib.import_module("pokemon")

# Revisar que exista el atributo pokedex y que sea privado
def test_empty_pokedex_attribute(trainer_module):
    Trainer = getattr(trainer_module, "Trainer")
    trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    assert not hasattr(trainer_instance, "pokedex"), "\n***** El atributo 'pokedex' debe ser privado *****\n"
    assert hasattr(trainer_instance, "_Trainer__pokedex"), "\n***** El atributo privado '__pokedex' no está definido en la instancia de 'Trainer' *****\n"
    assert isinstance(trainer_instance._Trainer__pokedex, list), "\n***** El atributo '__pokedex' no es una lista *****\n"
    assert len(trainer_instance._Trainer__pokedex) == 0, "\n***** El atributo '__pokedex' no está inicializado como una lista vacía *****\n"

def test_add_to_pokedex_method(trainer_module):
    Trainer = getattr(trainer_module, "Trainer")
    assert hasattr(Trainer, "add_to_pokedex"), "\n***** El método 'add_to_pokedex()' no está implementado en la clase 'Trainer' *****\n\
                ******  Agrega el método add_to_pokedex()   **************\n\
                ******  No olvides que este método debe recibir al menos un argumento de tipo 'Pokemon' o cualquiera de sus clases heredadas *****"

def test_get_pokedex_method_exists(trainer_module):
    Trainer = getattr(trainer_module, "Trainer")
    assert hasattr(Trainer, "get_pokedex"), "\n***** El método 'get_pokedex()' no está implementado en la clase 'Trainer' *****\n"

def test_get_pokedex_returns_list(trainer_module, pokemon_module):
    Trainer = getattr(trainer_module, "Trainer")
    Pokemon = getattr(pokemon_module, "Pokemon")
    FirePokemon = getattr(pokemon_module, "FirePokemon")

    try:
        trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
        pokemon_instance = Pokemon(id=1, name="Pikachu", weight=6.0, height=0.4, trainer=trainer_instance)
        fire_pokemon_instance = FirePokemon(id=2, name="Charmander", weight=8.5, height=0.6, trainer=trainer_instance)
        trainer_instance.add_to_pokedex(pokemon_instance)
        trainer_instance.add_to_pokedex(fire_pokemon_instance)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo crear una instancia de Trainer: {str(e)} ************\n")
    
    pokedex = trainer_instance.get_pokedex()
    assert isinstance(pokedex, list), "\n***** El método 'get_pokedex()' no devuelve una lista *****\n"
    

def test_add_single_pokemon_to_pokedex(trainer_module, pokemon_module):
    Trainer = getattr(trainer_module, "Trainer")
    Pokemon = getattr(pokemon_module, "Pokemon")
    FirePokemon = getattr(pokemon_module, "FirePokemon")

    try:
        trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo crear una instancia de Trainer: {str(e)} ************\n")

    try:
        pokemon_instance = Pokemon(id=1, name="Pikachu", weight=6.0, height=0.4, trainer=trainer_instance)
        fire_pokemon_instance = FirePokemon(id=2, name="Charmander", weight=8.5, height=0.6, trainer=trainer_instance)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudieron crear instancias de Pokemon: {str(e)} ************\n")

    try:
        trainer_instance.add_to_pokedex(pokemon_instance)
        trainer_instance.add_to_pokedex(fire_pokemon_instance)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo agregar un Pokemon al pokedex de Trainer: {str(e)} ************\n")

    assert isinstance(trainer_instance.get_pokedex(), list), "\n***** El atributo 'pokedex' ya no es una lista\n ***** Revisa bien cómo lo estás asignando en 'add_to_pokedex()'"
    assert len(trainer_instance.get_pokedex()) == 2, "\n**** El atributo pokedex no contiene los Pokemon agregados, tienes que realizar un 'append' para agregar el objeto a la lista ****\n"
    assert pokemon_instance in trainer_instance.get_pokedex(), "\n**** El pokedex no contiene el Pokemon 'Pikachu' agregado ****\n"
    assert fire_pokemon_instance in trainer_instance.get_pokedex(), "\n**** El pokedex no contiene el Pokemon 'Charmander' agregado ****\n"
    
def test_add_non_pokemon_to_pokedex(trainer_module):
    Trainer = getattr(trainer_module, "Trainer")
    notPokemon = "Charmander"

    try:
        trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo crear una instancia de Trainer: {str(e)} ************\n")

    with pytest.raises(TypeError):
        trainer_instance.add_to_pokedex(notPokemon)
    
def test_get_pokedex_contains_added_pokemon(trainer_module, pokemon_module):
    Trainer = getattr(trainer_module, "Trainer")
    Pokemon = getattr(pokemon_module, "Pokemon")

    try:
        trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo crear una instancia de Trainer: {str(e)} ************\n")

    pokemon1 = Pokemon(id=1, name="Pikachu", weight=6.0, height=0.4, trainer=trainer_instance)
    pokemon2 = Pokemon(id=2, name="Charmander", weight=8.5, height=0.6, trainer=trainer_instance)
    pokemon3 = Pokemon(id=3, name="Squirtle", weight=9.0, height=0.5, trainer=trainer_instance)

    trainer_instance.add_to_pokedex(pokemon1)
    trainer_instance.add_to_pokedex(pokemon2)
    trainer_instance.add_to_pokedex(pokemon3)

    pokedex = trainer_instance.get_pokedex()

    assert all(isinstance(p, Pokemon) for p in pokedex), "\n***** El pokedex contiene elementos que no son instancias de Pokemon *****\n"
    assert len(pokedex) == 3, "\n***** El pokedex debe contener exactamente los pokemon que fueron añadidos *****\n"
    assert pokemon1 in pokedex, "\n***** El Pokemon 'Pikachu' no está en el pokedex *****\n"
    assert pokemon2 in pokedex, "\n***** El Pokemon 'Charmander' no está en el pokedex *****\n"
    assert pokemon3 in pokedex, "\n***** El Pokemon 'Squirtle' no está en el pokedex *****\n"