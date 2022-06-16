from usuarios import usuario as modelo

class Acciones:

    def registro(self):
        print("se procedera a realizar tu registro en el sistema")
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿cuales son tus apeliidos?: ")
        email = input("¿Introduce tu email?: ")
        password = input("¿Introduce tu contraseña?: ")
        rol = input("Introduce el rol: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password, rol)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("no te has registrado correctamente")

