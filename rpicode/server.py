from flask import Flask, request,jsonify
import RPi.GPIO as GPIO
 
import json
# import firebase
app = Flask(__name__)
# db = firebase.FirebaseApplication('https://homeautomation-890be.firebaseio.com/',None) 


GPIO.setmode(GPIO.BOARD) 
GPIO.setup(13, GPIO.OUT) 

def ledon():
	GPIO.output(13,True)

def ledoff():
	GPIO.output(13,False)

def firebasepush(data):
	print data
	db.push('/Log',data)


def firebaseget():
	data = db.get('/Log',None)
	data = data.values()
	return data

# @app.route('/ledmanipulate', methods=['POST'])
# def ledmanipulate():
# 	data = request.data
# 	data = json.loads(data)
# 	print data
# 	data = data['payload']

# 	if data['mode'] == 1:
# 		print "led turned on"
# 		ledon()
# 		firebasepush(data)
# 	else:
# 		print "led turned off"
# 		ledoff()
# 		firebasepush(data)
# 	return jsonify({
# 		'message':'success'
# 		})

@app.route('/ledmanipulate', methods=['POST'])
def ledmanipulate():
	data = request.data
	data = json.loads(data)
	print data

	if data['mode'] == 1:
		print "led turned on"
		ledon()
		# firebasepush(data)
	else:
		print "led turned off"
		ledoff()
		# firebasepush(data)
	return jsonify({
		'message':'success'
		})


@app.route('/fetchdata')
def fetchdata():
	data = firebaseget()
	return json.dumps(data)

if(__name__ == '__main__'):
	app.run(host='0.0.0.0')
