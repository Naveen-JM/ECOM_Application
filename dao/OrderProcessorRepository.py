from abc import ABC, abstractmethod
from entity.customers import customers
from entity.products import products

class OrderProcessorRepository(ABC):
    @abstractmethod
    def createProduct(self,products:products) ->bool:
        pass
    @abstractmethod
    def createCustomer(self,customers:customers) ->bool:
        pass
    @abstractmethod
    def deleteProduct(self, product_id) ->bool:
        pass
    @abstractmethod
    def deleteCustomer(self,customer_id) ->bool:
        pass
    @abstractmethod
    def addtocart(self,customers:customers,products:products,quantity:int) ->bool:
        pass
    @abstractmethod
    def removefromcart(self,customers:customers,products:products) ->bool:
        pass
    @abstractmethod
    def getAllFromCart(self,customers:customers) ->list:
        pass
    @abstractmethod
    def placeOrder(self, customers:customers, products_and_quantities: list, shipping_address: str) -> bool:
        pass
    @abstractmethod
    def getOrdersByCustomer(self, customer_id) -> list:
        pass
    @abstractmethod
    def view_cart(self):
        pass





