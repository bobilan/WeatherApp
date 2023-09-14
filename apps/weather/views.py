from typing import Optional
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from .api_utils import \
    call_weather_api, \
    get_clothing_recommendation, \
    save_weather_data, \
    save_clothing_recommendations
from .form import SearchForm


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


def second_view(request):
    # Retrieve the weather_data dictionary from the session
    weather_data = request.session.get('weather_data', {})
    clothing_data = request.session.get('clothing_data', "")

    if not weather_data:
        # If data not found
        messages.error(request, 'Weather data not found in session.')
        return redirect('weather/index.html')  # Redirect to index

    return render(request, 'weather/second.html', {'weather_data': weather_data, "clothing_data": clothing_data})


def user_login_view(request):
    error_message = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            user = authenticate(
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect('user_profile')
            else:
                error_message = 'Sorry, something went wrong!'
    else:
        form = AuthenticationForm()

    context = {'form': form, 'error_message': error_message}
    return render(request, "user/user_login.html", context)


def user_profile(request):
    return render(request, "user/profile.html")
