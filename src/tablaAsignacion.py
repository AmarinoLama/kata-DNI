class tablaAsignacion:
    
    def __init__(self):
        self.tabla = [  
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]
        
    def getTabla(self):
        return self.tabla

    def getLetter(self,posicion):
        try:
            return self.getTabla()[posicion]
        except IndexError:
            return "La posición de la letra está fuera del índice."
    
    def getLength(self):
        return len(self.getTabla())
    
    def getPosition(self,DNI):
        return int(DNI) % self.getLength()
    
    def calculateLetter(self,DNI):
        return self.getLetter(self.getPosition(DNI))

    def __repr__(self) -> str:
        return str(self.getTabla())
