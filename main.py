import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from Font import font
import xlsxwriter
import xlrd

class Window (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        self.theme()
    def theme(self):
        font.adjust_font(self.loadFile_Label, "QLabel", "Trebuchet MS", font_size=14, bold=True, color="#0098FB")

        font.adjust_font(self.loadFile_Button, "QPushButton", "Trebuchet MS", font_size=12, 
                        bold=True, color="#0098FB", bg_color="black")

        font.adjust_font(self.browseData_Button, "QPushButton", "Trebuchet MS", font_size=12, 
                        bold=True, color="#0098FB", bg_color="black")
                        
    def ui(self):
        self.loadFile_Label     = QtWidgets.QLabel("FILE:  ")
        self.loadFile_Button    = QtWidgets.QPushButton("Load Data")
        self.browseData_Button  = QtWidgets.QPushButton("Browse Data")
        
        vbox        = QtWidgets.QVBoxLayout()
        file_hbox   = QtWidgets.QHBoxLayout()
    
        file_hbox.addWidget(self.loadFile_Label)
        file_hbox.addWidget(self.loadFile_Button)
        file_hbox.addWidget(self.browseData_Button)
        
        vbox.addLayout(file_hbox)
        file_hbox.addStretch()
        vbox.addStretch()

        self.setLayout(vbox)
        self.show()
        self.loadFile_Button.clicked.connect(self.loadProcess)
        self.browseData_Button.clicked.connect(self.openPage2)

    def loadProcess(self):
        fileDialog = QtWidgets.QFileDialog()
        fName = fileDialog.getOpenFileName(None,'Load File')

        if fName[0]:
            data = pd.read_excel(fName[0])
            self.df = pd.DataFrame(data)
        else:
            print("file couldn't read.")

    def openPage2(self):
        self.openPage = DataBrowser(self.df)

class DataBrowser(QtWidgets.QWidget):
    def __init__(self, df):
        super().__init__()
        self.setWindowTitle("Data Browser")
        self.init_ui()
        self.setTable(df)

    def init_ui(self):
        self.dataTable = QtWidgets.QTableWidget()
        font.adjust_font(self.dataTable, "QTableWidget", "Trebuchet MS", 14, 
                        bold=True, color="#0098FB", bg_color="#505050")
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()

        vbox.addWidget(self.dataTable)

        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.show()

    def setTable(self, df):

        self.df_row = df.shape[0]
        self.df_col = df.shape[1]

        self.dataTable.setRowCount(self.df_row)
        self.dataTable.setColumnCount(self.df_col)

        for rowIndex in range(0, self.df_row):
            for colIndex in range(0, self.df_col):
                cell = df.iat[rowIndex,colIndex]
                self.dataTable.setItem(rowIndex,colIndex, QtWidgets.QTableWidgetItem(str(cell)))

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.move(200, 120)
window.setFixedSize(500, 700)
app.setStyle("Fusion")
window.setStyleSheet("Window {background : #505050;}")
sys.exit(app.exec_())

