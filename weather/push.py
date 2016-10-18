from firebase import firebase
from datetime import datetime
import random
db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/',None)

def calculate(n,p,k,w):
	s1 = n/9;
	s2 = p/9
	s3 = 2*k/9
	s4 = 8*w/3
	return (s1+s2+s3+s4)/4



def pushdata(data):
	for s in data:
		n = random.uniform(14,22)
		p = random.uniform(18,27)
		k = random.uniform(12,20)
		w = random.uniform(8,25)
		score = calculate(n,p,k,w)
		time = datetime.now()
		data = {"N":n,"P":p,"K":k,"water":w,"time":time,"score":score}
		imageurl = s["body"]
		humidity = s["desc"]["humidity"]
		humidity = humidity[10:]
		overview = s["desc"]["overview"]
		pressure = s["desc"]["pressure"]
		pressure = pressure[10:]
		wind = s["desc"]["wind"]
		foot = s["foot"]
		head = s["head"]
		weatherstore = {"time":time,"foot": foot, "head": head, "humidity": humidity, "image_url": imageurl, "overview": overview, "pressure": pressure, "wind": wind}
		result = db.post('/weather_data', weatherstore)
		result2 = db.post('/soil_data',data)
	







