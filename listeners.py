from qutils import *
from affine import encrypt, decrypt, letter_range, attack
from PyQt5.QtGui import *


def clickCipherListener(form):
    try:
        k1 = int(form.k1Edit.text())
        k2 = int(form.k2Edit.text())
        txt = form.inputEdit.toPlainText()
        text, invm = encrypt(txt, k1, k2)
        #show_info("HINT: inv k1 mod 26 =" + str(invm))
        form.outputEdit.setText(text)
    except Exception as e:
        show_crit(e)

def clickDecipherListener(form):
    try:
        k1 = int(form.k1Edit.text())
        k2 = int(form.k2Edit.text())
        txt = form.inputEdit.toPlainText()
        text = decrypt(txt, k1, k2)
        form.outputEdit.setText(text)
    except Exception as e:
        show_crit(e)

def changeListener(form):
    try:
        form.cipherText.setPlainText(form.inputEdit.toPlainText())
    except Exception as e:
        show_crit(e)

def changeCipherListener(form):
    try:
        text = form.cipherText.toPlainText().upper()
        txt = getLegit(text, letter_range)
        stat = {}
        for c in txt: 
            if c in stat:
                stat[c]+=1
            else:
                stat[c] = 1
        for x in stat:
            stat[x] = stat[x] / len(txt)
        form.statsTable.clear()
        form.statsTable.setRowCount(0)
        form.statsTable.setHorizontalHeaderLabels(['Символ', 'Частота'])
        for el in stat:
            pos = form.statsTable.rowCount()
            form.statsTable.insertRow(pos)
            form.statsTable.setItem(pos, 0, QTableWidgetItem(el))
            form.statsTable.setItem(pos, 1, QTableWidgetItem(str(round(stat[el], 4))))
            form.statsTable.sortItems(1, 1) # По убыванию
    except Exception as e:
        show_crit(e)

def attackButtonListener(form):
    try:
        clf = form.cipherLF.text().upper()
        olf = form.openLF.text().upper()
        cls = form.cipherLS.text().upper()
        ols = form.openLS.text().upper()
        if clf not in letter_range or olf not in letter_range or cls not in letter_range or ols not in letter_range:
            raise Exception("Пожалуйста, заполните все четыре поля для символов")
        c1, p1, c2, p2 = [ord(x) - ord('A') for x in (clf, olf, cls, ols)]
        k1, k2 = attack(c1, p1, c2, p2)
        show_info("Возможные ключи: (k1, k2) = (%d, %d)" % (k1, k2))
        form.findk1.setText(str(k1))
        form.findk2.setText(str(k2))
    except Exception as e:
        show_crit(e)

def clickTranspListener(form):
    try:
        k1 = int(form.findk1.text())
        k2 = int(form.findk2.text())
        txt = form.cipherText.toPlainText().upper()
        text, i = encrypt(txt, k1, k2)
        form.plainTextEdit.setPlainText(text)
    except Exception as e:
        show_crit(e)