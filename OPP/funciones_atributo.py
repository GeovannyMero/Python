# funciones para atributos
class Persona:
    edad = 10
    nombre = "Mateo"

doctor = Persona()
print(doctor.nombre)
setattr(doctor, "nombre", "Nicolas")
print(doctor.nombre)