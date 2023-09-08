from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .api_utils import \
    call_weather_api, \
    get_clothing_recommendation, \
    save_weather_data, \
    save_clothing_recommendations
from .form import SearchForm


# @csrf_exempt
def weather_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)  # Bind form data to the SearchForm
        if form.is_valid():
            city = form.cleaned_data['search_bar']
            api_call = call_weather_api(city)
            if api_call:
                clothing_data = get_clothing_recommendation(api_call)
                weather_data = api_call

                new_weather_instance = save_weather_data(api_call)

                save_clothing_recommendations(new_weather_instance, clothing_data)

                # Store the weather_data dictionary in the session
                request.session['weather_data'] = weather_data
                request.session['clothing_data'] = clothing_data

                return redirect('second_view')
            else:
                # Handle the case when the API call fails
                print("Failed to fetch data.")
    else:
        form = SearchForm()  # Create an empty form for GET requests

    return render(request, 'weather/index.html', {'form': form})


# @csrf_exempt
# def weather_view(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         api_call = call_weather_api(city)
#         if api_call:
#             clothing_data = get_clothing_recommendation(api_call)
#             weather_data = api_call
#
#             new_weather_instance = save_weather_data(api_call)
#
#             save_clothing_recommendations(new_weather_instance, clothing_data)
#
#             # Store the weather_data dictionary in the session
#             request.session['weather_data'] = weather_data
#             request.session['clothing_data'] = clothing_data
#
#             return redirect('second_view')
#
#         else:
#             # Complete the logic
#             print("Failed to fetch data.")
#
#     return render(request, 'weather/index.html')


@csrf_exempt
def second_view(request):
    # Retrieve the weather_data dictionary from the session
    weather_data = request.session.get('weather_data', {})
    clothing_data = request.session.get('clothing_data', "")

    if not weather_data:
        # If data not found
        messages.error(request, 'Weather data not found in session.')
        return redirect('weather/index.html')  # Redirect to index

    return render(request, 'weather/second.html', {'weather_data': weather_data, "clothing_data": clothing_data})
