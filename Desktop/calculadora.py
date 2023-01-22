if __name__ == '__main__':
    
    welcome = input('Hola te gustaria hacer un calculo y/n: ')
    if welcome == 'y':
        print(
            'vamos a ello\n'
            'Que calculo te gustaria hacer?\n'
            'Suma\n'
            'Resta\n'
            'Multiplicacion\n'
            'Division'
        )
        
        
        operacion = input('Selecciona una de las siguientes opciones: ').lower()
        while operacion not in ['suma', 'resta', 'multiplicacion', 'division']:
            print('ERROR. Selecciona una de las opciones anteriores')
            operacion = input('Selecciona una de las siguientes opciones: ').lower()

        n1 = float(input('introduce el primer numero: '))
        n2 = float(input('introduce el segundo numero: '))
        match operacion:
            case 'suma':
                print('el resultado es', n1 + n2)
            case 'resta':
                print('el resultado es', n1 - n2)
            case 'multiplicacion':
                print('el resultado es', n1 * n2)
            case 'division':
                print('el resultado es', n1 / n2)

    elif welcome == 'n':
        print('Genial! Espero ayudarte la proxima vez')

    else:
        print('ERROR. Introduce y or n')
