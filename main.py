import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import uic
from pymodbus.client import ModbusTcpClient


class MainWindow(QMainWindow):
    pushButton: QPushButton

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        uic.loadUi('static/form.ui', self)
        self.pushButton.clicked.connect(self.try_modbus)

    def try_modbus(self):
        self.pushButton.setDisabled(True)
        client = ModbusTcpClient("0.0.0.0", timeout=1, retries=1)
        print("trying modbus...")
        client.connect()
        try:
            print("before request")
            client.read_discrete_inputs(512, 1)
        except Exception as ex:
            print(ex)
        finally:
            client.close()
            self.pushButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
