from firebase import firebase

def login(username, password):

    print username
    print password
    print "----------------------------------------------"
    db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/ ', None)
    result = db.get('/Users', None)
    dict = {}
    for key, value in result.iteritems():
    	dict[result[key]['username'][0:]] = result[key]['password'][0:]
    print dict
    for key, value in dict.iteritems():
    	print key
    	print value
    	if username == key and password == value:
    		return 1
    return 0

