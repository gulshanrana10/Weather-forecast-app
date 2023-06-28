# This file will be the entry point for your application.
# It will contain the main code logic for your Python weather app.

# Parse weather data from OpenWeatherMap API
# Display weather data in a readable format to the user
# Allow the user to search for a location by city name

# Import modules
import requests
import json
import os
from datetime import datetime
import secrets
import sys
from prettytable.colortable import ColorTable, Themes
# define three_hour_step_weather_forecast function on the basis of below definitions
def three_hour_step_weather_forecast(sel,choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    city=choice
    len=os.get_terminal_size ().columns
    # Get API key from secrets.py
    API_KEY = secrets.api_key
        
    # Make API call
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)

    # handle url exceptions
    if response.status_code != 200:
        print(f"Sorry, {city} is not a valid city name.")
        print("Something went wrong...")
        exit()

    # Parse JSON data
    try:
        data= json.loads(response.text)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response.")


    # Get current date and time
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    # prepare pretty table

    t = ColorTable(['Date and Time', 'Temperature °C', 'Feels like', 'Min Temperature', 'Max Temperature', 'Humidity', 'Wind Speed', 'Desciption'],theme=Themes.OCEAN)
    t.align["Description"] = "c"  # Left align city names
    # Print weather data
    print("=" *len)
    print("\033[95mWelcome to city Weather Forecast\033[00m".center(len))
    print("=" * len)
    print("")
    # for loop to print weather data for every 3 hours for today
    print("-" * len)
    
    for i in range(0, 8):
        # Print weather data
        
        t.add_row([data['list'][i]['dt_txt'], data['list'][i]['main']['temp'],data['list'][i]['main']['feels_like'], data['list'][i]['main']['temp_min'], data['list'][i]['main']['temp_max'], data['list'][i]['main']['humidity'], data['list'][i]['wind']['speed'], data['list'][i]['weather'][0]['description']])
    print("-" * len)
    print(t)
    #give menu options
    print("")
    print("=" * len)
    print("\033[93m 1. Type 1 to search with another city name\033[00m".ljust(len))
    print("\033[93m 2. Type 2 to go back to main menu\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("=" * len)
    print("")
    choice = input("YOUR SELECTION: >> ")
    choice = choice.strip()
    if choice == '0':
        sys.exit()
    elif choice == '1':
        sub_menu1(sel=False)
        sys.exit()
    elif choice == '2':
        main_menu(sel=False)
        sys.exit()
    return choice



# define current_weather_forecast function on the basis of below definitions
def current_weather_forecast(sel,choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    city=choice
    
    # Get API key from secrets.py
    API_KEY = secrets.api_key
    
    # Make API call
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)

    # handle url exceptions
    if response.status_code != 200:
        print(f"Sorry, {city} is not a valid city name.")
        print("Something went wrong...")
        exit()

    # Parse JSON data
    try:
        data= json.loads(response.text)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response.")

    len=os.get_terminal_size ().columns

    # Get current date and time
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")
    # prepare pretty table
    t = ColorTable(['Date and Time', 'Temperature °C', 'Feels like', 'Min Temperature', 'Max Temperature', 'Humidity', 'Wind Speed', 'Desciption'],theme=Themes.OCEAN)
    t.align["Description"] = "c"  # Left align city names
    t.add_row([now, data['main']['temp'],data['main']['feels_like'], data['main']['temp_min'], data['main']['temp_max'], data['main']['humidity'], data['wind']['speed'], data['weather'][0]['description']])
    
    # Print weather data
    print("=" * len)
    print("\033[95mWelcome to city Weather Forecast\033[00m".center(130))
    print("=" * len)
    print("")
    print("-" * len)
    print("\033[95m{}\033[00m".format(t))
    print("-" * len)
    print("")
    print("=" * len)
    print("\033[93m 1. Type 1 to search with another city name\033[00m".ljust(len))
    print("\033[93m 2. Type 2 to go back to main menu\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("=" * len)
    print("")
    choice = input("YOUR SELECTION: >> ")
    choice = choice.strip()
    if choice == '0':
        sys.exit()
    elif choice == '1':
        sub_menu1(sel=False)
        sys.exit()
    elif choice == '2':
        main_menu(sel=False)
        sys.exit()
    return choice

# define sub_menu2 function on the basis of below definitions
def sub_menu2(sel,choice):
    city=choice
    len=os.get_terminal_size ().columns

    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    print("="*len)
    print("\033[95m Welcome to city Weather Forecast\033[00m".center(len))
    print("="*len)
    print("")
    print("-" * len)
    print("\033[93m 1. Type 1 for current weather forecasts\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 2. Type 2 for 3-hour step weather forecasts\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 9. Type 9 to return to Main Menu\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("-" * len)
    print("")
    #prepare sub_menu2 choices
    choice = input("YOUR SELECTION: >> ")
    choice = choice.strip()
    if choice == '0':
        sys.exit()
    elif choice == '9':
        main_menu(sel=False)
        sys.exit()
    elif choice not in ['1', '2', '9']:
        choice = sub_menu2(sel=True)
    else:
        if choice == '1':
            current_weather_forecast(sel=False,choice=city)
        elif choice == '2':
            three_hour_step_weather_forecast(sel=False,choice=city)
        else:
            choice = sub_menu2(sel=True)
    return choice

# define sub_menu1 function on the basis of below definitions
def sub_menu1(sel):
    os.system('cls' if os.name == 'nt' else 'clear')
    len=os.get_terminal_size ().columns
    if sel:
        print("\033[91m Weather Forecast \033[00m")
    print("=" * len)
    print("\033[95m Welcome to city Weather Forecast\033[00m".center(len))
    print("=" * len)
    print("")
    print("-" * len)
    print("\033[93m Please enter the city name:\033[00m".ljust(len))
    print("-" * len)
    print("")
    #prepare sub_menu1 choices
    choice = input("YOUR SELECTION: >> ")
    choice = choice.strip()
    sub_menu2(sel=False,choice=choice)     
    return choice

# define main_menu function for weather forecast app
def main_menu(sel):
    os.system('cls' if os.name == 'nt' else 'clear')
    len=os.get_terminal_size ().columns
    #base condition
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    print("="*len)
    print("\033[95mWelcome to Weather forecasting using Github Co-pilot\033[00m".center(len))
    print("="*len)
    print("")
    print("-" * len)
    print("\033[93m 1. Type 1 to search with city name\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("-" * len)

    print("")
    choice = input("YOUR SELECTION: >> ")
    choice = choice.strip()
    #prepare main_menu choices
    if choice == '0':
        sys.exit()
    elif choice == '1':
        sub_menu1(sel=False)
    else:
        main_menu(sel=True)
    
    return choice

# define main function for weather forecast app
if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("\033[91mInvalid Usage\033[00m")
        print("\033[93mUsage        : ./{0} or python {0}".format(sys.argv[0]))
        print("")
        sys.exit(1)
    
    while True:
        main_menu(sel=False)
        input("Press Enter to continue...")

'''
# Save weather data to a text file
with open("weather.txt", "w") as f:
    f.write(f"\n{dt_string}\n")
    f.write(f"Current weather in {city}:\n")
    f.write(f"Temperature: {data['main']['temp']}°F\n")
    f.write(f"Weather: {data['weather'][0]['description']}\n")
    f.write(f"Humidity: {data['main']['humidity']}%\n")
    f.write(f"Wind: {data['wind']['speed']} mph\n")

# Print success message
print("\nWeather data saved to weather.txt")

# End of program
'''

