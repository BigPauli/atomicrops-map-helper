from graphics_view_test import *
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap
import os
import sys


class My_Application(QWidget):
    def __init__(self):
        super(My_Application, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap("images/bigger_map.png")
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)
        self.radioButtons = [self.ui.radioButton, self.ui.radioButton_2, self.ui.radioButton_3, self.ui.radioButton_4]
        self.stickerOffsets = [[3, 12], [15, 15], [13, 14], [17, 13]]
        self.stickerFilePaths = ['images/exclamation_point.png', 'images/smol_sprinkler.png', 'images/smol_wormsy.png', 'images/smol_car.png']
        self.selectedRadioButton = None
        self.ui.pushButton.clicked.connect(self.button_pushed)

    def mousePressEvent(self, event):
        current_selection = self.get_toggled_radio_button()
        # 675 by 880
        if 0 <= event.pos().x() <= 675 and 0 <= event.pos().y() <= 880 and current_selection is not None:
            temp_pixmap = QPixmap(self.stickerFilePaths[current_selection])
            temp_item = QtWidgets.QGraphicsPixmapItem(temp_pixmap)
            temp_item.setOffset(event.pos().x() - self.stickerOffsets[current_selection][0], event.pos().y() - self.stickerOffsets[current_selection][1])
            self.scene.addItem(temp_item)
        else:
            pass

    def button_pushed(self):
        for i in self.scene.items()[:-1]:
            self.scene.removeItem(i)

    def get_toggled_radio_button(self):
        for index in range(len(self.radioButtons)):
            if self.radioButtons[index].isChecked():
                return index
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_instance = My_Application()
    class_instance.show()
    sys.exit(app.exec())