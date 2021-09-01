class Mamifero:
    def __init__(self, nombre):
        print(nombre,"es un animal de sanre caliente")

class Leon(Mamifero):
    def __init__(self):
        print("el león es un animal de 4 patas")
        super().__init__("simba")

nuevoLeon = Leon()

