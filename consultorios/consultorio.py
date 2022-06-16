import conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Consultorio:

    def __init__(self, nombre, estado, ubicacion):
        self.nombre = nombre
        self.estado = estado
        self.ubicacion = ubicacion


    def registrar(self):

        sql = "INSERT INTO consultorios VALUES(null, %s, %s, %s)"
        usuario = (self.nombre, self.estado, self.ubicacion)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result
    
    def listar():
        sql = "SELECT * FROM consultorio WHERE estado = 'activo'"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result