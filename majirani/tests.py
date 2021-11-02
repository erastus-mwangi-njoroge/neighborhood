from django.test import TestCase
from .models import neighbourhood,healthservices
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Umoja = neighbourhood(neighbourhood='Umoja')

    def test_instance(self):
        self.assertTrue(isinstance(self.Umoja,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Umoja.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Umoja.delete_neighbourhood('Umoja')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.Nursing = healthservices(healthservices='Nursing')

    def test_instance(self):
        self.assertTrue(isinstance(self.Nursing,healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.Nursing.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Nursing.delete_healthservices('Nursing')
        health = healthservices.objects.all()
        self.assertTrue(len(health)==0)