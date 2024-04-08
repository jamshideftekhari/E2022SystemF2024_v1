class PriceCalculator:
    def __init__(self, unit_price, quantity, vat_rate, discount_rate=0):
        self.unit_price = float(unit_price)
        self.quantity = int(quantity)
        self.vat_rate = float(vat_rate)
        self.discount_rate = float(discount_rate)

    def calculate_price(self):
        return self.unit_price * self.quantity

    def calculate_vat(self):
        return (self.calculate_price() * self.vat_rate) / 100

    def calculate_total_price(self):
        return self.calculate_price() + self.calculate_vat()

    def calculate_discounted_price(self):
        discount_amount = (self.calculate_price() * self.discount_rate) / 100
        return self.calculate_price() - discount_amount

# Example usage:
unit_price = 15.99
quantity = 5
vat_rate = 19.0
discount_rate = 10.0

calculator = PriceCalculator(unit_price, quantity, vat_rate, discount_rate)

price = calculator.calculate_price()
vat = calculator.calculate_vat()
total_price = calculator.calculate_total_price()
discounted_price = calculator.calculate_discounted_price()

print(f"Price: {price:.2f}")
print(f"VAT: {vat:.2f}")
print(f"Total Price: {total_price:.2f}")
print(f"Discounted Price: {discounted_price:.2f}")
