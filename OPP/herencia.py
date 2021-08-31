# Herencia
# Clase Padre
class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return "{} es un pokemon de tipo {}".format(self.nombre, self.tipo)


# Clase Hijo
class Pikachu(Pokemon):
    def ataque(self, tipoAtaque):
        return "{}, tipo de ataque {}".format(self.tipo, tipoAtaque)

nuevoPokemon = Pikachu("pika", "electrico")
print(nuevoPokemon.descripcion())