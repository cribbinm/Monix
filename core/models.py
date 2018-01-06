# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(object):
    pass


class Coin(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=7)
    exchange = models.ForeignKey('Exchange')
    xbt_price = models.DecimalField(max_digits=40, decimal_places=20)
    usd_price = models.DecimalField(max_digits=40, decimal_places=20)
    eur_price = models.DecimalField(max_digits=40, decimal_places=20)


class Asset(Coin):
    amount = models.DecimalField(max_digits=40, decimal_places=20)


class Exchange(models.Model):
    name = models.CharField(max_length=30)


class Deposit(models.Model):
    amount = models.DecimalField(max_digits=40, decimal_places=20)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(
        max_length=200,
        help_text='Address to deposited from'
    )
    tx_id = models.CharField(max_length=200, help_text='Transaction ID')
    coin = models.ForeignKey('Coin')
    exchange = models.ForeignKey('Exchange')


class Withdrawal(models.Model):
    amount = models.DecimalField(max_digits=40, decimal_places=20)
    address = models.CharField(
        max_length=200,
        help_text='Address to withdraw to'
    )
    tx_id = models.CharField(max_length=200, help_text='Transaction ID')
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    coin = models.ForeignKey('Coin')
    exchange = models.ForeignKey('Exchange')


class Order(models.Model):
    ASK = 'ASK'
    BID = 'BID'
    LAST = 'LAST'
    LIMIT = 'LIM'
    STOP_LIMIT = 'SLIM'
    MARKET = 'MAR'
    ORDER_TYPE_CHOICES = (
        ('ASK', 'Ask'),
        ('BID', 'Bid'),
        ('LAST', 'Last'),
        ('LIM', 'Limit'),
        ('SLIM', 'Stop Limit'),
        ('MAR', 'Market'),
    )
    amount = models.DecimalField(
        max_digits=40,
        decimal_places=20,
        help_text='Amount of currency to purchase'
    )
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    base_currency = models.ForeignKey('Coin')
    quote_currency = models.ForeignKey('Coin')
    exchange = models.ForeignKey('Exchange')
    price = models.DecimalField(
        max_digits=40,
        decimal_places=20,
        help_text='Price of one unit of currency'
    )
    volume = models.DecimalField(
        max_digits=40,
        decimal_places=20,
        help_text='Amount of base currency to spend'
    )
    order_type = models.CharField(
        max_length=2,
        choices=ORDER_TYPE_CHOICES,
        default=MARKET,
        help_text='Type of order'
    )


class BuyOrder(Order):
    pass


class SellOrder(Order):
    pass


class NewBuyOrder(BuyOrder):
    pass


class NewSellOrder(SellOrder):
    pass
