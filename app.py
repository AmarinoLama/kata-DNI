from src.DNI import Dni

def main():
    inputData = input('Introduce your DNI: ')
    dni_user = Dni(f'{inputData}')

    if dni_user.checkDni():
        print(f'DNI letter is : {dni_user.getLetter()}')
        print(f'DNI numbers are : {dni_user.getNumbers()}')
        print(f'DNI: {dni_user.getDni()} is valid.')
    else:
        print('El código introducido no es correcto.')
    

if __name__ == "__main__":
    main()