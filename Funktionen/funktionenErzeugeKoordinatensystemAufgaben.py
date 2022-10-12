#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugePunkteImKoordsystemAufgabe(mitKoordsystem=False,kommazahlen=False,nurGroesserNull=False,mitText=True):
#Diese Funktion erzeugt eine Aufgabe, in der die Schüler Punkte in einem Koordinatensystem
#eintragen sollen.
    xMin,xMax,yMin,yMax=[0,5,0,5] if nurGroesserNull else [-5,5,-5,5]
    anzKoord=8
    doppelte=True
    while doppelte:
        koords=[]
        if kommazahlen:
            koords=[[random.randint((xMin+1)*10, (xMax-1)*10)/10, random.randint((yMin+1)*10, (yMax-1)*10)/10] for i in range(anzKoord)]
        else:
            koords=[[random.randint(xMin+1,xMax-1),random.randint(yMin+1,yMax-1)] for i in range(anzKoord)]
        if len(list(set(map(str,koords)))) == len(koords):
            doppelte=False
    afg=[F'{(("Erstelle ein Koordinatensystem und t" if not mitKoordsystem else "T")+"rage folgende Punkte ein:") if mitText else "" }']
    afg.append(','.join([F' ${buchstabenGross[i]}({strNW(koords[i][0])}|{strNW(koords[i][1])})$' for i in range(anzKoord)]))
    if mitKoordsystem:
        afg=['\\pbox{\\hsize}{']+afg+['\\\\']
        afg=afg+diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1])
        afg=afg+['}']
    textNode=[[koords[i][0],koords[i][1],"x",'red'] for i in range(anzKoord)]
    textNode=textNode+[[koords[i][0],koords[i][1],buchstabenGross[i],'above'] for i in range(anzKoord)]
    lsg=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],textNode=textNode)
    return [afg,lsg,koords]


def koordinatenFiguren(auswahl='auto',faktor=1):
    if auswahl=='auto':
        reifen=[[-10,0],[-8,-6],[-6,-8],[-4,-9],[0,-10],[4,-9],[6,-8],[8,-6],[10,0]]
        r1=[[x[0]-40,x[1]] for x in reifen[::-1]]
        r2=[[x[0]+40,x[1]] for x in reifen[::-1]]
        karosserie=[[-60,0],[-60,10],[-40,10],[-30,20],[30,20],[40,10],[60,10],[60,0]]
        xAchse=[-70*faktor,70*faktor,15]
        yAchse=[-20*faktor,40*faktor,7]
        streckenzug=[[x[0]*faktor,x[1]*faktor] for x in r2+r1+karosserie+[r2[0]]]
    if auswahl=='nikolaushaus':
        umriss=[[-1,-1],[-1,1],[0,2],[1,1],[-1,1],[1,-1],[1,1],[-1,-1],[1,-1]]
        xAchse=[-2*faktor,2*faktor,5 if faktor==1 else 15]
        yAchse=[-2*faktor,3*faktor,7 if faktor==1 else 15]
        streckenzug=[[x[0]*faktor,x[1]*faktor] for x in umriss]
    return [streckenzug,xAchse,yAchse]

def zeichneFigurImKoordsystem(auswahl='auto',faktor=1,mitKoordsystem=False,mitText=True):
    [streckenzug,xAchse,yAchse]=koordinatenFiguren(auswahl=auswahl, faktor=faktor)
    punkte=[x+['x','red'] for x in streckenzug]
    afg=['Zeichne und verbinde folgende Punkte in einem Koordinatensystem: ' if mitText else '']
    afg.append(','.join([F' ${{P_{{{i}}}({strNW(streckenzug[i][0])}|{strNW(streckenzug[i][1])})}}$' for i in range(len(streckenzug))]))
    if mitKoordsystem:
        afg=['\\pbox{\\hsize}{']+afg+['\\\\']
        afg=afg+diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=xAchse,yAchse=yAchse)
        afg=afg+['}']
    lsg=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=xAchse,yAchse=yAchse,streckenzug=streckenzug,textNode=punkte)
    return [afg,lsg,[streckenzug]]

