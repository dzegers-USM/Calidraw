# Glyph Exporter
Ejecutar mediante *ffpython*, incluido en instalaciones de [FontForge](https://fontforge.org/en-US/).

ffpython se ubica en FontForgeBuilds/bin (en Windows, por defecto, "Program Files (x86)/FontForgeBuilds/bin").

Se recomienda agregar FontForgeBuilds/bin a PATH.

## Uso
> ffpython export.py {font_path} {extension} {height}

- font_path: Locación de archivo .ttf
- extension: Extensión de archivos resultantes, sin incluir el punto. Los tipos soportados son detallados en la [documentación de FontForge](https://fontforge.org/docs/scripting/scripting-alpha.html), según la función "Export(format[, bitmap-size])".
- height: Altura en pixeles de archivos resultantes
- mode:
    - 1: Exportar solo letras a-z, mayúscula y minuscula (sin incluir la ñ).
    - default: Exportar todos los caracteres.
