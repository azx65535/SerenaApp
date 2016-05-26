from django.http import HttpResponse
import requests
import re
import random

def method_emergencycompliment():
    #http://emergencycompliment.com/
    data = requests.get('https://spreadsheets.google.com/feeds/list/1eEa2ra2yHBXVZ_ctH4J15tFSGEu-VTSunsrvaCAV598/od6/public/values?alt=json').json()["feed"]["entry"]
    data = data[random.randint(0, len(data)-1)]["gsx$compliments"]["$t"]
    return data.rstrip()

def method_toykeeper():
    #http://toykeeper.net/programs/mad/compliments
    data = requests.get('http://toykeeper.net/programs/mad/compliments')
    data = re.search('<h3 class="blurb_title_1">(.*)</h3>', data.text, re.DOTALL)
    return data.group(1).rstrip()

def method_peoplearenice():
    #http://peoplearenice.blogspot.com/p/compliment-list.html
    data = requests.get('http://peoplearenice.blogspot.com/p/compliment-list.html')
    data = re.findall('<span style="font-family: Georgia, \'Times New Roman\', serif;">[0-9]{1,3}\. (.*?)</span>', data.text, re.DOTALL)
    return data[random.randint(0, len(data)-1)].rstrip()

def compliment_me(method=-1):
    switcher = {
        0: method_emergencycompliment,
        1: method_toykeeper,
        2: method_peoplearenice,
    }
    if method==-1: method=random.randint(0,len(switcher)-1)
    switcher = switcher.get(method, lambda: "Invalid Method")
    return switcher()

def index(request):
    resp = HttpResponse()
    resp.write(compliment_me())
    return resp


