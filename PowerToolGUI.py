from PyQt5 import QtCore, QtGui, QtWidgets
from PowerTool import powerScrape, statementReturner, gradeChangeShow, gradelist1, classlist

guirunamount = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QtGui.QIcon("PowerTool.jpg"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("background-color: rgb(43, 45, 59);")
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background.setObjectName("background")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.background)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 4, 7, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 6, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.background)
        self.password_input.setMinimumSize(QtCore.QSize(225, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.password_input.setFont(font)
        self.password_input.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(232, 154, 115);\n"
"    border-radius: 5px;\n"
"    color: #FFF;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 169, 126);\n"
"}\n"
"")
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_input.setDragEnabled(True)
        self.password_input.setObjectName("password_input")
        self.gridLayout_3.addWidget(self.password_input, 6, 3, 1, 1)
        self.quarter_input = QtWidgets.QLineEdit(self.background)
        self.quarter_input.setMinimumSize(QtCore.QSize(225, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.quarter_input.setFont(font)
        self.quarter_input.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(232, 154, 115);\n"
"    border-radius: 5px;\n"
"    color: #FFF;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 169, 126);\n"
"}\n"
"")
        self.quarter_input.setText("")
        self.quarter_input.setMaxLength(1)
        self.quarter_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.quarter_input.setDragEnabled(True)
        self.quarter_input.setObjectName("quarter_input")
        self.gridLayout_3.addWidget(self.quarter_input, 7, 3, 1, 1)
        self.username_input = QtWidgets.QLineEdit(self.background)
        self.username_input.setMinimumSize(QtCore.QSize(225, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(232, 154, 115);\n"
"    border-radius: 5px;\n"
"    color: #FFF;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: rgb(255, 169, 126);\n"
"}\n"
"")
        self.username_input.setText("")
        self.username_input.setDragEnabled(True)
        self.username_input.setObjectName("username_input")
        self.gridLayout_3.addWidget(self.username_input, 5, 3, 1, 1)
        self.run_button = QtWidgets.QPushButton(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QtCore.QSize(250, 80))
        self.run_button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.run_button.setFont(font)
        self.run_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_button.setStyleSheet("QPushButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(232, 154, 115);\n"
"    border-radius: 40px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 169, 126);\n"
"\n"
"}")
        self.run_button.setAutoDefault(False)
        self.run_button.setFlat(False)
        self.run_button.setObjectName("run_button")
        self.gridLayout_3.addWidget(self.run_button, 3, 1, 6, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.background)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.background)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(232, 154, 115);\n"
"border-radius: 40px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-top: 10px;")
        self.textEdit.setMarkdown("")
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 1, 1, 1, 3)
        self.gridLayout_2.addWidget(self.background, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.username_input, self.password_input)
        MainWindow.setTabOrder(self.password_input, self.quarter_input)
        MainWindow.setTabOrder(self.quarter_input, self.run_button)
        MainWindow.setTabOrder(self.run_button, self.textEdit)

        #collects cresidentials from line boxes, runs PowerTool.py, and returns data in the text box.
    def runButton(self):
        global guirunamount
        guirunamount +=1
        username_arg = self.username_input.text()
        password_arg = self.password_input.text()
        quarter_arg = self.quarter_input.text()
        powerScrape(username_arg, password_arg, quarter_arg)
        statementReturner()
        gradeChangeShow()
        if guirunamount > 1:
                self.textEdit.setText(statementReturner() + gradeChangeShow())
                #self.textEdit.setText(gradeChangeShow())
        else:
                self.textEdit.setText(statementReturner())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PowerTool"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Password:"))
        self.quarter_input.setPlaceholderText(_translate("MainWindow", "Quarter Number:"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Username:"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        #when the run button is clicked, it runs the function runButton()
        self.run_button.clicked.connect(self.runButton)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())