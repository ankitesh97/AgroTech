from firebase import firebase
from __future__ import with_statement
from google.appengine.api import files
import cloudstorage as gcs
import main
import webapp2
from PIL import Image
import base64
import cStringIO
import PIL.Image
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

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
		read_file(imageurl)
		weatherstore = {"foot": foot, "head": head, "humidity": humidity, "image_url": imageurl, "overview": overview, "pressure": pressure, "wind": wind}
		result = db.post('/weather_data', weatherstore)

def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo






