constante = 9/5
celcius = float(0)

def temperatura (celcius):
    faren = (celcius * constante) + 32
    return faren

#celcius = float(input("Ingresa la temperatura: \t"))
temperatura_c = temperatura(celcius)
print(temperatura_c)

#Que tipos de pruebas se pueden hacer?
#constante, temperatura, celcius sea float
#si el celcius es 0, la temperatura es de 35

def test_variabletype(centigrados = celcius):
    assert type(constante)      ==  float
    assert type(centigrados)    ==  float
    assert type(temperatura_c)  ==  float
    
def test_values():
    assert  temperatura(0)      ==  32
    assert  temperatura(1)      >   32
    assert temperatura(38)      ==  94.2    #Failed