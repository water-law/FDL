# -*- coding:utf-8 -*-
import sys
import logging.config
import yaml
from PyQt5.QtCore import QTranslator, QFileInfo
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from utils.Constants import getConfValue, setConfValue
from form.frmFDLApp import FDLApp
# create logger
log_conf = 'log_conf.yml'
with open(log_conf, 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)


if __name__ == '__main__':
    translator = QTranslator()
    translator.load(getConfValue("Lang"))

    app = QApplication(sys.argv)
    app.installTranslator(translator)

    fdl = FDLApp()

    root = QFileInfo(__file__).absolutePath()
    fdl.setWindowIcon(QIcon(root + "/FDL.ico"))

    fdl.show()

    sys.exit(app.exec())
