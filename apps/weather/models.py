from django.db import models
from apps.core.models import CreatedModifiedAtDateTimeBase


class WeatherData(CreatedModifiedAtDateTimeBase):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    weather_main = models.CharField(max_length=50)
    weather_description = models.CharField(max_length=200)
    lon = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    weather_icon = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Weather Data"

    def formatted_city_name(self):
        return f"Weather in {self.city_name}"

    def __str__(self):
        return self.formatted_city_name()


class WeatherDescription(models.Model):
    weather_data = models.ForeignKey('WeatherData', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Description for {self.weather_data.city_name} - {self.description}"


class ClothingRecommendations(models.Model):
    weather_data = models.ForeignKey('WeatherData', on_delete=models.CASCADE)
    description = models.JSONField()

    class Meta:
        verbose_name_plural = "Clothing recommendations"

    def __str__(self):
        return f"Recommendations for {self.weather_data.city_name} - {self.description}"

