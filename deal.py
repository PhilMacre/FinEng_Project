class Deal:
    def __init__(self, quantity, price, book_name):
     """ a deal is defined with a quantity (amount of the transaction), its price and the book name it refers to """  
        self._quantity = quantity
        self._price = price
        self._book_name = book_name

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def get_book_name(self):
        return self._book_name

    def __str__(self):
        return 'Execute {quantity} at {price} in {book}'.format(quantity=self._quantity, price=self._price,
                                                                book=self._book_name)

