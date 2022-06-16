import conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Cita:
    def __init__(self, doctor, consultorio, turno):
        self.doctor = doctor
        self.consultorio = consultorio
        self.turno = turno

    def guardar(self):
        sql = "INSERT INTO citas VALUES (null, %s, %s, %s)"
        cita = (self.doctor, self.consultorio, self.turno)

        cursor.execute(sql, cita)
        database.commit()

        return [cursor.rowcount, self] 
    
    def listar():
        sql = "SELECT * FROM citas "

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM citas WHERE id = {self}"

        cursor.execute(sql)
        database.commit()
        
        return [cursor.rowcount, self]

 