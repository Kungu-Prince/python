#inventory management system using class and inheritance
from datetime import datetime

class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def calculate_value(self):
        pass

class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")

    def calculate_value(self):
        remaining_shelf_life = (self.expiry_date - datetime.now()).days
        discount = max(0, remaining_shelf_life / 30)  # Adjust as needed, considering a 30-day discount period
        return self.quantity_in_stock * self.unit_price * (1 - discount)

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price

# Taking user input for SimpleProduct
simple_product_id = int(input("Enter Simple Product ID: "))
simple_product_name = input("Enter Simple Product Name: ")
simple_product_quantity = int(input("Enter Simple Product Quantity in Stock: "))
simple_product_price = float(input("Enter Simple Product Unit Price: "))

# Instantiate SimpleProduct with user input
simple_product = SimpleProduct(product_id=simple_product_id, name=simple_product_name, quantity_in_stock=simple_product_quantity, unit_price=simple_product_price)

# Calculate and print SimpleProduct value
simple_product_value = simple_product.calculate_value()
print(f"Simple Product Value: ${simple_product_value:.2f}")

# Taking user input for PerishableProduct
perishable_product_id = int(input("Enter Perishable Product ID: "))
perishable_product_name = input("Enter Perishable Product Name: ")
perishable_product_quantity = int(input("Enter Perishable Product Quantity in Stock: "))
perishable_product_price = float(input("Enter Perishable Product Unit Price: "))
perishable_product_expiry_date = input("Enter Perishable Product Expiry Date (YYYY-MM-DD): ")

# Instantiate PerishableProduct with user input
perishable_product = PerishableProduct(product_id=perishable_product_id, name=perishable_product_name, quantity_in_stock=perishable_product_quantity, unit_price=perishable_product_price, expiry_date=perishable_product_expiry_date)

# Calculate and print PerishableProduct value
perishable_product_value = perishable_product.calculate_value()
print(f"Perishable Product Value: ${perishable_product_value:.2f}")

# Taking user input for DigitalProduct
digital_product_id = int(input("Enter Digital Product ID: "))
digital_product_name = input("Enter Digital Product Name: ")
digital_product_quantity = int(input("Enter Digital Product Quantity in Stock: "))
digital_product_price = float(input("Enter Digital Product Price: "))

# Instantiate DigitalProduct with user input
digital_product = DigitalProduct(product_id=digital_product_id, name=digital_product_name, quantity_in_stock=digital_product_quantity, price=digital_product_price)

# Calculate and print DigitalProduct value
digital_product_value = digital_product.calculate_value()
print(f"Digital Product Value: ${digital_product_value:.2f}")
