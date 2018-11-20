import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")

mycursor = db.cursor()

mycursor.execute("select * from products limit 34")
#
#
results=mycursor.fetchall()
#
for product in results:
    print(product[1])

sql = "DELETE FROM products WHERE name= 'Tissue'"

mycursor.execute(sql)

db.commit()

print(mycursor.rowcount, "Record Deleted.")