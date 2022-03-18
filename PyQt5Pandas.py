# importing
import sys
from PyQt5.QtWidgets import QApplication , QTableView
from PyQt5.QtCore import QAbstractTableModel , QModelIndex , Qt
from pandas import DataFrame

# create a dataframe
df = DataFrame({
    "names": ["Abdelghani" , "Riwa" , "Nour" , "Mohamad"],
    "ages" : [20 , 20 , 25 , 17],
    "grades" : [12 , 13 , 20 , 20]
})

# creation your own class
class DataFrameModel(QAbstractTableModel):
    def __init__(self , data : DataFrame):
        QAbstractTableModel.__init__(self)
        self._data = data
        
    # interface method not implemented
    def rowCount(self , parent = None): # returns the number of rows
        return self._data.shape[0]
    
    def columnCount(self , parent = None): # returns the number of columns
        return self._data.shape[1]
    
    def data(self, index: QModelIndex, role: int):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row() , index.column()])
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int ):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self._data.columns[section]

# create a pyqt5 application
app = QApplication(sys.argv)
data = DataFrameModel(df)
view = QTableView()
view.setModel(data)
view.resize(750 , 500)

# show your own ui class 
view.show()

# exit the application
sys.exit(app.exec_())