from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow
from engine_design import Ui_main_window

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import os

class Pyredengine(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
       

        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        
        
        
if __name__ == "__main__":
   app = QApplication([])
   widget = Pyredengine()
   widget.show()
   
   app.exec_() 