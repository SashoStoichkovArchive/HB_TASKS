from django.test import TestCase
from django.test.client import Client

from Planes.models import Plane, User
from Planes.forms import FlightForm

# Create your tests here.
class ViewsResponseTests(TestCase):
    
    def test_create_view_response(self):
        c = Client()
        res = c.get("/planes/flights/create/")

        self.assertEquals(res.status_code, 200)

    def test_list_view_response(self):
        c = Client()
        res = c.get("/planes/flights/list/")

        self.assertEquals(res.status_code, 200)

    def test_login_view_response(self):
        c = Client()
        res = c.get("/planes/login/")

        self.assertEquals(res.status_code, 200)

class ViewsTemplateTests(TestCase):

    def test_create_view_response(self):
        c = Client()
        res = c.get("/planes/flights/create/")

        self.assertTemplateUsed(res, 'planes/create.html')

    def test_list_view_response(self):
        c = Client()
        res = c.get("/planes/flights/list/")

        self.assertTemplateUsed(res, 'planes/list.html')

    def test_login_view_response(self):
        c = Client()
        res = c.get("/planes/login/")

        self.assertTemplateUsed(res, 'planes/user_login.html')

class FlightFormTest(TestCase):

    def test_flight_form(self):
        plane = Plane.objects.create(name="Hack Plane 101", capacity=100, crew=10)
        user = User.objects.create_user(username="Pesho", password="1234567")

        form_data = {'start_time': '2019-08-11 12:30',
                     'end_time': '2019-08-11 14:30',
                     'passengers': 50,
                     'max_passengers': 100,
                     'from_dest': 'Sofia',
                     'to_dest': 'London',
                     'plane': plane,
                     'user': user}

        form = FlightForm(data=form_data)

        self.assertTrue(form.is_bound)