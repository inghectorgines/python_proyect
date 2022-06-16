import conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self, nombre, apellidos, email, password, rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        self.rol = rol

    def registrar(self):

        sql = "INSERT INTO usuarios2 VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, self.password, self.rol)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    def consultar():
        sql = "SELECT * FROM usuarios2 WHERE rol = 'doctor' "

        cursor.execute(sql)
        result = cursor.fetchall()

        return result   