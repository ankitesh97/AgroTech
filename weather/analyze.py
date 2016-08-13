
import json
from datetime import datetime
import pprint
day = {"0":"Monday", "1":"Tuesday","2":"Wednesday","3":"Thursday","4":"Friday","5":"Saturday","6":"Sunday"}
answer = [{'head':"","body":"","foot":"","desc":{"overview":"", "pressure":"", "wind":"", "humidity":""}},
          {'head':"","body":"","foot":"","desc":{"overview":"", "pressure":"", "wind":"", "humidity":""}},
          {'head':"","body":"","foot":"", "desc":{"overview":"", "pressure":"", "wind":"", "humidity":""}}]

def degrees_to_c(d):
    '''
    note: this is highly approximate...
    '''
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = int((d + 11.25)/22.5)
    return dirs[ix % 16]

def analyze_data(city):

    data = open(city,"r")
    data = data.read()
    # pprint.pprint(data)
    # print "____________________________________________"
    data = json.loads(data)
    pat = "%Y-%m-%d %H:%M:%S"
    data = data["list"]
    curr = datetime.now()
    hr = curr.hour
    search_for_hr = int(hr/3)*3
    count = 0
    search_for_day = curr.day
    for x in data:
        hand = datetime.strptime(x['dt_txt'],pat)
        if(hand.day==search_for_day and hand.hour == search_for_hr and count<3):
            found = x
            weekday = day[str(hand.weekday())]
            temp = str(x["main"]["temp"]-273.15)
            answer[count]["head"] = weekday+", "+temp+"C"
            answer[count]["body"] = "images/"+x["weather"][0]["main"]+".png"
            foot = "min="+str(x["main"]["temp_min"]-273.15)+"C"+", max="+str(x["main"]["temp_max"]-273.15)+"C"
            answer[count]["foot"] = foot
            answer[count]["desc"]["pressure"] = "Pressure: "+str(x["main"]["pressure"])+"hPa"
            answer[count]["desc"]["wind"] = "Wind: "+str(x["wind"]["speed"])+"m/s"+", "+ degrees_to_c(x["wind"]["deg"])
            answer[count]["desc"]["humidity"] = "Humidity: "+str(x["main"]["humidity"])+"%"
            time_12 = hand.strftime("%I:%M %p")
            overview = weekday[0]+weekday[1]+weekday[2]+", "+time_12+", "+x["weather"][0]["description"]
            answer[count]["desc"]["overview"] = overview
            count += 1
            search_for_day += 1

    pprint.pprint(answer)
    return answer
