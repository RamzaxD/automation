#Testeo de clases
class Test_Class():#para validar una clase -> Test_nameclass
    def test_type(self):
        assert type(1)  == int  #PASSED
        assert type(.3) == str  #FAILED

    def test_str(self):
        assert str.upper("python")  ==  "python"    #FAILED
        assert str.lower("HOLA")    ==  "hola"      #PASSED  
        assert "pytest".capitalize  ==  "Pytest"    #Passed