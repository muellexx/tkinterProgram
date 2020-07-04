from tkinter import *
from PIL import ImageTk, Image
import requests, json, os
from io import BytesIO
from datetime import datetime, timedelta


class weather_app:

    def __init__(self, root):
        self.root = root
        self.add_search_frame()
        self.add_weather_frame()
        
    def add_search_frame(self):
        self.search_frame = LabelFrame(self.root, text="Search")

        search_input_label = Label(self.search_frame, text="City:")
        search_input_label.grid()
        self.search_input = Entry(self.search_frame)
        self.search_input.grid(padx=5, pady=5)
        search_btn = Button(self.search_frame, text="Search", command=self.search_weather)
        search_btn.grid(padx=5, pady=5)
        self.warning_message = Label(self.search_frame, fg="red")
        self.warning_message.grid()

        self.search_frame.grid(row=0, column=0, sticky=N+S+W)

    def add_weather_frame(self):
        bg_color="white"
        self.main_weather_frame = LabelFrame(self.root, text="Current Weather Information", bg=bg_color)
        self.main_weather_frame.grid(row=0, column=1, sticky=N+S+W+E)
        self.weather_frame_pad = Frame(self.main_weather_frame, bg=bg_color)
        self.weather_frame_pad.grid(padx=5, pady=5, sticky=N+S+E+W)
        # self.weather_frame_pad.pack(padx=5, pady=5, fill=BOTH)

        Label(self.weather_frame_pad, bg=bg_color).grid(row=0,column=1, padx=10)

        # City, Country, Coordinates
        self.city_frame = Frame(self.weather_frame_pad, bg=bg_color)
        self.city_frame.grid(row=0, column=0, sticky=N+S+E+W)
        Label(self.city_frame, bg=bg_color).grid(row=0,column=1, padx=10)

        Label(self.city_frame, text="City, Country:", anchor="e", bg=bg_color).grid(row=0, column=0, sticky="ew")
        self.city_country = Label(self.city_frame, anchor="w", bg=bg_color)
        self.city_country.grid(row=0, column=2, sticky="w")
        Label(self.city_frame, text="Coordinates:", anchor="e", bg=bg_color).grid(row=1,column=0, sticky="ew")
        self.coordinates = Label(self.city_frame, anchor="w", bg=bg_color)
        self.coordinates.grid(row=1, column=2, sticky="w")
        Label(self.city_frame, text="Time:", anchor="e", bg=bg_color).grid(row=2,column=0, sticky="ew")
        self.local_time = Label(self.city_frame, anchor="w", bg=bg_color)
        self.local_time.grid(row=2, column=2, sticky="w")
        
        # Weather
        self.weather_frame = LabelFrame(self.weather_frame_pad, text="Weather", bg=bg_color)
        self.weather_frame.grid(row=1, column=0, sticky=N+S+W+E, padx=5, pady=5)
        Label(self.weather_frame, bg=bg_color).grid(row=0,column=1, padx=10)

        Label(self.weather_frame, text="Weather:", anchor="e", bg=bg_color).grid(row=0,column=0, sticky="ew")
        self.weather = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.weather.grid(row=0, column=2, sticky="w")
        self.weather_icon = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.weather_icon.grid(row=0, column=3, rowspan=7, sticky="w")
        Label(self.weather_frame, text="Temperature:", anchor="e", bg=bg_color).grid(row=1,column=0, sticky="ew")
        self.temperature = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.temperature.grid(row=1, column=2, sticky="w")
        Label(self.weather_frame, text="Pressure:", anchor="e", bg=bg_color).grid(row=2,column=0, sticky="ew")
        self.pressure = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.pressure.grid(row=2, column=2, sticky="w")
        Label(self.weather_frame, text="Humidity:", anchor="e", bg=bg_color).grid(row=3,column=0, sticky="ew")
        self.humidity = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.humidity.grid(row=3, column=2, sticky="w")
        Label(self.weather_frame, text="Wind Speed:", anchor="e", bg=bg_color).grid(row=4,column=0, sticky="ew")
        self.wind_speed = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.wind_speed.grid(row=4, column=2, sticky="w")
        Label(self.weather_frame, text="Wind Direction:", anchor="e", bg=bg_color).grid(row=5,column=0, sticky="ew")
        self.wind_direction = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.wind_direction.grid(row=5, column=2, sticky="w")
        Label(self.weather_frame, text="Rain (1h):", anchor="e", bg=bg_color).grid(row=6,column=0, sticky="ew")
        self.rain = Label(self.weather_frame, anchor="w", bg=bg_color)
        self.rain.grid(row=6, column=2, sticky="w")
        


    def search_weather(self):
        self.warning_message['text'] = ''
        with open('/home/alex/workspace/tkinter/tkinterProgram/weather_api.json') as config_file:
            config = json.load(config_file)
        base_url = "http://api.openweathermap.org/data/2.5/weather?q="
        middle_url = "&units=metric&appid="
        api_key = config['weather_api']
        url = base_url + self.search_input.get() + middle_url + api_key
        response = requests.get(url)
        x = response.json()
        # x = {'coord': {'lon': 140.47, 'lat': 37.75}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'base': 'stations', 'main': {'temp': 18.07, 'feels_like': 20.05, 'temp_min': 17.78, 'temp_max': 18.33, 'pressure': 997, 'humidity': 96}, 'wind': {'speed': 0.81, 'deg': 355}, 'rain': {'1h': 0.51}, 'clouds': {'all': 100}, 'dt': 1593874199, 'sys': {'type': 3, 'id': 2002752, 'country': 'JP', 'sunrise': 1593804075, 'sunset': 1593857006}, 'timezone': 32400, 'id': 2112923, 'name': 'Fukushima', 'cod': 200}

        if not x['cod'] == 200:
            self.warning_message['text'] = 'The city was not found'
            return
        # city, country
        self.city_country['text'] = x['name'] + ", " + x['sys']['country']
        self.coordinates['text'] = str(x['coord']['lon']) + ", " + str(x['coord']['lat'])

        curr_time = datetime.utcnow() + timedelta(seconds=x['timezone'])
        self.local_time['text'] = curr_time.strftime("%Y/%m/%d, %H:%M")

        # weather
        self.weather['text'] = get_json_response(x,'weather',0,'description').title()
        try:
            icon = requests.get("http://openweathermap.org/img/wn/" + x['weather'][0]['icon'] + "@2x.png")
            img = Image.open(BytesIO(icon.content))
            self.my_img = ImageTk.PhotoImage(img)
            self.weather_icon['image'] = self.my_img
            self.weather_icon.grid()
        except KeyError:
            self.weather_icon.grid_forget()
        self.temperature['text'] = str(round(get_json_response(x,'main','temp',''),1)) + " °C"
        self.pressure['text'] = str(get_json_response(x,'main','pressure','')) + " hPa"
        self.humidity['text'] = str(get_json_response(x,'main','humidity','')) + " %"
        self.wind_speed['text'] = str(get_json_response(x,'wind','speed','')) + " m/s"
        self.wind_direction['text'] = wind_direction_calc(get_json_response(x,'wind','deg',''))
        self.rain['text'] = str(get_json_response(x,'rain','1h','')) + " mm"
        

def wind_direction_calc(degrees):
    if degrees < 0:
        degrees += 360
    
    if degrees < 23:
        return "North"
    if degrees < 68:
        return "Northeast"
    if degrees < 113:
        return "East"
    if degrees < 158:
        return "Southeast"
    if degrees < 203:
        return "South"
    if degrees < 248:
        return "SouthWest"
    if degrees < 293:
        return "West"
    if degrees < 338:
        return "Northwest"
    else:
        return "North"

def get_json_response(json, a, b, c):
    try:
        if b == '':
            return json[a]
        if c == '':
            return json[a][b]
        else:
            return json[a][b][c]
    except KeyError:
        return "-"
