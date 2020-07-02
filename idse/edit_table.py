class TableDialog(QDialog):
    def __init__(self, data=None):
        super().__init__()
        self.data = [] if data is None else data
        self.columns = sorted(set(key for x in self.data for key in x.keys()))
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        pb = QPushButton('Insert row')
        pb.clicked.connect(self.insert_row_triggered)
        hbox.addWidget(pb)
        hbox.addWidget(PushButton('Edit headers', self.edit_headers_triggered))
        vbox.addLayout(hbox)
        self.table = QTableWidget(len(self.data), len(self.columns), self)
        self.table.setHorizontalHeaderLabels(self.columns)
        for i, doc in enumerate(self.data):
            for j, (k, v) in enumerate(doc.items()):
                item = QTableWidgetItem(v)
                self.table.setItem(i, j, item)
        vbox.addWidget(self.table)
        hbox = QHBoxLayout()
        hbox.addWidget(PushButton('OK', self.accept))
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def insert_row_triggered(self):
        self.table.insertRow(self.table.rowCount())

    def update_columns(self, columns):
        self.columns = columns
        self.table.setColumnCount(len(self.columns))
        self.table.setHorizontalHeaderLabels(self.columns)

    def edit_headers_triggered(self):
        dialog = ListDialog(self.columns)
        if dialog.exec_():
            self.update_columns(dialog.result())

    def result(self):
        l = []
        for row in range(self.table.rowCount()):
            d = {}
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                d[self.columns[column]] = '' if item is None else item.text()
            l.append(d)
        return l
