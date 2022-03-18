import sys
from datetime import datetime
import calendar
from PyQt5.QtWidgets import QApplication , QWidget , QCalendarWidget
from PyQt5.QtCore import QDate

class CalendarDemo(QWidget):
    global currentMonth , currentYear
    currentMonth = datetime.now().month
    currentYear = datetime.now().year # year == 2022
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calendar Abdelghani')
        self.setGeometry(300 ,300 , 800 , 500)
        self.initUI()
        self.printDate
        

    def initUI(self):
        
        self.calendar = QCalendarWidget(self)
        self.calendar.move(200 , 200)
        self.calendar.setGridVisible(True)
        
        self.calendar.setMinimumDate(QDate(
            currentYear , currentMonth - 1 , 1
        ))
        
        self.calendar.setMaximumDate(QDate(
            currentYear  , currentMonth + 1, calendar.monthrange(currentYear , currentMonth)[1]
        ))
        
        self.calendar.setSelectedDate(QDate(
            currentYear , currentMonth , 1
        ))
        
        self.calendar.clicked.connect(
            self.printDate
        )
    
    def printDate(self , date : QDate):
        print(f"{date.month()}/{date.day()}/{date.year()}") # 5/5/2010
        print(f"Day number of year is {date.dayOfYear()}")
        
if __name__ == '__main__':
    
    root = QApplication(sys.argv)
    
    Calendar = CalendarDemo()
    
    Calendar.show()
    
    sys.exit(root.exec_())
    
