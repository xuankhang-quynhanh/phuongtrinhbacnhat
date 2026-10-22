def giai_phuong_trinh_bac_1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Phương trình có nghiệm duy nhất x = {x}"

try:
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
ket_qua = giai_phuong_trinh_bac_1(a, b)
print(ket_qua)
except ValueError:
    myui.lineEdit_MK.setText("Nhập hệ số a:")
    myui.lineEdit_MK_2.setText("Nhập hệ số b:")


