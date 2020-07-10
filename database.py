import mysql.connector


class Database:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="coursedb"
        )
        cursor = con.cursor()
        return tuple(con, cursor)

    def getAllCourse(self):
        con, cursor = self.__createCursor()
        cursor.execute("insert")
        con.commit()
        pass

    def insertCourse(self):
        con, cursor = self.__createCursor()
        cursor.execute("insert")
        con.commit()
        pass
