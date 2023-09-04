#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def datenQuartilAuswertung(werte=[list(range(1,13+1))],RS=True):
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand=tikzcommand+tikzTabelle(tabelle=werte,dim=[1.0,0.5],mitUmrandung=False)
    n=len(werte[0])
    dy=len(werte)*0.5
    if RS:
        tikzcommand.append(F'\\draw[thick,->] ({n/2},-{dy}) -- ({n/2},-{dy+1.5+ (0 if n>5 else 0.5)}) node[below] {{Zentralwert}};')
        quBraceX,qoBraceX= (n/2,n/2) if n%2==0 else (int(n/2),int(n/2)+1)
        tikzcommand.append(F'\\draw [blue, thick, decoration={{brace, mirror,raise=0cm,amplitude=0.5cm}},decorate] (0,-{dy}) -- ({quBraceX},-{dy});')
        tikzcommand.append(F'\\draw [violet, thick, decoration={{brace, mirror,raise=0cm,amplitude=0.5cm}},decorate] ({qoBraceX},-{dy}) -- ({len(werte[0])},-{dy});')
        quX, qoX = (int(n / 4), math.ceil(n *3/ 4 -0.1)) if n % 4 < 2 else (int(n / 4)+0.5, int(n*3/ 4) + 0.5)
        tikzcommand.append(F'\\draw[blue,thick,->] ({quX},-{dy}) -- ({quX},-{dy+1.0}) node[below] {{Unteres Quartil}};')
        tikzcommand.append(F'\\draw[violet,thick,->] ({qoX},-{dy}) -- ({qoX},-{dy+1.0+ (0 if n>5 else 0.5)}) node[below] {{Oberes Quartil}};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand