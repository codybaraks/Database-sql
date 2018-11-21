import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")

mycursor = db.cursor()

mycursor.execute("select * from products limit 34")
#
#
results=mycursor.fetchall()
#
# for product in results:
#     print(product[1])

name = input("Enter item to Delete")

if name == 'Cassis':

    sql = "DELETE FROM products WHERE name =%s"

    mycursor.execute(sql, (name,))

    db.commit()

print(mycursor.rowcount, "Record Deleted.")