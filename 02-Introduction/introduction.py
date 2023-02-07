### 9. Hola mundo ###
print("Hola mundo")


### 13. Números y operadores aritméticos ###
2 + 2
20 - 10
2 * 9
20 / 2 

8 + 2 * 10
(8 + 2) * 10

19 / 2  # 9.5
19 // 2 # 9

2 * 2 * 2 * 2 * 2 # 32
2 ** 5            # 2^5


### 14. Variables ###
x = 2
y = 2 ** 5

x + 2 #> 4
      #> x > 2

# asignación
x = x + 2 #> 4
x = x * 3 #> 12

# tipos de datos
z = 19/2         # float
a = "Hola mundo" # string

desayuno = "Huevos con jamón"

# asignar variables a variables
x = x + y 
# cambio de tipo de variables
x = "sandwich"
x = desayuno


### 16. Cadenas ###
#> "Canek"
# nombre = "Canek"
nombre = 'Canek'

# frase = "Ella me dijo: "Hola" "

# frase = "Ella me dijo: 'Hola' "
# frase = 'Ella me dijo: "Hola" '

# secuencia de escape:
# frase = "Ella me dijo: \"Hola\" "
# frase = 'Ella me dijo: \'Hola\' '

frase = "Ella me dijo: \n\"Hola\""
print(frase)

# concatenar cadenas:
saludo = "Hola"
print(saludo + " " + nombre)

print(nombre * 3)


### 21. Condiciones ###
edad = 21

# if edad == 21:
#     print("Puedes entrar al bar")
# print("y también puedes beber")

if edad < 18:
    print("No puedes entrar")
elif edad >= 21:
    print("Puedes entrar al bar y también puedes beber")
else:
    print("Puedes entrar al bar pero no puedes beber")


### 23. Funciones ###
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


### 24. Objetos ###
print("este es un objeto string".upper())


### 25. Listas ###
[1,2,3,4,5]

lista = [1,2,3,4,5]

# concatenar listas:
lista + [5,6]

lista = lista + [6,7]
lista += [8,9]

lista * 5

lista.append(10)
lista.append('canek')

# lista de listas:
lista.append([1,2,3])


lista_2 = [1,2,3,4,5]
lista_2.append(6) # [1,2,3,4,5,6]

lista_2.extend([7,8]) # [1,2,3,4,5,6,7,8]

lista_2.remove(8) # [1,2,3,4,5,6,7]
lista_2.remove(4) # [1,2,3,5,6,7]

# método list()
list([1,2,3,4,5])
list("canek")
list("Python") + list("es genial")


### 26. Split and Join ###
"canek".split() # el espacio es el delimitador por default.
"Python es genial".split()

comida_favorita = "hamburgesa,tacos,pizza"
comida_favorita.split(",") # ['hamburgesa', 'tacos', 'pizza']


lista_comida_favorita = ['hamburgesa','tacos','pizza']
", ".join(lista_comida_favorita) # 'hamburgesa, tacos, pizza'
",".join(lista_comida_favorita)  # 'hamburgesa,tacos,pizza'
"-".join(lista_comida_favorita)  # 'hamburgesa-tacos-pizza'

"Mi comida favorita es: " + ", ".join(lista_comida_favorita)


### 27. Indices ###
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_lista = list(alfabeto)

# saber el indice un elemento de la lista
alfabeto_lista.index("a") # 0
alfabeto_lista.index("b") # 1
alfabeto_lista.index("c") # 2
alfabeto_lista.index("z") # 26

alfabeto.index("a") # 0
alfabeto.index("b") # 1

# errores:
#alfabeto.index(1)
#alfabeto.index("$")
#alfabeto_lista.index("%")

# buscar elementos en la cadena:
alfabeto.index("bc") # 1

# buscar elementos en determinada posición:
alfabeto[10]       # k
alfabeto_lista[10] # k

# se pueden tener indices negativos:
alfabeto_lista[-1] # z
alfabeto_lista[26] # z
alfabeto[-1]       # z


### 28. del ###
vocales = "aeiou"
lista_vocales = list(vocales)

# borrar variables:
variable_basura = "Variable basura"
del variable_basura

# borrar elementos de listas:
del lista_vocales[0]  # ['e', 'i', 'o', 'u']
del lista_vocales[-1] # ['e', 'i', 'o']

# error: las cadenas son inmutables
#del vocales[0]
# alrternativa, usar estructuras auxiliares: 
"".join(lista_vocales)

del vocales
del lista_vocales


### 29. in ###
vocales = "aeiou"
lista_vocales = list(vocales)

"a" in vocales # True
"z" in vocales # False

"a" in lista_vocales # True
"z" in lista_vocales # False

if "a" in vocales:
    print("a es una vocal")

if "z" not in vocales:
    print("z no es una vocal")

if "a" in lista_vocales:
    print("a esta en la lista de vocales")


### 30. Ciclos ###
manzanas = 10

while manzanas > 0:
    print("Me estoy comiendo la manzana #" + str(manzanas))
    manzanas -= 1
print("Me quede sin manzanas")


lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# lista_numeros = [1,"canek",3,4,5,6,7,8,9,10]

for numero in lista_numeros:
    print(numero)
    
    # romper el ciclo en 5:
    # if numero > 5:
    #     break
    # print(numero)
    
    # omitir la iteración 5:
    # if numero == 5:
    #     continue
    # print(numero)



