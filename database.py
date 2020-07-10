import mysql.connector


class Database:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="coursedb"
        )
        cursor = con.cursor()
        return con, cursor

    def getAllCourse(self):
        con, cursor = self.__createCursor()
        cursor.execute("select * from coursedb.course;")
        data = cursor.fetchall()
        print(data, con)
        return data

    def insertCourse(self, name, entity_name):
        con, cursor = self.__createCursor()
        sql = (
            "insert into coursedb.course"
            + "(id, name, entity_name) "
            + f"values(0, '{name}', '{entity_name}');"
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount
