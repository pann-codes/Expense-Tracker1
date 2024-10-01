
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 610)
        MainWindow.setMinimumSize(QtCore.QSize(525, 610))
        MainWindow.setMaximumSize(QtCore.QSize(525, 610))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(210, 470, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setStyleSheet("border:2px solid black;\n"
"border-radius:50;\n"
"background-color:#888;")
        self.add.setObjectName("add")
        self.backward = QtWidgets.QPushButton(self.centralwidget)
        self.backward.setGeometry(QtCore.QRect(160, 530, 41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backward.setFont(font)
        self.backward.setStyleSheet("border:2px solid black;\n"
"border-radius:20;\n"
"background-color:#888;")
        self.backward.setObjectName("backward")
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(320, 530, 41, 41))
        self.forward.setMinimumSize(QtCore.QSize(41, 41))
        self.forward.setMaximumSize(QtCore.QSize(41, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.forward.setFont(font)
        self.forward.setStyleSheet("border:2px solid black;\n"
"border-radius:20;\n"
"background-color:#888;")
        self.forward.setObjectName("forward")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 80, 501, 291))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listView_1 = QtWidgets.QListView(self.page_1)
        self.listView_1.setObjectName("listView_1")
        self.horizontalLayout_2.addWidget(self.listView_1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = PlotWidget(self.page_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.crt_balance_lbl = QtWidgets.QLabel(self.page_3)
        self.crt_balance_lbl.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.crt_balance_lbl.setFont(font)
        self.crt_balance_lbl.setObjectName("crt_balance_lbl")
        self.daily_avg_lbl = QtWidgets.QLabel(self.page_3)
        self.daily_avg_lbl.setGeometry(QtCore.QRect(20, 60, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.daily_avg_lbl.setFont(font)
        self.daily_avg_lbl.setObjectName("daily_avg_lbl")
        self.monthly_avg_lbl = QtWidgets.QLabel(self.page_3)
        self.monthly_avg_lbl.setGeometry(QtCore.QRect(20, 90, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.monthly_avg_lbl.setFont(font)
        self.monthly_avg_lbl.setObjectName("monthly_avg_lbl")
        self.crt_balance = QtWidgets.QLabel(self.page_3)
        self.crt_balance.setGeometry(QtCore.QRect(160, 30, 191, 16))
        self.crt_balance.setText("")
        self.crt_balance.setObjectName("crt_balance")
        self.daily_avg = QtWidgets.QLabel(self.page_3)
        self.daily_avg.setGeometry(QtCore.QRect(160, 60, 191, 16))
        self.daily_avg.setText("")
        self.daily_avg.setObjectName("daily_avg")
        self.monthly_avg = QtWidgets.QLabel(self.page_3)
        self.monthly_avg.setGeometry(QtCore.QRect(160, 90, 191, 16))
        self.monthly_avg.setText("")
        self.monthly_avg.setObjectName("monthly_avg")
        self.budget_lbl = QtWidgets.QLabel(self.page_3)
        self.budget_lbl.setGeometry(QtCore.QRect(20, 120, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.budget_lbl.setFont(font)
        self.budget_lbl.setObjectName("budget_lbl")
        self.budget_avg = QtWidgets.QLabel(self.page_3)
        self.budget_avg.setGeometry(QtCore.QRect(160, 120, 191, 16))
        self.budget_avg.setText("")
        self.budget_avg.setObjectName("budget_avg")
        self.budget_monthly_avg = QtWidgets.QLabel(self.page_3)
        self.budget_monthly_avg.setGeometry(QtCore.QRect(160, 150, 191, 16))
        self.budget_monthly_avg.setText("")
        self.budget_monthly_avg.setObjectName("budget_monthly_avg")
        self.budget_monthly_lbl = QtWidgets.QLabel(self.page_3)
        self.budget_monthly_lbl.setGeometry(QtCore.QRect(20, 150, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.budget_monthly_lbl.setFont(font)
        self.budget_monthly_lbl.setObjectName("budget_monthly_lbl")
        
        self.actual_budget_lbl = QtWidgets.QLabel(self.page_3)
        self.actual_budget_lbl.setGeometry(QtCore.QRect(20, 180, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actual_budget_lbl.setFont(font)
        self.actual_budget_lbl.setObjectName("budget_lbl")
        self.actual_budget_avg = QtWidgets.QLabel(self.page_3)
        self.actual_budget_avg.setGeometry(QtCore.QRect(160, 180, 191, 16))
        self.actual_budget_avg.setText("")
        self.actual_budget_avg.setObjectName("budget_avg")
        
        self.stackedWidget.addWidget(self.page_3)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(65, 10, 400, 65))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.delete = QtWidgets.QPushButton(self.centralwidget)
        self.delete.setGeometry(QtCore.QRect(20, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete.setFont(font)
        self.delete.setStyleSheet("border:2px solid black;\n"
"border-radius:20;\n"
"background-color:#888;")
        self.delete.setObjectName("delete")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(400, 530, 101, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update.sizePolicy().hasHeightForWidth())
        self.update.setSizePolicy(sizePolicy)
        self.update.setMinimumSize(QtCore.QSize(101, 41))
        self.update.setMaximumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update.setFont(font)
        self.update.setStyleSheet("border:2px solid black;\n"
"border-radius:20;\n"
"background-color:#888;")
        self.update.setObjectName("update")
        self.dateEdit = QtWidgets.QLabel(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(100, 80, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setText(str(date.today()))#new
        self.dateEdit.setFont(font)
        self.date_lbl = QtWidgets.QLabel(self.centralwidget)
        self.date_lbl.setGeometry(QtCore.QRect(26, 80, 61, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_lbl.setFont(font)
        self.date_lbl.setObjectName("date_lbl")
        self.expense_lbl = QtWidgets.QLabel(self.centralwidget)
        self.expense_lbl.setGeometry(QtCore.QRect(20, 370, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.expense_lbl.setFont(font)
        self.expense_lbl.setObjectName("expense_lbl")
        self.balance_lbl = QtWidgets.QLabel(self.centralwidget)
        self.balance_lbl.setGeometry(QtCore.QRect(20, 400, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.balance_lbl.setFont(font)
        self.balance_lbl.setObjectName("balance_lbl")
        self.expense_dsp = QtWidgets.QLabel(self.centralwidget)
        self.expense_dsp.setGeometry(QtCore.QRect(100, 370, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.expense_dsp.setFont(font)
        self.expense_dsp.setText("")
        self.expense_dsp.setObjectName("expense_dsp")
        self.balance_dsp = QtWidgets.QLabel(self.centralwidget)
        self.balance_dsp.setGeometry(QtCore.QRect(100, 400, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.balance_dsp.setFont(font)
        self.balance_dsp.setText("")
        self.balance_dsp.setObjectName("balance_dsp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSave.setObjectName("actionSave")
        self.actionAdd_Balance = QtWidgets.QAction(MainWindow)
        self.actionAdd_Balance.setObjectName("actionAdd_Balance")
        self.actionUpdate_Balance = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Balance.setObjectName("actionUpdate_Balance")
        self.actionExcel = QtWidgets.QAction(MainWindow)
        self.actionExcel.setObjectName("actionExcel")
        self.actionCsv = QtWidgets.QAction(MainWindow)
        self.actionCsv.setObjectName("actionCsv")
        self.actionMail_Report = QtWidgets.QAction(MainWindow)
        self.actionMail_Report.setObjectName("actionMail_Report")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionAdd_Balance)
        self.menuFile.addAction(self.actionUpdate_Balance)
        self.menuReport.addAction(self.actionExcel)
        self.menuReport.addAction(self.actionCsv)
        self.menuReport.addAction(self.actionMail_Report)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backward.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forward.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expense Tracker"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.add.setShortcut(_translate("MainWindow", "A"))
        self.backward.setText(_translate("MainWindow", "<"))
        self.backward.setShortcut(_translate("MainWindow", "Left"))
        self.forward.setText(_translate("MainWindow", ">"))
        self.forward.setShortcut(_translate("MainWindow", "Right"))
        self.crt_balance_lbl.setText(_translate("MainWindow", "Current Balance:"))
        self.daily_avg_lbl.setText(_translate("MainWindow", "Daily avg:"))
        self.monthly_avg_lbl.setText(_translate("MainWindow", "Monthly avg:"))
        self.budget_lbl.setText(_translate("MainWindow", "Budget avg (daily):"))
        self.budget_monthly_lbl.setText(_translate("MainWindow", "Budget avg (monthly):"))
        self.actual_budget_lbl.setText(_translate("MainWindow", "Budget total:"))
        self.title.setText(_translate("MainWindow", "Expense Tracker"))
        self.delete.setText(_translate("MainWindow", "Delete"))
        self.delete.setShortcut(_translate("MainWindow", "Del"))
        self.update.setText(_translate("MainWindow", "Change"))
        self.update.setShortcut(_translate("MainWindow", "Space"))
        self.date_lbl.setText(_translate("MainWindow", "Date:"))
        self.expense_lbl.setText(_translate("MainWindow", "Expense:"))
        self.balance_lbl.setText(_translate("MainWindow", "Balance:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuReport.setTitle(_translate("MainWindow", "Report")) #Add the report button to menu 
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAdd_Balance.setText(_translate("MainWindow", "Add Budget"))
        self.actionAdd_Balance.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionUpdate_Balance.setText(_translate("MainWindow", "Update Budget"))
        self.actionUpdate_Balance.setShortcut(_translate("MainWindow", "Alt+B"))
        self.actionExcel.setText(_translate("MainWindow", "Excel"))
        self.actionExcel.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionCsv.setText(_translate("MainWindow", "Csv"))
        self.actionCsv.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionMail_Report.setText(_translate("MainWindow", "Mail Report"))
        self.actionMail_Report.setShortcut(_translate("MainWindow", "Ctrl+M"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#testing pr
