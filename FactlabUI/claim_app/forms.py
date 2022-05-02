from attr import field
from django.forms import ModelForm
from .models import claim

class claimForm(ModelForm):
    class Meta:
        model = claim
        fields = '__all__'