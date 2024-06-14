import sys
import os

from PySide6.QtCore import QThread, Qt, Slot
from PySide6.QtWidgets import QFileDialog, QApplication, QWidget
from BMPToSTRUI.ui_form import Ui_Widget
from Processing.Processing import clsBMPToSTRConverter

from pathlib import Path

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Initialise the file path parameters
        self.input_file_path = ""
        self.input_folder_path = ""
        self.output_file_path = ""
        #Initialise the UI
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #Disable the Start conversion button until an input image file has been selected.
        self.ui.pushButtonStartConversion.setEnabled(False)
        #Select the input image file
        self.ui.pushButtonInputImageFile.clicked.connect(self.openInputBMPFile)
        #Start conversion
        self.ui.pushButtonStartConversion.clicked.connect(self.startConversion)

    #Find the input BMP file
    def openInputBMPFile(self):
        #Record the file location
        tupleFName = QFileDialog.getOpenFileName(self, "Select the input image file", os.getcwd(), "Image files (*.bmp)")
        local_bmp_file_path = tupleFName[0]
        
        #Report back
        self.ui.lineEdit_InputFileLocation.clear()
        self.ui.lineEdit_InputFileLocation.setText(local_bmp_file_path)
        self.input_file_path = local_bmp_file_path
        self.input_folder_path = os.path.dirname(os.path.abspath(local_bmp_file_path))
        
        #Enable the Start conversion button
        if (self.input_file_path != ""):
            self.ui.pushButtonStartConversion.setEnabled(True)
    
    #Save the output STR file
    @Slot()
    def saveOutputFile(self):
        #Record the output file name
        tupleSaveFName = QFileDialog.getSaveFileName(self, "Input the output file name", self.input_folder_path, "STR files (*.str)")
        #Report it back
        self.output_file_path = tupleSaveFName[0]
        #Output the file
        f = open(self.output_file_path, 'wb')
        f.write(self.newConversion.byteImageWidth)
        f.write(self.newConversion.byteImageHeight)
        f.write(self.newConversion.byteArrayInputImage)
        f.close
    
    #Start conversion and save the output STR file
    def startConversion(self):
        #Start conversion
        #Create a new object
        self.newConversion = clsBMPToSTRConverter(self.input_file_path)

        #Create a QThread object
        self.thread = QThread()
        #Move the process to the thread
        self.newConversion.moveToThread(self.thread)
        #Connect the start signal to the function
        self.thread.started.connect(self.newConversion.run)
        #Start the thread
        self.thread.start()
        #Connect signals to slots
        #Save the output file
        self.newConversion.signalSaveOutputFile.connect(self.saveOutputFile) 
        #When the conversion is finished.
        self.newConversion.finished.connect(self.thread.quit)
        self.newConversion.finished.connect(self.newConversion.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        #Set up the UI during the conversion
        self.ui.pushButtonStartConversion.setEnabled(False)
        self.ui.pushButtonStartConversion.setText("Under conversion!")
        self.thread.finished.connect(
            lambda: self.ui.pushButtonStartConversion.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.ui.pushButtonStartConversion.setText("Conversion finished. Click for the next conversion!")
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Widget()#
    widget.show()

    sys.exit(app.exec())