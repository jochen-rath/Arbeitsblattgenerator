#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeMandala(anzSpalten=2):
    from RandomMandala import random_mandala, figure_to_image
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.cm
    from PIL import Image, ImageOps
    from mpl_toolkits.axes_grid1 import ImageGrid
    import tikzplotlib
    os.environ["XDG_SESSION_TYPE"] = "xcb"
    radius=random.randint(2,50)
    random.seed(random.randint(1,200))
    cf=random.choice(['line','bezier'])
    fig=random_mandala(connecting_function=cf,radius=radius,figsize=(10,10), dpi=240)
    groesse='{14 cm}{!}' if anzSpalten == 1 else '{6 cm}{!}'
#Passe Mandalacode an:
#Alle Koordinaten in table { ... }; enden mit \\
#table wird um [row sep=crcr] erweitert
    mandala=tikzplotlib.get_tikz_code().split('\n')
    gefunden=False
    for i,c in enumerate(mandala):
        if '};' in c:
            gefunden=False
        if gefunden:
            mandala[i]=mandala[i]+' \\\\'
        if 'table {' in c:
            mandala[i]='table [row sep=crcr] {%'
            gefunden=True
    afg=[f'\\resizebox{groesse}{{']+mandala+['}']
#    afg=tikzplotlib.get_tikz_code().split('\n')
    return afg,[],[]
