# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models


class BinanceConfiguration(models.Model):
    user = models.ForeignKey(User)
    api_key = models.CharField(
        max_length=100, blank=True, unique=True, null=True,
        help_text='Binance API key'
    )
    api_secret = models.CharField(
        max_length=100, blank=True, unique=True, null=True,
        help_text='Binance API Secret'
    )