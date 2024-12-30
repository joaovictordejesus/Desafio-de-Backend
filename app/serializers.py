from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Partner

class PartnerSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Partner
        geo_field = 'coverage_area'
        fields = ('id', 'trading_name', 'owner_name', 'document', 'coverage_area', 'address')
