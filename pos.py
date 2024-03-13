#point of sale code
class SaleItem:
    def __init__(self, item_id, item_name, unit_price):
        self.item_id = item_id
        self.item_name = item_name
        self.unit_price = unit_price

    def calculate_total(self, quantity):
        return self.unit_price * quantity

class StandardItem(SaleItem):
    def calculate_total(self, quantity):
        return super().calculate_total(quantity)

class DiscountedItem(SaleItem):
    def __init__(self, item_id, item_name, unit_price, discount_percentage):
        super().__init__(item_id, item_name, unit_price)
        self.discount_percentage = discount_percentage

    def calculate_total(self, quantity):
        discounted_price = self.unit_price * (1 - self.discount_percentage / 100)
        return discounted_price * quantity

class ServiceItem(SaleItem):
    def __init__(self, item_id, item_name, unit_price, hourly_rate):
        super().__init__(item_id, item_name, unit_price)
        self.hourly_rate = hourly_rate

# Example usage:
standard_item = StandardItem("123", "Widget", 10.0)
print(f"Total cost for 5 widgets: ${standard_item.calculate_total(5)}")
