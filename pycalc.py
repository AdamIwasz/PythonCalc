import sys

from PyQt5.QtWidgets import QApplication

from PyCalcCtrl import PyCalcCtrl
from PyCalcUi import PyCalcUi
from PyCalcModel import PyCalcModel


def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    view.show()
    model = PyCalcModel.evaluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(pycalc.exec_())
    
    

if __name__=='__main__':
    main()