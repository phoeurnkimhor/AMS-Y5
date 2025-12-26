class CartFullError(Exception):
    """Custom exception for when the cart is full."""
    pass


class Cart:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = []  

    def add_item(self, name, price):
        """Add an item to the cart. Raise error if cart is full."""
        if len(self.items) >= self.capacity:
            raise CartFullError("Cart is full. Cannot add more items.")
        self.items.append((name, price))

    def total_price(self):
        """Calculate total price of items in the cart."""
        return sum(price for _, price in self.items)
