from idse.qt import *


class PushButton(QPushButton):
    def __init__(self, label, func, *args, **kwargs):
        super().__init__(label, *args, **kwargs)
        self.clicked.connect(func)
