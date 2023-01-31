### 9. Hola mundo ###
print("Hola mundo")


### 1. Números y operadores aritméticos ###
2 + 2
20 - 10
2 * 9
20 / 2 

8 + 2 * 10
(8 + 2) * 10

19/2 #9.5
19//2 #9

2 ** 5 # 2^5


### 2. Variables ###
x = 2
y = 6 ** 3
x + 2
x = x + 2
x = x * 3
z = 19/2
a = "Hola mundo"

desayuno = "Huevos con tocino"
x = x + y

x = "sandwich"


### 3. Cadenas ###
# nombre = "Canek"
nombre = 'Canek'

# frase = "Ella me dijo: 'Hola'"
# frase = 'Ella me dijo: "Hola"'
# frase = "Ella me dijo: \"Hola\""
# frase = 'Ella me dijo: \'Hola\''
frase = "Ella me dijo: \n\"Hola\""

saludo = "Hola"
print(saludo + " " + nombre)

print(nombre * 3)


### 4. Condiciones ###
edad = 20

if edad < 18:
    print("No puedes entrar")
elif edad >= 21:
    print("Puedes entrar al bar y también puedes beber")
else:
    print("Puedes entrar al bar pero no puedes beber")


### 5. Funciones ###
def pedir_pizza():
    print("Pedir pizza")

pedir_pizza()


def checar_entrada(edad):
    if edad < 18:
        print("No puedes entrar")
    elif edad >= 21:
        print("Puedes entrar al bar y también puedes beber")
    else:
        print("Puedes entrar al bar pero no puedes beber")

edad   = 21
edad_2 = 17
checar_entrada(edad)
checar_entrada(edad_2)


### 6. Objetos ###
print("este es un objeto string".upper())


### 7. Listas ###
[1,2,3,4,5]

lista = [1,2,3,4,5]

lista + [5,6]
lista = lista + [6,7]
lista += [8,9]
lista * 5

lista.append(10)
lista.append('canek')
lista.append([1,2,3])


lista_2 = [1,2,3,4,5]

lista_2.append(6)
lista_2.extend([7,8])
lista_2.remove(8)
lista_2.remove(4)