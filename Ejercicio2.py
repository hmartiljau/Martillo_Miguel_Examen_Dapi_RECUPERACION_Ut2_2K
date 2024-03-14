diccionario = {}
while True :
    alimento = str(input('Ingresa el nombre del alimento: '))
    cantidad = str(input('Ingresa la cantidad consumida (en gramos): '))
    registro = input('¿Quieres registrar otro alimento? (si/no) :')
    diccionario[alimento] = cantidad
    if registro == 'si' :
        for x in diccionario.values():
            diccionario[alimento] = cantidad
    elif registro == 'no' :
        print (diccionario.values())
        