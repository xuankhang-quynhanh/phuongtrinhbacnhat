#1 import shit
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from learning_self.Simple_Login_with_3_attemps.Ui.untitled import Ui_Loginwindow

app = QApplication(sys.argv)

#2 Tạo khung cửa sổ chính
main_window = QMainWindow()
myui = Ui_Loginwindow()

#3 Lắp ráp giao diện vào cửa sổ chính
myui.setupUi(main_window)
#ma cai nay moi kho
main_window.show()
app.exec()