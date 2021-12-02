import os
import sys
import six

from PySide2.QtWidgets import QPushButton, QApplication
from Qt import QtCompat, QtWidgets, QtCore

from pipeline.engine import get_Engine
from pipeline.tools import datas

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
        # self.buttonOpen.clicked.connect(self.open_file)
        # self.buttonSave.clicked.connect(self.save_file)
        # self.buttonTool.clicked.connect(self.create_tool)

        '''if 'maya' in sys.executable:
            self.buttonTool.setText('Tool Maya')
        elif 'houdini' in sys.executable:
            self.buttonTool.setText('Tool Houdini')'''

        for f in datas.get_files():
            addListWidgetItem(self.listItems, f, os.path.basename(f))

        implement = get_Engine().implements
        for f in implement:
            button = QPushButton(f.capitalize())
            button.clicked.connect(self.buttonClicked)
            self.verticalLayout.addWidget(button)
            button.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' a été sélectionné')
        print(sender.text())

        fonction = getattr(get_Engine(), sender.text().lower())
        #print(fonction)
        item = self.listItems.currentItem()
        path = item.data(UserRole)
        fonction(path)

def addListWidgetItem(listWidget, data, label):
    """ Used to fill a UI listWidget with listWidgetItem (label + data) """
    item = QtWidgets.QListWidgetItem()
    item.setData(UserRole, data)
    item.setText(label)
    listWidget.addItem(item)
    return item


'''def open_file(self):
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
        engine_base.Engine.get_Engine(self).tool(self)'''

if __name__ == '__main__':
    app = QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()
