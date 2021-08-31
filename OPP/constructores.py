# Constructor
class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def description(self):
        return '{} tiene {}'.format(self.nombre, self.año)

doctor = Persona('Mateo',4)
print(doctor.nombre)
        