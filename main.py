from Services.calculator_object import PriceCalculator
from Persistance.MysqlDbConnector import MySQLRepository

host = "localhost"
user = "root"
password = "jam2003eft"
database = "orderdb"
repository = MySQLRepository(host, user, password, database)

# Example: Execute a query to retrieve all rows from a table
query = "SELECT * FROM orders"
rows = repository.execute_query(query)
print("Rows:", rows)

# get the unit price, quantity, vat rate and discount rate from the database

query = "SELECT * FROM orders WHERE order_id = %s"
params = (1001,)
rows_with_params = repository.execute_query(query, params)
print("Rows with params:", rows_with_params)
unit_price = rows_with_params[0][3]
print("Unit Price:", unit_price)
quantity = rows_with_params[0][2]
print("Quantity:", quantity)
subtotal = rows_with_params[0][4]
print("SubToal price", subtotal)
vat_price = rows_with_params[0][5]
print("VAT Price:", vat_price)
discount_price = rows_with_params[0][6]
print("Discount Price:", discount_price)
total_price = rows_with_params[0][7]
print("Total Price:", total_price)
print("-----------------")
print("VAT info:")
vat_id = rows_with_params[0][8]
print("Vat id",vat_id)
query = "SELECT Country, VAT_Rate, Country_Code FROM vat WHERE vat_id = %s"
params = (vat_id,)
vat_info = repository.execute_query(query, params)
print("VAT Info:", vat_info)
vat_rate = vat_info[0][1]
print("VAT Rate:", vat_rate)
print("-----------------")
print("Discount info:")
discount_id = rows_with_params[0][9]
print("discount Id: ",discount_id)
query = "SELECT Discount_Rate, OrderValue FROM discount WHERE discount_id = %s"
params = (discount_id,)
discount_info = repository.execute_query(query, params)
print("Discount Info:", discount_info)
discount_rate = discount_info[0][0]
print("Discount Rate:", discount_rate)
print("-----------------")
print("Calculate the price:")
calculator = PriceCalculator(unit_price, quantity, vat_rate, discount_rate)
price = calculator.calculate_price()
vat = calculator.calculate_vat()
total_price = calculator.calculate_total_price()
discounted_price = calculator.calculate_discounted_price()
print(f"Price no VAT: {price:.2f}")
print(f"VAT: {vat:.2f}")
print(f"Total Price: {total_price:.2f}")
print(f"Discounted Price no vat: {discounted_price:.2f}")


# Example: Execute a query to retrieve all rows from the view
query = "SELECT * FROM orderdetail"
rows = repository.execute_query(query)
print("Rows: ", rows)
print("Row 0: ",rows[0])
id = rows[1][0]
print("ID: ", id)
item = rows[0][1]
print("Item: ", item)
quantity = rows[0][2]
print("Quantity: ", quantity)
price = rows[0][3]
print("Price: ", price)
vat = rows[0][5]
print("VAT: ", vat)
discount = rows[0][6]
print("Discount: ", discount)
calc = PriceCalculator(price, quantity, vat, discount)
sub_total_price = float(calc.calculate_price())
print("Subtotal Price: ", sub_total_price)
vat_price = float(calc.calculate_vat())
print("VAT Price: ", vat_price)
total_price = float(calc.calculate_total_price())
print("Total Price: ", total_price)
discounted_price = float(calc.calculate_discounted_price())
print("Discounted Price: ", discounted_price)
print("Done!")
query = "update orders set total_price = %s, discount_price = %s, vat_price = %s, sub_total_price = %s where order_id = %s"
params = (total_price, discounted_price, vat_price, sub_total_price, id)
rows = repository.execute_update_query(query, params)
print("Uodate Done!")
print("Number of Rows: ", rows)
query = "SELECT * FROM orders"
rows = repository.execute_query(query)
print("Rows: ", rows)
#print("Row 0: ",rows[0])