from PyQt5 import QtCore
from aqt import mw as window, utils, qt, addons
import aqt
from . import templates
import os


def _edit_config():
    addons.ConfigEditor(window, __name__, window.addonManager.getConfig(__name__))


def _help():
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.md")
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            doc = f.read()
        box = aqt.QMessageBox(window)
        box.setTextFormat(QtCore.Qt.MarkdownText)
        box.setText(doc)
        box.exec()
    else:
        show_error("Help document missing!!")


def init():
    # init error dialog
    global err
    err = aqt.QErrorMessage(window)

    # menu items
    menu = aqt.QMenu(window.form.menuTools)
    menu.setTitle("Import / Export templates")
    window.form.menuTools.addAction(menu.menuAction())

    actions = [
        (qt.QAction("Export to ...", menu), templates.export_tmpls),
        (qt.QAction("Import from ...", menu), templates.import_tmpls),
        (qt.QAction("Configure", menu), _edit_config),
        (qt.QAction("Help / Guide", menu), _help)
    ]

    for action, func in actions:
        utils.qconnect(action.triggered, func)
        menu.addAction(action)

    # editor setup for _edit_config
    window.mgr = window.addonManager


def show_error(msg: str, err_type: str = "all"):
    err.showMessage(msg, err_type)


def get_dir():
    folder = aqt.QFileDialog.getExistingDirectory(window, "Select a Directory")
    return folder if len(folder) != 0 else None


def notify(msg: str, time: int = 5000):
    utils.tooltip(msg, time)


err = None
