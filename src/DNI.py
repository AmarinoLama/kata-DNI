from src.tablaAsignacion import tablaAsignacion

class Dni:

    LENGHT_DNI = 9
    LENGHT_DNI_NUMBERS = 8

    def __init__(self, dni):
        self.tabla = tablaAsignacion()
        self.dni = dni
        self.numbers = dni[:self.LENGHT_DNI_NUMBERS]
        self.letter = dni[-1]


    def getDni(self):
        return self.dni
    
    def checkDni(self):
        return (
             self.isValidLenght() and 
             self.isValidNumber() and 
             self.isValidLetter()
             )
    
    def isValidNumber(self):
        try:
            int(self.numbers)
            return True
        except ValueError:
            return False

    def getNumbers(self):
        return int(self.numbers) if self.isValidNumber() else 'El número del DNI introducido no es válido.'
    
    def getLetter(self):
        return self.dni[-1] if self.isValidLetter() else 'La letra del DNI introducido no es válida.'

    def isValidLenght(self):
        return len(self.dni) == self.LENGHT_DNI        

    def isLetterInTabla(self):
        return self.letter in self.tabla.getTabla()
    
    def isValidLetter(self):
        return self.letter == self.tabla.calculateLetter(self.getNumbers()) if self.isLetterInTabla() else False
    
    def __repr__(self) -> str:
        return str(self.getDni)

