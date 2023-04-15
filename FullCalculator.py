from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QFont


check = True
ans = None


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("5.ico"))
        MainWindow.resize(328, 465)
        MainWindow.setMinimumSize(QtCore.QSize(324, 465))
        MainWindow.setMaximumSize(QtCore.QSize(324, 465))
        font = QtGui.QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(5, 0, 330, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 250);")
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 400, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 400, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 400, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/record-button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(6, 6))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 400, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/equal (1).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 350, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_6.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 350, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(90, 350, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(250, 350, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_10.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/add.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QtCore.QSize(25, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(170, 300, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 300, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(90, 300, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(250, 300, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(29)
        font.setBold(False)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_15.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_15.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_15.setIcon(icon3)
        self.pushButton_15.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(170, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(90, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(250, 250, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_20.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_20.setIcon(icon4)
        self.pushButton_20.setIconSize(QtCore.QSize(100, 15))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(170, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_21.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/percentage.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_21.setIcon(icon5)
        self.pushButton_21.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_21.setFlat(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_24 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(90, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_24.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/superscript-512.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_24.setIcon(icon6)
        self.pushButton_24.setIconSize(QtCore.QSize(35, 22))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(250, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_25.setAutoFillBackground(True)
        self.pushButton_25.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_25.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/divide.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_25.setIcon(icon7)
        self.pushButton_25.setIconSize(QtCore.QSize(45, 25))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(170, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(10, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_27.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_29 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(90, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(250, 150, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_30.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_30.setIcon(icon8)
        self.pushButton_30.setIconSize(QtCore.QSize(60, 25))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_28 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(10, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("border-color: rgb(129, 255, 224);")
        self.pushButton_28.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/square_root_square_x_math_symbol_function-512.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_28.setIcon(icon9)
        self.pushButton_28.setIconSize(QtCore.QSize(35, 25))
        self.pushButton_28.setObjectName("pushButton_28")
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        
        
        # connections
        self.pushButton_27.clicked.connect(self.Left_parenthese)
        self.pushButton_29.clicked.connect(self.Right_parenthese)
        self.pushButton_26.clicked.connect(self.Clear)
        self.pushButton_30.clicked.connect(self.Backspace)
        self.pushButton_28.clicked.connect(self.Root)
        self.pushButton_24.clicked.connect(self.Squared)
        self.pushButton_21.clicked.connect(self.mod)
        self.pushButton_17.clicked.connect(self.Seven)
        self.pushButton_19.clicked.connect(self.Eight)
        self.pushButton_16.clicked.connect(self.Nine)
        self.pushButton_20.clicked.connect(self.Multiply)
        self.pushButton_12.clicked.connect(self.Four)
        self.pushButton_14.clicked.connect(self.Five)
        self.pushButton_11.clicked.connect(self.Six)
        self.pushButton_15.clicked.connect(self.Minus)
        self.pushButton_7.clicked.connect(self.One)
        self.pushButton_9.clicked.connect(self.Two)
        self.pushButton_6.clicked.connect(self.Three)
        self.pushButton_2.clicked.connect(self.Zero)
        self.pushButton_3.clicked.connect(self.Dot)
        self.pushButton_4.clicked.connect(self.Equal)
        self.pushButton_10.clicked.connect(self.Add)
        self.pushButton_25.clicked.connect(self.Division)
        self.pushButton.clicked.connect(self.Ans)





        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Full Calculator"))
        self.pushButton.setText(_translate("MainWindow", "ANS"))
        self.pushButton_2.setText(_translate("MainWindow", "0"))
        self.pushButton_6.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "1"))
        self.pushButton_9.setText(_translate("MainWindow", "2"))
        self.pushButton_11.setText(_translate("MainWindow", "6"))
        self.pushButton_12.setText(_translate("MainWindow", "4"))
        self.pushButton_14.setText(_translate("MainWindow", "5"))
        self.pushButton_16.setText(_translate("MainWindow", "9"))
        self.pushButton_17.setText(_translate("MainWindow", "7"))
        self.pushButton_19.setText(_translate("MainWindow", "8"))
        self.pushButton_26.setText(_translate("MainWindow", "C"))
        self.pushButton_27.setText(_translate("MainWindow", "("))
        self.pushButton_29.setText(_translate("MainWindow", ")"))


    # check = True


    # functions
    def Left_parenthese(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"(")
        if not check:
            self.lineEdit.setText("(")
    def Right_parenthese(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+")")
        if not check:
            self.lineEdit.setText(")")
    def Clear(self):
        self.lineEdit.setText("")
    
    def Backspace(self):
        self.lineEdit.setText(self.lineEdit.text()[0:-1])
        
    def Zero(self):
        global check
        if  check:
            self.lineEdit.setText(self.lineEdit.text()+"0")
        if not check:
            self.lineEdit.setText("0")
        check = True
            
    def One(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"1")
        if not check:
            self.lineEdit.setText("1")

            
    def Two(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"2")
        if not check:
            self.lineEdit.setText("2")
               
    def Three(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"3")
        if not check:
            self.lineEdit.setText("3")  
                  
    def Four(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"4")
        if not check:
            self.lineEdit.setText("4")
            
    def Five(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"5")
        if not check:
            self.lineEdit.setText("5") 
                   
    def Six(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"6")
        if not check:
            self.lineEdit.setText("6") 
                   
    def Seven(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text()+"7")
        if not check:
            self.lineEdit.setText("7") 
                   
    def Eight(self):
        global check
        if  check:
            self.lineEdit.setText(self.lineEdit.text()+"8")
        if not check:
            self.lineEdit.setText("8")
            
                    
    def Nine(self):
        global check
        if  check:
            self.lineEdit.setText(self.lineEdit.text()+"9")
        if not check:
            self.lineEdit.setText("9") 
                   
    def Add(self):
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "+")
        check = True
                
    def Minus(self):
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "-")
        check = True
                
    def Multiply(self):
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "*")
        check = True
        
    def Division(self):
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "/")
        check = True
                
    def mod(self):
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "%")
        check = True
        
        
        
    

            
            

    def Squared(self):
        # number = float(self.lineEdit.text())
        # self.lineEdit.setText(str(number**2))
         
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "**2")
        
        # number = float(self.lineEdit.text())
        # self.lineEdit.setText(str(number**2))
        check = True
            

                
    def Root(self):
        # self.lineEdit.setText(str(pow(float(self.lineEdit.text()),0.5)))
        
        global check
        self.lineEdit.setText(self.lineEdit.text()+ "**0.5")
        
        # self.lineEdit.setText(str(pow(float(self.lineEdit.text()),0.5)))
        check = True
        
        

    def Dot(self):
        global check
        if check:
            self.lineEdit.setText(self.lineEdit.text() +".")
        if not check:
            self.lineEdit.setText(".")
       
                    
    def Equal(self):
        global check
        global ans
        
        try:
            self.lineEdit.setText(str(eval(self.lineEdit.text())))
            ans = self.lineEdit.text()
                
        except ZeroDivisionError:
            
            # self.lineEdit.setStyleSheet("color: red")
            self.lineEdit.setFont(QFont("sanserif",15))
            self.lineEdit.setText("Math EROR")

        except SyntaxError:
            # self.lineEdit.setStyleSheet("color: red")
            self.lineEdit.setFont(QFont("sanserif",15))
            self.lineEdit.setText("Sytax ERROR")
        except:
            self.lineEdit.setText("ERROR")
            
            

        check = False

    def Ans(self):
        if ans is not None:
            self.lineEdit.setText(self.lineEdit.text()+str(ans))
        else:
            pass
        








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
