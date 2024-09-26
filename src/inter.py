import sys
from PySide6 import QtCore, QtWidgets, QtGui

class Interface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Constants
        self.WINDOW_HEIGHT = 600
        self.WINDOW_WIDTH = 400

        self.list_options = ['ADD NEW ACCOUNT',]
        
        # Window Configuration
        self.setWindowTitle('Password Vault')
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # Load stylesheet
        self.load_stylesheet()

        # Initialize UI
        self.initialize_ui()

    def load_stylesheet(self):
        with open('src/style.qss', 'r') as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def initialize_ui(self):
        main_layout = QtWidgets.QVBoxLayout()

        ## Initialize groups ##
        
        # Logo
        pixmap_logo = QtGui.QPixmap('assets/logo.png')
        widget_logo =  QtWidgets.QLabel('logo here')
        widget_logo.setPixmap(pixmap_logo)

        # Select Plaform Area
        platform_layout = QtWidgets.QHBoxLayout()

        group_platform = QtWidgets.QGroupBox("Select Account")
        self.box_platforms = QtWidgets.QComboBox()
        self.box_platforms.addItem('ADD NEW ACCOUNT')

        add_button = QtWidgets.QPushButton('Add')
        add_button.setFixedWidth(50)
        add_button.clicked.connect(self.action_add)

        delete_button = QtWidgets.QPushButton('Delete')
        delete_button.setFixedWidth(50)
        delete_button.clicked.connect(self.action_delete)

        platform_layout.addWidget(self.box_platforms)
        platform_layout.addWidget(add_button)
        platform_layout.addWidget(delete_button)
        group_platform.setLayout(platform_layout)

        # Enter Credentials Area
        credentials_layout = QtWidgets.QVBoxLayout()

        group_credentials = QtWidgets.QGroupBox("Your Username and E-mail")
        text_username = QtWidgets.QTextBrowser()
        text_email = QtWidgets.QTextBrowser()
        text_username.setFixedHeight(30)
        text_email.setFixedHeight(30)

        credentials_layout.addWidget(text_username)
        credentials_layout.addWidget(text_email)
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

    def action_add(self):
        print('add')

    def action_delete(self):
        print('delete')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    interface = Interface()
    interface.show()

    sys.exit(app.exec())
