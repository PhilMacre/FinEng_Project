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
    def __repr__(self): # unambiguous representation of the object
        return f"Order({self.quantity}, {self.price})"

class Book:
    def __init__(self,NAME):
        self.NAME = NAME
        self.buy_orders=[]
        self.sell_orders=[]

    def __str__(self):
        a=f"Book on {self.NAME} \n \t "
        print(a)
        for i in range(len(self.sell_orders)-1): 
            print(f"{self.sell_orders[i].__str__}")
        for j in range(len(self.buy_orders)-1):
            print(f"{self.buy_orders[i].__str__}")
        

    def insert_sell(self,quantity,price):
        sell_order=Order(quantity,price,False)
        print(f"----- Insert {sell_order.__str__()} on {self.NAME}")
        self.sell_orders.sort(key=lambda x: x.price*x.id,reverse=False)#sell donc le plus petit prix en premier mais pour s'épargner l'ordre qui est arrivé en premier aura son produit P0*id plus petit, plus besoin de comparer les id
        while len(self.buy_orders)!=0 and self.buy_orders[0].price >= sell_order.price and sell_order.quantity > 0:
            if sell_order.quantity < self.buy_orders[0].quantity:
                self.buy_orders[0].quantity-=sell_order.quantity
            else : 
                sell_order.quantity -= self.buy_orders[0].quantity
                self.buy_orders=self.buy_orders[1:]
        bisect.insort(self.sell_orders,sell_order)
        print(self.__str__())
        

    def insert_buy(self,quantity,price):
        buy_order=Order(quantity,price,True)
        print(f"----- Insert {buy_order.__str__()} on {self.NAME}")
        
        self.buy_orders.sort(key=lambda x: x.price*x.id,reverse=True) #buy donc le plus élevé en premier
        while len(self.sell_orders)!=0 and self.sell_orders[0].price <= buy_order.price and buy_order.quantity > 0:
            if buy_order.quantity<self.sell_orders[0].quantity: #Ordre cmplet
                self.sell_orders[0].quantity-=buy_order.quantity
            else : #Ordre partiel
                buy_order.quantity-=self.sell_orders[0].quantity
                self.sell_orders=self.sell_orders[1:]
        bisect.insort(self.buy_orders,buy_order)
        #print(self.__str__())






