from django import forms
from .models import Commodity,Market,State

# class CommudityForm(forms.ModelForm):
#     class Meta:
#         model = Commodity
#         fields ='__all__'
        
# class StateForm(forms.ModelForm):
#     class Meta:
#         model = State
#         fields ='__all__'
        
class MarketForm(forms.Form):
    commodity = forms.ModelChoiceField(queryset = Commodity.objects.all(),
    widget = forms.Select(attrs = {"hx-get":"load_state/","hx-target":"#id_state"})) 
    state = forms.ModelChoiceField(queryset=State.objects.none()),
    market = forms.ModelChoiceField(queryset=Market.objects.none()),
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['state'].queryset = State.objects.none()
        
        if "commodity" in self.data:
            commodity_id = int(self.data.get("commodity"))
            self.fields["state"].queryset = State.objects.filter(commodity_id = commodity_id)