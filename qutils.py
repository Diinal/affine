from PyQt5.QtWidgets import *


def show_info(msg):
    w = QWidget()
    z = QMessageBox.information(w, 'Информация!', str(msg))
    w.show()

def show_crit(msg):
    w = QWidget()
    z = QMessageBox.critical(w, 'Ошибка!', str(msg))
    w.show()

def getLegit(text, _range):
    txt = ''
    for t in text:
        if t in _range:
            txt+=t
    return txt