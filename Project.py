# OOP-Final-Project
# ===Ryan===

import sys
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

        self.setWindowTitle(self.title)
        
        def buttons():
            self.button = QPushButton('Continue',self)
            self.button.setToolTip("Continue to Main Window")
            self.button.clicked.connect(self.Window_2)
            self.button.resize(100,50)
            self.button.move(200,400)

            self.button1 = QPushButton('Quit',self)
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

    def Window_3(self):
        self.wndw3 = Window3()
        self.wndw3.show()

class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window-3")
        self.setGeometry(350,100,700,500)
        
        self.text = QLabel(QPushButton("HI",self))
        
        print("HI")
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()
    sys.exit(app.exec_())  
