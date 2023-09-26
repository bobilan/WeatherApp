from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from apps.weather.views import weather_view


class WeatherViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_weather_view_GET(self):
        response = self.client.get(
            reverse('weather_view'),
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weather/index.html')
    #
    def test_weather_view_POST(self):
        form_data = {'search_bar': 'New York'}
        response = self.client.post(
            reverse('weather_view'),
            data=form_data,
            HTTP_USER_AGENT="Mozilla/5.0 (Macintosh; Intel Mac OS X 10)",
            HTTP_CONTENT_TYPE="",
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('second_view'))


