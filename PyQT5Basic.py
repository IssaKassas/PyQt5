# importing
from sys import argv , exit
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication , QMainWindow

# creation your own class
class App(QMainWindow): # inheritance
    def __init__(self): # create a constructor
        super().__init__()
        uic.loadUi('designer.ui' , self)

# create a pyqt5 application
app = QApplication(argv) # Tk()

# show your own ui class 
mostafa = App()
mostafa.show()

# exit the application
exit(app.exec_()) # app.mainloop()