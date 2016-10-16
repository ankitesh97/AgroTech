
from firebase import firebase
import numpy as np

db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/',None)
result = db.get('/dataset',None)
result = result.values()
temp = [result[0]['N'],result[0]['P'],result[0]['K'],result[0]['water']]
X = np.matrix(temp)
y = np.matrix(result[0]['crop_class'])

for i in range(1,len(result)):
	temp = [result[i]['N'],result[i]['P'],result[i]['K'],result[i]['water']]
	X = np.vstack((X,temp))
	temp = result[i]['crop_class']
	y = np.vstack((y,temp))

print(X)
print(y)
