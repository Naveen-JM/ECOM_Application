class order_items:
    def __init__(self, order_item_id=None, order_id=None, product_id=None, quantity=None):
        self._order_item_id = order_item_id
        self._order_id = order_id
        self._product_id = product_id
        self._quantity = quantity

    @property
    def order_item_id(self):
        return self._order_item_id

    @property
    def order_id(self):
        return self._order_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    @order_item_id.setter
    def order_item_id(self, value):
        self._order_item_id = value

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def __str__(self):
        return f"Order Item ID: {self._order_item_id}, Order ID: {self._order_id}, Product ID: {self._product_id}, Quantity: {self._quantity}"
