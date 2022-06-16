## Descargo y procedo a revisar y calificar.

from usuarios import acciones
from citas import acciones as accionesCitas


print("""
!hola andiministrador!\n¿Que desea hacer hoy? :
- solicitar cita
- agregar usuarios
- ver todas las citas
- eliminar una cita
""")


haz = acciones.Acciones()
hazCita = accionesCitas.Acciones()

accion = input("¿que quieres hacer?:")


if accion == "agregar usuarios":
	haz.registro()
elif accion == "solicitar cita":
    hazCita.crear()
elif accion == "ver todas las citas":
    hazCita.mostrar()
elif accion == "eliminar una cita":
    hazCita.borrar()
