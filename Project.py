# OOP-Final-Project
# ===Ryan x Donald===

import sys
from sqlitedict import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Project"
        self.x = 350
        self.y = 100
        self.width = 700
        self.height = 500
    
    def initUi(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.textbox1 = QLineEdit(self)
        self.textboxlbl = QLabel("What's your name pilot ?: ", self)
        self.textboxlbl.move(190,79)
        self.textbox1.setText(" Enter your name before launching to space !")
        self.textbox1.move(250,70)
        self.textbox1.resize(280,30)

        self.textbox2 = QLineEdit(self)
        self.textboxlbl2 = QLabel("What grade level are you in ?:", self)
        self.textboxlbl2.move(190,119)
        self.textbox2.setText("Enter your grade level (Ex: Grade 1)")
        self.textbox2.move(250,110)
        self.textbox2.resize(280,30)

        self.button = QPushButton('Submit', self)
        self.button.setToolTip("Submit your information to NASA !")
        self.button.move(149,310)
        self.button.clicked.connect(self.data) 
        self.button2 = QPushButton('Clear',self)
        self.button2.setToolTip("Clearing all information ")
        self.button2.move(305,310)
        self.button2.clicked.connect(self.clear)
        
        self.show()
    
        def buttons():
            self.button = QPushButton('Continue',self)
            self.button.setStyleSheet("font: Bold")
            self.button.setToolTip("Continue to Main Window")
            self.button.clicked.connect(self.Window_2)
            self.button.resize(100,50)
            self.button.move(200,400)

            self.button1 = QPushButton('Quit',self)
            self.button1.setStyleSheet("font: Bold")
            self.button1.setToolTip("Exit Application")
            self.button1.clicked.connect(self.Cancel)
            self.button1.resize(100,50)
            self.button1.move(350,400)
        buttons()

        def labels():
            self.label = QLabel("Programmed by: Donald G. Jardiolin and John Ryan L. Montecalvo",self)
            self.label.resize(490,20)
            self.label.move(180,450)

            self.label1 = QLabel("Technological Institute of the Philippines",self)
            self.label1.resize(400,20)
            self.label1.move(240,470)
        labels()

        self.Window()

    @pyqtSlot()
    def submitBox(self):
        buttonReply = QMessageBox.question(self,"Submitting Data", "Do you want to submit the information partner ? ", 
                                                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            QMessageBox.warning(self,"Evalutaion", "Registration Complete", QMessageBox.Ok,QMessageBox.Ok)

        else:
           pass

    def clear(self):
        self.textbox1.setText("")
        self.textbox2.setText("")

    def data(self):
        name = self.textbox1.text()
        grdlevel = self.textbox2.text()

        self.submitdata(name, grdlevel)

    def submitdata(self,name,grdlevel):
        submitting = QMessageBox.question(self, "Submitting Data", "Confirm?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if submitting == QMessageBox.Yes and name != "" and grdlevel != "":
            dataB = SqliteDict("Ddb.db", autocommit = True)
            reglist = dataDB.get('reg',[])
            listdict = {"Name":name, "Grade Level":grdlevel}
            reglist.append(listdict)
            dataB['reg'] = reglist
            print(dataB['reg'])
            
            QMessageBox.information(self, "Evaluation", "Registration Complete", QMessageBox.Ok, QMessageBox.Ok)

        elif submitting == QMessageBox.No:
            pass
        elif submitting == QMessageBox.No and name == "" and grdlevel == "":
            pass
        elif submitting == QMessageBox.No and name == "" or grdlevel == "":
            QMessageBox.warning(self, "Error","Ooops partner you have to answer all the information to be an austronaut", QMessageBox.Ok, QMessageBox.Ok)
    

    def Cancel(self):
        Confirmation = QMessageBox.warning(self,"Warning","Quit Application?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if Confirmation == QMessageBox.Yes:
            MainWindow.close()
        else:
            pass

    def Window(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.show()

    def Window_2(self):
        self.wndw2 = Window2()
        self.wndw2.show()
        MainWindow.close(self)


    
class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window-2")
        self.setGeometry(350,100,700,500)
        
        self.button = QPushButton('',self)
        self.button.setIcon(QIcon('Nike.png'))
        self.button.setToolTip("Description\nDescription")
        self.button.setIconSize(QSize(100, 100))
        self.button.resize(100,100)
        self.button.move(10,150)
        self.button.clicked.connect(self.Window_3)

        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-arrow.ico'))
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)

    @pyqtSlot()

    def Window_3(self):
        self.wndw3 = Window3()
        self.wndw3.show()
        Window2.close(self)

    def back(self):
        Window2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()

class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window-3")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-arrow.ico'))
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
    
    @pyqtSlot()

    def back(self):
        Window3.close(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(app.exec_())
