import sys
from PyQt5 import QtWidgets, uic
from Vista.Login import login

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = login ()
    app.exec()
    




