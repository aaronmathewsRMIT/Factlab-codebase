import django_filters
from .models import claim
from django_filters import DateTimeFilter, IsoDateTimeFilter

class claimFilter(django_filters.FilterSet):
    #startdate = DateTimeFilter(field_name='date created',lookup_expr='gte')
    class Meta:
        model = claim
        fields = ['claim_id']
