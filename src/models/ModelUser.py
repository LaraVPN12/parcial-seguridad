from .entities.User import User, UserInfo
class ModelUser():
    @classmethod
    def login(self, connection, user):
        try:
            cursor = connection.cursor()
            sql = """SELECT id_usuario, nombre_usuario, password_usuario FROM usuario 
                    WHERE nombre_usuario = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self, connection, id):
        try:
            cursor = connection.cursor()
            sql = "SELECT nombre, apellido, edad, descripcion, id_usuario FROM usuario_info WHERE id_usuario={}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return UserInfo(row[0], row[1], row[2], row[3], row[4])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

