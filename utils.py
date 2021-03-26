from aqt import mw as window


def get_config(key: str):
    return window.addonManager.getConfig(__name__)[key]


def get_configs():
    return window.addonManager.getConfig(__name__)
