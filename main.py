from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, \
    QListWidget, QDateTimeEdit, QInputDialog, QMessageBox
from Smart_NoteUI import*
import json
app = QtWidgets.QApplication([])
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
with open("zamitku.json","r",encoding="utf-8") as file:
    spusok_zamitok=json.load(file)
#text, ok = QInputDialog.getText(None, "Введите имя", "Как вас зовут?")
def make_zam_f():
    text, ok = QInputDialog.getText(None, "Введите имя", "Введите имя")
    if ok and text:
        spusok_zamitok.append({"name":text,
                               "tags":[],
                               "text":""})
        ui.zamitku_lw.addItem(text)
    if not text and ok:
        QMessageBox.warning(None,"Warning","Name cant be empty")
def del_zam():
    if ui.zamitku_lw.currentItem() is not None:
        del spusok_zamitok[ui.zamitku_lw.currentRow()]
        ui.zamitku_lw.takeItem(ui.zamitku_lw.currentRow())
def save_zam():
    if ui.zamitku_lw.currentItem() is not None:
        spusok_zamitok[ui.zamitku_lw.currentRow()]["text"]=ui.zamitku_te.toPlainText()
for zam in spusok_zamitok:
    ui.zamitku_lw.addItem(zam["name"])
for zam in spusok_zamitok:
    for tag in zam["tags"]:
        ui.tegi_lw.addItem(tag)
def make_te():
    ui.zamitku_te.setText(spusok_zamitok[ui.zamitku_lw.currentRow()]["text"])
def add_tag():
    row=ui.zamitku_lw.currentRow()
    print(row)
    if row != -1:
        spusok_zamitok[row]["tags"].append(ui.tegi_le.text())
        ui.tegi_lw.clear()
        for zam in spusok_zamitok:
            for tag in zam["tags"]:
                ui.tegi_lw.addItem(tag)

def change_tags():
    row = ui.zamitku_lw.currentRow()
    ui.tegi_lw.clear()
    for tag in spusok_zamitok[row]["tags"]:
        ui.tegi_lw.addItem(tag)
def del_tag():
    row = ui.zamitku_lw.currentRow()
    row1 = ui.tegi_lw.currentRow()
    if row !=-1 and row1!=-1:
        del spusok_zamitok[row]["tags"][row1]
        ui.tegi_lw.clear()
        for zam in spusok_zamitok:
            for tag in zam["tags"]:
                ui.tegi_lw.addItem(tag)
def search_tags():
    text=ui.tegi_le.text()
    ui.zamitku_lw.clear()
    if text!="":
        for zam in spusok_zamitok:
            for tag in zam["tags"]:
                if text in tag:
                    ui.zamitku_lw.addItem(zam["name"])
    else:
        for zam in spusok_zamitok:
            ui.zamitku_lw.addItem(zam["name"])
def make_tags():
    '''row = ui.zamitku_lw.currentRow()
    if row==-1:
        for tag in spusok_zamitok[row]["tags"]:
            ui.tegi_lw.addItem(tag)'''
    pass




ui.make_zam.clicked.connect(make_zam_f)
ui.del_zam.clicked.connect(del_zam)
ui.save_zam.clicked.connect(save_zam)
ui.zamitku_lw.clicked.connect(make_te)
ui.add_teg.clicked.connect(add_tag)
ui.del_teg.clicked.connect(del_tag)
ui.zamitku_lw.clicked.connect(change_tags)
ui.tegi_le.textEdited.connect(search_tags)
ui.zamitku_lw.itemSelectionChanged.connect(make_tags)
app.exec_()
with open("Zamitku.json", "w", encoding="utf-8") as file:
    json.dump(spusok_zamitok, file, ensure_ascii=False, indent=4)