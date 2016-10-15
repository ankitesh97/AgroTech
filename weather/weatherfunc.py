import requests
import sys
from PyQt4 import QtGui, QtCore
import analyze,random
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import pyqtgraph as pg
#1263967
maps = {"Mumbai":"1275339", "Thane":"5557906", "Pune":"1259229", "Delhi":"1273294","Boulder":"5819347"}
class MyApp():
    _hand = []
    _plots = []
    def get_curr_city_data(self):
        import weathergui2
        curr_city = str(self.comboBox.currentText())
        print self.comboBox.currentIndex()
        print curr_city
        if(curr_city==""):
            curr_city = "Mumbai"
        if(curr_city!=""):
            api_call = 'http://api.openweathermap.org/data/2.5/forecast/city?id='+maps[curr_city]+'&APPID=7c04a3b79de8d85866aaa33ff5b98033'
            response = requests.get(api_call)
            file_n = "cities/"+curr_city+".txt"
            write_file = open(file_n,"w")
            data = response.text
            write_file.write(data)
            write_file.close()
            print "success in writing data"
            self.hand = analyze.analyze_data(file_n)
            self.display()
            self.plots = analyze.all_plots(file_n)
            self.plot_t(self.plots[0])
            self.plot_w(self.plots[1])
            self.plot_h(self.plots[2])

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

    def plot_t(self,coor):
        self.win_t.removeItem(self.plot1)
        self.x = [coor["xco"][i] for i in range(5)]
        self.y = [int(coor["yco"][i][0]+coor["yco"][i][1]) for i in range(5)]
        self.z = [coor["yco"][i] for i in range(5)]
        self.zdict = dict(enumerate(self.z))
        self.stringaxis = pg.AxisItem(orientation='bottom')
        self.stringaxis.setTicks([self.zdict.items()])
        self.plot1 = self.win_t.addPlot(axisItems={'bottom': self.stringaxis})
        self.plot1.setLabel('bottom','Time')
        self.plot1.setLabel('left',coor["x"])
        self.curve = self.plot1.plot(self.zdict.keys(), self.x)

    def plot_w(self,coor):

        self.win_w.removeItem(self.plot2)
        self.x = [coor["xco"][i] for i in range(5)]
        self.y = [int(coor["yco"][i][0]+coor["yco"][i][1]) for i in range(5)]
        self.z = [coor["yco"][i] for i in range(5)]
        self.zdict = dict(enumerate(self.z))
        self.stringaxis = pg.AxisItem(orientation='bottom')
        self.stringaxis.setTicks([self.zdict.items()])
        self.plot2 = self.win_w.addPlot(axisItems={'bottom': self.stringaxis})
        self.plot2.setLabel('bottom','Time')
        self.plot2.setLabel('left',coor["x"])
        self.curve = self.plot2.plot(self.zdict.keys(), self.x,pen=None,symbol='o')

    def plot_h(self,coor):
        self.win_h.removeItem(self.plot3)
        self.x = [coor["xco"][i] for i in range(5)]
        self.y = [int(coor["yco"][i][0]+coor["yco"][i][1]) for i in range(5)]
        self.z = [coor["yco"][i] for i in range(5)]
        self.zdict = dict(enumerate(self.z))
        self.stringaxis = pg.AxisItem(orientation='bottom')
        self.stringaxis.setTicks([self.zdict.items()])
        self.plot3 = self.win_h.addPlot(axisItems={'bottom': self.stringaxis})
        self.plot3.setLabel('bottom','Time')
        self.plot3.setLabel('left',coor["x"])
        self.curve = self.plot3.plot(self.zdict.keys(), self.x)



