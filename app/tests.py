# app/tests.py
from django.test import TestCase
from django.contrib.gis.geos import Point, MultiPolygon, Polygon
from .models import Partner

class PartnerTests(TestCase):

    def setUp(self):
        coverage_area = MultiPolygon(Polygon(((30, 20), (45, 40), (10, 40), (30, 20))))
        address = Point(-46.57421, -21.785741)

        Partner.objects.create(
            id="1",
            trading_name="Adega da Cerveja - Pinheiros",
            owner_name="Zé da Silva",
            document="1432132123891/0001",
            coverage_area=coverage_area,
            address=address
        )

    def test_create_partner(self):
        partner = Partner.objects.get(id="1")
        self.assertEqual(partner.trading_name, "Adega da Cerveja - Pinheiros")

    def test_partner_in_coverage_area(self):
        partner = Partner.objects.get(id="1")
        point_inside = Point(30, 30)
        self.assertTrue(partner.coverage_area.contains(point_inside))

    def test_partner_outside_coverage_area(self):
        partner = Partner.objects.get(id="1")
        point_outside = Point(0, 0)
        self.assertFalse(partner.coverage_area.contains(point_outside))
