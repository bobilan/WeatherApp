from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .api_utils import call_weather_api, get_clothing_recommendation


@csrf_exempt
def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_call = call_weather_api(city)
        if api_call:
            clothing_data = get_clothing_recommendation(api_call)
            weather_data = api_call

            # Store the weather_data dictionary in the session
            request.session['weather_data'] = weather_data
            request.session['clothing_data'] = clothing_data

            return redirect('second_view')

        else:
            # Finish with the logic
            print("Failed to fetch data.")

    return render(request, 'weather/index.html')


@csrf_exempt
def second_view(request):
    # Retrieve the weather_data dictionary from the session
    weather_data = request.session.get('weather_data', {})
    clothing_data = request.session.get('clothing_data', "")

    if not weather_data:
        # Handle the case where weather_data is not found in the session
        messages.error(request, 'Weather data not found in session.')
        return redirect('weather/index.html')  # Redirect to another view or page

    return render(request, 'weather/second.html', {'weather_data': weather_data, "clothing_data": clothing_data})



# @csrf_exempt
# def weather_view(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         weather_data = {
#             'city_name': 'Kyiv',
#             'weather_main': 'Clouds',
#             'temperature': 26,
#             'humidity': 59,
#             'wind_speed': 0.5,
#             'weather_icon': '04d'}
#
#         return redirect('second_view')
#     return render(request, 'weather/index.html')  # returns the index.html template
#
#
# def second_view(request):
#     return render(request, 'weather/second.html')
