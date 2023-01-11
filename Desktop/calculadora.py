welcome = str(input('Hola te gustaria hacer un calculo y/n: '))
if str(welcome) == 'y':
    print('vamos a ello')
    
    print('Que calculo te gustaria hacer?')
    print('Selecciona una de las siguientes opciones:')
    print('Suma')
    print('Resta')
    print('Multiplicacion')
    print('Dividision')

    operacion = str(input())
    if operacion == 'suma':
        n1 = float(input('introduce el primer numero '))
        n2 = float(input('introduce el segundo numero '))
        print('el resultado es', n1 + n2)

    if operacion == 'resta':
        n1 = float(input('introduce el primer numero '))
        n2 = float(input('introduce el segundo numero '))
        print('el resultado es', n1 - n2)

    if operacion == 'multiplicacion':
        n1 = float(input('introduce el primer numero '))
        n2 = float(input('introduce el segundo numero '))
        print('el resultado es', n1 * n2)

    if operacion == 'division':
        n1 = float(input('introduce el primer numero '))
        n2 = float(input('introduce el segundo numero '))
        print('el resultado es', n1 / n2)

elif str(welcome) == 'n':
    print('Genial! Espero ayudarte la proxima vez')
    quit()
elif str(welcome) != 'y' or str(welcome) != 'n':
    print('ERROR. Introduce y or n')