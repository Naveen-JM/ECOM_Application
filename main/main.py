from dao.OrderProcessorRepositoryImpl import OrderProcessorRepositoryImpl
from entity.customers import customers
from entity.products import products
from entity.orders import orders
from exception import customer_exceptions
class EcomApp:
    def __init__(self):
        self.OrderProcessorRepository =  OrderProcessorRepositoryImpl()

    def display_menu(self):
        print("Welcome to the E-commerce Application!")
        print("1. Register Customer.")
        print("2. Create Product.")
        print("3. Delete Product.")
        print("4. Add to Cart.")
        print("5. View Cart.")
        print("6. Place Order.")
        print("7. View Customer Orders.")
        print("8. Exit")

    def createCustomer(self):
        customer_id=input("Enter customer ID: ")
        name=input("Enter customer name: ")
        email=input("Enter customer email: ")
        password=input("Enter customer password: ")

        customer=customers(customer_id, name, email, password)
        success=self.OrderProcessorRepository.createCustomer(customer)

        if success:
            print("Customer registered successfully!")
        else:
            print("Failed to register customer.")

    def createProduct(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        description = input("Enter product description: ")
        stock_quantity = int(input("Enter product stock quantity: "))

        product=products(product_id, name, price, description, stock_quantity)
        success=self.OrderProcessorRepository.createProduct(product)

        if success:
            print("Product created successfully!")
        else:
            print("Failed to create product.")

    def deleteProduct(self):
        product_id = input("Enter product ID to delete: ")
        success=self.OrderProcessorRepository.deleteProduct(product_id)

        if success:
            print("Product deleted successfully!")
        else:
            print("Failed to delete product.")


    def addtocart(self):
        try:
            customer_id=input("Enter customer ID: ")
            product_id=input("Enter product ID to add to cart: ")
            quantity=int(input("Enter quantity: "))
            customers=self.OrderProcessorRepository.getCustomerById(customer_id)
            products=self.OrderProcessorRepository.getProductById(product_id)
            if customers is not None and products is not None:
                success = self.OrderProcessorRepository.addToCart(customers,products,quantity)
        except ValueError:
            print("the quantity is not available")
        except Exception as e:
            print(f"failed to add to cart")

    def view_cart(self):
        # Implement logic for viewing cart
        pass

    def place_order(self):
        # Implement logic for placing order
        pass

    def view_customer_orders(self):
        # Implement logic for viewing customer orders
        pass

    def getAllFromCart(self,customers:customers) -> list:
        pass
    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.createCustomer()
            elif choice == "2":
                self.createProduct()
            elif choice == "3":
                self.deleteProduct()
            elif choice == "4":
                self.addtocart()
            elif choice == "5":
                self.getAllFromCart()
            elif choice == "6":
                self.placeOrder()
            elif choice == "7":
                self.getOrdersByCustomer()
            elif choice == "8":
                print("Exiting the E-commerce Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number from 1 to 8.")

if __name__ == "__main__":
    ecom_app = EcomApp()
    ecom_app.main()
