import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np 
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Font import font
import xlsxwriter
import xlrd

class WelcomePage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to DataVis!")
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QtGui.QIcon('.\\app_photos\\window_icon.png'))
        self.setStyleSheet("QWidget {background: #505050;}")
        self.infoLabel = QtWidgets.QLabel()
        self.infoLabel.setText("""\n
        Hi there! Welcome to DataVis application.
        There are a few important information you must to know.""")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.infoLabel2 = QtWidgets.QLabel("""\n
        First of all, these are the default settings of the graph you'll create:
                —Line size: 1 inch
                —Line style: Straight Line
                —Marker: False
                —Marker Style: Dotted
                —Grahp size: 9 (horizontal), 6 (vertical) inch.
                —Graph title font size: 14 px
                —Grahp x label font size: 12 px
                —Grahp y label font size: 12 px
        
                You're all free to change them!

        In the second place, there are a few tips to see details
        of operations. For instance, you can see the line styles 
        when you put your mouse onto "See styles."
        In time, you'll see the other tips when you use the application.

        The last thing, If the app. crash just mail me that problem you've experienced.

        See ya!
        E-mail: ethemguener@gmail.com
        Github: ethemguner (yeah, that handsome one)""")
        self.infoLabel2.setAlignment(QtCore.Qt.AlignLeft)

        font.adjust_font(self.infoLabel, "QLabel", "Trebuchet MS", font_size=10,
                        bold=True, italic=True, color="#FFD700")

        font.adjust_font(self.infoLabel2, "QLabel", "Trebuchet MS", font_size=10,
                        bold=True, italic=True, color="#FFFAFA")
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.infoLabel)
        vbox.addWidget(self.infoLabel2)

        hbox = QtWidgets.QHBoxLayout()
        hbox.addLayout(vbox)

        print("running!")
        
        self.setLayout(hbox)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()
        self.centerOnScreen()
        self.importMain()

    def centerOnScreen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))
        print("has run")
    
    def importMain(self):
        import main

app = QtWidgets.QApplication(sys.argv)
window = WelcomePage()
#window.move(400, 80)
#window.setFixedSize(550, 850)
app.setStyle("Fusion")
window.setStyleSheet("Window {background : #505050;}")
sys.exit(app.exec_())