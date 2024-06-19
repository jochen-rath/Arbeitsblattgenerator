#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugePunkteImKoordsystemAufgabe(mitKoordsystem=False,kommazahlen=False,nurGroesserNull=False,mitText=True,anzSpalten=[2,2]):
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
    afg=[F'{(("Erstelle ein Koordinatensystem und t" if not mitKoordsystem else "T")+"rage folgende Punkte ein:")}' ] if mitText else []
    afg.append(','.join([F' ${buchstabenGross[i]}({strNW(koords[i][0])}|{strNW(koords[i][1])})$' for i in range(anzKoord)]))
    if mitKoordsystem:
        afg=['\\pbox{\\hsize}{']+afg+['\\\\']
        afg=afg+diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1])
        afg=afg+['}']
    textNode=[[koords[i][0],koords[i][1],"x",'red'] for i in range(anzKoord)]
    textNode=textNode+[[koords[i][0],koords[i][1],buchstabenGross[i],'above'] for i in range(anzKoord)]
    lsg=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[xMin,xMax,(xMax-xMin)+1],yAchse=[yMin,yMax,(yMax-yMin)+1],textNode=textNode)
    return [afg,lsg,koords]


def koordinatenFiguren(auswahl='auto',faktor=1,negZahlen=False):
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
    if auswahl=='dino':
        dino=[[2,58],[6,62],[17,57],[30,55],[47,57],[102,59],[105,65],[108,69],[112,72],[118,71],[128,65]]
        dino=dino+[[130,61],[130,53],[122,57],[125,49],[123,47],[117,48],[113,53],[110,56]]
        dino=dino+[[107,54],[105,49],[104,44],[107,38],[105,36],[102,40],[98,35],[97,41],[82,35],[100,17]]
        dino=dino+[[94,14],[76,33],[62,14],[67,7],[59,5],[56,10],[55,15],[65,33],[65,37],[30,48],[2,58]]
        auge=[[115,67],[113,65],[115,63],[117,65],[115,67]]
        xAchse=[0,130,13.5]
        yAchse=[0,70,7.5]
        if negZahlen:
            maxX=max([x[0] for x in dino]+[x[0] for x in auge])
            maxY=max([x[1] for x in dino]+[x[1] for x in auge])
            dino=[[x[0]-maxX/2,x[1]-maxY/2] for x in dino]
            auge=[[x[0]-maxX/2,x[1]-maxY/2] for x in auge]
            xAchse=[-maxX/2,130-maxX/2,13.5]
            yAchse=[-maxY/2,70-maxY/2,7.5]
        streckenzug=[2,dino,auge]
    if auswahl=='drache':
        drache=[[20,0],[12,17],[7,6],[10,20],[4,19],[9,27],[4,26],[14,32],[0,35],[10,40],[5,41],[19,50]]
        drache=drache+[[5,48],[15,54],[29,55],[35,57],[21,63],[13,76],[23,66],[33,61],[41,59],[45,60]]
        drache=drache+[[45,63],[32,69],[46,67],[58,55],[58,52],[67,47],[72,41],[69,36],[72,35],[71,29]]
        drache=drache+[[68,25],[51,38],[56,25],[49,26],[42,32],[38,39],[36,43],[33,42],[29,35],[32,24]]
        drache=drache+[[40,20],[54,10],[55,0],[20,0]]
        auge=[[46,55],[52,55],[54,52],[50,52],[46,55]]
        xAchse=[0,80,8.5]
        yAchse=[0,80,8.5]
        if negZahlen:
            maxX=max([x[0] for x in drache]+[x[0] for x in auge])
            maxY=max([x[1] for x in drache]+[x[1] for x in auge])
            drache=[[x[0]-maxX/2,x[1]-maxY/2] for x in drache]
            auge=[[x[0]-maxX/2,x[1]-maxY/2] for x in auge]
            xAchse=[-maxX/2,80-maxX/2,8.5]
            yAchse=[-maxY/2,80-maxY/2,8.5]
        streckenzug=[2,drache,auge]
    return [streckenzug,xAchse,yAchse]

def zeichneFigurImKoordsystem(auswahl='auto',negZahlen=False,faktor=1,mitKoordsystem=False,mitText=True,anzSpalten=[2,2]):
    [streckenzug,xAchse,yAchse]=koordinatenFiguren(auswahl=auswahl, faktor=faktor,negZahlen=negZahlen)
    punkte=[]
    afgText='Zeichne und verbinde folgende Punkte in ein Koordinatensystem. Jeder Buchstabe ist ein einzelner Streckenzug von Anfang bis Ende.\\\\'
    groesse='{6 cm}{!}' if anzSpalten[0] == 2 else '{!}{!}'
    afg=['\\pbox{\\hsize}{']+[(afgText if mitText else '')]
    if isinstance(streckenzug[0],int):
        nr=0
        for strZug in streckenzug[1:]:
            afg.append(','.join([F' ${{{buchstabenGross[15+nr]}_{{{i}}}({strNW(strZug[i][0])}|{strNW(strZug[i][1])})}}$' for i in range(len(strZug))]))
            afg[-1]=afg[-1]+'\\\\'
            nr=nr+1
            punkte=punkte+[x+['x', 'red'] for x in strZug]
    else:
        afg.append(','.join([F' ${{P_{{{i}}}({strNW(streckenzug[i][0])}|{strNW(streckenzug[i][1])})}}$' for i in range(len(streckenzug))]))
        punkte=[x+['x', 'red'] for x in streckenzug]
    if mitKoordsystem:
        groesse='{6 cm}{!}' if anzSpalten[1] == 2 else '{!}{!}'
        afg=afg+[f'\\resizebox{groesse}{{']+diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=xAchse,yAchse=yAchse)+['}']
    afg=afg+['}']
    groesse='{6 cm}{!}' if anzSpalten[1] == 2 else '{!}{!}'
    lsg=[f'\\resizebox{groesse}{{']+diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=xAchse,yAchse=yAchse,streckenzug=streckenzug,textNode=punkte)+['}']
    return [afg,lsg,[streckenzug]]

