import bisect
from functools import total_ordering

class Order:
    identi=0
    def __init__(self, quantity, price, buy=True,id=0):
        self.quantity = quantity
        self.price = price
        self.buy = True  #quand on insert sell on change le self.buy to false
        Order.identi+=1
        self.id = Order.identi
def  __str__(self):
    if self.buy == True:
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

    def exec(self,order):
        if order.buy :
            while len(self.sell_orders)!=0 and self.sell_orders[0].price <= order.price and order.quantity > 0:
                if order.quantity<self.sell_orders[0]: #Ordre cmplet
                    self.sell_orders[0].quantity-=order.quantity
                else : #Ordre partiel
                    order.quantity-=self.sell_orders[0]
                    self.sell_orders=self.sell_orders[1:]
                    
                    
        else : 
            while len(self.buy_orders)!=0 and self.buy_orders[0].price >= order.price and order.quantity > 0:
                if order.quantity < self.buy_orders[0]:
                    self.buy_orders[0].quantity-=order.quantity
                else : 
                    order.quantity -= self.buy_orders[0]
                    self.buy_orders=self.buy_orders[1:]

    def insert_sell(self,quantity,price):
        sell_order=Order(quantity,price,False)
        print(f"----- Insert {sell_order.__str__()} on {self.NAME}")
        self.sell_orders.sort(key=lambda x: x.price*x.id,reverse=False)#sell donc le plus petit prix en premier mais pour s'épargner l'ordre qui est arrivé en premier aura son produit P0*id plus petit, plus besoin de comparer les id
        exec(self,sell_order)
        bisect.insort(self.sell_orders,sell_order)
        print(sell_order)

    def insert_buy(self,quantity,price):
        buy_order=Order(quantity,price,True)
        print(f"----- Insert {buy_order.__str__()} on {self.NAME}")
        
        self.buy_orders.sort(key=lambda x: x.price*x.id,reverse=True) #buy donc le plus élevé en premier
        exec(self,buy_order)
        bisect.insort(self.buy_orders,buy_order)





