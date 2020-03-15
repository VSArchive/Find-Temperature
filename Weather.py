from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import json

class Ui_Weather(object):
    def setupUi(self, Weather):
        Weather.setObjectName("Weather")
        Weather.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(Weather)
        self.centralwidget.setObjectName("centralwidget")

        self.City = QtWidgets.QTextEdit(self.centralwidget)
        self.City.setGeometry(QtCore.QRect(0, 0, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.City.setFont(font)
        self.City.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.City.setObjectName("City")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("btnsearch")

        self.pushButton_location = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_location.setGeometry(QtCore.QRect(250, 50, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_location.setFont(font)
        self.pushButton_location.setObjectName("btnLocationSearch")

        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(0, 100, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.temp.setFont(font)
        self.temp.setText("")
        self.temp.setObjectName("temperature")

        self.pressure = QtWidgets.QLabel(self.centralwidget)
        self.pressure.setGeometry(QtCore.QRect(0, 200, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pressure.setFont(font)
        self.pressure.setText("")
        self.pressure.setObjectName("pressure")

        self.hunidity = QtWidgets.QLabel(self.centralwidget)
        self.hunidity.setGeometry(QtCore.QRect(0, 150, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hunidity.setFont(font)
        self.hunidity.setText("")
        self.hunidity.setObjectName("humidity")

        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(0, 250, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description.setFont(font)
        self.description.setText("")
        self.description.setObjectName("description")

        self.city_status = QtWidgets.QLabel(self.centralwidget)
        self.city_status.setGeometry(QtCore.QRect(0, 300, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.city_status.setFont(font)
        self.city_status.setText("")
        self.city_status.setObjectName("Found")

        Weather.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Weather)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        Weather.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Weather)
        self.statusbar.setObjectName("statusbar")
        Weather.setStatusBar(self.statusbar)
        self.retranslateUi(Weather)
        QtCore.QMetaObject.connectSlotsByName(Weather)

        self.pushButton.clicked.connect(self.W)
        self.pushButton_location.clicked.connect(self.LW)

    def retranslateUi(self, Weather):
        _translate = QtCore.QCoreApplication.translate
        Weather.setWindowTitle(_translate("Weather", "Weather"))
        self.City.setHtml(_translate("Weather",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Weather", "Search"))
        self.pushButton_location.setText(_translate("Weather", "Location Search"))

    def W(self):
        api_key = "62d29c78b5095382788bb55c811e13ac"
        url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = self.City.toPlainText()
        if city_name == "":
            city_name = "kalyani"
        complete_url = url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            temp = int(current_temperature) - 273
            pressure = float (current_pressure/1013.2501)
            self.temp.setText("Temperature : " + str(temp))
            self.hunidity.setText("Humidity : " + str(current_humidity) + " %")
            self.pressure.setText("Pressure : " + str(pressure) + " Atm")
            self.description.setText("Weather Description : " + str(weather_description))
            self.city_status.setText("City Found - " + city_name)

        else:
            self.temp.setText("")
            self.pressure.setText("")
            self.hunidity.setText("")
            self.description.setText("")
            self.city_status.setText(" City Not Found ")

    def LW(self):
        loc_url = "http://api.ipstack.com/check?access_key=532d61f6d5a9750abc91b118d14a4168"
        geo_req = requests.get(loc_url)
        geo_json = json.loads(geo_req.text)
        api_key = "62d29c78b5095382788bb55c811e13ac"
        url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = geo_json['city']
        complete_url = url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            temp = int(current_temperature) - 273
            pressure = int(current_pressure/1013.2501)
            self.temp.setText("Temperature : " + str(temp))
            self.hunidity.setText("Humidity : " + str(current_humidiy) + " %")
            self.pressure.setText("Pressure : " + str(pressure) + " Atm")
            self.description.setText("Weather Description : " + str(weather_description))
            self.city_status.setText("City Found - " + city_name)

        else:
            self.temp.setText("")
            self.pressure.setText("")
            self.hunidity.setText("")
            self.description.setText("")
            self.city_status.setText(" City Not Found ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Weather = QtWidgets.QMainWindow()
    ui = Ui_Weather()
    ui.setupUi(Weather)
    Weather.show()
    sys.exit(app.exec_())