import pymysql
# Open database connection
db = pymysql.connect("localhost")
cursor = db.cursor()
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

# prepare a cursor object using cursor() method

