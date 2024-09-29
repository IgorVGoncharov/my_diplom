from data.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from data.db import banks
from data.tables import tables


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    new_tables = tables()
    new_tables.create_tables()

    #bank_headers_labels = ['БИК', 'Наименование Банка', 'Рег.номер Банка', 'Рег.номер Филиала']
    #ui.set_table_all(4, 6, bank_headers_labels, banks)

    sys.exit(app.exec_())