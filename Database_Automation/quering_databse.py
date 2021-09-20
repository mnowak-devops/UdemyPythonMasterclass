import psycopg2

try:
    connection = psycopg2.connect(database="staff", user = "mihai", password = "python3", host = "127.0.0.1", port = "5432")

except psycopg2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()

cursor.execute("SELECT * FROM mystaff.employees WHERE salary > 50000;")

records  = cursor.fetchall()
print(records)

for record in records:
    print (record)



cursor.execute("SELECT * FROM mystaff.employees WHERE salary between 40000 and 45000;")

records = cursor.fetchall()
for record in records:
    print (record)
print("\n")

cursor.execute("SELECT * FROM mystaff.employees WHERE department in ('Sales', 'Logistics');")

records = cursor.fetchall()
for record in records:
    print (record)

print("\n")

cursor.execute("SELECT * FROM mystaff.employees WHERE last_name like 'D%';")

records = cursor.fetchall()
for record in records:
    print (record)