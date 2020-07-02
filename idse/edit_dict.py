import uuid

from idse.common import *


class DictDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()
        self.data = dict() if data is None else data.copy()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox2 = QVBoxLayout()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(PushButton('Add key', self.add_key_triggered))
        vbox2.addLayout(hbox2)
        self.key_list = QListWidget()
        for key in self.data.keys():
            item = QListWidgetItem()
            item.setText(key)
            item.setData(Qt.UserRole, key)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.key_list.addItem(item)
        self.key_list.currentItemChanged.connect(self.current_key_changed)
        self.key_list.itemChanged.connect(self.key_changed)
        vbox2.addWidget(self.key_list)
        hbox.addLayout(vbox2)
        self.value_edit = QTextEdit()
        self.value_edit.textChanged.connect(self.value_changed)
        hbox.addWidget(self.value_edit)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(PushButton('OK', self.accept))
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def add_key_triggered(self):
        key = str(uuid.uuid4())
        self.data[key] = ''
        item = QListWidgetItem()
        item.setText(key)
        item.setData(Qt.UserRole, key)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.key_list.addItem(item)

    def key_changed(self, item):
        pass

    def value_changed(self):
        self.data[self.key_list.currentItem().data(Qt.UserRole)] = self.value_edit.toPlainText()

    def current_key_changed(self, new, old):
        self.value_edit.setPlainText(self.data[new.data(Qt.UserRole)])

    def result(self):
        d = dict()
        for i in range(self.key_list.count()):
            item = self.key_list.item(i)
            d[item.text()] = self.data[item.data(Qt.UserRole)]
        return d
