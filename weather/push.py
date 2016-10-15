from firebase import firebase

db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/',None)

def pushdata(data):
	for s in data:
		imageurl = s["body"]
		humidity = s["desc"]["humidity"]
		humidity = humidity[10:]
		overview = s["desc"]["overview"]
		pressure = s["desc"]["pressure"]
		pressure = pressure[10:]
		wind = s["desc"]["wind"]
		foot = s["foot"]
		head = s["head"]
		weatherstore = {"foot": foot, "head": head, "humidity": humidity, "image_url": imageurl, "overview": overview, "pressure": pressure, "wind": wind}
		result = db.post('/weather_data', weatherstore)
	







