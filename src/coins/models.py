from django.db import models

class Coin(models.Model):
    symbol = models.CharField(max_length=5)
    trading_pair = models.CharField(max_length=5)

    def __str__(self):
        return self.symbol