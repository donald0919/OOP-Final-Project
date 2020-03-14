

import sys
from sqlitedict import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Educational Solar System for Kids!"
        self.x = 350
        self.y = 100
        self.width = 700
        self.height = 500
    
    def initUi(self):
        self.setWindowTitle(self.title)

        
        self.show()
    
        def buttons():
            self.button = QPushButton('Continue',self)
            self.button.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: lightblue }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton { color: white }'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 13px }')
            self.button.setToolTip("Continue to Main Window")
            self.button.clicked.connect(self.Window_2)
            self.button.resize(100,50)
            self.button.move(200,400)

            self.button1 = QPushButton('Quit',self)
            self.button1.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: lightblue }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton { color: white }'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 13px }')
            self.button1.setToolTip("Exit Application")
            self.button1.clicked.connect(self.Cancel)
            self.button1.resize(100,50)
            self.button1.move(400,400)
        buttons()

        def labels():
            self.label = QLabel("Programmed by: Donald G. Jardiolin and John Ryan L. Montecalvo",self)
            self.label.resize(490,20)
            self.label.move(190,450)
            self.label.setStyleSheet("color: white")

            self.label1 = QLabel("Technological Institute of the Philippines",self)
            self.label1.resize(400,20)
            self.label1.move(240,470)
            self.label1.setStyleSheet("color: white")
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
            MainWindow.close(self)
        else:
            pass

    def Window(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.show()

    def Window_2(self):
        self.wndw2 = Window2()
        self.wndw2.show()
        MainWindow.hide(self)




    
class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Solar System")
        self.setGeometry(350,100,700,500)

        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()   
        
        def buttons():
            def Sun():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('Sun.png'))
                self.button.setToolTip("Sun")
                self.button.setStyleSheet('QPushButton { background-color: transparent }')
                self.button.setIconSize(QSize(400, 400))
                self.button.resize(400,400)
                self.button.move(525,-50)
                self.button.clicked.connect(self.Window_sun)
            Sun()

            def Mercury():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('mercury.png'))
                self.button.setToolTip("Mercury")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(25, 25))
                self.button.resize(25,25)
                self.button.move(500,200)
                self.button.clicked.connect(self.Window_mercury)
            Mercury()

            def Venus():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('venus.png'))
                self.button.setToolTip("Venus")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(50, 50))
                self.button.resize(50,50)
                self.button.move(430,190)
                self.button.clicked.connect(self.Window_venus)
            Venus()

            def Earth():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('earth.png'))
                self.button.setToolTip("Earth")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(50,50))
                self.button.resize(50,50)
                self.button.move(370,150)
                self.button.clicked.connect(self.Window_earth)
            Earth()

            def Mars():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('mars.png'))
                self.button.setToolTip("Mars")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(35,35))
                self.button.resize(35,35)
                self.button.move(340,240)
                self.button.clicked.connect(self.Window_mars)
            Mars()

            def Jupiter():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('jupiter.png'))
                self.button.setToolTip("Jupiter")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(200,200))
                self.button.resize(200,200)
                self.button.move(200,300)
                self.button.clicked.connect(self.Window_jupiter)
            Jupiter()

            def Saturn():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('saturn.png'))
                self.button.setToolTip("Saturn")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(200,200))
                self.button.resize(200,200)
                self.button.move(120,30)
                self.button.clicked.connect(self.Window_saturn)
            Saturn()

            def Uranus():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('uranus.png'))
                self.button.setToolTip("Uranus")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(125,125))
                self.button.resize(125,125)
                self.button.move(50,230)
                self.button.clicked.connect(self.Window_uranus)
            Uranus()

            def Neptune():
                self.button = QPushButton('',self)
                self.button.setIcon(QIcon('neptune.png'))
                self.button.setToolTip("Neptune")
                self.button.setStyleSheet('background-color: transparent')
                self.button.setIconSize(QSize(100,100))
                self.button.resize(100,100)
                self.button.move(0,50)
                self.button.clicked.connect(self.Window_neptune)
            Neptune()

            def back():
                self.backbutton = QPushButton('',self)
                self.backbutton.setIcon(QIcon('back-icon.ico'))
                self.backbutton.setStyleSheet('background-color: transparent')
                self.backbutton.setToolTip("Back")
                self.backbutton.setIconSize(QSize(25,25))
                self.backbutton.resize(50,40)
                self.backbutton.move(5,5)
                self.backbutton.clicked.connect(self.back)
            back()
        buttons()

    @pyqtSlot()

    def Window_sun(self):
        self.wndw = WindowSun()
        self.wndw.show()
        Window2.hide(self)

    def Window_mercury(self):
        self.wndw = WindowMercury()
        self.wndw.show()
        Window2.hide(self)

    def Window_venus(self):
        self.wndw = WindowVenus()
        self.wndw.show()
        Window2.hide(self)

    def Window_earth(self):
        self.wndw = WindowEarth()
        self.wndw.show()
        Window2.hide(self)

    def Window_mars(self):
        self.wndw = WindowMars()
        self.wndw.show()
        Window2.hide(self)

    def Window_jupiter(self):
        self.wndw = WindowJupiter()
        self.wndw.show()
        Window2.hide(self)

    def Window_saturn(self):
        self.wndw = WindowSaturn()
        self.wndw.show()
        Window2.hide(self)

    def Window_uranus(self):
        self.wndw = WindowUranus()
        self.wndw.show()
        Window2.hide(self)

    def Window_neptune(self):
        self.wndw = WindowNeptune()
        self.wndw.show()
        Window2.hide(self)

    def back(self):
        Window2.close(self)
        self.MainWindow()

    def MainWindow(self):
        self.mnwndw = MainWindow()
        self.mnwndw.show()




class WindowSun(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sun")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowSun.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowMercury(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mercury")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowMercury.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()
        
class WindowVenus(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Venus")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowVenus.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowEarth(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Earth")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowEarth.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowMars(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mars")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowMars.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowJupiter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jupiter")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowJupiter.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowSaturn(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Saturn")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowSaturn.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowUranus(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Uranus")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowUranus.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

class WindowNeptune(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Neptune")
        self.setGeometry(350,100,700,500)
        
        self.backbutton = QPushButton('',self)
        self.backbutton.setIcon(QIcon('back-icon.ico'))
        self.backbutton.setStyleSheet('background-color: transparent')
        self.backbutton.setToolTip("Back")
        self.backbutton.setIconSize(QSize(25,25))
        self.backbutton.resize(50,40)
        self.backbutton.move(5,5)
        self.backbutton.clicked.connect(self.back)
        
        def background():
            bg = QImage("stars-space.png")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

    @pyqtSlot()

    def back(self):
        WindowNeptune.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()

