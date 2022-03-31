from django import forms
from dbupdate.models import individual, claim, factchecker

class claimForm(forms.ModelForm):
    class Meta:
        model = claim
        fields = "__all__"
    
class claimindividual(forms.ModelForm):
    class Meta:
        model = individual
        fields = "__all__"
    
class claimfactchecker(forms.ModelForm):
    class Meta:
        model = factchecker
        fields = "__all__"
    
