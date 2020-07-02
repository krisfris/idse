from idse.common import *
from idse.edit_dict import DictDialog


def open_link_in_browser(url):
    QDesktopServices.openUrl(QUrl(url))

def prompt(text, stuff=''):
    answer, ok = QInputDialog.getText(None, '', text, text=str(stuff))
    return answer if ok else None

def prompt_text(label, text=''):
    dialog = QInputDialog(None)
    dialog.setInputMode(QInputDialog.TextInput)
    dialog.setTextValue(str(text))
    dialog.setOption(QInputDialog.UsePlainTextEditForTextInput, True)
    dialog.setLabelText(label)
    dialog.resize(800, 600)
    ok = dialog.exec_()
    if ok:
        return dialog.textValue()

def prompt_table(data):
    try:
        dialog = TableDialog(data)
        if dialog.exec_():
            return dialog.result()
    except:
        QMessageBox.critical(None, 'Error', traceback.format_exc())

def prompt_dict(data):
    dialog = DictDialog(data)
    if dialog.exec_():
        return dialog.result()

def prompt_color(color=None):
    if color is not None:
        color = QColor(*[min(255, x*255) for x in color])
    color = QColorDialog.getColor(color, None, 'Select color', QColorDialog.ShowAlphaChannel)
    if color.isValid():
        color = tuple(x/255 for x in color.getRgb())
        return color


def find(items, keyfunc):
    dialog = FindDialog(items, keyfunc)
    if dialog.exec_():
        return dialog.result()
