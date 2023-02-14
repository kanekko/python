""" Función suma

__author__ = "Teresa Becerril Torres"
"""

def s(m):
    """
    Función sucesor.
    
    Arguments
    ---------
    m : int
        Entero del que se tiene su sucesor.
    
    Returns
    -------
        Sucesor de m, i.e. m+1
    """
    return m+1


def suma(m,n):
    """
    Función de suma de dos enteros.
    
    Arguments
    ---------
    m,n : int
        Entereso que se sumarán.
    
    Results
    -------
        Suma m+n
    """
    #Caso base
    if n == 0:
        result = m
    #Regla recursiva
    else:
        result = s(suma(m, n-1))
    
    return result

print(suma(5,5))


def producto(m,n):
    """
    Función que regresa el producto de dos enteros.
    
    Arguments
    ---------
    m,n : int
        Enteros que se multiplicarán.
        
    Returns
    -------
        Producto de los dos enteros m*n
    """
    #Caso base
    if n == 0:
        result = 0
    #Regla recursiva
    else:
        result = suma(producto(m, n-1), m)
        
    return result

print(producto(3,5))


def potencia(m,n):
    """
    Función para calcular la potencia de un entero elevado a otro entero.
    
    Arguments
    ---------
    m,n : int
        Enteros que se usarán en la potenciación.
        
    Returns
    -------
        m elevado a la n, m^n
    """
    #Caso base
    if n == 0:
        result = 1
    #Regla recursiva
    else:
        result = producto(potencia(m,n-1),m)
    
    return result


print(potencia(3,4))

def exponencial(m):
    """
    Función que calcula el factorial de un entero.
    
    Arguments
    ---------
    m : int
        Entero de entrada para calcular factorial
        
    Returns
    -------
        Factorial de m, m!
    """
    #Caso base
    if m == 0:
        result = 1
    #Regla recursiva
    else:
        result = producto(exponencial(m-1), m)
        
    return result

print(exponencial(2))