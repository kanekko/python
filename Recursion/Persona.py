class Persona:
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape
 
persona1=Persona("Jose","Rodriguez")
print(persona1)

class Persona:
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape

    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena
 
persona1=Persona("Jose","Rodriguez")
print(persona1)