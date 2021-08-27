import pyodbc

## Conexion mediante odbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-RROBOR5;'
                      'Database=MediSoft;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.City')

for row in cursor:
    print(row[2])