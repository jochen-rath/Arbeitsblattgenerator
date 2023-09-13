#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def einstufierZufallversuch(erg={'1':'1/6','2':'1/6','3':'1/6','4':'1/6','5':'1/6','6':'1/6',},mitText=True):
    dx=3
    W=list(erg.keys())
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,pattern=north west lines, pattern color=black!40] ({0},{0}) circle ({0.5}) ;  ')
    tikzcommand.append(F'\\coordinate (0) at (0,0);')
    for i,w in enumerate(W):
        tikzcommand.append(F'\\node[draw,circle] ({i+1}) at ({dx}cm,{0.5*len(W)-i-(0.5 if len(W)%2==0 else 0)}cm) {{{w}}};')
    for i,w in enumerate(W):
        tikzcommand.append(F'\\draw [->] (0,0) to ({i+1}) ;')
        tikzcommand.append(F'\\node at ($(0)!{0.55+(0.05*(i%2))}!({i+1})$) {{${erzeugeLatexFracAusdruck(erg[w])}$}};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand