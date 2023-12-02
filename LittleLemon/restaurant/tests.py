from django.test import TestCase

# Create your tests here.
from django.urls import reverse 
from .forms import BookingForm  
from datetime import datetime 

class ViewTestCase(TestCase):

    def test_my_view(self):  
        response = self.client.get(reverse('menu'))  
        self.assertEqual(response.status_code, 200)  


class FormTestCase(TestCase):  
    
    def test_valid_form(self):  
        form_data = {'first_name': 'Test', 'reservation_date': datetime.now(), 'reservation_slot': 1}  
        form = BookingForm(data=form_data)  
        self.assertTrue(form.is_valid())  