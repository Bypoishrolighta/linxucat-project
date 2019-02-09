import requests
import datetime
import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

url = "http://t.weather.sojson.com/api/weather/city/101300101"#获取url（南宁）
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=20) #设置超时
        # 判断连接状态，为4XX或5XX时抛出异常信息
        r.raise_for_status()   
        # 将返回对象的编码格式设为响应内容编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except: #异常处理
        return "产生异常"

demo = getHTMLText(url) #调用函数


def getList(demo):
    global list_demo
    pattern = re.compile(r'(?<=\{)[^}]*(?=\})')#定义正则（搜索{}中的内容）
    list_demo = pattern.findall(demo) #获取list

getList(demo)

def cutList():
    global list_today,list_tomorrow #定义全局变量
    list_today = list_demo[2] #获取今天天气
    list_tomorrow = list_demo[3] #获取明天天气
cutList()

def getWeather(list_today, list_tomorrow):
    global high_today, low_today, type_today
    global high_tomorrow, low_tomorrow, type_tomorrow
    st = ''
    str_today = str(list_today)
    str_tomorrow = str(list_tomorrow)
    
    match_number = re.compile('/d{1}|[0-9][0-9]')
    match_letter = re.compile('[\u4e00-\u9fa5]')
    
    cut_high_today = str_today[35:50]
    cut_low_today = str_today[55:64]
    cut_type_today = str_today[154:158]
    
    type_today = st.join(match_letter.findall(cut_type_today))
    high_today = str(list(map(int, match_number.findall(cut_high_today)))[0])
    low_today = str(list(map(int, match_number.findall(cut_low_today)))[0])

    cut_high_tomorrow = str_tomorrow[35:50]
    cut_low_tomorrow = str_tomorrow[55:64]
    cut_type_tomorrow = str_tomorrow[154:158]

    type_tomorrow = st.join(match_letter.findall(cut_type_tomorrow))
    high_tomorrow = match_number.findall(cut_high_tomorrow)[0]
    low_tomorrow = match_number.findall(cut_low_tomorrow)[0]    

getWeather(list_today, list_tomorrow)    

def date():
    global date
    date = datetime.datetime.now().strftime('%Y-%m-%d')

date()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 30, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nn = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nn.setObjectName("nn")
        self.gridLayout.addWidget(self.nn, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 180, 290, 180))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.jinrizuigaoqiwen = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.jinrizuigaoqiwen.setObjectName("jinrizuigaoqiwen")
        self.gridLayout_3.addWidget(self.jinrizuigaoqiwen, 3, 0, 1, 1)
        self.jinritainqi = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.jinritainqi.setObjectName("jinritainqi")
        self.gridLayout_3.addWidget(self.jinritainqi, 0, 0, 1, 1)
        self.leixingjinri = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.leixingjinri.setObjectName("leixingjinri")
        self.gridLayout_3.addWidget(self.leixingjinri, 4, 0, 1, 1)
        self.jinrizuidiqiwen = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.jinrizuidiqiwen.setObjectName("jinrizuidiqiwen")
        self.gridLayout_3.addWidget(self.jinrizuidiqiwen, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(220, 180, 161, 181))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.leixingjinri1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.leixingjinri1.setObjectName("leixingjinri1")
        self.gridLayout_5.addWidget(self.leixingjinri1, 4, 0, 1, 1)
        self.jinrizuigao1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.jinrizuigao1.setObjectName("jinrizuigao1")
        self.gridLayout_5.addWidget(self.jinrizuigao1, 3, 0, 1, 1)
        self.jinrizuidi1 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.jinrizuidi1.setObjectName("jinrizuidi1")
        self.gridLayout_5.addWidget(self.jinrizuidi1, 2, 0, 1, 1)
        self.kong = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.kong.setText("")
        self.kong.setObjectName("kong")
        self.gridLayout_5.addWidget(self.kong, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(590, 180, 161, 181))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.mingririzuigao1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.mingririzuigao1.setObjectName("mingririzuigao1")
        self.gridLayout_7.addWidget(self.mingririzuigao1, 3, 0, 1, 1)
        self.kong_2 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.kong_2.setObjectName("kong_2")
        self.gridLayout_7.addWidget(self.kong_2, 0, 0, 1, 1)
        self.leixingmingri1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.leixingmingri1.setObjectName("leixingmingri1")
        self.gridLayout_7.addWidget(self.leixingmingri1, 4, 0, 1, 1)
        self.mingrizuidi1 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.mingrizuidi1.setObjectName("mingrizuidi1")
        self.gridLayout_7.addWidget(self.mingrizuidi1, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(430, 180, 164, 181))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.mingrizuigao = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.mingrizuigao.setObjectName("mingrizuigao")
        self.gridLayout_9.addWidget(self.mingrizuigao, 3, 0, 1, 1)
        self.mingri = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.mingri.setObjectName("mingri")
        self.gridLayout_9.addWidget(self.mingri, 0, 0, 1, 1)
        self.mingrileixing = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.mingrileixing.setObjectName("mingrileixing")
        self.gridLayout_9.addWidget(self.mingrileixing, 4, 0, 1, 1)
        self.mingrizuidi = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.mingrizuidi.setObjectName("mingrizuidi")
        self.gridLayout_9.addWidget(self.mingrizuidi, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "天气"))
        self.nn.setText(_translate("MainWindow", "city：南宁"))
        self.label_26.setText(_translate("MainWindow", date))
        self.jinrizuigaoqiwen.setText(_translate("MainWindow", "最高气温℃"))
        self.jinritainqi.setText(_translate("MainWindow", "今日天气"))
        self.leixingjinri.setText(_translate("MainWindow", "类型"))
        self.jinrizuidiqiwen.setText(_translate("MainWindow", "最低气温℃"))
        self.leixingjinri1.setText(_translate("MainWindow", type_today))
        self.jinrizuigao1.setText(_translate("MainWindow", high_today))
        self.jinrizuidi1.setText(_translate("MainWindow", low_today))
        self.mingririzuigao1.setText(_translate("MainWindow", high_tomorrow))
        self.kong_2.setText(_translate("MainWindow", ''))
        self.leixingmingri1.setText(_translate("MainWindow", type_tomorrow))
        self.mingrizuidi1.setText(_translate("MainWindow", low_tomorrow))
        self.mingrizuigao.setText(_translate("MainWindow", "最高气温℃"))
        self.mingri.setText(_translate("MainWindow", "明日天气"))
        self.mingrileixing.setText(_translate("MainWindow", "类型"))
        self.mingrizuidi.setText(_translate("MainWindow", "最低气温℃"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow()                    # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication

