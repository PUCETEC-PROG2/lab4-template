import importlib.util
import pytest

@pytest.fixture
def trainer_module():
    spec = importlib.util.find_spec("trainer")
    assert spec is not None, "\n***** El módulo 'trainer' no existe. Crea el archivo trainer.py. *****\n"
    return importlib.import_module("trainer")

def test_module_exists(trainer_module):
    assert trainer_module is not None, "\n***** El módulo 'trainer' no existe. *****\n"

def test_class_exist(trainer_module):
    assert hasattr(trainer_module, "Trainer"), "La clase 'Trainer' no existe en el módulo 'trainer'."

def test_class_attributes(trainer_module):
    Trainer = getattr(trainer_module, "Trainer")
    try:
        trainer_instance = Trainer(id=1, first_name="Ash", last_name="Ketchum", age=10, level=5)
    except Exception as e:
        pytest.fail(f"\n\n***********  No se pudo crear una instancia de Trainer: ************\
                          \nAsegúrate de tener los siguientes atributos:\n\
                          \n- 'id' (entero)\
                          \n- 'first_name' (cadena),\
                          \n- 'last_name' (cadena),\
                          \n- 'age' (entero),\
                          \n- 'level' (entero)\
                          \n\nEstos atributos deben ser parámetros del constructor \n ********************")

    assert isinstance(trainer_instance.first_name, str), "\n**** El atributo 'first_name' debe ser de tipo cadena de caracteres (str) ****\n"
    assert isinstance(trainer_instance.last_name, str), "\n**** El atributo 'last_name' debe ser de tipo cadena de caracteres (str) ****\n"
    assert isinstance(trainer_instance.age, int), "\n**** El atributo 'age' debe ser de tipo entero ****\n"
    assert isinstance(trainer_instance.level, int), "\n**** El atributo 'level' debe ser de tipo entero ****\n"
    
    assert not hasattr(trainer_instance, "id"), "\n**** El atributo 'id' no debería ser público ****\n"

    assert hasattr(trainer_instance, "get_id"), "\n**** El método 'get_id' no existe ****\n"
    assert callable(getattr(trainer_instance, "get_id")), "\n**** El atributo 'get_id' debe ser un método ****\n"
    assert isinstance(trainer_instance.get_id(), int), "\n**** El método 'get_id' debe devolver un entero ****\n"
    assert trainer_instance.get_id() == 1, "\n**** El método 'get_id' no devuelve el ID correcto ****\n"

    assert hasattr(trainer_instance, "set_id"), "\n**** El método 'set_id' no existe ****\n"
    assert callable(getattr(trainer_instance, "set_id")), "\n**** El atributo 'set_id' debe ser un método ****\n"
    trainer_instance.set_id(2)
    assert trainer_instance.get_id() == 2, "\n**** El método 'set_id' no cambia el ID correctamente ****\n"
    with pytest.raises(TypeError):
        trainer_instance.set_id("Not an integer")

def test_str_method(trainer_module):
    Trainer = getattr(trainer_module, "Trainer")
    trainer_instance = Trainer(1, "Ash", "Ketchum", 10, 5)
    assert str(trainer_instance) == "Ash Ketchum", "\n**** El método __str__() debe devolver el nombre y apellido del entrenador ****\n"
