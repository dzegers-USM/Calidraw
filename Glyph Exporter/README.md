# Glyph Exporter
Ejecutar mediante *ffpython*, incluido en instalaciones de [FontForge](https://fontforge.org/en-US/).

ffpython se ubica en FontForgeBuilds/bin (en Windows, por defecto, "Program Files (x86)/FontForgeBuilds/bin").

Se recomienda agregar FontForgeBuilds/bin a PATH.

## Uso
> ffpython export.py {font_path} {extension} {height}

- font_path: Locación de archivo .ttf
- extension: Extensión de archivos resultantes. Los tipos soportados son detallados en la [documentación de FontForge](https://fontforge.org/docs/scripting/scripting-alpha.html), según la función "Export(format[, bitmap-size])".
- height: Altura en pixeles de archivos resultantes
