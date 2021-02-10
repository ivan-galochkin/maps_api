from PyQt5 import QtWidgets, QtGui, QtCore
import sys
import logic
import api
from map_api import Ui_Form


class MapApp():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.ui = Ui_Form(QtWidgets.QWidget())
        self.ui.form.keyPressEvent = self.keyPressEvent
        self.ui.form.mousePressEvent = self.mousePressEvent
        self.ui.form.show()
        self.logic = logic.Logic(render_callback=self.render_map)
        self.render_map()
        self.ui.button_search.clicked.connect(self.change_cords)
        self.ui.coords_y_lineedit.returnPressed.connect(self.ui.coords_y_lineedit.clearFocus)
        self.ui.coords_x_lineedit.returnPressed.connect(self.ui.coords_x_lineedit.clearFocus)

        sys.exit(self.app.exec_())

    def render_map(self):
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(api.get_map(self.logic.cords, self.logic.zoom_level, self.logic.map_type).read())
        self.ui.map_label.setPixmap(pixmap)

    def mousePressEvent(self, event):
        focused_widget = QtWidgets.QApplication.focusWidget()
        if isinstance(focused_widget, QtWidgets.QLineEdit):
            focused_widget.clearFocus()

    def change_cords(self):
        x = float(self.ui.coords_x_lineedit.text())
        y = float(self.ui.coords_y_lineedit.text())
        self.logic.change_cords((x, y))
        self.ui.coords_x_lineedit.clearFocus()
        self.ui.coords_y_lineedit.clearFocus()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.logic.move((0, 1))
        if event.key() == QtCore.Qt.Key_Down:
            self.logic.move((0, -1))
        if event.key() == QtCore.Qt.Key_Right:
            self.logic.move((1, 0))
        if event.key() == QtCore.Qt.Key_Left:
            self.logic.move((-1, 0))
        if event.key() == QtCore.Qt.Key_PageUp:
            self.logic.change_zoom(0.05)
        if event.key() == QtCore.Qt.Key_PageDown:
            self.logic.change_zoom(-0.05)
        if event.key() == QtCore.Qt.Key_1:
            self.logic.change_map('map')
        if event.key() == QtCore.Qt.Key_2:
            self.logic.change_map('sat')
        if event.key() == QtCore.Qt.Key_3:
            self.logic.change_map('sat,skl')

        event.accept()


if __name__ == "__main__":
    MapApp()
