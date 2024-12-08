#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())


def dreieckRechtw(k=[5,6],label=['5 dm','6 dm',''],mitBogen=True):
    dR=random.randint(0,360)
    ur=[random.randint(0,10)/10,random.randint(0,10)/10]
    hyp=(k[0]**2+k[1]**2)**0.5
    winkel=90
    seitenPos={'a':'above,sloped','b':'above,sloped','c':'below,sloped'}
#l1 ist immer die Seite links von dem Winkel, gedreht gegen Uhrzeigersinn.
#Beschriftungen
#Dreieck zeichnen
    sL=['']*len(label)
    for i,l in enumerate(label):
        sL[i]=f'node[above,sloped]{{{l}}}'
    tikzcommand=[f'\\coordinate (E) at ({ur[0]},{ur[1]});']
    tikzcommand.append(f'\\coordinate (F) at ($(E)+({dR}:{k[0]})$);')
    tikzcommand.append(f'\\coordinate (G) at ($(F)+({dR+winkel}:{k[1]})$);')
    tikzcommand.append(f'\\draw (E) coordinate -- {sL[0]} (F) -- {sL[1]} (G)   --{sL[2]} (E);')
    if mitBogen:    
        tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.6cm, "•"] {{angle = G--F--E}};')        
    return erzeugeTikzUmrandung(tikzcommand)

    