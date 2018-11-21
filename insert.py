import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")

mycursor = db.cursor()

# mycursor.execute("select * from products limit 34")
#
#
# results=mycursor.fetchall()
#
# for product in results:
#     print(product[1])

name = input("Enter the name of the product:")
quantity = int(input("Enter product Quantity:"))
price = int(input("Enter the price of the product:"))
sql = "INSERT INTO products (name, quantity, price) VALUES (%s, %s,%s)"
val = (name, quantity, price)
mycursor.execute(sql, val)

db.commit()

print(mycursor.rowcount, "record inserted.")