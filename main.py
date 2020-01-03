from model.modelTelaSistema import ModelTelaSistema
from controller.controllerTelaSistema import ControllerTelaSistema
from PyQt5.QtWidgets import QApplication

import sys

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = ModelTelaSistema()
        self.view = ControllerTelaSistema(self.model)
        self.view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())