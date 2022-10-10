#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugePunkteImKoordsystemAufgabe(mitKoordsystem=False,nurGroesserNull=False,mitText=True):
#Diese Funktion erzeugt eine Aufgabe, in der die Schüler Punkte in einem Koordinatensystem
#eintragen sollen.
    xMin,xMax,yMin,yMax=[0,5,0,5] if nurGroesserNull else [-5,5,-5,5]
    anzKoord=8
    doppelte=True
    while doppelte:
        koords=[]
        koords=[[random.randint(xMin+1,xMax-1),random.randint(yMin+1,yMax-1)] for i in range(anzKoord)]
        if len(list(set(map(str,koords)))) == len(koords):
            doppelte=False
    afg=[F'{(("Erstelle ein Koordinatensystem und t" if not mitKoordsystem else "T")+"rage folgende Punkte ein:") if mitText else "" }']
    afg.append(','.join([F' ${buchstabenGross[i]}({strNW(koords[i][0])}|{strNW(koords[i][1])})$' for i in range(anzKoord)]))
    if mitKoordsystem:
        afg=['\\pbox{\\hsize}{']+afg+['\\\\']
        afg=afg+diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1])
        afg=afg+['}']
    textNode=[[koords[i][0],koords[i][1],"x"] for i in range(anzKoord)]
    textNode=textNode+[[koords[i][0],koords[i][1],buchstabenGross[i],'above'] for i in range(anzKoord)]
    lsg=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],textNode=textNode)
    return [afg,lsg,koords]