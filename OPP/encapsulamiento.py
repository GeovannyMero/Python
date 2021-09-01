class Cliente:
    def __init__(self):
        self.__codigo = 4321 ## encapsular variable

    def getcodigo(self):
        return self.__codigo 
    
    ## Encapsular funcion
    def __cuenta(self):
        print("cuenta de procesamiento")

persona = Cliente()
print(persona._Cliente__codigo) ## llamar variables privada 
persona._Cliente__cuenta() ## llamar funcion privada
print(persona.getcodigo())
        