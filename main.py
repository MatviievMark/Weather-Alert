import requests as requests
from sendEmail import sendEmail
import os

#api key will not work unless you use your own key 
#you can get it over here --> openweathermap.org
api_key = 'YOUR KEY'


# Jackson Mississippi
lat = 32.29876
lon = -90.18481

# test somewhere when it was raining
# lat = 4.091354
# lon = -72.955918
units = "metric"
exclude = "current,minutely,daily"
api_url =\
    f'https://api.openweathermap.org/data/2.5/onecall?lat=' \
    f'{lat}&lon={lon}&units={units}&exclude={exclude}&appid={api_key}'

response = requests.post(url = api_url)
response.raise_for_status()
data = response.json()


weather_slice = data["hourly"][:12]

will_rain = False

for hours in weather_slice:
    weather_data = hours["weather"][0]["id"]
    if int(weather_data) < 700:
        will_rain = True

myEmail = "mark.mason2025@gmail.com"
toEmail = "mark23902390@gmail.com"

myPassword = "Zer0.Chance"

email_subject = "Weather alert"
email_message = "It will rain!!!"

if will_rain:
    sendEmail(myEmail, toEmail, myPassword, email_subject, email_message)

