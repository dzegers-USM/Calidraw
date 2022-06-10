import os
import errno
import fontforge

if (len(os.sys.argv) == 4):
    font_path = os.sys.argv[1]
    extension = os.sys.argv[2]
    height = os.sys.argv[3]
    font = fontforge.open(font_path)
    try:
        os.mkdir("out")
    except OSError as err:
        if err.errno != errno.EEXIST:
            print("Failed to open provided font")
            os._exit()

    for glyph in font:
        if font[glyph].isWorthOutputting():
            if font[glyph].glyphname in "abcdefghijklmnopqrstuvwxyz":
                # Prevents, for ex., "a.png" overwriting "A.png"
                fpath = "out/" + glyph + "lower." + extension
            else:
                fpath = "out/" + glyph + "." + extension
            font[glyph].export(fpath, int(height) - 1)
else:
    print("Usage: ffpython export.py {font_path} {extension} {height}")
