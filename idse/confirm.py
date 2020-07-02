def confirm(text='are you sure?'):
    dialog = QMessageBox()
    dialog.setWindowTitle("confirm");
    dialog.setText(text)
    dialog.setStandardButtons(QMessageBox.Yes);
    dialog.addButton(QMessageBox.No);
    dialog.setDefaultButton(QMessageBox.No);
    if dialog.exec_() == QMessageBox.Yes:
        return True
    return False
