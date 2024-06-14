import sys
import os

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QFileDialog
import numpy as np
import cv2

class clsBMPToSTRConverter(QThread):
    finished = Signal()
    signalSaveOutputFile = Signal()

    def __init__(self, input_file_path, parent=None):
        super(clsBMPToSTRConverter, self).__init__(parent)
        #Copy the user input information to the local variables
        self.image_file_path = input_file_path
        self.image_file_directory = os.path.dirname(input_file_path)
        self.byteImageWidth = 0
        self.byteImageHeight = 0

    def run(self):
        self.startConversion()

        self.finished.emit()

    def startConversion(self):
        #Copy the image into a 2D np array
        #Only read the blue channel
        np2DArrayInputImage = cv2.imread(self.image_file_path)[:, :, 0]
        
        #Covert the 2D array into a 1D STR file
        #Find the image dimensions
        imageWidth = np2DArrayInputImage.shape[1]
        imageHeight = np2DArrayInputImage.shape[0]
        #Convert the dimensions into bytes
        self.byteImageWidth = imageWidth.to_bytes(4, byteorder='little')
        self.byteImageHeight = imageHeight.to_bytes(4, byteorder='little')
        #Flattern the 2D image array into a 1D image array
        np1DArrayInputImage = np2DArrayInputImage.flatten()
        np1DArrayIntInputImage = np1DArrayInputImage.astype('uint8')
        #Conver the 1D image array to a byte array
        self.byteArrayInputImage = np1DArrayIntInputImage.tobytes()
        #Emit the singal for saving the file
        self.signalSaveOutputFile.emit()
