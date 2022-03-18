from sys import argv , exit

from PyQt5.QtWidgets import QApplication , QTableView, QWidget

from PyQt5.QtSql import QSqlDatabase , QSqlQueryModel , QSqlQuery

ServerName = "DESKTOP-MHVCVPT\SQLDATABASE"
DatabaseName = "ArzMusic"
username = ""
password = ""

class DataBase(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Database Musicians')
        self.setGeometry(250 , 250  , 1000 , 500)
    
    def createConnection(self):
        connect = f"DRIVER={{SQL Server}};"\
            f"SERVER={ServerName};"\
                f"DATABASE={DatabaseName}"
                
        global db
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName(connect)
        
        if db.open():
            print("connected to SQL Sever Sucessfully")
            return True
        
        else:
            print('Connection Failed')
            return False
    
    def displayData(self , statement):
        print('processing query')
        query = QSqlQuery(db)
        query.prepare(statement)
        query.exec()
        
        model = QSqlQueryModel()
        model.setQuery(query)
        
        table = QTableView()
        table.setModel(model)
        return table

def main():
    
    app = QApplication(argv)
    data = DataBase()
    
    if data.createConnection():
        sqlStatement = "select * from musicians where gender = 'female'"
        tableView = data.displayData(sqlStatement)
        tableView.show()
    exit(app.exec_())

main()