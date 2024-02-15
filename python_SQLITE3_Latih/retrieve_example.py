import sqlite3

conn = sqlite3.connect('companies.db')

cursor = conn.execute("SELECT name,address,salary FROM COMPANY")
for row in cursor:
    print("NAME =", row[0])
    print("ADDRESS =", row[1])
    print("SALARY =", row[2], "\n")
    
print('\n\nin Case Salary upper limit\n\n')

salary_upper_limit = 20000
cursor = conn.execute("SELECT name,address,salary FROM COMPANY WHERE salary > ?", (salary_upper_limit,))
for row in cursor:
    print("NAME =", row[0])
    print("ADDRESS =", row[1])
    print("SALARY =", row[2], "\n")

conn.close()
