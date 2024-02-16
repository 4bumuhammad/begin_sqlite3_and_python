import sqlite3

conn = sqlite3.connect('companies.db')

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
    VALUES ('Paul',32,'California',20000.00)");

company_5_array = ['Amith', 28, 'Kyrgyzstan', 100000]

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
    VALUES (?,?,?,?)", (company_5_array[0],company_5_array[1],company_5_array[2],company_5_array[3]));

conn.commit()
conn.close()