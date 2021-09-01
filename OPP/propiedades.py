class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    
    def __getnombre(self):
        return self.__nombre
    
    def __getsalario(self):
        return self.__salario
    
    def __setnombre(self, nombre):
        self.__nombre = nombre
    
    def __setsalario(self, salario):
        self.__salario = salario
    
empleado = Empleado("Geovanny",1000)
print(empleado.getnombre(), ',',empleado.getsalario())
empleado.setnombre("Jefferson")
print(empleado.getnombre(), ',',empleado.getsalario())

##
##nombre = property(  fget = __getnombre,
##                    fset = __setnombre)

