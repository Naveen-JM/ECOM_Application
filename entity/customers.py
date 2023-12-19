class customers:
    def __init__(self, customer_id=None, name=None, email=None, password=None):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._password = password

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @name.setter
    def name(self, value):
        self._name = value

    @email.setter
    def email(self, value):
        self._email = value

    @password.setter
    def password(self, value):
        self._password = value

    def __str__(self):
        return f"Customer ID: {self._customer_id}, Name: {self._name}, Email: {self._email}, Password: {self._password}"

# Example Usage:
# customer = Customer(customer_id=1, name="John Doe", email="john@example.com", password="secure_password")
# print(customer)
