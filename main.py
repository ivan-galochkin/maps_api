from PyQt5 import QtWidgets
import sys
from map_api import Ui_Form


class MapApp():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_Form(QtWidgets.QWidget())
        self.ui.form.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    MapApp()