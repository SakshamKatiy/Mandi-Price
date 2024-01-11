from django.db import models
from django.utils import timezone
# Create your models here.
class Commodity(models.Model):
    name=models.CharField('Commodity',default='Select Commodity',max_length=255,blank=True,null=True)

    def __str__(self):
       return self.name

class State(models.Model):
    commodity = models.ForeignKey(Commodity , on_delete=models.CASCADE,null=True)
    name=models.CharField("State",default='Select State',max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name

class Market(models.Model):
    commodity = models.ForeignKey(Commodity , on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(State , on_delete=models.CASCADE, null=True )
    name=models.CharField('Market',default='Select Market',max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name
    
class CommodityData(models.Model):
    commodity = models.ForeignKey(Commodity , on_delete=models.CASCADE,null=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE,null=True)
    
    name=models.CharField('CommodityData',max_length=255,blank=True,null=True)
    avgPrice=models.CharField(max_length=255,blank=True,null=True)
    minPrice=models.CharField(max_length=255,blank=True,null=True)
    maxPrice=models.CharField(max_length=255,blank=True,null=True)
    priceUpdated=models.DateTimeField(default=timezone.now(),blank=True,null=True )
    prevprice=models.CharField(max_length=255,blank=True,null=True)
    
class AllData(models.Model):
        commodity = models.ForeignKey(Commodity , on_delete=models.CASCADE,null=True)
        name=models.CharField('AllData',max_length=255,blank=True,null=True)
        location=models.CharField(max_length=255,blank=True,null=True)

        avgPrice=models.CharField(max_length=255,blank=True,null=True)
        minPrice=models.CharField(max_length=255,blank=True,null=True)
        maxPrice=models.CharField(max_length=255,blank=True,null=True)
        priceUpdated=models.DateTimeField(default=timezone.now(),blank=True,null=True )
        prevprice=models.CharField(max_length=255,blank=True,null=True)
    