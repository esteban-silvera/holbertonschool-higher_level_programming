import mysql.connector

# coment
cnx = mysql.connector.connect(
  host="localhost",
  user="tu_nombre_de_usuario",
  password="tu_contraseña"
)

# coment
cursor = cnx.cursor()

# coment
cursor.execute("SHOW DATABASES")

# coment
for db in cursor:
  print(db[0])

# coment
cnx.close()
