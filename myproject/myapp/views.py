from django.shortcuts import render
from django.db.models import Q

from .models import State,Market,Commodity,CommodityData,AllData
# Create your views here.
def price(request):
    commodityid = request.GET.get('commodity',None)
    stateid = request.GET.get('state',None)
    marketid = request.GET.get('market',None)
    state= None
    market = None
    commodityData=None
    allData = None
    if commodityid:
        getcommodity = Commodity.objects.get(id = commodityid)
        state = State.objects.filter(commodity = getcommodity)
        allData = AllData.objects.filter(commodity = getcommodity)
        
    if stateid:
           getcommodity = Commodity.objects.get(id=commodityid)
           getstate = State.objects.get(Q(id=stateid) & Q(commodity=getcommodity))
           market = Market.objects.filter(state=getstate)
        
    if marketid:
            getmarket = Market.objects.filter(Q(id=marketid) & Q(state__commodity__id=commodityid)).first()
        
            commodityData = CommodityData.objects.filter(market=getmarket)
            
    
    
        
    commodity = Commodity.objects.all()
    return render (request,'mandi.html',{'commodity':commodity,'state':state,'market':market,'commodityData':commodityData,'allData':allData})

