from aqt import mw as window
from . import gui


def get_config(key: str):
    try:
        r = window.addonManager.getConfig(__name__)[key]
    except KeyError:
        gui.show_error("\"{}\" missing in configuration!!".format(key))
        r = None
    return r



def get_configs():
    return window.addonManager.getConfig(__name__)
