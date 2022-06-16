from citas import cita as modelo
from usuarios import usuario
from consultorios import consultorio as departamento

class Acciones:
    def crear(self):
        print("OK vamos a crear una cita!!")
        
        doctores = usuario.Usuario.consultar()
        print("---------Doctores Disponibles---------")
        for i in doctores:
            print(f"Nombre:{i[1]}, Apellido:{i[2]}\n")

        doctor = input(
            "Introduce el nombre del doctor o (a) que este disponible..")

        consultorios = departamento.Consultorio.listar()
        print("---------Consultorios Disponibles---------")
        for a in consultorios:
            print(f"Nombre:{a[1]}, Ubicacion:{a[3]}\n")


        consultorio = input("Elija un consultorio..")
        turno = input("introduzca que turno (matutino, despertino)")
        cita = modelo.Cita(doctor, consultorio, turno)
        guardar = cita.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has agendado con el doctor(a): {doctor}")

        else:
            print("no se guardo la nota, intentalo mas tarde:")

    def mostrar(self):
        

        citas = modelo.Cita.listar()


        print("---- Todas las citas ----")
        for no in citas:
            print(f"NUMERO DE CITA: {no[0]}\nDOCTOR: {no[1]},\nCONSULTORIO: {no[2]}, \nTURNO: {no[3]}")

    def borrar(self):
        print("Que cita desesa borrar")

        citaBorrar = input("Introduce el numero de la cita que deseas borrar: ")

        cita = modelo.Cita.eliminar(citaBorrar)
        #eliminar = cita.eliminar(citaBorrar)

        if cita[0] >= 1:
            print(f"OK se elimino la cita numero: {cita}")

        else:
            print("no se borro la nota, pruebe mas tarde")
