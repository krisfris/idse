class FindDialog(QDialog):
    def __init__(self, items, keyfunc):
        super().__init__()
        self.items = items
        self.keyfunc = keyfunc
        vbox = QVBoxLayout()
        self.query_edit = QLineEdit()
        self.query_edit.textChanged.connect(self.query_changed)
        self.result_list = QListWidget()
        vbox.addWidget(self.query_edit)
        vbox.addWidget(self.result_list)
        self.setLayout(vbox)

    def query_changed(self, value):
        self.result_list.clear()
        if not value:
            return
        for item in self.items:
            key = self.keyfunc(item)
            if key and key.startswith(value):
                x = QListWidgetItem()
                x.setData(Qt.UserRole, item)
                x.setText(key)
                self.result_list.addItem(x)
        self.set_current(0)

    def set_current(self, row):
        count = self.result_list.count()
        if count:
            self.result_list.setCurrentRow(row % count)

    def result(self):
        return self.result_list.currentItem().data(Qt.UserRole)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.set_current(self.result_list.currentRow() - 1)
        elif key == Qt.Key_Down:
            self.set_current(self.result_list.currentRow() + 1)
        elif key == Qt.Key_Return:
            if self.result_list.currentRow() == -1:
                self.reject()
            else:
                self.accept()
        else:
            super().keyPressEvent(event)
