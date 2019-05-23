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
        self.otherSettings()
        
    def otherSettings(self):
        self.loadFile_Button.setFixedWidth(250)
        self.browseData_Button.setFixedWidth(250)
        self.selectColButton.setFixedWidth(140)
        self.browseColumnButton.setFixedWidth(140)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.columnsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.yTitle.setPlaceholderText("for instance: Price")
        self.yTitle.setFixedWidth(250)
        self.xTitle.setPlaceholderText("for instance: Currency")
        self.xTitle.setFixedWidth(250)
        self.graphTitle.setPlaceholderText("the title of graph")
        self.graphTitle.setFixedWidth(250)

    def theme(self):
        font.adjust_font(self.loadFile_Label, "QLabel", "Trebuchet MS", 
                        font_size=14, bold=True, color="#0098FB")

        font.adjust_font(self.loadFile_Button, "QPushButton", "Candara", 
                        font_size=12, bold=True, color="#0098FB", 
                        bg_color="black")

        font.adjust_font(self.browseData_Button, "QPushButton", "Candara", 
                        font_size=12, bold=True, color="#0098FB", 
                        bg_color="black")

        font.adjust_font(self.infoLabel, "QLabel", "Candara", 
                        font_size=12, bold=True, color="black", 
                        bg_color="#5F5F5F")

        font.adjust_font(self.settingsLabel, "QLabel", "Trebuchet MS", 
                        font_size=14, bold=True, color="#0098FB")

        font.adjust_font(self.timeSeriesRB, "QRadioButton", "Trebuchet MS", 
                        font_size=11, color="#FFBD06")

        font.adjust_font(self.barChartRB, "QRadioButton", "Trebuchet MS", 
                        font_size=11, color="#FFBD06")

        font.adjust_font(self.lineChartRB, "QRadioButton", "Trebuchet MS", 
                        font_size=11, color="#FFBD06")

        font.adjust_font(self.trendCheckBox, "QCheckBox", "Trebuchet MS", 
                        font_size=11, color="#FFBD06")

        font.adjust_font(self.yTitleLabel, "QLabel", "Candara", 
                        font_size=12, color="#3685FA")

        font.adjust_font(self.xTitleLabel, "QLabel", "Candara", 
                        font_size=12, color="#3685FA")

        font.adjust_font(self.graphTitleLabel, "QLabel", "Candara", 
                        font_size=12, color="#3685FA")

        font.adjust_font(self.graphTitle, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.xTitle, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.yTitle, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.dataSettingsLabel, "QLabel", "Trebuchet MS", 
                        font_size=14, bold=True, color="#0098FB")

        font.adjust_font(self.columns, "QListWidget", "Trebuchet MS", 
                        font_size=12, bold=True, color="#FFBD06", bg_color="#5F5F5F")

        font.adjust_font(self.columnsLabel, "QLabel", "Candara", 
                        font_size=13, color="#DADADA")

        font.adjust_font(self.selectColButton, "QPushButton", "Candara", 
                        font_size=12, bold=True, color="#0098FB", 
                        bg_color="black")

        font.adjust_font(self.browseColumnButton, "QPushButton", "Candara", 
                        font_size=12, bold=True, color="#0098FB", 
                        bg_color="black")
    def ui(self):
        #Empty Label
        self.emptyLabel         = QtWidgets.QLabel("")

        #FILE SECTION.
        self.loadFile_Label     = QtWidgets.QLabel("FILE")
        self.loadFile_Button    = QtWidgets.QPushButton("Load File")
        self.browseData_Button  = QtWidgets.QPushButton("Browse Data")
        self.infoLabel          = QtWidgets.QLabel("No data loaded.")

        #GRAPH SETTINGS
        self.settingsLabel      = QtWidgets.QLabel("\nGRAPH SETTINGS")
        self.timeSeriesRB       = QtWidgets.QRadioButton("Time Series")
        self.barChartRB         = QtWidgets.QRadioButton("Bar chart")
        self.lineChartRB        = QtWidgets.QRadioButton("Line Chart")
        self.trendCheckBox      = QtWidgets.QCheckBox("Show Trend")
        self.yTitleLabel        = QtWidgets.QLabel("Title of y Line\t")
        self.xTitleLabel        = QtWidgets.QLabel("Title of x Line\t")
        self.graphTitleLabel    = QtWidgets.QLabel("Title of Graph\t")
        self.yTitle             = QtWidgets.QLineEdit()
        self.xTitle             = QtWidgets.QLineEdit()
        self.graphTitle         = QtWidgets.QLineEdit()

        #DATA SETTINGS
        self.dataSettingsLabel  = QtWidgets.QLabel("\nDATA SETTINGS")
        self.columns            = QtWidgets.QListWidget()
        self.columnsLabel       = QtWidgets.QLabel("Columns of Data")
        self.selectColButton    = QtWidgets.QPushButton("Select Column")
        self.browseColumnButton = QtWidgets.QPushButton("Browse Column")
        
        vbox           = QtWidgets.QVBoxLayout()
        hbox           = QtWidgets.QHBoxLayout()
        buttonsLayout  = QtWidgets.QHBoxLayout()
        infoHLayout    = QtWidgets.QHBoxLayout()
        settingHBox    = QtWidgets.QHBoxLayout()
        rbHBox         = QtWidgets.QHBoxLayout()
        yTitlesHBox    = QtWidgets.QHBoxLayout()
        xTitlesHBox    = QtWidgets.QHBoxLayout()
        titleGraphHBox = QtWidgets.QHBoxLayout()
        emptyHBox      = QtWidgets.QHBoxLayout()
        dataSettHBox   = QtWidgets.QHBoxLayout()
        dataColLabHBox = QtWidgets.QHBoxLayout()
        columnListHBox = QtWidgets.QHBoxLayout()
        buttonHBox     = QtWidgets.QHBoxLayout()

        vbox.addWidget(self.loadFile_Label)
        buttonsLayout.addWidget(self.loadFile_Button)
        buttonsLayout.addWidget(self.browseData_Button)
        infoHLayout.addWidget(self.infoLabel)
        settingHBox.addWidget(self.settingsLabel)
        rbHBox.addWidget(self.timeSeriesRB)
        rbHBox.addWidget(self.barChartRB)
        rbHBox.addWidget(self.lineChartRB)
        rbHBox.addWidget(self.trendCheckBox)
        emptyHBox.addWidget(self.emptyLabel)
        xTitlesHBox.addWidget(self.xTitleLabel)
        xTitlesHBox.addWidget(self.xTitle)
        yTitlesHBox.addWidget(self.yTitleLabel)
        yTitlesHBox.addWidget(self.yTitle)
        titleGraphHBox.addWidget(self.graphTitleLabel)
        titleGraphHBox.addWidget(self.graphTitle)
        dataSettHBox.addWidget(self.dataSettingsLabel)
        dataColLabHBox.addWidget(self.columnsLabel)
        columnListHBox.addWidget(self.columns)
        buttonHBox.addWidget(self.selectColButton)
        buttonHBox.addWidget(self.browseColumnButton)
        
        vbox.addLayout(buttonsLayout)
        vbox.addLayout(infoHLayout)
        vbox.addLayout(settingHBox)
        vbox.addLayout(rbHBox)
        vbox.addLayout(emptyHBox)
        vbox.addLayout(xTitlesHBox)
        vbox.addLayout(yTitlesHBox)
        vbox.addLayout(titleGraphHBox)
        vbox.addLayout(dataSettHBox)
        vbox.addLayout(dataColLabHBox)
        vbox.addLayout(columnListHBox)
        vbox.addLayout(buttonHBox)
        vbox.addStretch()

        hbox.addStretch()
        hbox.addLayout(vbox)
        hbox.addStretch()

        self.setLayout(hbox)
        self.show()
        self.loadFile_Button.clicked.connect(self.loadProcess)
        self.browseData_Button.clicked.connect(self.dataBrowse)
        self.selectColButton.clicked.connect(self.columnSelector)
        self.browseColumnButton.clicked.connect(self.columnBrowse)
        self.SELECTED_COLUMNS = []

    def loadProcess(self):
        fileDialog = QtWidgets.QFileDialog()
        self.fName = fileDialog.getOpenFileName(None,'Load File')

        try:
            if self.fName[0]:
                data = pd.read_excel(self.fName[0])
                self.mainDF = pd.DataFrame(data)
                self.successfulLoad()
                self.listColumns()
        except:
            self.failureLoad()
    
    def listColumns(self):
        self.columns.clear()
        for column in list(self.mainDF.columns):
            self.columns.addItem(column)

    def columnSelector(self):
        self.CURRENT_COLUMN = self.columns.currentItem().text()
        self.SELECTED_COLUMNS.append(self.CURRENT_COLUMN)

        print("Current selected columns: ", self.SELECTED_COLUMNS)

    def successfulLoad(self):
        spliting_list = self.fName[0].split("/")
        loadedFileName = spliting_list[len(spliting_list)-1]
        self.infoLabel.setText("{} loaded successfully!".format(loadedFileName) )
        font.adjust_font(self.infoLabel, "QLabel", 
                        "Candara", font_size=12, 
                        bold=True, color="#00FF66", 
                        bg_color="#5F5F5F")

    def failureLoad(self):
        try:
            spliting_list = self.fName[0].split("/")
            loadedFileName = spliting_list[len(spliting_list)-1]
            self.infoLabel.setText("FAILED! {} couldn't load.".format(loadedFileName) )
            font.adjust_font(self.infoLabel, "QLabel", 
                            "Candara", font_size=12, 
                            bold=True, color="#FF0000", 
                            bg_color="#5F5F5F")
        except AttributeError:
            self.failureBrowse()

    def failureBrowse(self):
        self.infoLabel.setText("There isn't any loaded data to browse.")
        font.adjust_font(self.infoLabel, "QLabel", 
                        "Candara", font_size=12, 
                        bold=True, color="#FF0000", 
                        bg_color="#5F5F5F")

    def dataBrowse(self):
        try:
            self.isItSingleColumn = False
            self.openPage = DataBrowser(self.mainDF, self.isItSingleColumn)
        except AttributeError:
            self.failureLoad()

    def columnBrowse(self):
        try:
            self.isItSingleColumn = True
            self.singleColumn = self.mainDF['{}'.format(self.columns.currentItem().text() )]
            self.openPage = DataBrowser(self.singleColumn, self.isItSingleColumn)
        except AttributeError:
            self.failureLoad()

class DataBrowser(QtWidgets.QWidget):
    def __init__(self, df, condition):
        super().__init__()
        self.setWindowTitle("Data Browser")
        self.init_ui()
        self.setTable(df, condition)

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

    def setTable(self, df, condition):
        print(condition)
        if condition == False:
            self.df_row = df.shape[0]
            self.df_col = df.shape[1]

            self.dataTable.setRowCount(self.df_row)
            self.dataTable.setColumnCount(self.df_col)

            for rowIndex in range(0, self.df_row):
                for colIndex in range(0, self.df_col):
                    cell = df.iat[rowIndex,colIndex]
                    self.dataTable.setItem(rowIndex,colIndex, QtWidgets.QTableWidgetItem(str(cell)))
        else:
            self.df_row = df.shape[0]

            self.dataTable.setRowCount(self.df_row)
            self.dataTable.setColumnCount(1)

            for rowIndex in range(0, self.df_row):
                cell = df.iat[rowIndex]
                self.dataTable.setItem(rowIndex,0, QtWidgets.QTableWidgetItem(str(cell)))

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.move(400, 120)
window.setFixedSize(550, 850)
app.setStyle("Fusion")
window.setStyleSheet("Window {background : #505050;}")
sys.exit(app.exec_())

