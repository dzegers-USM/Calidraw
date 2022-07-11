import os
import sys
import errno
import fontforge

if (len(os.sys.argv) == 4) or (len(os.sys.argv) == 5):
    font_path = os.sys.argv[1]
    extension = os.sys.argv[2]
    height = int(os.sys.argv[3])
    if (len(os.sys.argv) == 5):
        mode = int(os.sys.argv[4])
    else:
        mode = 0
    try:
        font = fontforge.open(font_path)
    except OSError as err:
        sys.exit(1)

    try:
        os.mkdir("out")
    except OSError as err:
        if err.errno != errno.EEXIST:
            print("Failed to create \"out\" folder")
            sys.exit(1)

    for glyph in font:
        if font[glyph].isWorthOutputting():
            if (mode == 1):  # Only letters
                export = False
                if font[glyph].glyphname in "abcdefghijklmnopqrstuvwxyz":
                    # Prevents, for ex., "a.png" overwriting "A.png"
                    fpath = "out/" + glyph + "lower." + extension
                    export = True
                elif font[glyph].glyphname in "ABCDEFGHIJKLMNOPQRSTUVWYXZ":
                    fpath = "out/" + glyph + "." + extension
                    export = True
                if export:
                    font[glyph].export(fpath, height - 1)
            else:  # Default
                if font[glyph].glyphname in "abcdefghijklmnopqrstuvwxyz":
                    # Prevents, for ex., "a.png" overwriting "A.png"
                    fpath = "out/" + glyph + "lower." + extension
                else:
                    fpath = "out/" + glyph + "." + extension
                font[glyph].export(fpath, height - 1)
else:
    print("Usage: ffpython export.py {font_path} {extension} {height}")
sys.exit(0)
