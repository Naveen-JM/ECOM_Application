import unittest
from entity.customers import customers
from entity.products import products
from dao.OrderProcessorRepository import OrderProcessorRepository


class TestEcommerce(unittest.TestCase):
    def setUp(self):
        self.opr_instance = OrderProcessorRepository()

    def test_product_creation(self):
        prod = products(product_id=107, name='Tab', price=30200,
                       description='High performance and user friendly', stock_quantity=34)
        result = self.opr_instance.create_product(product=prod)
        self.assertEqual(result, True, 'Product Creation Successful.')

    def test_customer_reg(self):
        cust = customers(customer_id=9, name='ramya', email='ramya@gmail.com', password='ramya123')
        result = self.opr_instance.create_customer(customer_object=cust)
        self.assertEqual(result, True, 'Customer Registration Successful.')


if __name__ == '__main__':
    unittest.main()