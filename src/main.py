import sys
from PySide6 import QtWidgets 
from inter import Interface

if __name__ == '__main__':
    
    # Start application
    app = QtWidgets.QApplication([])

    interface = Interface()
    interface.show()

    # Load account database
    accounts = ['jahbook', 'jahstagram']

    interface.box_platforms.addItems(accounts)



    sys.exit(app.exec())


