import sys
from PySide6 import QtWidgets 
from inter import Interface
from filemanager import FileManager

if __name__ == '__main__':
    
    # Start application
    app = QtWidgets.QApplication([])

    interface = Interface()
    interface.show()

    # Load account database
    manager = FileManager()
    manager.load_xml('data/database.xml')

    # Add platforms to combobox
    platforms = []
    for account in manager.accounts_list:
        platforms.append(account['platform'])

    interface.box_platforms.addItems(platforms)



    sys.exit(app.exec())


