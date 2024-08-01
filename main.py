# main.py

import sys
from PyQt5 import QtWidgets
from main_app import MainApp

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
