#TEST unilaterales. testear solo ciertas funciones -> test_nombre_programa::test_nombre_funcion
#el archivo init lo creamos para inicializar bibliotecas, paquetes, clases
from . import suma

def test_suma(a = 2, b = 2):
    assert a + b == 4 #Passed
    
def test_suma_fail (a = 3, b = 2):
    assert a + b == 8 #Failed

def test_caracter():
    assert "abc" not in "Hola mundo bello Casa" #Passed
    assert "Hola" in "Holajssjjs mundo" #Passed
    
def test_list():
    assert [1,2] in [1,2,3,4,5] #Failed
    assert [1] in [1,2,3,4,5] #Passed
    assert 5 in [1,2,5] #Passed
    assert [1,2] == [1,2] #Passed 
