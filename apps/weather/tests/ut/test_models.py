from django.test import TestCase
from apps.weather.models import WeatherData, ClothingRecommendations


class WeatherDataModelTest(TestCase):
    def setUp(self):
        self.weather_data = WeatherData(
            city_name="New York",
            weather_main="Clear",
            weather_description="Clear sky",
            lon=-74.006,
            lat=40.7128,
            temperature=25.5,
            humidity=60.0,
            wind_speed=5.0,
            weather_icon="01d",
        )
        self.weather_data.save()

    def test_formatted_city_name(self):
        self.assertEqual(self.weather_data.formatted_city_name(), "Weather in New York")

    def test_str_method(self):
        self.assertEqual(str(self.weather_data), "Weather in New York")

    def test_verbose_name_plural(self):
        self.assertEqual(WeatherData._meta.verbose_name_plural, "Weather Data")


class ClothingRecommendationsModelTest(TestCase):
    def setUp(self):
        self.weather_data = WeatherData.objects.create(
            city_name="New York",
            weather_main="Clear",
            weather_description="Clear sky",
            lon=-74.006,
            lat=40.7128,
            temperature=25.5,
            humidity=60.0,
            wind_speed=5.0,
            weather_icon="01d",
        )

        self.clothing_recommendations = ClothingRecommendations.objects.create(
            weather_data=self.weather_data,
            description={
                'top': 'T-shirt',
                'bottom': 'Shorts',
                'footwear': 'Sneakers',
            },
        )

    def test_str_method(self):
        expected_str = f"Recommendations for {self.weather_data.city_name} - {self.clothing_recommendations.description}"
        self.assertEqual(str(self.clothing_recommendations), expected_str)

    def test_verbose_name_plural(self):
        self.assertEqual(ClothingRecommendations._meta.verbose_name_plural, "Clothing recommendations")
