import requests
import sys
from PyQt4 import QtGui, QtCore
import analyze

maps = {"Mumbai":"1275339", "Thane":"5557906", "Pune":"1259229", "Delhi":"1273294"}
class MyApp():
    _hand = []
    def get_curr_city_data(self):
        import weathergui2
        curr_city = str(self.comboBox.currentText())
        if(curr_city!=""):
            api_call = 'http://api.openweathermap.org/data/2.5/forecast/city?id='+maps[curr_city]+'&APPID=7c04a3b79de8d85866aaa33ff5b98033'
            response = requests.get(api_call)
            file_n = curr_city+".txt"
            write_file = open(file_n,"w")
            data = response.text
            write_file.write(data)
            write_file.close()
            print "success in writing data"
            self.hand = analyze.analyze_data(file_n)
            self.display()

    def display(self):
        tmp = self.hand[0]
        self.headc.setText(tmp["head"])
        self.bodyc.setPixmap(QtGui.QPixmap(tmp["body"]))
        self.bodyc.setAlignment(QtCore.Qt.AlignCenter)
        self.footc.setText(tmp["foot"])
        self.overviewde.setText(tmp["desc"]["overview"])
        self.pressurede.setText(tmp["desc"]["pressure"])
        self.Windde.setText(tmp["desc"]["wind"])
        self.humidde.setText(tmp["desc"]["humidity"])
        tmp = self.hand[1]
        self.headn.setText(tmp["head"])
        self.bodyn.setPixmap(QtGui.QPixmap(tmp["body"]))
        self.bodyn.setAlignment(QtCore.Qt.AlignCenter)
        self.footn.setText(tmp["foot"])
        tmp = self.hand[2]
        self.headnn.setText(tmp["head"])
        self.bodynn.setPixmap(QtGui.QPixmap(tmp["body"]))
        self.bodynn.setAlignment(QtCore.Qt.AlignCenter)
        self.footnn.setText(tmp["foot"])

    def fir(self):
        tmp = self.hand[0]
        self.overviewde.setText(tmp["desc"]["overview"])
        self.pressurede.setText(tmp["desc"]["pressure"])
        self.Windde.setText(tmp["desc"]["wind"])
        self.humidde.setText(tmp["desc"]["humidity"])

    def seco(self):
        tmp = self.hand[1]
        self.overviewde.setText(tmp["desc"]["overview"])
        self.pressurede.setText(tmp["desc"]["pressure"])
        self.Windde.setText(tmp["desc"]["wind"])
        self.humidde.setText(tmp["desc"]["humidity"])

    def thir(self):
        tmp = self.hand[2]
        self.overviewde.setText(tmp["desc"]["overview"])
        self.pressurede.setText(tmp["desc"]["pressure"])
        self.Windde.setText(tmp["desc"]["wind"])
        self.humidde.setText(tmp["desc"]["humidity"])






