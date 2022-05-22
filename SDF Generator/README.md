# SDF Generator
Requiere instalación de opencv, numpy.

Las imágenes recibidas por el programa deben ser de dos colores, sin valores entremedios. Efectos de, por ejemplo, anti-aliasing no son fatales, pero incrementan el error del método, debido a la presencia de valores entremedios en las fronteras de cada figura.

## Uso 
> python gen.py {img_path} {max_dist}

-img_path: Locación de imágenes a las que se les aplicará SDF
-max_dist: Distancia máxima a la frontera de cada figura
