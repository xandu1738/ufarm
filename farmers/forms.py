from django import forms
from .models import FarmerOne, UrbanFarmer, Activity

class FarmerOneForm(forms.ModelForm):
    class Meta:
        model = FarmerOne
        fields = "__all__"
        
class UrbanFarmerForm(forms.ModelForm):
    class Meta:
        model = UrbanFarmer
        fields = "__all__"
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"    