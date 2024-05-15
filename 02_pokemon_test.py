import importlib.util
import pytest
#from trainer_test import trainer_module
from trainer import Trainer

@pytest.fixture
def pokemon_module():
    spec = importlib.util.find_spec("pokemon")
    assert spec is not None, "\n\n***********     ERROR: El módulo 'pokemon' no existe    *************\
                \n\n***********     Crea el archivo pokemon.py, con eso será suficiente"
    return importlib.import_module("pokemon")

def test_module_exist(pokemon_module):
    assert pokemon_module is not None, "\n\n***********     ERROR: El módulo 'pokemon' no existe    *************"

def test_class_exists(pokemon_module):
    assert hasattr(pokemon_module, "Pokemon"), "\n\n***********     La clase 'Pokemon' no existe en el módulo 'pokemon' *******\
                            \n***********     Asegúrate de crear la clase con el constructor\n"

def test_class_attributes(pokemon_module):
    Pokemon = getattr(pokemon_module, "Pokemon")
    try:
        #Trainer = getattr(trainer_module, "Trainer")
        trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
        pokemon_instance = Pokemon(id=1, name="Pikachu", weight=6.0, height=0.4, trainer=trainer_instance)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo crear una instancia de Pokemon: ************\
                          \n***********  Asegúrate que existan los siguientes atributos:\
                          \n-'id' (entero)\
                          \n-'name' (cadena),\
                          \n- weight (flotante),\
                          \n- height(flotante)\
                          \n- trainer (Trainer)\
                          \n***********  No olvides que estos atributos también deben estar como parámetros del constructor ***********")
    
    assert isinstance(pokemon_instance.name, str), "\n***** El atributo 'name' debe ser de tipo cadena de caracteres (str) ******\n"
    assert isinstance(pokemon_instance.weight, float), "\n*****El atributo 'weight' debe ser de tipo flotante (float) *****\n"
    assert isinstance(pokemon_instance.height, float), "\n*****El atributo 'height' debe ser de tipo flotante (float) *****\n"
    assert isinstance(pokemon_instance.trainer, Trainer), "\n***** El atributo 'trainer' debe ser de tipo Trainer ****\n"
    assert not hasattr(pokemon_instance, "id"), "\n***** El atributo 'id' no debería ser público ***** \n"
    
    assert hasattr(pokemon_instance, "get_id"), "\n***** El método 'get_id' no existe ****\n"
    assert callable(getattr(pokemon_instance, "get_id")), "\n***** El atributo 'get_id' debe ser un método ****\n"
    assert isinstance(pokemon_instance.get_id(), int), "\n***** El método 'get_id' debe devolver un entero ****\n"
    assert pokemon_instance.get_id() == 1, "\n***** El método 'get_id' no devuelve el ID correcto *****\n"
    
    assert hasattr(pokemon_instance, "set_id"), "\n ****** El método 'set_id' no existe *****\n"
    assert callable(getattr(pokemon_instance, "set_id")), "\n***** El atributo 'set_id' debe ser un método *****\n"
    pokemon_instance.set_id(2)
    assert pokemon_instance.get_id() == 2, "\n***** El método 'set_id' no cambia el ID correctamente ****\n"
    with pytest.raises(TypeError):
        pokemon_instance.set_id("Not an integer")

def test_str_method(pokemon_module):
    Pokemon = getattr(pokemon_module, "Pokemon")
    trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    pokemon_instance = Pokemon(1, "Pikachu", 6.0, 0.4, trainer_instance)
    assert str(pokemon_instance) == "Pikachu", "\n***** El método __str__() debe devolver el nombre del Pokemon ****\n"
