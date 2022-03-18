# PyQt5 Progress bar combobox
# oop class object ,....

from PyQt5.QtWidgets import QApplication , QWidget , QProgressBar , QPushButton
from PyQt5.QtCore import QBasicTimer
import sys

class progressBar(QWidget):
    def __init__(self):
        super().__init__()
        # creation a progress
        self.progress = QProgressBar(self)
        self.progress.setGeometry(50 , 50 , 400 , 20)
        
        # creation start button
        self.btn = QPushButton('Start' , self)
        self.btn.move(100 , 80)
        self.btn.clicked.connect(self.startProgress)
        
        # creation reset button
        self.reset = QPushButton('Reset' , self)
        self.reset.move(300 , 80)
        self.reset.clicked.connect(self.resetProgress)
        
        # creation a timer
        self.timer = QBasicTimer()
        self.step = 0

    def startProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Continue')
        else:
            self.timer.start(100 , self)
            self.btn.setText("Pause")
    
    def resetProgress(self):
        self.step = 0
        self.progress.setValue(self.step)
    
    def timerEvent(self , event):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Continue')
            return
        self.step += 1
        self.progress.setValue(self.step)
        
# def main():
#     app = QApplication(sys.argv)

#     progress = progressBar()
#     progress.show()

#     sys.exit(app.exec_())
    
# main()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    progress = progressBar()
    progress.show()

    sys.exit(app.exec_())