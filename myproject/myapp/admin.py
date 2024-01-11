from django.contrib import admin
from .models import Commodity
from .models import State
from .models import Market,CommodityData,AllData
# Register your models here.
admin.site.register(Commodity)
admin.site.register(State)
admin.site.register(Market)
admin.site.register(CommodityData)
admin.site.register(AllData)