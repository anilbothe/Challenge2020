from django.test import TestCase
from app.models import WeatherAudit


# Testing Model
class TestModels(TestCase):
    def setUp(self):
        self.obj1 = WeatherAudit.objects.create(city='Pune', temperature='20F', description="clear sky", icon="10n")
        self.obj2 = WeatherAudit.objects.create(city='Mumbai', temperature='40F', description="fog sky", icon="12n")
        self.obj3 = WeatherAudit.objects.create(city='Aurangabad', temperature='80F', description="cloudy sky", icon="13n")

    def test_weatheraudit_is_assigned_city_on_creation(self):
        self.assertEqual(self.obj1.city, 'Pune')
        self.assertEqual(self.obj2.city, 'Mumbai')
        self.assertEqual(self.obj3.city, 'Aurangabad')

# Testing Url
class TestUrls(TestCase):
    pass