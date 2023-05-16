import mysql.connector


class Conexaobd:
    _conn = None
    _host = "localhost"
    _user = "root"
    _password = "admin123"
    _bd = "crud"

    @staticmethod
    def conect():
        if Conexaobd._conn == None:
            try:
                Conexaobd._conn = mysql.connector.connect(
                    host=Conexaobd._host,
                    database=Conexaobd._bd,
                    user=Conexaobd._user,
                    password=Conexaobd._password
                )
                return Conexaobd._conn
            except Exception as error:
                return error
        return Conexaobd._conn

    @staticmethod
    def execute(sql, dados):
        try:
            cursor = Conexaobd._conn.cursor(prepared=True)
            cursor.execute(sql, dados)
            Conexaobd._conn.commit()
            return cursor.rowcount
        except Exception as error:
            return error
