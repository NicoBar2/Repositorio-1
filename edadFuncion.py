nombre = input("Ingrese Nombre: ")

edad = int (input("Porafvor ingrese su edad: "))

def edadCalcular(int:edad):
    global edad
    if edad >= 18 and edad<= 65:
        print("Es mayor de edad")
    elif edad >= 65:
        print("Usted es parte de la 3ra edad")    
    else:
        print("Es menor de edad")  

edadCalcular(edad)          