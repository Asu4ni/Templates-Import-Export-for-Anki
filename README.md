Templates Import / Export : an Anki Add-on
====
A tool for Anki user to **import / export** **CSS** and **card templates** of all note types.

Functions & Things to notice
----

+ **Export**: choose the directory as the destination for export
  - Each note type has its own folder, containing the CSS and templates of all cards.
  - Each template file is named after the card, containing both the front & back templates.
  - The front & back templates are separated by the **configur**able delimiter.
+ **Import**: choose the directory as the source for import
  - Each folder in the chosen directory will be regarded as each individual note type to be
    imported, matched by the name of the folder.
  - Folders or template files without corresponding note types or cards in Anki will be ignored. The
    add-on won't create note types and cards as a result. Therefore, importing the directory which
    was exported earlier is recommended.
  - An extra CSS file can be present in the source directory (compared to what **Export** outputs),
    regarded as the global CSS. When the CSS file is missing under a note type folder, the global
    CSS will be used if present. The behavior when both are present is **configur**able.
+ **Configure**: some configurable settings in JSON format
  - *delimiter between front and back template*: the demimiter for separating front & back templates
    in each card. Default: `` ```<br> `` (``<br>`` is line break)
  - *CSS file name*: the filename for all CSS files. Default: ``style.css``
  - *insert global CSS before individual ones of all note types*: if ``true``, global CSS file will
    be inserted before each note type's CSS file. Otherwise, global CSS will be ignored if there is
    a CSS file for the note type. Default: ``false``
  - *filename extensions for card template files*: an empty string ``""`` for no extension. An
    alternative might be ``".html"``. Default: ``""``

Others
----
+ The source can be found on GitHub: https://github.com/Asu4ni/Templates-Import-Export-for-Anki
+ The add-on page on AnkiWeb: https://ankiweb.net/shared/info/712027367
