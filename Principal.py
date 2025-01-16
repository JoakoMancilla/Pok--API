from Poke_API import Poke_API

class Pirncipal():
    
    __pk_api = Poke_API()

    def __init__(self):
        pass

    def ejecutarPrograma(self):
        self.__pk_api.menuInicio()

p = Pirncipal()
p.ejecutarPrograma()