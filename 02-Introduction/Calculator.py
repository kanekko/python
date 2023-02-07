
def operaciones(opcion, numero_a, numero_b):
    if opcion == '1':
        return numero_a + numero_b
    elif opcion == '2':
        return numero_a - numero_b
    elif opcion == '3':
        return numero_a * numero_b
    elif opcion == '4':
        return numero_a / numero_b
    else:
        print('Opción inválida')


print('Bienvenido a la calculadora')
print('Estas son las operaciones que puedes realizar:')
print('1 - Suma')
print('2 - Resta')
print('3 - Multiplicación')
print('3 - División')

opcion = input('Introduce el número de operación que quieres realizar: ')
numero_a = int(input('Introduce el primer número: '))
numero_b = int(input('Introduce el segu1ndo número: '))

numero_c = operaciones(opcion, numero_a, numero_b)
print('El resultado es: ' + str(numero_c))


#continuar = input("¿Deseas continuar? si/no")
