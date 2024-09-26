import xml.dom.minidom

class FileManager:
    def load_xml(self, xmlfile):
        # Load file
        self.domtree = xml.dom.minidom.parse(xmlfile)
        self.group = self.domtree.documentElement
        self.accounts = self.group.getElementsByTagName('account')
        self.ids = []

        # Load Attributes
        self.accounts_list = []
        for account in self.accounts:
            account_info = {}
            
            account_info['id'] = account.getAttribute('id')
            self.ids.append(account_info['id'])
            account_info['platform'] = account.getElementsByTagName('platform')[0].childNodes[0].nodeValue
            account_info['username'] = account.getElementsByTagName('username')[0].childNodes[0].nodeValue
            account_info['email'] = account.getElementsByTagName('email')[0].childNodes[0].nodeValue
            account_info['password'] = account.getElementsByTagName('password')[0].childNodes[0].nodeValue

            self.accounts_list.append(account_info)
        
    def add_account(self, platform, username, email, password, xml_file):
        new_account = self.domtree.createElement('account')
        new_id = str(self.create_id())
        new_account.setAttribute('id', new_id)

        element_platform = self.domtree.createElement('platform')
        element_platform.appendChild(self.domtree.createTextNode(platform))
        element_username = self.domtree.createElement('username')
        element_username.appendChild(self.domtree.createTextNode(username))
        element_email = self.domtree.createElement('email')
        element_email.appendChild(self.domtree.createTextNode(email))
        element_password = self.domtree.createElement('password')
        element_password.appendChild(self.domtree.createTextNode(password))

        new_account.appendChild(element_platform)
        new_account.appendChild(element_username)
        new_account.appendChild(element_email)
        new_account.appendChild(element_password)

        self.group.appendChild(new_account)

        self.domtree.writexml(open(xml_file, 'w'))

    def create_id(self):
        new_id = 1
        while str(new_id) in self.ids:
            new_id += 1
        return new_id


if __name__ == '__main__':
    manager = FileManager()

    xml_file = 'data/database.xml'
    print(manager.accounts_list)