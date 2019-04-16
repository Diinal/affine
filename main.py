from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main_ui import Ui_Form
from listeners import clickCipherListener, clickDecipherListener, changeCipherListener, changeListener, clickTranspListener, attackButtonListener
import sys
### MAIN FORM CLASS
class Form(QMainWindow, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.statsTable.setHorizontalHeaderLabels(['Символ', 'Частота'])
        self.show()
        self.add_listeners()
        def add_listeners(self):
            self.ciphButton.clicked.connect(lambda: clickCipherListener(self))
            self.deciphButton.clicked.connect(lambda: clickDecipherListener(self))
            self.inputEdit.textChanged.connect(lambda: changeListener(self))
            self.cipherText.textChanged.connect(lambda: changeCipherListener(self))
            self.transportButt.clicked.connect(lambda: clickTranspListener(self))
            self.attack.clicked.connect(lambda: attackButtonListener(self))

class AppContext(ApplicationContext):
    def run(self):
        # 1. Subclass ApplicationContext
        # 2. Implement run()
        window = Form()
        version = self.build_settings['version']
        window.setWindowTitle('Аффинный шифр')
        window.show()
        return self.app.exec_()
# 3. End run() with this line
if __name__ == '__main__':
    appctxt = AppContext() # 4. Instantiate the subclass
    exit_code = appctxt.run()