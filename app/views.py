# app/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Partner
from .serializers import PartnerSerializer

class PartnerCreateView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnerDetailView(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_field = 'id'

class PartnerNearestView(generics.GenericAPIView):
    serializer_class = PartnerSerializer

    def get(self, request, *args, **kwargs):
        longitude = float(request.query_params.get('long'))
        latitude = float(request.query_params.get('lat'))
        user_location = Point(longitude, latitude, srid=4326)

        nearest_partner = Partner.objects.annotate(distance=Distance('address', user_location))
        nearest_partner = nearest_partner.filter(coverage_area__contains=user_location).order_by('distance').first()

        if not nearest_partner:
            return Response({"detail": "No partner found covering this location."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(nearest_partner)
        return Response(serializer.data)
