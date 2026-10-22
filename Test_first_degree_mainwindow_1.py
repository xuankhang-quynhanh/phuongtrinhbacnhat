#1 import shit
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from learning_K26411E.learn_ui_C.Ui.FirstDegreeMainWindowEx import Ui_MainWindow

app = QApplication(sys.argv)

#2 Tạo khung cửa sổ chính
main_window = QMainWindow()
myui = Ui_MainWindow()

#3 Lắp ráp giao diện vào cửa sổ chính
myui.setupUi(main_window)
#5 giải phương trình?
x=0
def giai_phuong_trinh():
    try:
#try = không lỗi
        a = float(myui.line_edit_A.text())
        b = float(myui.line_edit_B.text())
        if a==0:
            if b == 0:
                myui.line_edit_solution.setText("phuong trinh vo so  nghiem")
            else:
                myui.line_edit_solution.setText("phuong trinh vo nghiem")
        else:
            x=-1*b/a
            myui.line_edit_solution.setText(str(x))
    except ValueError:
        myui.line_edit_solution.setText("vai lon nhap cai deo j the, deo tinh duoc")
#6 nút xóa(clear_button) hoặc (push_clear)
def nut_clear():
    myui.line_edit_A.clear()
    myui.line_edit_B.clear()
    myui.line_edit_solution.setText("")
    myui.line_edit_A.setFocus()

#7 bấm nút solution để giải phương trình
myui.push_solution.clicked.connect(giai_phuong_trinh)
myui.push_clear.clicked.connect(nut_clear)
#8 thầy nói là lặp(app.exec()) là bắt buộc để app mở, main_window.show() để mở màn hình ( hai lệnh này phải đặt cuối cùng chương trình )
main_window.show()
app.exec()




