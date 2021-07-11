from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

from lib.share import SI


class win_login:
    def __init__(self):
        self.ui = QUiLoader().load('login.ui')
        self.ui.cbox_material.addItems(['sus304', ])
        self.ui.btn_calc.clicked.connect(self.calcWithSpringParam)
        # self.ui.edt_password.returnPressed.connect(self.onSignIn)
        # self.ui.edt_username.returnPressed.connect(self.onSignIn)

    def calcWithSpringParam(self):
        try:
            dia_exter = int(self.ui.edt_dia_external.text())
            dia_line = int(self.ui.edt_dia_line.text())
            dia_pitch = dia_exter-dia_line
            self.ui.label_dia_pitch.setText(str(dia_pitch))
        except:
            QMessageBox.warning(
                self.ui, "warning", "Please input numbers", QMessageBox.Yes, QMessageBox.Yes)


app = QApplication([])
SI.loginWin = win_login()
SI.loginWin.ui.show()
app.exec_()
