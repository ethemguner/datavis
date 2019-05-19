from PyQt5 import QtGui

def adjust_font(widget, widget_type, font_type="Arial", font_size=10, bold=False, 
                italic= False, color="black", bg_color="transparent"):


    if bold == False and italic == True:
        print("11")
        FONT = QtGui.QFont(font_type, font_size)
        widget.setStyleSheet(widget_type + "{color: " + color + ";" + 
                            "background: " + bg_color + ";" + 
                            "font: italic;}")
        widget.setFont(FONT)

    elif bold == True and italic == False:
        print("22")
        FONT = QtGui.QFont(font_type, font_size)
        widget.setStyleSheet(widget_type + "{color: " + color + ";" + 
                            "background: " + bg_color + ";" + 
                            "font: bold;}")
        widget.setFont(FONT)

    elif bold == True and italic == True:
        print("33")
        FONT = QtGui.QFont(font_type, font_size, QtGui.QFont.Bold)
        widget.setStyleSheet(widget_type + "{color: " + color + ";" + 
                            "background: " + bg_color + ";" + 
                            "font: italic;}")
        widget.setFont(FONT)
        
    else:
        FONT = QtGui.QFont(font_type, font_size, QtGui.QFont.Normal)
        widget.setStyleSheet(widget_type + "{color: " + color + ";" + 
                            "background: " + bg_color + ";}")
        widget.setFont(FONT)
