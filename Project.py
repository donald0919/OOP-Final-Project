"""

    March 2020
    Final project in OOP
    Programmed by: Ryan and Donald

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sqlitedict import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Educational Solar System for Kids!"
        self.x = 350
        self.y = 100
        self.width = 700
        self.height = 500
        self.setWindowTitle(self.title)

        def background():
            bg = QImage("planet-space.jpg")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

        def info():
            self.label1 = QLabel("ALMOST THERE SPACE RANGER!",self)
            self.label1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { font: bold italic 20px}'
                                'QLabel { color: white}')
            self.label1.move(197,10)
            self.label1.resize(500,40)

            self.label2 = QLabel("          Hold on to your seat space ranger \n"
                            " In order to proceed on your next journey\n"
                            "                    just click continue!\n\n"
                            "If you dont want to continue on the journey\n"
                            "                 just click the quit button!",self)
            self.label2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { font-size: 15px}'
                                'QLabel { color: white}')
            self.label2.move(210,45)
            self.label2.resize(300,200)
        info()

        def buttons():
            self.button = QPushButton('Continue',self)
            self.button.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                                    'QPushButton:pressed { color: black }'
                                    'QPushButton { font-family: Comic Sans MS}'
                                    'QPushButton { color: white }'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 13px }')
            self.button.setToolTip("Continue to the Solar System")
            self.button.clicked.connect(self.Window_2)
            self.button.resize(100,50)
            self.button.move(200,400)

            self.button1 = QPushButton('Quit',self)
            self.button1.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                                    'QPushButton { color: white }'
                                    'QPushButton { font-family: Comic Sans MS}'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 13px }')
            self.button1.setToolTip("Exit")
            self.button1.clicked.connect(self.Cancel)
            self.button1.resize(100,50)
            self.button1.move(400,400)

            self.button2 = QPushButton("About",self)
            self.button2.move(600,0)
            #self.button2.clicked.connect(self.about)
            self.button2.setToolTip('Learn about this program')
            self.button2.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                                    'QPushButton { color: white }'
                                    'QPushButton { font-family: Comic Sans MS}'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 12px }')
        buttons()

        def labels():
            self.label = QLabel("Programmed by: Donald G. Jardiolin and John Ryan L. Montecalvo",self)
            self.label.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 12x}')
            self.label.resize(490,20)
            self.label.move(190,450)

            self.label1 = QLabel("Technological Institute of the Philippines",self)
            self.label1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 12px}')
            self.label1.resize(400,20)
            self.label1.move(230,470)

            self.label2 = QLabel("",self)
            self.label2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 15px}')
            self.label2.resize(700,40)
            self.label2.move(50,40)
        labels()

        self.Window()

    @pyqtSlot()

    #def about(self):

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

#class About(QMainWindow)

class SurveyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Educational Solar System for Kids!")
        self.setGeometry(550,150,300,500)
        

        def background():
            bg = QImage("bluegreen-space.jpg")
            bg1 = bg.scaled(QSize(700,500))
            palette = QPalette()
            palette.setBrush(QPalette.Window,QBrush(bg1))
            self.setPalette(palette)
        background()

        def Label():
            
            self.label1 = QLabel("Welcome Space Ranger!",self)
            self.label1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { font: bold italic 20px}'
                                'QLabel { color: white}')
            self.label1.move(30,10)
            self.label1.resize(500,40)

            self.label2 = QLabel("Before we proceed our escapade on\n"
                            " the Solar System, we would like to\n"
                            "           know more about you!\n\n"
                            " Don't worry Space Ranger, we will\n"
                            "    keep your information private!",self)
            self.label2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { font-size: 15px}'
                                'QLabel { color: white}')
            self.label2.move(25,45)
            self.label2.resize(300,150)
        Label()

        def Text():
            self.text1 = QLabel("Name: ",self)
            self.text1.move(25,210)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 15px}')

            self.text2 = QLabel("Age: ",self)
            self.text2.move(25,255)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 15px}')

            self.text2 = QLabel("Grade Level: ",self)
            self.text2.move(25,300)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 15px}')

            self.text2 = QLabel("Name of School: ",self)
            self.text2.resize(200,20)
            self.text2.move(25,345)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 15px}')
        Text()
        
        def Buttons():
            self.b1 = QPushButton('Submit',self)
            self.b1.move(25,400)
            self.b1.clicked.connect(self.info)
            self.b1.setToolTip("Submit data")
            self.b1.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                                    'QPushButton { color: white }'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 13px }')

            self.b2 = QPushButton('Clear',self)
            self.b2.move(175,400)
            self.b2.clicked.connect(self.clear)
            self.b2.setToolTip('Clear data')
            self.b2.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                                    'QPushButton:hover { border-style: inset }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                                    'QPushButton { color: white }'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 13px }')
        Buttons()

        def Textbox():
            self.textbox1 = QLineEdit(self)
            self.textbox1.move(80,215)
            self.textbox1.resize(200,20)
            self.textbox1.setStyleSheet('QLineEdit { background-color: transparent}'
                                        'QLineEdit { color: white}'
                                        'QLineEdit { font-family: Comic Sans MS}'
                                        'QLineEdit { font: 15px}'
                                        'QLineEdit { border: 1px solid white}'
                                        'QLineEdit { border-color: transparent transparent white transparent}')

            self.textbox2 = QLineEdit(self)
            self.textbox2.move(80,260)
            self.textbox2.resize(200,20)
            self.textbox2.setStyleSheet('QLineEdit { background-color: transparent}'
                                        'QLineEdit { color: white}'
                                        'QLineEdit { font-family: Comic Sans MS}'
                                        'QLineEdit { font: 15px}'
                                        'QLineEdit { border: 1px solid white}'
                                        'QLineEdit { border-color: transparent transparent white transparent}')

            self.textbox3 = QLineEdit(self)
            self.textbox3.move(120,305)
            self.textbox3.resize(160,20)
            self.textbox3.setStyleSheet('QLineEdit { background-color: transparent}'
                                        'QLineEdit { color: white}'
                                        'QLineEdit { font-family: Comic Sans MS}'
                                        'QLineEdit { font: 15px}'
                                        'QLineEdit { border: 1px solid white}'
                                        'QLineEdit { border-color: transparent transparent white transparent}')

            self.textbox4 = QLineEdit(self)
            self.textbox4.move(145,345)
            self.textbox4.resize(135,20)
            self.textbox4.setStyleSheet('QLineEdit { background-color: transparent}'
                                        'QLineEdit { color: white}'
                                        'QLineEdit { font-family: Comic Sans MS}'
                                        'QLineEdit { font: 15px}'
                                        'QLineEdit { border: 1px solid white}'
                                        'QLineEdit { border-color: transparent transparent white transparent}')
        Textbox()

        self.show()
         

    @pyqtSlot()

       
    def toMainWindow(self):
        self.toMainWindow = MainWindow()
        self.toMainWindow.show()
        SurveyWindow.hide(self)

    def clear(self):
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText("")
        self.textbox4.setText("")

    def info(self):
        name = self.textbox1.text()
        age = self.textbox2.text()
        gradelevel = self.textbox3.text()
        school = self.textbox4.text()

        self.submit(name, age, gradelevel, school)
    

    def submit(self, name, age, gradelevel, school):
        submit = QMessageBox.question(self, "Submit", "Submit Data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if submit == QMessageBox.No:
            pass
        
        elif submit == QMessageBox.Yes and name == "" and age == "" and gradelevel == "" and school == "":
            warning = QMessageBox.warning(self, "Warning", "Are you sure?\nWe want to know you more!",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if warning == QMessageBox.Yes:
                self.toMainWindow()
            else:
                pass

        elif submit == QMessageBox.Yes and name != "" and age != "" and gradelevel != "" and school != "":
            database = SqliteDict("info.db", autocommit=True)
            inf = database.get('data',[])
            temporary = {"Name: ":name, "Age: ":age, "Grade Level":gradelevel,"School: ":school}
            inf.append(temporary)
            database['data'] = inf
            for i  in range(len(database['data'])):
                print(database['data'][i])
            QMessageBox.information(self, "Submit", "Submitted Successfully!",
                                        QMessageBox.Ok, QMessageBox.Ok)
            self.toMainWindow()
            

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

        def text():
            self.text1 = QLabel("T H E   S O L A R   S Y S T E M",self)
            self.text1.move(170,10)
            self.text1.resize(350,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 20px}'
                                'QLabel { font: bold}')

            self.text2 = QLabel("You may click the planets to view more information!",self)
            self.text2.move(170,40)
            self.text2.resize(350,20)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 15px}'
                                'QLabel { background-color: black}') 
        text()  
        
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
                self.backbutton = QPushButton('Back',self)
                self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                                    'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                                    'QPushButton:hover { color: black }'
                                    'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                                    'QPushButton:pressed { color: black }'
                                    'QPushButton { color: white }'
                                    'QPushButton { border-style: outset }'
                                    'QPushButton { border-width: 1px }'
                                    'QPushButton { border-radius: 10px }'
                                    'QPushButton { padding: 5px }'
                                    'QPushButton { font: bold 9px }')
                self.backbutton.setToolTip("Go back to previous window")
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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")  
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

	
        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Sun.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Sun",self)
            self.text.move(300,50)
            self.text.resize(55,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• Derive from the Latin word 'Sol'.",self)
            self.text1.move(300,120)
            self.text1.resize(290,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• Contains about 98% of all the rocks, dust,\n   and gas in the Solar System.",self) 
            self.text2.move(300,150)
            self.text2.resize(350,60)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• If hollow, 1 million Earth could fit inside.",self)
            self.text3.move(300,220)
            self.text3.resize(350,20)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Acts as a giant magnet.",self)
            self.text4.move(300,260)
            self.text4.resize(220,25)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text5 = QLabel("• Its surface has a temperature of\n   6,000° celsius.",self)
            self.text5.move(300,300)
            self.text5.resize(300,50)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')     
        text()



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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Mercury.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Mercury",self)
            self.text.move(300,50)
            self.text.resize(150,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• It is 36 million miles away from the Sun.",self)
            self.text1.move(300,120)
            self.text1.resize(360,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• Mercury is so hot that you could burn to \n death during daytime.",self) 
            self.text2.move(300,150)
            self.text2.resize(330,100)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• There is almost no air on Mercury.",self)
            self.text3.move(300,240)
            self.text3.resize(350,20)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Mercury is the smallest planet in the solar system.",self)
            self.text4.move(300,280)
            self.text4.resize(380,20)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 16px}')

            self.text5 = QLabel("• Mercury does not have any moons or rings.",self)
            self.text5.move(300,310)
            self.text5.resize(370,50)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')     
        text()


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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Venus.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Venus",self)
            self.text.move(300,50)
            self.text.resize(150,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• It is 67 million miles away from the Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(360,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• You can't live here because it is way too hot.",self) 
            self.text2.move(300,170)
            self.text2.resize(310,20)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• Venus is the second brightest natural object in the sky.",self)
            self.text3.move(300,210)
            self.text3.resize(370,20)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Referred to as the 'MORNING STAR' \n and 'EVENING STAR'. ",self)
            self.text4.move(300,240)
            self.text4.resize(380,70)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 16px}')

            self.text5 = QLabel("• It has mountains, venus quakes, \n valley and volcanoes.",self)
            self.text5.move(300,320)
            self.text5.resize(380,70)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()

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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Earth.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Earth",self)
            self.text.move(300,50)
            self.text.resize(150,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• We are 93 million miles away from the Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(360,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• Only planet that have living things.",self) 
            self.text2.move(300,170)
            self.text2.resize(350,20)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• Earth is 4.54 billion years old.",self)
            self.text3.move(300,210)
            self.text3.resize(370,20)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Earth has a perfect combination of weather, \n temperature and atmosphere to keep \n us alive. ",self)
            self.text4.move(300,245)
            self.text4.resize(380,65)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 16px}')

            self.text5 = QLabel("• The Earth's shape is oblate spheroid.",self)
            self.text5.move(300,320)
            self.text5.resize(380,20)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()

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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Mars.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Mars",self)
            self.text.move(300,50)
            self.text.resize(120,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• Mars is 139 million miles away from the Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(360,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• Mars has the highest mountains and deepest \n canyon in the whole solar system.",self) 
            self.text2.move(300,170)
            self.text2.resize(380,50)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• Mars is a dusty, cold, desert world with \n a very thin atmposhere.",self)
            self.text3.move(300,230)
            self.text3.resize(370,50)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Mars once had streams, rivers, lakes \n and an ocean. ",self)
            self.text4.move(300,290)
            self.text4.resize(380,50)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text5 = QLabel("• Mars is also called the 'RED PLANET'.",self)
            self.text5.move(300,350)
            self.text5.resize(380,20)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()


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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Jupiter.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Jupiter",self)
            self.text.move(300,50)
            self.text.resize(150,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• Jupiter is 483 million miles away from the Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(360,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• It only takes 10 hours to go from night to day in jupiter.",self) 
            self.text2.move(300,160)
            self.text2.resize(380,50)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• There is no solid surface here, it is just \n  one huge ocean of hydrogen and water.",self)
            self.text3.move(300,220)
            self.text3.resize(370,70)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Jupiter is the fastest spinning planet. ",self)
            self.text4.move(300,300)
            self.text4.resize(380,50)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text5 = QLabel("• Did you know that Jupiter has 67 moons.",self)
            self.text5.move(300,360)
            self.text5.resize(380,20)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()


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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Saturn.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Saturn",self)
            self.text.move(300,50)
            self.text.resize(130,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• Saturn is 888 million miles away from the Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(380,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• It only takes 10 hours to go from night to day in jupiter.",self) 
            self.text2.move(300,160)
            self.text2.resize(380,50)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• Saturn is ver similar to Jupiter because \n it's atmosphere is an ocean of liquid chemicals.",self)
            self.text3.move(300,220)
            self.text3.resize(370,60)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• The ring of Saturn is made up of rock, ice \n and tiny dust. ",self)
            self.text4.move(300,300)
            self.text4.resize(380,50)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text5 = QLabel("• It is a large gas planet made mostly of hydrogen \n and helium.",self)
            self.text5.move(300,360)
            self.text5.resize(400,50)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()

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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Uranus.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Uranus",self)
            self.text.move(300,50)
            self.text.resize(150,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• Uranus is 1,784 million miles away from the Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(360,20)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• It is almost identical or same with Neptune.",self) 
            self.text2.move(300,160)
            self.text2.resize(380,50)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• Uranus has 11 rings made up of dust, ice \n and a bits of rocks.",self)
            self.text3.move(300,220)
            self.text3.resize(370,70)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• Uranus could possible have trillions of \n large diamonds. ",self)
            self.text4.move(300,300)
            self.text4.resize(360,50)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text5 = QLabel("• Uranus is known as the 2nd coldest planet in \n the solar system.",self)
            self.text5.move(300,360)
            self.text5.resize(385,50)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()

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
        self.backbutton = QPushButton('Back',self)
        self.backbutton.setStyleSheet('QPushButton { background-color: transparent }'
                            'QPushButton:hover { background-color: rgb(117, 220, 255) }'
                            'QPushButton:hover { color: black }'
                            'QPushButton:pressed { background-color: rgb(82, 149, 171) }'
                            'QPushButton:pressed { color: black }'
                            'QPushButton { color: white }'
                            'QPushButton { border-style: outset }'
                            'QPushButton { border-width: 1px }'
                            'QPushButton { border-radius: 10px }'
                            'QPushButton { padding: 5px }'
                            'QPushButton { font: bold 9px }')
        self.backbutton.setToolTip("Go back to previous window")
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

        def image():
            self.Image = QLabel(self)
            self.Image.setGeometry(30,80,250,250)
            pixmap = QPixmap('Neptune.png')
            self.Image.setPixmap(pixmap)
            self.Image.setScaledContents(True)
        image()

        def text():
            self.text = QLabel("Neptune",self)
            self.text.move(300,50)
            self.text.resize(150,50)
            self.text.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 30px}')

            self.text1 = QLabel("• Neptune is 2,794 million miles away from the \n Sun.",self)
            self.text1.move(300,130)
            self.text1.resize(380,40)
            self.text1.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text2 = QLabel("• Neptune was discovered in September 23,1846 .",self) 
            self.text2.move(300,160)
            self.text2.resize(390,50)
            self.text2.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text3 = QLabel("• Neptune is the coldest planet in the solar \n system.",self)
            self.text3.move(300,220)
            self.text3.resize(380,70)
            self.text3.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text4 = QLabel("• The gravity of neptune is very similar to the \n Earth. ",self)
            self.text4.move(300,300)
            self.text4.resize(380,50)
            self.text4.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')

            self.text5 = QLabel("• Neptune consists of 'icy' materials such as \n water, ammonia and methane .",self)
            self.text5.move(300,360)
            self.text5.resize(380,60)
            self.text5.setStyleSheet('QLabel { font-family: Comic Sans MS}'
                                'QLabel { background-color: black}'
                                'QLabel { color: white}'
                                'QLabel { font-size: 17px}')
        text()

    @pyqtSlot()

    def back(self):
        WindowNeptune.hide(self)
        self.Window2()

    def Window2(self):
        self.wndw2 = Window2()
        self.wndw2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = SurveyWindow()
    sys.exit(app.exec_())  

