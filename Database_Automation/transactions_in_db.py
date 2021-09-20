import psycopg2

try:
    connection = psycopg2.connect(database="staff", user = "mihai", password = "python3", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()

cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary)\
    values (6, 'Jane', 'Sanders', 'HR', '0123452289', '6th Dtreet, Miami', 61000);")

cursor.execute("SELECT * FROM mystaff.employees;")
records = cursor.fetchall()
for i in records:
    print(i)
print("\n")

cursor = connection.cursor()
connection.rollback()

cursor.execute("SELECT * FROM mystaff.employees;")
records = cursor.fetchall()
for i in records:
    print(i)
cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary)\
    values (6, 'Jane', 'Sanders', 'HR', '0123452289', '6th Dtreet, Miami', 61000);")
connection.commit()