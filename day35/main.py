import requests
OWN_END_POINT="https://api.openweathermap.org/data/2.5/forecast"
API_KEY="c324c6ff9a6558d1c27eecc676dac8dc"

WEATHER_PARAMS={
    "lat":13.082680,
    "lon":80.270721,
    "appid":API_KEY,
    "cnt":4
}
response=requests.get(OWN_END_POINT,params=WEATHER_PARAMS)
response.raise_for_status()
data=response.json()
for i in range(4):
   if data["list"][i]["weather"][0]["id"]<700:
      print("Bring an umbrella")
      