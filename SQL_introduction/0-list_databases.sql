import mysql.connector

cnx = mysql.connector.connect(
  host="localhost",
  user="tu_nombre_de_usuario",
  password="tu_contraseña"
)

cursor = cnx.cursor()

cursor.execute("SHOW DATABASES")

for db in cursor:
  print(db[0])

cnx.close()