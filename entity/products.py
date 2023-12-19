class products:
    def __init__(self, product_id=None, name=None, price=None, description=None, stock_quantity=None):
        self._product_id=product_id
        self._name=name
        self._price=price
        self._description=description
        self._stock_quantity=stock_quantity

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @product_id.setter
    def product_id(self, value):
        self._product_id=value

    @name.setter
    def name(self, value):
        self._name=value

    @price.setter
    def price(self, value):
        self._price=value

    @description.setter
    def description(self, value):
        self._description=value

    @stock_quantity.setter
    def stock_quantity(self, value):
        self._stock_quantity=value

    def __str__(self):
        return f"Product ID: {self._product_id}, Name: {self._name}, Price: {self._price}, Description: {self._description}, Stock Quantity: {self._stock_quantity}"

