import requests
import sys
from PyQt4 import QtGui, QtCore

maps = {"Mumbai":"1275339", "Thane":"5557906", "Pune":"1259229", "Delhi":"1273294"}
class MyApp():
    def get_curr_city_data(self):
        import weathergui
        curr_city = str(self.comboBox.currentText())
        if(curr_city!=""):
            api_call = 'http://api.openweathermap.org/data/2.5/forecast/city?id='+maps[curr_city]+'&APPID=7c04a3b79de8d85866aaa33ff5b98033'
            response = requests.get(api_call)
            file_n = curr_city+".txt"
            write_file = open(file_n,"w")
            data = response.text
            write_file.write(data)
            print "success in writing data"
