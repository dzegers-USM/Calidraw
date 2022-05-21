import os
import errno
import fontforge

if (len(os.sys.argv) == 3):
    font_path = os.sys.argv[1]
    height = os.sys.argv[2]
    font = fontforge.open(font_path)
    try:
        os.mkdir("out")
    except OSError as err:
        if err.errno != errno.EEXIST:
            raise

    for glyph in font:
        if font[glyph].isWorthOutputting():
            if font[glyph].glyphname in "abcdefghijklmnopqrstuvwxyz":
                # Prevents, for ex., "a.png" overwriting "A.png"
                fpath = "out/" + glyph + "lower.png"
            else:
                fpath = "out/" + glyph + ".png"
            font[glyph].export(fpath, int(height) - 1)
else:
    print("usage: ffpython export.py {font_path} {height}")
