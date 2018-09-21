import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='ali.welightworld.com',
                             user='root',
                             password='dockermysql',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_users_table():
    with connection.cursor() as cursor:
        # 使用预处理语句创建表
        sql = """CREATE TABLE `test`.`users`  (
  `userId` int(0) NOT NULL AUTO_INCREMENT,
  `wechatId` varchar(0) NOT NULL,
  PRIMARY KEY (`userId`)
);"""
        cursor.execute(sql)


def insert_user():
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
    finally:
        connection.close()


def query_user():
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)


if __name__ == '__main__':
    create_users_table()
    # insert_user()
