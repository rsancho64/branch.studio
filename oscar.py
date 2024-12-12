#class Datos:
#    def __init__(self, nombre, apellido, grupo):
#        self.nombre = nombre
#        self.apellido = apellido
#        self.grupo = grupo

        
    
#    nombre = str(input("dame tu nombre: "))
#    apellido = str(input("dame tu apellido: "))
#    grupo = int(input("dame tu grupo: "))
    
#    print(f"Los datos estan compuestos por tu nombre: {nombre}, tu apellido: {apellido}, y tu grupo: {grupo}")




class Pedir_Datos:
    
    def __init__(self):
        nombre = str(input("dame tu nombre: "))
        apellido = str(input("dame tu apellido: "))
        grupo = int(input("dame tu grupo(numero): "))
        print(f"tu nombre es {nombre}, con el apellido {apellido}, y del grupo {grupo}")
    
    def pedir_clase(self):
        clase = str(input("dame el nombre de tu clase: "))
        numero = int(input("dame el numero de tu clase(numero): "))
        profesor = str(input("dame el nombre del profesor de la clase: "))
        print(f"el nombre de la clase es {clase}, con el numero {numero}, y su profesor es {profesor}")

class Querer(Pedir_Datos):
    def __init__(self):
        Pedir_Datos().pedir_clase()

    def verdad_absoluta(self):
        print("Ademas de todo lo de antes, entre raul y saray algo hay...")
        
        
        
primera_persona = Querer()
primera_persona.verdad_absoluta()