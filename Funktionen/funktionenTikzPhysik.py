#!/usr/bin/env python
# coding: utf8
import math
import random


#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Proportionalitätsrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def bogenlaengeSpirale(p,a):
    return (a/2)*(p*((1+p**2)**0.5)+math.log(p+(1+p**2)**0.5))
def erzeugeAtom(n=11,massenzahl=0,ion=0,pfeile=False):
#Hintergrund: Die Protonen und Neutronen werden auf einer Spirale angeordnent.
#Damit die sich zufällig überlagern und die Spiralform nicht erkennbar ist, wird die Liste der
#Spiralpositionen gemischt.
#Aufruf:
#       tikzCommand=erzeugeAtom(n,massenzahl,ion)
#           n=Kernladungszahl
#  massenzahl=2*n+massenzahl wenn massenzahl kleiner als n ist, sonst n
#         ion=Anzahl Elektronen = n+ion
#if True:
    massenzahl=2*n+massenzahl if massenzahl < n else massenzahl
    a=0.00075  #Durch Versuch bestimmt
    minAbstand=0.01
    anzahlElektroneProSchale=[2*i**2 for i in range(10)]
    anzahlGesElektronen=[sum(anzahlElektroneProSchale[0:i]) for i in range(len(anzahlElektroneProSchale))][1:]
    anzahlSchalen=anzahlGesElektronen.index(next(x for x in anzahlGesElektronen if x>=n+ion))
#Bestimme Winkel auf Spirale. Alle Atome gleichen Abstand auf Spirale zueinander.
    winkel=[0]
    for i in range(massenzahl):
        winkel2=winkel[-1]+1
        while bogenlaengeSpirale(math.radians(winkel2),a)-bogenlaengeSpirale(math.radians(winkel[-1]),a)<minAbstand:
            winkel2=winkel2+1
        winkel.append(winkel2)
    winkel=winkel[1:]    #Winkel 0  nicht sichtbar
    maxR=winkel[-1]*a
    random.shuffle(winkel)
    teilchen=[F"\\proton({phi})" for phi in winkel[:n]]+[F"\\neutron({phi})" for phi in winkel[n:]]
#Pfeile für Loesung:
    protonPfeilWinkel=winkel[:n]
    neutronPfeilWinkel=winkel[n:]
    random.shuffle(teilchen)
    tikzcommand=[]
    tikzcommand.append("\\definecolor{myyellow}{RGB}{254,241,24}")
    tikzcommand.append("\\definecolor{myorange}{RGB}{234,125,1}")
    tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    tikzcommand.append('\\begin{tikzpicture}')
    tikzcommand.append("\\def\\proton(#1){%")
    tikzcommand.append(F"    \\fill[ball color=myyellow]  (#1:{a}*#1) circle (0.3 cm);")
    tikzcommand.append(F"    \\node at (#1:{a}*#1) {{\\texttt{{+}}}};")
    tikzcommand.append("}")
    tikzcommand.append("\\def\\neutron(#1){%")
    tikzcommand.append(F"    \\fill[ball color=myorange]  (#1:{a}*#1) circle (0.3 cm);")
    tikzcommand.append("}")
    tikzcommand.append("\\def\\electron{%")
    tikzcommand.append("    \\fill[ball color=gray!30] (0,0) circle (5pt);")
    tikzcommand.append("    \\node at (0,0) {\\texttt{-}};")
    tikzcommand.append("}")
    for element in teilchen:
        tikzcommand.append(element)
    if False:
        tikzcommand.append("\\foreach \\x in {0, 1, ..., 1000}")
        tikzcommand.append(F"    \\node at(\\x: {a}*\\x) {{.}};")
#Zeichne zuerst alle vollen Schalen
    for i in range(anzahlSchalen-1):
        tikzcommand.append("\\draw[")
        tikzcommand.append("  postaction=decorate,")
        tikzcommand.append("  decoration={markings, ")
        for j in range(anzahlElektroneProSchale[i+1]):
            tikzcommand.append(F"  mark=at position {j/anzahlElektroneProSchale[i+1]} with {{\\electron}},")
        tikzcommand.append("}] ")
        tikzcommand.append(F"  (0,0) circle ({maxR+i}+1);")
#Dann die letzte:
    restElektronen=n+ion-sum(anzahlElektroneProSchale[0:anzahlSchalen])
    tikzcommand.append("\\draw[")
    tikzcommand.append("  postaction=decorate,")
    tikzcommand.append("  decoration={markings, ")
    for j in range(restElektronen):
        tikzcommand.append(F"  mark=at position {j/restElektronen} with {{\\electron}},")
    tikzcommand.append("}] ")
    tikzcommand.append(F"  (0,0) circle ({maxR+anzahlSchalen}+1);")
    if pfeile:
        for i in range(n):
            tikzcommand.append(F'\draw[<-,line width=2pt,red] ({protonPfeilWinkel[i]}:{a*protonPfeilWinkel[i]}) to ++({protonPfeilWinkel[i]}:{a*protonPfeilWinkel[i]+2}) node {{\LARGE {i+1}}} ;')
        for i in range(len(neutronPfeilWinkel)):
            tikzcommand.append(F'\draw[<-,line width=2pt,blue] ({neutronPfeilWinkel[i]}:{a*neutronPfeilWinkel[i]}) to ++({neutronPfeilWinkel[i]}:{a*neutronPfeilWinkel[i]+2}) node {{\LARGE {i+1+n}}} ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand