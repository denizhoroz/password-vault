import sys
from PySide6 import QtWidgets 
from inter import Interface
from filemanager import FileManager

if __name__ == '__main__':
    
    # Load account database
    xml_file = 'data/database.xml'
    manager = FileManager()
    manager.load_xml(xml_file)

    # Start application
    app = QtWidgets.QApplication([])

    interface = Interface(manager, xml_file)
    interface.show()

    # Add platforms to combobox
    platforms = []
    for account in manager.accounts_list:
        platforms.append(account['username'])

    interface.box_accounts.addItems(platforms)


    sys.exit(app.exec())


