import mysql.connector
from mysql.connector import Error

class MySQLRepository:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def execute_query(self, query, params=None):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
                     
            if params:
                cursor = connection.cursor(buffered=True)
                cursor.execute(query, params)
                connection.commit()
                rows = cursor.fetchall()
                if not rows:
                    rows = [("No data found",)]   
            else:
                cursor = connection.cursor(buffered=True)
                cursor.execute(query)
                connection.commit()
                rows = cursor.fetchall()            
            return rows

        except Error as e:
            print(f"Error executing query: {e}")
            return None

        finally:
            if connection in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def execute_update_query(self, query, params):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
                     
    
            cursor = connection.cursor(buffered=True)
            cursor.execute(query, params)
            connection.commit()                
            return cursor.rowcount

        except Error as e:
            print(f"Error executing query: {e}")
            return None

        finally:
            if connection in locals() and connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == "__main__":
    # Example usage:
    # host = "jamshid.mysql.database.azure.com"
    # user = "jamshid"
    # password = "Eftekhar2024!"
    # database = "orderdb"

    host = "localhost"
    user = "root"
    password = "jam2003eft"
    database = "orderdb"
    repository = MySQLRepository(host, user, password, database)

    # Example: Execute a query to retrieve all rows from a table
    query = "SELECT * FROM orders"
    rows = repository.execute_query(query)
    print("Rows:", rows)

    # Example: Execute a query with parameters to retrieve specific rows
    query = "SELECT * FROM orders WHERE order_id = %s"
    params = (1001,)
    rows_with_params = repository.execute_query(query, params)
    print("Rows with params:", rows_with_params)
    print("Done!", rows_with_params[0][4])
    vat_id = rows_with_params[0][8]
    print(vat_id)
    query = "SELECT Country, VAT_Rate, Country_Code FROM vat WHERE vat_id = %s"
    params = (vat_id,)
    vat_info = repository.execute_query(query, params)
    print("VAT Info:", vat_info)
    vat_rate = vat_info[0][1]
    print("VAT Rate:", vat_rate)
    discount_id = rows_with_params[0][9]
    print(discount_id)
    query = "SELECT Discount_Rate, OrderValue FROM discount WHERE discount_id = %s"
    params = (discount_id,)
    discount_info = repository.execute_query(query, params)
    print("Discount Info:", discount_info)


