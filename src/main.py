import sys
from PySide6 import QtWidgets 
from inter import Interface

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    interface = Interface()
    interface.show()

    sys.exit(app.exec())


