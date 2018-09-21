import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='ali.welightworld.com',
                             user='root',
                             password='dockermysql',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)

        # 使用预处理语句创建表
        # sql = """CREATE TABLE EMPLOYEE (
        #          FIRST_NAME  CHAR(20) NOT NULL,
        #          LAST_NAME  CHAR(20),
        #          AGE INT,
        #          SEX CHAR(1),
        #          INCOME FLOAT )"""
        # cursor.execute(sql)
finally:
    connection.close()



