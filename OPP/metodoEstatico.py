import math

class Person:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @staticmethod
    def ValidarEdad(A):
        return A ** 2 * math.pi

person = Person("Geovanny",28)
print(person.nombre)
print(Person.ValidarEdad(5))
