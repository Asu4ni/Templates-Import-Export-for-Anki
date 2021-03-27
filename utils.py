from aqt import mw as window
from . import gui

_config_map = {
    "delimiter": "delimiter between front and back template",
    "mergeCSS": "insert global CSS before individual ones of all note types",
    "cssName": "CSS file name",
    "tmplExt": "filename extensions for card template files"
}

_cfg = {}


def reload_config():
    global _cfg
    _cfg = window.addonManager.getConfig(__name__)


def cfg(key: str):
    try:
        r = _cfg[_config_map[key]]
    except KeyError:
        gui.show_error("\"{}\" missing in configuration!!".format(key))
        r = None
    return r
