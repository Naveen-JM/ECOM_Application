from dao.OrderProcessorRepository import OrderProcessorRepository
from entity.customers import customers
from entity.products import products
from util.DBUtil import DBUtil
from exception import customer_exceptions
from exception import order_exceptions
from exception import product_exceptions


class OrderProcessorRepositoryImpl:
    def createCustomer(self,customers:customers) -> bool:
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            insert_query="INSERT INTO customers(customer_id,name, email,password)VALUES(%s,%s,%s,%s)"
            cursor.execute(insert_query,(customers.customer_id, customers.name, customers.email, customers.password))
            connection.commit()
            return True
        except Exception as e:
            print(f"Failed to create a Customer: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def createProduct(self, products: products) -> bool:
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            insert_query="INSERT INTO products(product_id,name,price,description,stockQuantity)VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(insert_query,(products.product_id,products.name,products.price,products.description,products.stock_quantity))
            connection.commit()
            return True
        except Exception as e:
            print(f"Failed to create a Product: {e}")
            return False
        finally:
            cursor.close()
            connection.close()


    def deleteCustomer(self, customer_id) -> bool:
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()
            delete_query = "DELETE FROM customers WHERE customer_id = %s"
            cursor.execute(delete_query, (customer_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Failed to delete customer: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def deleteProduct(self, product_id) ->bool:
        try:
            connection=DBUtil.getDBConn()
            cursor=connection.cursor()
            delete_query="DELETE FROM customers WHERE product_id = %s"
            cursor.execute(delete_query,(product_id,))
            connection.commit()
            return True
        except Exception as e:
            print(f"Failed to delete customer: {e}")
            return False
        finally:
            cursor.close()
            connection.close()

    def addtocart(self, customers:customers,products:products,quantity:int) -> bool:
     try:
        connection = DBUtil.getDBConn()
        cursor = connection.cursor()

        # To check the customer and product
        check_query = "SELECT * FROM cart WHERE customer_id = %s AND product_id = %s"
        cursor.execute(check_query, (customers.customer_id, products.product_id))
        item_exists = cursor.fetchone()

        # Now check if the product is in cart and update the cart
        if item_exists:
            update_query = "UPDATE cart SET quantity = quantity + %s WHERE customer_id = %s AND product_id = %s"
            cursor.execute(update_query,(quantity, customers.customer_id, products.product_id))
        else:
            insert_query = "INSERT INTO cart(customer_id, product_id, quantity) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (customers.customer_id, products.product_id,quantity))

        connection.commit()
        return True
     except Exception as e:
         print(f"Failed to add to cart: {e}")
         return False
     finally:
         cursor.close()
         connection.close()



