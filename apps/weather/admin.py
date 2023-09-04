from django.contrib import admin
from apps.weather.models import WeatherData, ClothingRecommendations


class CustomWeatherData(admin.ModelAdmin):
    list_display = (
        'city_name',
        'weather_main',
        'weather_description',
        'temperature',
        'humidity',
        'wind_speed',
        'weather_icon',
        'formatted_created_at',  # Custom column
    )
    list_filter = ('city_name', 'created_at')
    search_fields = ('city_name', 'weather_main')

    @admin.display(description="Created At")
    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")


class ClothingRecommendationsAdmin(admin.ModelAdmin):
    list_display = (
        'weather_data_city_name',
        'weather_data_created_at',
        'display_recommendations',
    )

    def weather_data_city_name(self, obj):
        return obj.weather_data.city_name
    weather_data_city_name.short_description = 'City Name'

    def weather_data_created_at(self, obj):
        return obj.weather_data.created_at
    weather_data_created_at.short_description = 'Created At'

    @admin.display(description="Recommendations")
    def display_recommendations(self, obj):
        recommendations = obj.description
        return ', '.join(recommendations)


admin.site.register(WeatherData, CustomWeatherData)
admin.site.register(ClothingRecommendations, ClothingRecommendationsAdmin)
