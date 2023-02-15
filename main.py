import requests
from twilio.rest import Client
import os
API_KEY=os.environ.get('OWN_API_KEY')
MY_LAT=4.274490
MY_LNG=-54.381340
account_sid=os.environ.get('ACCOUNT_SID')
auth_token=os.environ.get('OWN_AUTH_TOKEN')
parameters={"lat":MY_LAT,"lon":MY_LNG,"appid":API_KEY,"exclude":"current,minutely,daily"}
response=requests.get("https://api.openweathermap.org/data/3.0/onecall",params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        

if will_rain:
    
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19403704292",
        to="+16142560712"
    )
    print(message.status)