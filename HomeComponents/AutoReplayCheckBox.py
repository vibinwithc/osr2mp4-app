from PyQt5 import QtWidgets, QtCore
import os


class AutoReplayCheckBox(QtWidgets.QCheckBox):
    def __init__(self, parent):
        super(AutoReplayCheckBox, self).__init__(parent)
        self.setText("Auto Replay")
        self.checked_img = os.path.join(parent.app_directory, "images/checked.png").replace("\\", "/")
        self.unchecked_img = os.path.join(parent.app_directory, "images/unchecked.png").replace("\\", "/")
        self.setMinimumSize(QtCore.QSize(50, 21))
        self.setGeometry(518, 144, 185, 21)
        self.setStyleSheet("""
                QCheckBox {
                color: white;font-size:15pt;
                }
                QCheckBox::indicator {
                    width: 25;
                    height: 25;
		        }
        		QCheckBox::indicator:checked {
        		    image: url(%s);
        		}
        		QCheckBox::indicator:unchecked {
        		    image: url(%s);
        		}
        					""" % (self.checked_img, self.unchecked_img))