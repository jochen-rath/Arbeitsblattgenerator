#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
import math
import random


def dreieckFuerFlaechenBer(g=4,h=2,drehung=30,dx=-1,mitBeschr=True):
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black] ({drehung}:{dx}) -- node{{{F"g={strNW(g)} cm" if mitBeschr else "" }}} ({drehung}:{dx+g});')
    tikzcommand.append(F'\\draw[thick,black] ({drehung}:{dx})  -- ({drehung+90}:{h});')
    tikzcommand.append(F'\\draw[thick,black] ({drehung}:{dx+g})  -- ({drehung+90}:{h});')
    if mitBeschr:
        tikzcommand.append(F'\\draw[dashed,black] (0,0)  -- node{{h={strNW(h)} cm}} ({drehung+90}:{h});')
        tikzcommand.append(F'\\draw[dashed,black] (0,0)  -- ({drehung}:{dx});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def strahlensatz(A=[4,1],B=[3,5],k=1.5,farben=['green','violet','blue','orange','purple','brown'],punkte=['S','A','B',"A'","B'"],strecken=buchstabenKlein[0:6]):
#Diese Funktion erzeugt ein Dreieck für den Strahlensatz
# Das Zentrum S,Z ist im Ursprung.
    Sname,Aname,AstrName,Bname,BstrName=punkte
    SA,SAstr,SB,SBstr,AB,AstrBstr=strecken
    Astr=[x*k for x in A]
    Bstr=[x*k for x in B]
    farbeSA,farbeSAstr,farbeSB,farbeSBstr,farbeAB,farbeAstrBstr=farben
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[very thick,{farbeSAstr}] (0 cm,0 cm) node[black,below] {{{Sname}}} -- node[black,below] {{{SAstr}}} ({Astr[0]} cm,{Astr[1]}cm) node[black,below] {{{AstrName}}};')
    tikzcommand.append(F'\\draw[very thick,{farbeSA}{",dashed" if k>=0 else ""}] (0 cm,0 cm) -- node[black,below] {{{SA}}} ({A[0]} cm,{A[1]} cm) node[black,below] {{{Aname}}};')
    tikzcommand.append(F'\\draw[very thick,{farbeSBstr}] (0 cm,0 cm) -- node[black,above] {{{SBstr}}} ({Bstr[0]} cm,{Bstr[1]}cm) node[black,below] {{{BstrName}}};')
    tikzcommand.append(F'\\draw[very thick,{farbeSB}{",dashed" if k>=0 else ""}] (0 cm,0 cm) -- node[black,above] {{{SB}}} ({B[0]} cm,{B[1]} cm) node[black,below] {{{Bname}}};')
    tikzcommand.append(F'\\draw[very thick,{farbeAstrBstr}] ({Astr[0]} cm,{Astr[1]} cm) -- node[black,right] {{{AstrBstr}}}({Bstr[0]} cm,{Bstr[1]}cm);')
    tikzcommand.append(F'\\draw[very thick,{farbeAB}] ({A[0]} cm,{A[1]} cm)-- node[black,right] {{{AB}}} ({B[0]} cm,{B[1]} cm);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def leererKaroBereich(x=17,y=10):
    tikzTabelle=[]
    tikzTabelle.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzTabelle.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzTabelle.append('\\node at (0.3,0) { } ;')
    tikzTabelle.append('\\node at ('+str(x)+','+str(y)+') { } ;')
    tikzTabelle.append('\\end{tikzpicture}')
    return tikzTabelle


def rechteckTikz(a,b,beschrSeiten=False,beschrPunkte=False,texta='a',textb='b',textMitte=''):
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append('\\draw[black, very thick] (0cm,0.1cm) rectangle ('+str(a)+'cm,'+str(b)+'cm);')
    if beschrSeiten:
        tikzcommand.append(F'\\draw ({0.5*a}cm,{b}cm) node[below]{{{texta}}}; ')
        tikzcommand.append(F'\\draw ({a}cm,{0.5*b}cm) node[right]{{{textb}}}; ')
    if beschrPunkte:
        tikzcommand.append('\\draw ('+str(0)+'cm,'+str(0)+'cm) node[below]{A}; ')
        tikzcommand.append('\\draw ('+str(a)+'cm,'+str(0)+'cm) node[below]{B}; ')
        tikzcommand.append('\\draw ('+str(a)+'cm,'+str(b)+'cm) node[above]{C}; ')
        tikzcommand.append('\\draw ('+str(0)+'cm,'+str(b)+'cm) node[above]{D}; ')
    if len(textMitte)>0:
        tikzcommand.append('\\node at ('+str(a/2.0)+','+str(b/2.0)+'){'+str(textMitte)+'}; ')
#    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def zusammengesetzteRechtecke(punkte,beschrSeiten=False,beschrPunkte=False,mitLsg=False,texta='a',textb='b'):
#Beispiel:
#  zusammengesetzteRechtecke(erzeugeZusammengesetzRechtecke(n=3,gesamtlaenge=5,hoehe=5),mitLsg=True)
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    startPkt=[0,0]
    endPkt=[0,0]
    for i,pkt in enumerate(punkte):
        if mitLsg:
            tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,0cm) rectangle ('+str(endPkt[0]+pkt[0])+'cm,'+str(pkt[1])+'cm);')
            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(pkt[1])+'cm) node[below]{$'+texta+'_'+str(i+1)+'$}; ')
            tikzcommand.append('\\draw ('+str(endPkt[0]+pkt[0])+'cm,'+str(0.5*pkt[1])+'cm) node[left]{$'+textb+'_'+str(i+1)+'$}; ')
#            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(0.5*pkt[1])+'cm) node{$A'+'_'+str(i+1)+'$}; ')
            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(pkt[1])+'cm) node[above]{$A'+'_'+str(i+1)+'$}; ')
        else:
            tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,'+str(endPkt[1])+'cm) -- ('+str(endPkt[0])+'cm,'+str(pkt[1])+'cm);')
            tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,'+str(pkt[1])+'cm) -- ('+str(endPkt[0]+pkt[0])+'cm,'+str(pkt[1])+'cm);')
            tikzcommand.append('\\draw[black] ('+str(endPkt[0]+pkt[0])+'cm,'+str(0.0)+'cm) -- ('+str(endPkt[0])+'cm,'+str(0.0)+'cm);')
        if beschrSeiten:
            tikzcommand.append('\\draw ('+str(0.5*(endPkt[0]+pkt[0]))+'cm,'+str(pkt[1])+'cm) node[below]{$'+texta+'_'+str(i)+'$}; ')
            tikzcommand.append('\\draw ('+str(endPkt[0]+pkt[0])+'cm,'+str(0.5*pkt[1])+'cm) node[right]{'+textb+'}; ')
        endPkt=[endPkt[0]+pkt[0],pkt[1]]
    tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,'+str(pkt[1])+'cm) -- ('+str(endPkt[0])+'cm,'+str(0.0)+'cm);')
    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def zusammengesetzteRechtecke2(punkte,mitLsg=False,texta='a',textb='b'):
#Beispiel:
#  zusammengesetzteRechtecke(erzeugeZusammengesetzRechtecke(n=3,gesamtlaenge=5,hoehe=5),mitLsg=True)
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    startPkt=[0,0]
    endPkt=[0,0]
    for i,pkt in enumerate(punkte):
        if mitLsg:
            tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,0cm) rectangle ('+str(endPkt[0]+pkt[0])+'cm,'+str(pkt[1])+'cm);')
            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(pkt[1])+'cm) node[below]{$'+texta+'_'+str(i+1)+'$}; ')
            tikzcommand.append('\\draw ('+str(endPkt[0]+pkt[0])+'cm,'+str(0.5*pkt[1])+'cm) node[left]{$'+textb+'_'+str(i+1)+'$}; ')
#            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(0.5*pkt[1])+'cm) node{$A'+'_'+str(i+1)+'$}; ')
            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(pkt[1])+'cm) node[above]{$A'+'_'+str(i+1)+'$}; ')
        else:
            tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,'+str(endPkt[1])+'cm) -- ('+str(endPkt[0])+'cm,'+str(pkt[1])+'cm);')
            tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,'+str(pkt[1])+'cm) -- ('+str(endPkt[0]+pkt[0])+'cm,'+str(pkt[1])+'cm);')
            tikzcommand.append('\\draw[black] ('+str(endPkt[0]+pkt[0])+'cm,'+str(0.0)+'cm) -- ('+str(endPkt[0])+'cm,'+str(0.0)+'cm);')
        endPkt=[endPkt[0]+pkt[0],pkt[1]]
    tikzcommand.append('\\draw[black] ('+str(endPkt[0])+'cm,'+str(pkt[1])+'cm) -- ('+str(endPkt[0])+'cm,'+str(0.0)+'cm);')
    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def zusammengesetzteRechteckeSchwer(rechtecke,beschrSeiten=False,beschrPunkte=False,mitLsg=False,texta='a',textb='b'):
#Beispiel:
#  zusammengesetzteRechtecke(erzeugeZusammengesetzRechtecke(n=3,gesamtlaenge=5,hoehe=5),mitLsg=True)
#Jedes Rechteck wird von zwei Punkte aufgespannt:
#           rechtecke=[punkte1,punkte2,...
#           punkte1=[[x_0,y_0],[x_1,y_1]] usw.
    tikzcommand=[]
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    startPkt=[0,0]
#1. Rechteck Zeichnen
    tikzcommand.append('\\draw[black] ('+str(rechtecke[0][0][0])+'cm,'+str(rechtecke[0][0][1])+'cm) -- ('+str(rechtecke[0][0][0])+'cm,'+str(rechtecke[0][1][1])+'cm);')
    tikzcommand.append('\\draw[black] ('+str(rechtecke[0][0][0])+'cm,'+str(rechtecke[0][1][1])+'cm) -- ('+str(rechtecke[0][1][0])+'cm,'+str(rechtecke[0][1][1])+'cm);')
    tikzcommand.append('\\draw[black] ('+str(rechtecke[0][1][0])+'cm,'+str(rechtecke[0][0][1])+'cm) -- ('+str(rechtecke[0][0][0])+'cm,'+str(rechtecke[0][0][1])+'cm);')
#Zeichen Jedes Rechteck, indem die Punkte abgelaufen werden.
    for i,pkt in enumerate(rechtecke):
        if mitLsg:
            tikzcommand.append('\\draw[black] ('+str(pkt[0][0])+'cm,'+str(pkt[0][1])+'cm) rectangle ('+str(pkt[1][0])+'cm,'+str(pkt[1][1])+'cm);')
            tikzcommand.append('\\draw ('+str(0.5*(pkt[0][0]+pkt[1][0]))+'cm,'+str(pkt[1][1])+'cm) node[below]{$'+texta+'_'+str(i+1)+'$}; ')
            tikzcommand.append('\\draw ('+str(pkt[1][0])+'cm,'+str(0.5*(pkt[0][1]+pkt[1][1]))+'cm) node[left]{$'+textb+'_'+str(i+1)+'$}; ')
#            tikzcommand.append('\\draw ('+str(endPkt[0]+0.5*pkt[0])+'cm,'+str(0.5*pkt[1])+'cm) node{$A'+'_'+str(i+1)+'$}; ')
            tikzcommand.append('\\draw ('+str(0.5*(pkt[0][0]+pkt[1][0]))+'cm,'+str(0.5*(pkt[0][1]+pkt[1][1]))+'cm) node{$A'+'_'+str(i+1)+'$}; ')
        else:
            if i>0:
                tikzcommand.append('\\draw[black] ('+str(pkt[0][0])+'cm,'+str(rechtecke[i-1][1][1])+'cm) -- ('+str(pkt[0][0])+'cm,'+str(pkt[1][1])+'cm);')
                tikzcommand.append('\\draw[black] ('+str(pkt[0][0])+'cm,'+str(pkt[1][1])+'cm) -- ('+str(pkt[1][0])+'cm,'+str(pkt[1][1])+'cm);')
                tikzcommand.append('\\draw[black] ('+str(pkt[1][0])+'cm,'+str(pkt[0][1])+'cm) -- ('+str(pkt[0][0])+'cm,'+str(pkt[0][1])+'cm);')
                tikzcommand.append('\\draw[black] ('+str(pkt[0][0])+'cm,'+str(rechtecke[i-1][0][1])+'cm) -- ('+str(pkt[0][0])+'cm,'+str(pkt[0][1])+'cm);')
#Anbschluss Letztes Rechteck Zeichnen
    tikzcommand.append('\\draw[black] ('+str(rechtecke[-1][1][0])+'cm,'+str(rechtecke[-1][0][1])+'cm) -- ('+str(rechtecke[-1][1][0])+'cm,'+str(rechtecke[-1][1][1])+'cm);')
    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def trapezEinSeiteSenkrecht(a=7,c=3,d=4,aStr='7',bStr='',cStr='3',dStr='5',zeichneX=False):
#Diese Funktion zeichnet ein Trapez, bei dem eine Seite Senkrecht steht, d.h. die Höhe ist.
#Beispiel:
#          D     d      C
#           ------------
#           |           \
#        c=h|            \b
#           |             \
#           ----------------
#          A        a        B
    tikzcommand=[]
    A=[0,0]
    B=[a,0]
    C=[d,c]
    D=[0,c]
    X=[d,0] if a>d else [a,c]
    Y=[d,c] if a>d else [a,0]
    Z=[a,0] if a>d else [d,c]
    x='c' if len(bStr)==0 or len(cStr)==0 else ''
    y=''  if len(bStr)==0 or len(cStr)==0 else 'x'
    yPos='below' if a>d else 'above'
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append('\\draw[black, very thick] ('+str(A[0])+'cm,'+str(A[1])+'cm) -- node[below] {'+aStr+'} ('+str(B[0])+'cm,'+str(B[1])+'cm);')
    tikzcommand.append('\\draw[black, very thick] ('+str(B[0])+'cm,'+str(B[1])+'cm) -- node[right] {'+bStr+'} ('+str(C[0])+'cm,'+str(C[1])+'cm);')
    tikzcommand.append('\\draw[black, very thick] ('+str(C[0])+'cm,'+str(C[1])+'cm) -- node[above] {'+dStr+'} ('+str(D[0])+'cm,'+str(D[1])+'cm);')
    tikzcommand.append('\\draw[black, very thick] ('+str(D[0])+'cm,'+str(D[1])+'cm) -- node[left] {'+cStr+'} ('+str(A[0])+'cm,'+str(A[1])+'cm);')
    if zeichneX:
        tikzcommand.append(F'\\draw[red, very thick] ({str(X[0])}cm,{str(X[1])}cm) -- node[left] {{{x}}} ({str(Y[0])}cm,{str(Y[1])}cm);')
        tikzcommand.append(F'\\draw[red, very thick] ({str(X[0])}cm,{str(X[1])}cm) -- node[{yPos}] {{{y}}} ({str(Z[0])}cm,{str(Z[1])}cm);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def dreieckMitHalbkreis(kx=3,ky=2,seiten=[],mitUmrandung=True,ohneHyp=True,hypRot=True):
#Diese Funktion zeichnet ein Dreieck, bei dem die Hypotynuse durch ein Halbkreis ersetzt ist.
#Die Seite a ist dabei die Hypotynuse, b ist die Kathe in y Richtung (=ky) und c die Hypotynuse in x Richtung (=kx)
    c=(kx**2+ky**2)**0.5
    if len(seiten)==0:
        seiten=[strNW(c,runden=True),strNW(ky,True),strNW(kx,True)]
    rechtWinkBei = 'alpha'
    tikzcommand=[]
    if mitUmrandung:
        tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\coordinate (a) at ({0},{0});')
    tikzcommand.append(F'\\coordinate (b) at ({kx},{ky});')
    tikzcommand=tikzcommand+dreieckRechtwinklig(kx=kx,ky=ky,rotWinkel=0,mitBogen=False,seiten=seiten,rechtWinkBei=rechtWinkBei,mitUmrandung=False)
    if ohneHyp:
        tikzcommand[-5]=''
    if hypRot:
        tikzcommand[-5]=tikzcommand[-5].replace('black','red')
    alpha= round(math.degrees(math.asin(ky/c)), 6)
#Siehe:https://tex.stackexchange.com/questions/66216/draw-arc-in-tikz-when-center-of-circle-is-specified/66219#66219
#Der Halbbogen wird gezeichnet, von -alpha bis (180-alpha) mit dem Radius c/2 um den Mittelpunkt kx/2 und ky/2
#Dabei ist z.B. -alpha:c/2 eine Polarkoordinate
    tikzcommand.append(F'\\draw[thick, black]([shift = (-{alpha}:{c/2}cm)]{kx/2}, {ky/2}) arc(-{alpha}: {180-alpha}:{c/2}cm);')
#    tikzcommand.append(F'\\node[thick, red] at ({kx/2}cm, {ky/2}cm) {{$\\cdot$}};')
    if mitUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def zeichneKreis(r=2,alpha=360,mitUmrandung=True):
#Diese Funktion erzeugt einen Kreis oder Kreisabschnitt mit eingetragenem Winkel und radius.
#Aufruf:
#              tikzcommand=zeichneKreis(r=2,alpha=270,mitUmrandung=True)
    tikzcommand=[]
    radiusWinkel=random.randint(0,360)
    if mitUmrandung:
        tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        tikzcommand.append('\\noindent\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick, black] (0,0) -- node[below]{{r={strNW(r)}cm}} (0:{r}cm) arc(0:{alpha}:{r}cm) -- (0,0) ;')
    if alpha<360:
        tikzcommand.append(F'\\draw[thick, black] (0:0.7cm) arc(0:{alpha}:0.7cm) ;')
        tikzcommand.append(F'\\node at ({alpha/2}:0.35cm) {{{alpha}circ}} ;'.replace('circ','$^\\circ$'))

    if mitUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
