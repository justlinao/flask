import pymysql.cursors


class Mysql:

    def queryData(self):
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',  # 密码
            'db': 'test',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
        }
        # Connect to the database
        connection = pymysql.connect(**config)

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM school"  # sql语句
                cursor.execute(sql)
                row_1 = cursor.fetchone()  # 我这边查询的是第一条的数据
                print(row_1)
                return row_1
            connection.commit()
        finally:
            connection.close()