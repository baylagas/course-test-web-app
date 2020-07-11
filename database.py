import mysql.connector


class Database:
    def __createConCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="coursedb"
        )
        cursor = con.cursor()
        return con, cursor

    def getAllCourse(self):
        con, cursor = self.__createConCursor()
        cursor.execute("select * from coursedb.course;")
        data = cursor.fetchall()
        print(con)
        return data

    def insertCourse(self, name, entity_name):
        con, cursor = self.__createConCursor()
        sql = (
            "insert into coursedb.course"
            + "(id, name, entity_name) "
            + f"values(0, '{name}', '{entity_name}');"
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def getCourseById(self, id):
        """
        description:
            este metodo utiliza createCursorOnly ya que es un select el cual no modifica
            la base de datos. Por esta razon no necesita que usemos un instancia de la 
            conexion. (Nota: cuando son insert, update, delete, etc: que si modifica la 
            base de datos entonces usamos createConCursor)
        """

        con, cursor = self.__createConCursor()
        sql = f"select * from coursedb.course where id={id}"
        cursor.execute(sql)
        data = cursor.fetchall()
        print(con)
        return data

    def updateCourse(self, id, name, entity_name):
        con, cursor = self.__createConCursor()
        sql = (
            "update coursedb.course "
            + f"set name='{name}', entity_name='{entity_name}' "
            + f"where id = {id}"
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def deleteCourseById(self, id):
        con, cursor = self.__createConCursor()
        sql = f"delete from coursedb.course where id = {id}"
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount
