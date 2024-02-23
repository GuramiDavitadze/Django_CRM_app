import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='guka',
    passwd='guka1234',
)

cursorObject = dataBase.cursor(
    
)

cursorObject.execute('CREATE DATABASE elderco')

print("All Done!")