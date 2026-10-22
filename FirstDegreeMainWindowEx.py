from learning_K26411E.learn_ui_C.Ui.FIrstDegreeMainwindow import Ui_MainWindow


class FirstDegreeMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUI(MainWindow)
        self.Mainwindow=MainWindow
    def showWIndow(self):
        self.Mainwindow.show()
