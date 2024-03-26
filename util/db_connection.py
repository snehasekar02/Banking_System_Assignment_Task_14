import pymysql.cursors


class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='Sneha@123',
                database='BankSystem',
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except Exception as e:
            print("Error connecting to the database:", e)
            return None
