class cart:
    def __init__(self, cart_id=None, customer_id=None, product_id=None, quantity=None):
        self._cart_id = cart_id
        self._customer_id = customer_id
        self._product_id = product_id
        self._quantity = quantity

    @property
    def cart_id(self):
        return self._cart_id

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    @cart_id.setter
    def cart_id(self, value):
        self._cart_id = value

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def __str__(self):
        return f"Cart ID: {self._cart_id}, Customer ID: {self._customer_id}, Product ID: {self._product_id}, Quantity: {self._quantity}"
