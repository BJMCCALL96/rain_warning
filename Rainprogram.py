import requests
from twilio.rest import Client

OWM_end="https://api.openweathermap.org/data/2.5/onecall"
# Weather API KEy
api_key=""

# TWILIO API KEY AND TOKEN
account_sid = ''
auth_token = ''



#https://api.openweathermap.org/data/2.5/weather?lat=37.6922361&lon=-97.3375448&appid=5d902227bbb3723953ebd6140c482511


def text():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='        ',                  # TWILIO KEY
        body='It is going to rain today, bring an umbrella  ☂',
        #Enter your phone number below
        to='+1-111-1111'
    )

param={
    #Enter your latitude and longitude 
    "lat": 137.6922361,
    "lon": -97.3375448,
    "appid": api_key,
    "units": "imperial",
    "exclude":"current,minutely,daily,alerts"

}

rain=False

response=requests.get(url=(OWM_end), params=param)
print(response.json()["hourly"][0]["weather"][0]["main"])
while rain is False:
    for x in range(0,12):
        main=(response.json()["hourly"][x]["weather"][0]["main"])
        if main == "Rain":
            rain = True
            text()
            break
