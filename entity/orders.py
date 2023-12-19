class orders:
    def __init__(self, order_id=None, customer_id=None, order_date=None, total_price=None, shipping_address=None):
        self._order_id = order_id
        self._customer_id = customer_id
        self._order_date = order_date
        self._total_price = total_price
        self._shipping_address = shipping_address

    @property
    def order_id(self):
        return self._order_id

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def order_date(self):
        return self._order_date

    @property
    def total_price(self):
        return self._total_price

    @property
    def shipping_address(self):
        return self._shipping_address

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @order_date.setter
    def order_date(self, value):
        self._order_date = value

    @total_price.setter
    def total_price(self, value):
        self._total_price = value

    @shipping_address.setter
    def shipping_address(self, value):
        self._shipping_address = value

    def __str__(self):
        return f"Order ID: {self._order_id}, Customer ID: {self._customer_id}, Order Date: {self._order_date}, Total Price: {self._total_price}, Shipping Address: {self._shipping_address}"

