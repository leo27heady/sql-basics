import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="051227", database="CovidDatabase"
)

cursor = db.cursor()

cursor.execute("DELETE FROM Blood_test")
cursor.execute("DELETE FROM Covid_analysis")
cursor.execute("DELETE FROM Patient")

db.commit()
cursor.close()
db.close()
