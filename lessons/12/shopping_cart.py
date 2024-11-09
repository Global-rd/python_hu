

class ShoppingCart:

    def __init__(self):
        self.items = {}

    
    def add_item(self, item_name:str, price:float, quantity:int=1):
        
        if quantity <=0:
            raise ValueError("Quantity must be positive")
        if price < 0:
            raise ValueError("Price can not be negative")
        
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
        else:
            self.items[item_name] = {"price": price, "quantity": quantity}

    def remove_item(self, item_name:str, quantity:int=1):
        if item_name not in self.items:
            raise ValueError("Item not in cart.")

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if self.items[item_name]["quantity"] <= quantity:
            del self.items[item_name]
        else:
            self.items[item_name]["quantity"] -= quantity

    def get_total_cost(self):
        
        return sum(item["price"] * item["quantity"] for item in self.items.values())

    def apply_discount(self, discount_code:str):
        #in prod there would be an external service to check if discount code is valid
        #for this case we return a dictionary
        valid_codes = {"SAVE10": 0.1, "SAVE20": 0.2}
        discount = valid_codes.get(discount_code, 0)
        return self.get_total_cost() * (1 - discount)

    def checkout(self, discount_code:str):
        
        discounted_price = self.apply_discount(discount_code)
        return discounted_price


#MOCKING: egy konkrét objektum kreálása aminek egy fix visszatérési értéket adunk : pl időjárás api -> fixen mindig 15 fokot ad vissza
#PATCHING: szimplán egy metódus felülírása statikus visszatérési értékkel. pl: apply discount mindig 10%-ot fog visszaadni.