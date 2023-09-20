#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def baumdiagramm(erg=[{'K':'1/2','Z':'1/2'},{'K':'1/2','Z':'1/2'}]):
    dx=3
    koords=[]
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    dy=sum([len(x) for x in erg[1:]]) if len(erg)>1 else 1
    tikzAst, k, endNr=astVomBaumdiagramm(erg=erg[0],dx=dx,dy=dy,mitTikzUmrandung=False)
    koords.append(k)
    tikzcommand=tikzcommand+tikzAst
    for j in range(len(erg)-1):
        koord2=[]
        for i,K in enumerate(koords[j]):
            W=list(erg[j].keys())[i%len(erg[j])]
            dy=sum([len(x) for x in erg[j+2:]])
            tikzAst, k, endNr=astVomBaumdiagramm(erg=erg[j+1], ursp=K, phantom=W, startNr=endNr+1,dx=dx,dy=dy if dy>0 else 1, mitTikzUmrandung=False)
            koord2=koord2+k
            tikzcommand=tikzcommand+tikzAst
        koords.append(koord2)
    for i,k in enumerate(koords[-1]):
        #Wenn man die Zahl zur Basis der Stufe umwandelt, dann kann man die Wahrscheinlichkeiten
        #Korrekt abgreifen. Gilt nur, wenn alle Stufen die Gleiche Anzahl an Wahrscheinlichkeiten haben.
        #    3 Stufige: 3 Basis 3 ist '010'
        werte=list(erg[0].keys())
        wertePos=list(np.base_repr(i, base=len(erg[0])).zfill(len(erg)))
        PList=[werte[int(pos)] for j,pos in enumerate(wertePos)]
        WList=[erg[j][P] for j,P in enumerate(PList)]
        WListFrac=[erzeugeLatexFracAusdruck(erg[j][P]) for j,P in enumerate(PList)]
        tikzcommand.append(F'\\node[right] at ({k[0]+0.5},{k[1]}) {{$P({",".join(PList)})={"*".join(WListFrac)}={strNW(eval("*".join(WList))*100,2)}\\%$}};'.replace('*','\\cdot'))
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def astVomBaumdiagramm(erg={'1':'1/6','2':'1/6','3':'1/6','4':'1/6','5':'1/6','6':'1/6'},ursp=[0,0],phantom='M',startNr=0,dx=3,dy=1,mitTikzUmrandung=True):
    W=list(erg.keys())
    koords=[]
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]'] if mitTikzUmrandung else []
    if mitTikzUmrandung:
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    #tikzcommand.append(F'\\draw[thick,pattern=north west lines, pattern color=black!40] ({0},{0}) circle ({0.5}) ;  ')
    tikzcommand.append(F'\\node[draw,circle] ({startNr}) at ({ursp[0]},{ursp[1]}) {{\\phantom{{{phantom}}}}};')
    for i,w in enumerate(W):
        koords.append([ursp[0]+dx,ursp[1]+dy*((0.5*len(W)-i-0.5) if len(W)%2==0 else (int(0.5*len(W))-i))])
        tikzcommand.append(F'\\node[draw,circle] ({startNr+i+1}) at ({koords[-1][0]},{koords[-1][1]}) {{{w}}};')
    for i,w in enumerate(W):
        endNr=startNr+i+1
        tikzcommand.append(F'\\draw [->] ({startNr}) to ({startNr+i+1}) ;')
        tikzcommand.append(F'\\node at ($({startNr})!{0.55+(0.05*(i%2))}!({endNr})$) {{${erzeugeLatexFracAusdruck(erg[w])}$}};')
    if mitTikzUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand,koords,endNr


def DrehscheibeFarblich(farben=['Rot','Grün','Blau','Orange','Gelb']):
    print(farben)
    winkel=[i*360/len(farben)+90 for i in range(len(farben))]+[360+90]
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\pgfmathsetmacro{{\R}}{{2}}   ')
    tikzcommand.append(F'\\draw[thick] (0,0) circle (\R); ')
    for i,farbe in enumerate(farben):
        tikzcommand.append(F'\\draw[{farbenTikzDeutsch[farbe]}] (0,0) -- ({winkel[i]}:\R);')
        tikzcommand.append(F'\\draw[black,thick,fill={farbenTikzDeutsch[farbe]}] (0,0) -- ({winkel[i]}:\R) arc ({winkel[i]}:{winkel[i+1]}:\R) -- (0,0);')
    tikzcommand.append(F'\\draw[black,very thick,->] (0,0) -- ({random.randint(-45,45)}:\R*3/4); ')

    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand