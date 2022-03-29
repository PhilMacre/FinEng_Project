

class Order:
    identi=0
    def __init__(self, quantity, price, buy=True,id=0):
        self.quantity = quantity
        delf.price = price
        self.buy = True  #quand on insert sell on change le self.buy to false
        order.identi+=1
        self.id = order.identi
def  __str__(self):
    if self.buy = True:
        return f"BUY {self.quantity}@{self.price} id={self.id}" #pas besoin de mettre l'id et le nom du book, on le fera pour override book.__str__
    else :
        return f"SELL {self.quantity}@{self.price} id={self.id} "

def __eq__(self, other):
    return other and self.quantity == other.quantity and self.price==other.price

def __lt__(self,other):
    return other and self.price < other.price


class Book:
    def __init__(self,NAME):
        self.NAME = NAME
        self.buy_orders=[]
        self.sell_orders=[]

    def insert_sell(self,quantity,price):
        sell_order=Order(self.quantity,self.price,False)
        self.sell_orders.sort(key=lambda x: x.price*x.id,reverse=False)#sell donc le plus petit prix en premier mais pour s'épargner l'ordre qui est arrivé en premier aura son produit P0*id plus petit, plus besoin de comparer les id
        bisect.insort(self.sell_orders,sell_order,key= lambda x: x.price*x.id)





