

class Order:
    def __init__(self, quantity, price, buy=True):
        self.quantity = quantity
        delf.price = price
        self.buy = True  #quand on insert sell on change le self.buy to false

def  __str__(self):
    if self.buy = True:
        return f"BUY {self.quantity}@{self.price}" #pas besoin de mettre l'id et le nom du book, on le fera pour override book.__str__
    else :
        return f"SELL {self.quantity}@{self.price}"

def __eq__(self, other):
    return other and self.quantity == other.quantity and self.price==other.price

def __lt__(self,other):
    return other and self.price < other.price

