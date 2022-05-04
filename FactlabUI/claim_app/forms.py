from django.forms import ModelForm

from .models import claim

class ClaimForm(ModelForm):
    class Meta:
        model = claim
        fields = '__all__'
    

