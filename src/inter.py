import sys
from PySide6 import QtCore, QtWidgets, QtGui


class Interface(QtWidgets.QWidget):
    def __init__(self, manager, xml_file):
        super().__init__()

        # File handlers
        self.manager = manager
        self.xml_file = xml_file

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
        self.main_layout = QtWidgets.QVBoxLayout()

        ## Initialize groups ##
        
        # Logo
        pixmap_logo = QtGui.QPixmap('assets/logo.png')
        widget_logo =  QtWidgets.QLabel('logo here')
        widget_logo.setPixmap(pixmap_logo)

        # Select Plaform Area
        platform_layout = QtWidgets.QHBoxLayout()

        group_platform = QtWidgets.QGroupBox("Select Account")
        self.box_accounts = QtWidgets.QComboBox()
        self.box_accounts.addItem('ADD NEW ACCOUNT')
        self.box_accounts.currentIndexChanged.connect(self.on_index_changed)

        add_button = QtWidgets.QPushButton('Add')
        add_button.setFixedWidth(50)
        add_button.clicked.connect(self.action_add)

        delete_button = QtWidgets.QPushButton('Delete')
        delete_button.setFixedWidth(50)
        delete_button.clicked.connect(self.action_delete)

        platform_layout.addWidget(self.box_accounts)
        platform_layout.addWidget(add_button)
        platform_layout.addWidget(delete_button)
        group_platform.setLayout(platform_layout)

        # Add platform entry area
        self.add_platform_layout = QtWidgets.QVBoxLayout()

        self.group_add_platform = QtWidgets.QGroupBox("Enter Platform")
        self.input_platform = QtWidgets.QTextEdit()
        self.input_platform.setFixedHeight(30)

        self.add_platform_layout.addWidget(self.input_platform)
        self.group_add_platform.setLayout(self.add_platform_layout)

        # Enter Credentials Area
        self.credentials_layout = QtWidgets.QVBoxLayout()

        group_credentials = QtWidgets.QGroupBox("Your Username and E-mail")
        self.input_username = QtWidgets.QTextEdit()
        self.input_email = QtWidgets.QTextEdit()
        self.input_username.setFixedHeight(30)
        self.input_email.setFixedHeight(30)

        self.credentials_layout.addWidget(self.input_username)
        self.credentials_layout.addWidget(self.input_email)
        group_credentials.setLayout(self.credentials_layout)

        # Output Password Area
        self.password_layout = QtWidgets.QVBoxLayout()

        group_password = QtWidgets.QGroupBox("Your Password")
        self.input_password = QtWidgets.QTextEdit()

        self.password_layout.addWidget(self.input_password)
        group_password.setLayout(self.password_layout)

        # Configure Layout
        self.main_layout.addWidget(widget_logo)
        self.main_layout.addWidget(group_platform)
        self.main_layout.addWidget(self.group_add_platform)
        self.main_layout.addWidget(group_credentials)
        self.main_layout.addWidget(group_password)
        self.setLayout(self.main_layout)

    def on_index_changed(self, index):
        if index == 0: # ADD NEW ACCOUNT is selected
            self.credentials_layout.removeWidget(self.text_username)
            self.credentials_layout.removeWidget(self.text_email)
            self.password_layout.removeWidget(self.text_password)
            self.text_username.deleteLater()
            self.text_email.deleteLater()
            self.text_password.deleteLater()

            self.input_username = QtWidgets.QTextEdit()
            self.input_email = QtWidgets.QTextEdit()
            self.input_password = QtWidgets.QTextEdit()
            self.input_username.setFixedHeight(30)
            self.input_email.setFixedHeight(30)

            self.credentials_layout.insertWidget(0, self.input_username)
            self.credentials_layout.insertWidget(1, self.input_email)
            self.password_layout.insertWidget(0, self.input_password)

            # add a new platform entry area
            self.add_platform_layout = QtWidgets.QVBoxLayout()

            self.group_add_platform = QtWidgets.QGroupBox("Enter Platform")
            self.input_platform = QtWidgets.QTextEdit()
            self.input_platform.setFixedHeight(30)

            self.add_platform_layout.addWidget(self.input_platform)
            self.group_add_platform.setLayout(self.add_platform_layout)
            self.main_layout.insertWidget(2, self.group_add_platform)
            

        else: # any other option is selected
            self.credentials_layout.removeWidget(self.input_username)
            self.credentials_layout.removeWidget(self.input_email)
            self.password_layout.removeWidget(self.input_password)
            self.input_username.deleteLater()
            self.input_email.deleteLater()
            self.input_password.deleteLater()

            self.main_layout.removeWidget(self.group_add_platform)
            self.group_add_platform.deleteLater()

            self.text_username = QtWidgets.QTextBrowser()
            self.text_email = QtWidgets.QTextBrowser()
            self.text_password = QtWidgets.QTextBrowser()
            self.text_username.setFixedHeight(30)
            self.text_email.setFixedHeight(30)

            self.credentials_layout.insertWidget(0, self.text_username)
            self.credentials_layout.insertWidget(1, self.text_email)
            self.password_layout.insertWidget(0, self.text_password)

    def action_add(self):
        if not self.box_accounts.currentText() == 'ADD NEW ACCOUNT':
            return
        else:
            platform = self.input_platform.toPlainText()
            username = self.input_username.toPlainText()
            email = self.input_email.toPlainText()
            password = self.input_password.toPlainText()
            self.manager.add_account(platform, username, email, password, self.xml_file)
            self.box_accounts.addItem(username)


    def action_delete(self, manager):
        if self.box_accounts.currentText() == 'ADD NEW ACCOUNT':
            return
        else:
            account_to_del = self.box_accounts.currentText()
            index = self.box_accounts.findText(account_to_del)
            self.manager.delete_account(account_to_del, self.xml_file)
            self.box_accounts.removeItem(index)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    interface = Interface()
    interface.show()

    sys.exit(app.exec())
