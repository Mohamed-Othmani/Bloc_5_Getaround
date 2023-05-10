import requests

response = requests.post("https://mohdeploiment098.herokuapp.com/predict/", json={
  "model_key": "Peugeot",
  "mileage":21167,
  "engine_power":135,
  "fuel": "petrol",
  "paint_color": "white",
  "car_type": "onvertible",
  "private_parking_available": False,
  "has_gps": False,
  "has_air_conditioning": True,
  "automatic_car": False,
  "has_getaround_connect": False,
  "has_speed_regulator": False,
  "winter_tires": False
  })
print(response.json())
#Peugeot	21167	135	petrol	white	convertible	False	False	True	False	False	False	False	148