from . import gui, utils
from aqt import mw as window
import aqt
from os import path
import os


def import_tmpls():
    root = gui.get_dir()
    delimiter = utils.get_config("delimiter between front and back template")

    notetypes = [item for item in os.listdir(root) if os.path.isdir(path.join(root, item))]

    count_notetype = 0
    count_template = 0
    for name in notetypes:
        nt = window.col.models.byName(name)
        if not nt: continue

        file = path.join(root, name, "css")
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                nt["css"] = f.read()
        for tmpl in nt.get("tmpls", []):
            if "name" not in tmpl: continue
            file = path.join(root, name, tmpl["name"])
            if os.path.exists(file):
                with open(file, "r", encoding="utf-8") as f:
                    tmpl["qfmt"], _, tmpl["afmt"] = f.read().partition(delimiter)
                count_template += 1
        window.col.models.save(nt)
        count_notetype += 1
    aqt.utils.tooltip("imported (Template: {} from NoteType:{})".format(count_template, count_notetype), 5000)


def export_tmpls():
    root = gui.get_dir()
    delimiter = utils.get_config("delimiter between front and back template")

    count_notetype = 0
    count_template = 0
    for nt in window.col.models.all():
        try:
            notetype_name = nt.get("name")
        except KeyError:
            gui.show_error("The notetype has no name!!")
            continue
        notetype_path = path.join(root, notetype_name)
        os.makedirs(notetype_path, exist_ok=True)
        if "css" in nt:
            with open(path.join(notetype_path, "css"), "w", encoding="utf-8") as f:
                f.write(nt["css"])
        for tmpl in nt.get("tmpls", []):
            try:
                tmpl_name = tmpl.get("name")
            except KeyError:
                gui.show_error("A template in notetype \"{}\" has no name!!".format(notetype_name))
                continue
            with open(path.join(notetype_path, tmpl_name), "w", encoding="utf-8") as f:
                if "qfmt" in tmpl and "afmt" in tmpl:
                    f.write(tmpl["qfmt"] + delimiter + tmpl["afmt"])
            count_template += 1
        count_notetype += 1
    aqt.utils.tooltip("exported (Template: {} from NoteType:{})".format(count_template, count_notetype), 5000)
