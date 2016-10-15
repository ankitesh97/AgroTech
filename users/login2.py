from firebase import firebase


db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/ ', None)

result = db.get('/Users', None)

#print result

#import pprint

#pprint.pprint(result)

#for i in range(0, result.length())
#    if()

dict = {}

for key, value in result.iteritems():
    #for i_key, i_value in value:
    #dict[i_key] = i_value
    #for i, j in result[key]:
    #    print i
    dict[result[key]['username'][0:]] = result[key]['password'][0:]
    #print i_value
    #print value
    #    print type(value)

#print "\n"
#print dict

username = 'ankitesh'
password = 'ankites'


def login(username, password):
    for key, value in dict.iteritems():
        if username == key and password == value:
            return 1
    return 0

print login(username, password)
