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
        self.enabledWidgets()
        self.SELECTED_COLUMNS = []
        self.MULTIPLE_COLUMNS = []
        plt.style.use('ggplot')
    
    def enabledWidgets(self):
        self.multipleColumnCB.setEnabled(False)

        font.adjust_font(self.multipleColumnCB, "QCheckBox", "Trebuchet MS", 
                        font_size=11, color="#908F8F")
        
    def otherSettings(self):
        self.loadFile_Button.setFixedWidth(250)
        self.browseData_Button.setFixedWidth(250)
        self.selectColButton.setFixedWidth(140)
        self.browseColumnButton.setFixedWidth(140)
        self.clearSelectedButt.setFixedWidth(140)
        self.printGraph.setFixedWidth(140)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.columnsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.yTitle.setPlaceholderText("for instance: Price")
        self.yTitle.setFixedWidth(250)
        self.xTitle.setPlaceholderText("for instance: Currency")
        self.xTitle.setFixedWidth(250)
        self.graphTitle.setPlaceholderText("the title of graph")
        self.graphTitle.setFixedWidth(250)
        self.figSizeX.setPlaceholderText("inch type")
        self.figSizeX.setFixedWidth(250)
        self.figSizeY.setPlaceholderText("inch type")
        self.figSizeY.setFixedWidth(250)

        self.rbGroup.addButton(self.timeSeriesRB)
        self.rbGroup.addButton(self.barChartRB)
        self.rbGroup.addButton(self.lineChartRB)


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
        self.figSizeLabelX      = QtWidgets.QLabel("Fig. size horizontal")
        self.figSizeLabelY      = QtWidgets.QLabel("Fig. size vertical")
        self.figSizeX           = QtWidgets.QLineEdit()
        self.figSizeY           = QtWidgets.QLineEdit()
        self.rbGroup            = QtWidgets.QButtonGroup()


        #DATA SETTINGS
        self.dataSettingsLabel  = QtWidgets.QLabel("\nDATA SETTINGS")
        self.columns            = QtWidgets.QListWidget()
        self.multipleColumnCB   = QtWidgets.QCheckBox("Multiple Column")
        self.columnsLabel       = QtWidgets.QLabel("Columns of Data")
        self.selectColButton    = QtWidgets.QPushButton("Select Column")
        self.browseColumnButton = QtWidgets.QPushButton("Browse Column")
        self.clearSelectedButt  = QtWidgets.QPushButton("Clear Selected Data")

        #PRINT GRAPH
        self.printGraph         = QtWidgets.QPushButton("Create Graph")
        
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
        figSizeXHBox   = QtWidgets.QHBoxLayout()
        figSizeYHBox   = QtWidgets.QHBoxLayout()
        lineRBHBox     = QtWidgets.QHBoxLayout()
        printGraphHBox = QtWidgets.QHBoxLayout()

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
        figSizeXHBox.addWidget(self.figSizeLabelX)
        figSizeXHBox.addWidget(self.figSizeX)
        figSizeYHBox.addWidget(self.figSizeLabelY)
        figSizeYHBox.addWidget(self.figSizeY)
        dataSettHBox.addWidget(self.dataSettingsLabel)
        lineRBHBox.addWidget(self.multipleColumnCB)
        dataColLabHBox.addWidget(self.columnsLabel)
        columnListHBox.addWidget(self.columns)
        buttonHBox.addWidget(self.selectColButton)
        buttonHBox.addWidget(self.browseColumnButton)
        buttonHBox.addWidget(self.clearSelectedButt)
        printGraphHBox.addWidget(self.printGraph)
        
        vbox.addLayout(buttonsLayout)
        vbox.addLayout(infoHLayout)
        vbox.addLayout(settingHBox)
        vbox.addLayout(rbHBox)
        vbox.addLayout(emptyHBox)
        vbox.addLayout(xTitlesHBox)
        vbox.addLayout(yTitlesHBox)
        vbox.addLayout(titleGraphHBox)
        vbox.addLayout(figSizeXHBox)
        vbox.addLayout(figSizeYHBox)
        vbox.addLayout(dataSettHBox)
        vbox.addLayout(lineRBHBox)
        vbox.addLayout(dataColLabHBox)
        vbox.addLayout(columnListHBox)
        vbox.addLayout(buttonHBox)
        vbox.addLayout(printGraphHBox)
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
        self.printGraph.clicked.connect(self.graphType)
        self.clearSelectedButt.clicked.connect(self.clearSelections)
        self.lineChartRB.toggled.connect(self.enableLineChartSelections)
    
    def enableLineChartSelections(self):
        if self.lineChartRB.isChecked() == True:
            self.multipleColumnCB.setEnabled(True)

            font.adjust_font(self.multipleColumnCB, "QCheckBox", "Trebuchet MS", 
                            font_size=11, color="#FFBD06")
        
        elif self.lineChartRB.isChecked() == False:
            self.multipleColumnCB.setEnabled(False)

            font.adjust_font(self.multipleColumnCB, "QCheckBox", "Trebuchet MS", 
                            font_size=11, color="#908F8F")

    def clearSelections(self):
        self.CURRENT_COLUMN = None
        self.SELECTED_COLUMNS.clear()
        self.MULTIPLE_COLUMNS.clear()
        self.MULTIPLE_X = None
        self.singleColumn = None
        self.MULTIPLE_CHOICE = None
        self.columns.setEnabled(True)
        font.adjust_font(self.columns, "QListWidget", "Trebuchet MS", 
                        font_size=12, bold=True, color="#FFBD06", bg_color="#5F5F5F")
        self.multipleColumnCB.setChecked(False)

        self.infoLabel.setText("All variables have cleared successfuly!")
        font.adjust_font(self.infoLabel, "QLabel", 
                        "Franklin Gothic Book", font_size=12, color="#FFB200", 
                        bg_color="#5F5F5F")

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

        self.singleColumn = self.mainDF['{}'.format(self.CURRENT_COLUMN)]
        self.definingData()

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
    
    def definingData(self):

        if self.multipleColumnCB.isChecked() == False:
            self.MULTIPLE_CHOICE = False

            self.singleColumn = self.mainDF['{}'.format(self.columns.currentItem().text() )]
            self.X = self.singleColumn

            self.columns.setEnabled(False)
            font.adjust_font(self.columns, "QListWidget", "Trebuchet MS", 
                            font_size=12, bold=True, color="#B4B4B4", bg_color="#5F5F5F")
    
            self.infoLabel.setText("Selected column: {}".format(self.columns.currentItem().text()) )
            font.adjust_font(self.infoLabel, "QLabel", 
                            "Franklin Gothic Book", font_size=12, color="#FFB200", 
                            bg_color="#5F5F5F")

        elif self.multipleColumnCB.isChecked() == True:
            self.MULTIPLE_CHOICE = True
            self.MULTIPLE_COLUMNS.append(self.columns.currentItem().text() )

            self.columns.setEnabled(True)
            font.adjust_font(self.columns, "QListWidget", "Trebuchet MS", 
                            font_size=12, bold=True, color="#FFBD06", bg_color="#5F5F5F")

            self.infoLabel.setText("Selected columns: {}".format(self.MULTIPLE_COLUMNS) )
            font.adjust_font(self.infoLabel, "QLabel", 
                            "Franklin Gothic Book", font_size=12, color="#FFB200", 
                            bg_color="#5F5F5F")

    def graphType(self):
        if self.timeSeriesRB.isChecked() == True:
            self.timeSeriesGraph()
        elif self.barChartRB.isChecked() == True:
            self.barGraph()
        elif self.lineChartRB.isChecked() == True:
            self.lineGraph()
        else:
            print("it was at this moment, he knew, he fucked up (graph type)")

    def timeSeriesGraph(self):
        data = pd.read_excel(self.fName[0],index_col='Date',parse_dates=True)
        data[self.columns.currentItem().text()].plot()
        plt.show()

    def lineGraph(self):
        if self.MULTIPLE_CHOICE == False:
            try:
                fig_lineGraph = plt.figure(figsize=(float(self.figSizeX.text() ), 
                                            float(self.figSizeY.text()) ), 
                                            dpi=100)
                axes = fig_lineGraph.add_axes([0.1, 0.1, 0.8, 0.8])
                axes.plot(self.X)
                axes.set_xlabel(str(self.xTitle.text() ))
                axes.set_ylabel(str(self.yTitle.text() ))
                axes.set_title(str(self.graphTitle.text() ))
                axes.grid(True)
                plt.show()
                
            except ValueError:
                fig_lineGraph = plt.figure()
                axes = fig_lineGraph.add_axes([0.1, 0.1, 0.8, 0.8])
                axes.plot(self.X)
                axes.grid(True)
                plt.show()

        elif self.MULTIPLE_CHOICE == True:
            try:
                fig_lineGraph = plt.figure(figsize=(float(self.figSizeX.text() ), 
                                            float(self.figSizeY.text()) ), 
                                            dpi=100)

                axes = fig_lineGraph.add_axes([0.1, 0.1, 0.8, 0.8])

                for i in range(0, len(self.MULTIPLE_COLUMNS)):
                    axes.plot(self.mainDF[self.MULTIPLE_COLUMNS[i]], label=self.MULTIPLE_COLUMNS[i])

                axes.set_xlabel(str(self.xTitle.text() ))
                axes.set_ylabel(str(self.yTitle.text() ))
                axes.set_title(str(self.graphTitle.text() ))

                axes.grid(True)
                axes.legend()
                plt.show()

            except ValueError:
                fig_lineGraph = plt.figure()

                axes = fig_lineGraph.add_axes([0.1, 0.1, 0.8, 0.8])

                for i in range(0, len(self.MULTIPLE_COLUMNS)):
                    axes.plot(self.mainDF[self.MULTIPLE_COLUMNS[i]], label=self.MULTIPLE_COLUMNS[i])

                axes.grid(True)
                axes.legend()
                plt.show()

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

        font.adjust_font(self.figSizeLabelX, "QLabel", "Candara", 
                        font_size=12, color="#3685FA")

        font.adjust_font(self.figSizeLabelY, "QLabel", "Candara", 
                        font_size=12, color="#3685FA")

        font.adjust_font(self.graphTitle, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.xTitle, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.yTitle, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.figSizeX, "QLineEdit", "Trebuchet MS", 
                        font_size=10, color="#000000", bg_color="#9E9E9E")

        font.adjust_font(self.figSizeY, "QLineEdit", "Trebuchet MS", 
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

        font.adjust_font(self.clearSelectedButt, "QPushButton", "Candara", 
                        font_size=12, bold=True, color="#0098FB", 
                        bg_color="black")

        font.adjust_font(self.printGraph, "QPushButton", "Candara", 
                        font_size=12, bold=True, color="#0098FB", 
                        bg_color="black")
            
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

