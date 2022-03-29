from order import Order
from deal import Deal
import warnings
import pandas as pd
warnings.simplefilter(action='ignore', category=FutureWarning)

class Book:
    def __init__(self, name='Default order book', buy_orders=[], sell_orders=[], execute_deals=[]):
        
        self._name = name
        self._buy_orders = buy_orders
        self._sell_orders = sell_orders
        self._execute_deals = execute_deals
         
        

    def insert_sell(self, quantity, price):
        
        sell_order = Order(quantity, price, type_of_order='sell')

        if quantity != 0:
            self._sell_orders.append(sell_order)
            self._sell_orders.sort()
            print('--- Insert {order} on {book}'.format(order=sell_order.__str__(), book=self._name))

        while len(self._buy_orders) != 0 and self._buy_orders[0].get_price() >= sell_order.get_price() and sell_order.get_quantity() > 0:

           
            if sell_order.get_quantity() > self._buy_orders[0].get_quantity():
                deal = Deal(self._buy_orders[0].get_quantity(), self._buy_orders[0].get_price(), self._name)
                self._execute_deals.append(deal)

                new_qty = sell_order.get_quantity() - self._buy_orders[0].get_quantity()

               
                self._buy_orders.remove(self._buy_orders[0])

                sell_order.set_quantity(new_qty)
                print(deal.__str__())
            else:
                deal = Deal(sell_order.get_quantity(), self._buy_orders[0].get_price(), self._name)
                self._execute_deals.append(deal)

               
                self._buy_orders[0].set_quantity(self._buy_orders[0].get_quantity() - sell_order.get_quantity())

                sell_order.set_quantity(0)

                if self._buy_orders[0].get_quantity() == 0:
                    self._buy_orders.remove(self._buy_orders[0])

                self._sell_orders.remove(self._sell_orders[0])
                
                print(deal.__str__())
        
        print(self.get_status())

        return None

    def insert_buy(self, quantity, price):
       
        buy_order = Order(quantity, price, type_of_order='buy')

        if quantity != 0:
            self._buy_orders.append(buy_order)
            self._buy_orders.sort()
            self._buy_orders.reverse()
            print('--- Insert {order} on {book}'.format(order=buy_order.__str__(), book=self._name))

        while len(self._sell_orders) != 0 and self._sell_orders[0].get_price() <= buy_order.get_price() and buy_order.get_quantity() > 0:

            if buy_order.get_quantity() > self._sell_orders[0].get_quantity():
                
                deal = Deal(self._sell_orders[0].get_quantity(), self._sell_orders[0].get_price(), self._name)
                
                self._execute_deals.append(deal)

                new_qty = buy_order.get_quantity() - self._sell_orders[0].get_quantity()
               
                self._sell_orders.remove(self._sell_orders[0])

                buy_order.set_quantity(new_qty)
                print(deal.__str__())

          
            else:
                deal = Deal(buy_order.get_quantity(), self._sell_orders[0].get_price(), self._name)
                
                self._execute_deals.append(deal)

                self._sell_orders[0].set_quantity(self._sell_orders[0].get_quantity() - buy_order.get_quantity())

                buy_order.set_quantity(0)

                self._buy_orders.remove(self._buy_orders[0])

                if self._sell_orders[0].get_quantity() == 0:
                    
                    self._sell_orders.remove(self._sell_orders[0])
                print(deal.__str__())
        print(self.get_status())
        return None

    def insert_deals(self, deal):
        
        self._execute_deals.append(deal)
        return None

    def get_sell_order(self):
        return self._sell_orders

    def get_buy_orders(self):
        return self._buy_orders

    def get_status(self):
        """
            Return the order book status (string)
        :return: string
            Status of the order book
        """
        status = ""

        status += 'Book on {}\n'.format(self._name.upper())
        order_book = self.create_df_order()
        status += order_book.to_string(index=False)
        status += '\n------------------------'
        return status

    def create_df_order(self):
 
        df_sell_orders = pd.DataFrame([sell_order.__dict__ for sell_order in self._sell_orders])
        df_buy_orders = pd.DataFrame([buy_order.__dict__ for buy_order in self._buy_orders])
        df_all_orders = df_sell_orders.append(df_buy_orders)
        df_all_orders.columns = ['QTY', 'PRICE', 'TYPE', 'ID']
        return df_all_orders



         

