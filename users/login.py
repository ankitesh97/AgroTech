from firebase import firebase


db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/ ', None)

result = db.get('/Users', None)

dict = {}

for key, value in result.iteritems():
    dict[result[key]['username'][0:]] = result[key]['password'][0:]

username = 'ankitesh'
password = 'ankites'


def login(username, password):
    for key, value in dict.iteritems():
        if username == key and password == value:
            return 1
    return 0

print login(username, password)
