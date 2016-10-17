
from firebase import firebase
import random

db = firebase.FirebaseApplication('https://agrilife-7cbc7.firebaseio.com/',None)

def calculate(n,p,k,w):
	s1 = n/9;
	s2 = p/9
	s3 = 2*k/9
	s4 = 8*w/3
	return (s1+s2+s3+s4)/4

result = db.get('/crops',None)
crops_data = result.values()

for i in range(70):
	n = random.uniform(14,22)
	p = random.uniform(18,27)
	k = random.uniform(12,20)
	w = random.uniform(8,25)
	score = calculate(n,p,k,w)
	crop_id = random.randrange(1,len(crops_data))
	crop = filter(lambda item:item['id']==crop_id,crops_data)[0]
	data = {'N':n,'P':p,'K':k,'water':w,'score':score,'crop_class':crop['id'],'crop_name':crop['name']}
	db.post('/dataset',data)

