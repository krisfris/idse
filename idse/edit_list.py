class ListDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()
        self.data = [] if data is None else data
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(PushButton('Insert item', self.insert_item_triggered))
        vbox.addLayout(hbox)
        self.listwidget = QListWidget()
        for text in self.data:
            self.add_item(text)
        vbox.addWidget(self.listwidget)
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(PushButton('OK', self.accept))
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def add_item(self, text):
        x = QListWidgetItem()
        x.setFlags(x.flags() | Qt.ItemIsEditable)
        self.listwidget.addItem(x)

    def insert_item_triggered(self):
        self.add_item('')

    def result(self):
        return [self.listwidget.item(i).text() for i in range(self.listwidget.count())]
