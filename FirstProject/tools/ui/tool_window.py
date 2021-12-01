import os
import six
import sys

from Qt import QtCompat, QtWidgets, QtCore
from PySide2.QtWidgets import QApplication, QPushButton

from tools import datas
from engine import engine_base

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path

ui_path = Path(__file__).parent / 'qt' / 'Window.ui'
UserRole = QtCore.Qt.UserRole


class ToolWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ToolWindow, self).__init__()
        QtCompat.loadUi(str(ui_path), self)
        self.buttonOpen.clicked.connect(self.open_file)
        #self.buttonSave.clicked.connect(self.save_file)
        #self.buttonTool.clicked.connect(self.create_tool)

        if 'maya' in sys.executable:
            self.buttonTool.setText('Tool Maya')

        if 'houdini' in sys.executable:
            self.buttonTool.setText('Tool Houdini')

        for f in datas.get_files():
            addListWidgetItem(self.listItems, f, os.path.basename(f))

        for f in engine_base.Engine.get_Engine(self).implements:
            print(f)
            button = QPushButton(f)
            self.verticalLayout.addWidget(button)

        button.clicked.connet(open)





    def open_file(self):
        item = self.listItems.currentItem()
        path = item.data(UserRole)
        print('{} -> {}'.format(item.text(), path))
        print(path)
        print(item.text())
        engine_base.Engine.get_Engine(self).open(path)

    def save_file(self):
        engine_base.Engine.get_Engine(self).save(self)
        print("Le fichier à bien été sauvegardé")

    def create_tool(self):
        engine_base.Engine.get_Engine(self).tool(self)


def addListWidgetItem(listWidget, data, label):
    """ Used to fill a UI listWidget with listWidgetItem (label + data) """
    item = QtWidgets.QListWidgetItem()
    item.setData(UserRole, data)
    item.setText(label)
    listWidget.addItem(item)
    return item


if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()

