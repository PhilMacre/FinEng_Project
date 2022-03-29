import itertools


class Order:
    nb_of_id = itertools.count(1) 
    
    
    
    def __init__(self, quantity, price, type_of_order):
        
        self._quantity = quantity
        self._price = price
        self._type = type_of_order.upper()
        self._id = next(self.nb_of_id)
        
        
        
    def __str__(self): 
        return self._type.upper() + " %s@%s id=%s" % (self._quantity, self._price, self._id)

    def __eq__(self, other):
        
        return (self._quantity, self._price) == (other._quantity, other._price)

    def __lt__(self, other):
        
        return self._price <= other._price

    def get_id(self):
        
        return self._id

    def get_quantity(self):
        
        return self._quantity

    def get_price(self):
       
        return self._price

    def set_quantity(self, quantity):
        
        self._quantity = quantity

