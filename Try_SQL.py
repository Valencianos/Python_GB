import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="sqluse",
    password="password",
    database="gb_lesson_3"
)

print(connection)

select_students_query = "SELECT * FROM staff"
with connection.cursor() as cursor:
    cursor.execute(select_students_query)
    result = cursor.fetchall()
    for row in result:
        print(row)
