from django.http import HttpResponse
import requests

def index(request):
    resp = HttpResponse()
    resp.write("Hello World!<br>")

    data = requests.get('http://api.wunderground.com/api/fb5ae3d2bef1572c/hourly/q/10003.json')
    data = data.json()

    for hour in data["hourly_forecast"]:
        resp.write(hour["FCTTIME"]["pretty"]+hour["temp"]["metric"]+"<br>")

    return resp
