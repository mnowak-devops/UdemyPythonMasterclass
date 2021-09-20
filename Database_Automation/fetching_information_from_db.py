import psycopg2

try:
    connection = psycopg2.connect(database="staff", user = "mihai", password = "python3", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()


cursor.execute("SELECT * FROM mystaff.employees WHERE salary between 40000 and 55000;")

records  = cursor.fetchall()

for i in records:
    print (i)


cursor.execute("SELECT * FROM mystaff.employees WHERE salary between 40000 and 55000;")

records  = cursor.fetchone()

for i in records:
    print (i)

records  = cursor.fetchone()

for i in records:
    print (i)

records  = cursor.fetchone()

for i in records:
    print (i)

records  = cursor.fetchone()

for i in records:
    print (i)



cursor.execute("SELECT * FROM mystaff.employees WHERE salary between 40000 and 55000;")

records  = cursor.fetchmany(size = 2)

for i in records:
    print (i)