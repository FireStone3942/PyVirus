
# importing the required libraries
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
 
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.acceptDrops()
        # set the title
        self.setWindowTitle("Image")
 
        # creating label
        self.label = QLabel(self)
         
        # loading image
        self.pixmap = QPixmap('image.jpg')
 
        # adding image to label
        self.label.setPixmap(self.pixmap)
 
        self.pixmap.move(900, 800)
        # show all the widgets
        self.showFullScreen()
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())