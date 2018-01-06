from __future__ import absolute_import, unicode_literals

from monix.exchanges.binance.webservice.client import Client
from monix.exchanges.binance.webservice.exceptions import BinanceAPIException, BinanceWithdrawException


class BinanceWebService(object):

    def __init__(self, api_key='', api_secret='', client=None):
        # self.client = client
        # self.authtoken = self.client.factory.create(b'Authentication')
        # self.authtoken.UserName = username
        # self.authtoken.Password = password
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(api_key, api_secret)

    def get_market_depth(self, symbol):
        # get market depth
        depth = self.client.get_order_book(symbol=symbol)
        return depth

    # place a test market buy order, to place an actual order use the create_order function
    def create_buy_test_order(self, symbol, quantity):
        order = self.client.create_test_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=quantity)
        return order
    
    def create_new_sell_test_order(self, symbol, quantity):
        order = self.client.create_test_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=quantity)
        return order

    def create_buy_order(self, symbol, quantity):
        order = self.client.create_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=quantity)

    def create_sell_order(self, symbol, quantity):
        order = self.client.create_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=quantity)
    
    # get all symbol prices
    def get_all_prices(self):
        prices = self.client.get_all_tickers()
        return prices


    def withdraw(self, asset, address, quantity):
    # check docs for assumptions around withdrawals
        try:
            result = self.client.withdraw(
                asset=asset,
                address=address,
                amount=quantity)
        except BinanceAPIException as e:
            return e
        except BinanceWithdrawException as e:
            return e
        else:
            print("Success")
            return result

    def withdrawal_history(self, asset=None):
        if asset:
            return self.client.get_withdraw_history(asset=asset)
        else:
            return self.client.get_withdraw_history()

    def get_deposit_address(self, asset):
        return self.client.get_deposit_address(asset=asset)
    #
    # # start trade websocket
    # def process_message(self, msg):
    #     print("message type: {}".format(msg['e']))
    #     print(msg)
    #     # do something
    #
    # from binance.websockets import BinanceSocketManager
    # bm = BinanceSocketManager(client)
    # bm.start_aggtrade_socket(symbol=symbol)
    # bm.start()
    
