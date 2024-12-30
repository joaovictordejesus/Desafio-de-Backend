# app/urls.py
from django.urls import path
from .views import PartnerCreateView, PartnerDetailView, PartnerNearestView

urlpatterns = [
    path('partners', PartnerCreateView.as_view(), name='partner-create'),
    path('partners/<str:id>', PartnerDetailView.as_view(), name='partner-detail'),
    path('partners/nearest', PartnerNearestView.as_view(), name='partner-nearest'),
]
