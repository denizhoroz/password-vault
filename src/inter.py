import sys
from PySide6 import QtCore, QtWidgets, QtGui

class Interface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Constants
        self.WINDOW_HEIGHT = 600
        self.WINDOW_WIDTH = 400
        
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # Initialize UI
        self.initialize_ui()

    def initialize_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

        ## Initialize groups ##
        
        # Logo
        #pixmap_logo = QtGui.QPixmap()
        widget_logo =  QtWidgets.QLabel('logo here')

        # Select Plaform Area
        platform_layout = QtWidgets.QVBoxLayout()

        group_platform = QtWidgets.QGroupBox("Select Plaform")
        box_platforms = QtWidgets.QComboBox()

        platform_layout.addWidget(box_platforms)
        group_platform.setLayout(platform_layout)

        # Enter Credentials Area
        credentials_layout = QtWidgets.QVBoxLayout()

        group_credentials = QtWidgets.QGroupBox("Enter Your Username or E-mail")
        text_credentials = QtWidgets.QTextEdit()

        credentials_layout.addWidget(text_credentials)
        group_credentials.setLayout(credentials_layout)

        # Output Password Area
        password_layout = QtWidgets.QVBoxLayout()

        group_password = QtWidgets.QGroupBox("Your Password")
        text_password = QtWidgets.QTextBrowser()

        password_layout.addWidget(text_password)
        group_password.setLayout(password_layout)

        
        # Configure Layout
        main_layout.addWidget(widget_logo)
        main_layout.addWidget(group_platform)
        main_layout.addWidget(group_credentials)
        main_layout.addWidget(group_password)
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    interface = Interface()
    interface.show()

    sys.exit(app.exec())
