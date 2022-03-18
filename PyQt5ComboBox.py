import sys
from PyQt5.QtWidgets import QApplication , QWidget , QComboBox
from PyQt5.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300 , 300)
    
    combo = QComboBox(window)
    combo.resize(100 , 50)
    combo.move(100 , 50)
    
    combo.addItem(QIcon('facebook.png'), 'Facebook')
    combo.addItem(QIcon('whatsapp.jfif'), 'Whatsapp')
    
    combo.addItems([
        'Instagram', 'TikTok'
    ])
    
    window.show()
    
    sys.exit(app.exec_())
    
main()