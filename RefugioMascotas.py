# anioActual = input("Año Actual: ")
# print("El Año Actual es " +str(anioActual))
print("Bienvenida/o al Sistema de Gestión del Refugio!!")
class Perro():
    def __init__(self, nombreRecibido, edadRecibida, pesoRecibido, razaRecibida, fecha_ult_vacunaRecibida):
        self.nombre = nombreRecibido
        self.edad = edadRecibida
        self.peso = pesoRecibido
        self.raza = razaRecibida
        self.fecha_ult_vacuna = fecha_ult_vacunaRecibida
    
    # def tocarBocinaEspecial(self):
    #     print("Beep beep. Soy un " + self.marca)

    # def nuevoPerro(self, nombreRecibido, edadRecibida, pesoRecibido, razaRecibida, fecha_ult_vacunaRecibida):
    #     self.nombre = nombreRecibido
    #     self.edad = edadRecibida
    #     self.peso = pesoRecibido
    #     self.raza = razaRecibida
    #     self.fecha_ult_vacuna = fecha_ult_vacunaRecibida

    def Vacunas(self, anioActual=2020):
        if ((int(self.fecha_ult_vacuna)) >= (anioActual-2)) and ((int(self.fecha_ult_vacuna) <= anioActual)):
            return print("Las vacunas de " +self.nombre.upper()+ " están al día! ")
        if (int(self.fecha_ult_vacuna) < (anioActual-2)):
            return print("Las vacunas de " +self.nombre.upper()+ " NO están al día! ")
        elif self.fecha_ult_vacuna == "":
            # una """"Excepcion"""
            print("ATENCION!! Se desconoce cuando fue la ultima fecha de vacunación de " +self.nombre)
            return False

    # def calcularAntiguedad(self, anioActual=2050):
    #     if(self.anio):
    #         return anioActual - self.anio
    #     else:
    #         # una """"Excepcion"""
    #         print("ATENCION!! ESTAS INTENTANDO CALCULAR LA ANTIGUEDAD DE UN AUTO CUYO AÑO NO ESTÁ ESPECIFICADO")
    #         return False

numeroPerro = 0
listaPerros=[]

respuesta = input("Desea registrar un Perro? (SI/NO)\n").upper()
while respuesta == "SI":
    numeroPerro = numeroPerro + 1
    nombrePerro = input("Nombre del Perro: ")
    edadPerro = int(input("Edad del Perro (años, solo números): "))
    pesoPerro = int(input("Peso del Perro (kg, sólo números): "))
    razaPerro = input("Raza del Perro: ")
    fechaUltVacunaPerro = input("Año de la ultima vacunación del Perro: ")
    nuevoPerro = Perro(nombreRecibido=nombrePerro, edadRecibida=edadPerro, pesoRecibido=pesoPerro, razaRecibida=razaPerro, fecha_ult_vacunaRecibida=fechaUltVacunaPerro)
    listaPerros.append(nuevoPerro)
    print("Gracias, hemos registrado a " +nuevoPerro.nombre.upper()+ " !!")
    vacunacionPerro = nuevoPerro.Vacunas(anioActual=2020)
    print("--------------------------------------------------------")
    respuesta = input("Desea registrar un Perro? (SI/NO)\n").upper()

mostrarPerro = input("¿Desea ver los datos de un perro ingresado? (SI/NO)").upper()

while mostrarPerro == "SI":
    numeroIngresado = int(input("Ingrese el número de Perro que desea consultar: "))

    posicion = numeroIngresado-1 #Tengo que tener en cuenta que el 0 es el primer número de una lista
    try:
        print("El nombre del perro es " + listaPerros[posicion].nombre)
        print("La edad del perro es " + str(listaPerros[posicion].edad) + " años")
        print("El peso del perro es " + str(listaPerros[posicion].peso) + " kg")
        print("La raza del perro es " + listaPerros[posicion].raza) 
        print("El año de la última vacunación del perro es " + str(listaPerros[posicion].fecha_ult_vacuna)) 
        vacunacionPerro = nuevoPerro.Vacunas(anioActual=2020)
        # print("--------------------------------------------------------")
        # mostrarPerro = input("¿Desea ver los datos de un perro ingresado? (SI/NO)").upper()
    except IndexError:
        print("El tamaño de la Lista es: " +str(len(listaPerros)))
        print("Atención! NO existe ningún Perro cargado para esa posición!")
    print("--------------------------------------------------------")
    mostrarPerro = input("¿Desea ver los datos de un perro ingresado? (SI/NO)").upper()

print("Gracias y Adiós !!")