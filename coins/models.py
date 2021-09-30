from django.db import models

class Coin(models.Model):
    rank = models.IntegerField(default=0, blank=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0, blank=True)
    price_change_percentage_24h = models.FloatField(default=0, blank=True)
    market_cap = models.FloatField(default=0, blank=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']