#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
import math
import random

def dracheFuerFlaechenBer(e=4,f=2,dx=1,drehung=0,mitBeschr=True,mitEundF=True):
#rotate in draw geht nur mit relativen Koordinaten und nicht, wenn die Koordinaten mit
#\cordinate (A) at (0,0);vorher definiert werden.
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    if mitEundF:
        tikzcommand.append(F'\\draw[thick,dashed,black,rotate={drehung}] (0,0) -- node{{{F"e={strNW(e)} cm" if mitBeschr else ""}}} ++({e},0);')
        tikzcommand.append(F'\\draw[thick,dashed,rotate={drehung}] ({dx},{f/2}) -- node[above]{{{F"f={strNW(f)} cm" if mitBeschr else ""}}} ++(0,{-f});')
    tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] (0,0) -- ++({dx},{f/2}) -- ++({e-dx},{-f/2}) -- ++({-e+dx},{-f/2}) --cycle;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def parallogrammFuerFlaechenBer(g=4,h=2,dx=2,drehung=0,mitBeschr=True):
#rotate in draw geht nur mit relativen Koordinaten und nicht, wenn die Koordinaten mit
#\cordinate (A) at (0,0);vorher definiert werden.
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(
        F'\\draw[thick,black,rotate={drehung}] (0,0) -- node{{{F"g={strNW(g)} cm" if mitBeschr else ""}}} ++({g},0) -- ++({dx},{h}) -- ++({-g},0) --cycle;')
    if mitBeschr:
        tikzcommand.append(F'\\draw[dashed,black,rotate={drehung}] ({g/2},0)  -- node{{h={strNW(h)} cm}} ++(0,{h});')
        if dx>g/2:
            tikzcommand.append(F'\\draw[dashed,black,rotate={drehung},red] ({g/2},{h})  -- ++({dx-g/2},0);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def trapezFuerFlaechenBer(a=5,c=2,h=3,dx=1,drehung=0,mitBeschr=True):
#rotate in draw geht nur mit relativen Koordinaten und nicht, wenn die Koordinaten mit
#\cordinate (A) at (0,0);vorher definiert werden.
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] (0,0) -- node[below]{{{F"a={strNW(a)} cm" if mitBeschr else ""}}} ++({a},{0}) -- ++({-dx},{h}) --node[below]{{{F"c={strNW(c)} cm" if mitBeschr else ""}}} ++({-c},{0}) --cycle;')
    if mitBeschr:
        tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] ({a-c-dx},0) --node[left]{{{F"h={strNW(h)} cm" if mitBeschr else ""}}}  ++(0,{h});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
def pfeilFlaechenBer(a=4,b=1.4,g=2.8,h=2,z=0.7,lsg=False):
    if lsg:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=['\\begin{tikzpicture}']
    tikzcommand.append(F'\\draw[thick] (0,0) coordinate(A)-- ++({a},{0})coordinate(B) -- ++({0},{-z})coordinate(C) -- ++({h},{g/2})coordinate(D) -- ++({-h},{g/2})coordinate(E) -- ++({0},{-z})coordinate(F) -- ++({-a},{0})coordinate(G) -- cycle; ')
    tikzcommand.append(F'\\node[{"above" if lsg else "below"}] at ($(G)!0.5!(F)$){{{"a=" if lsg else ""}{strNW(a)} cm}} ;')
    if lsg:
        tikzcommand.append(F'\\draw (C) --node[above] {{g={strNW(g)} cm}} (E);')
        tikzcommand.append(F'\\draw (D) --node[below] {{h={strNW(h)} cm}} ++(-{h},0) coordinate(H);')
#        tikzcommand.append(F'\\pic [draw,very thick, -,angle radius=0.5cm, $\\boldsymbol{{\cdot}}$] {{angle = D--H--B}};')
        tikzcommand.append(F'\\pic [draw, -,angle radius=0.5cm] {{angle = B--H--D}};')
        tikzcommand.append(F'\\node[left] at ($(A)!0.5!(G)$){{b={strNW(b)} cm}} ;')
        tikzcommand.append(F'\\node[red] at ($(A)!0.5!(F)$) {{$A_R$}};')
        tikzcommand.append(F'\\node[red] at ($(H)!0.5!(D)$) {{$A_D$}};')
    else:
        tikzcommand.append(F'\\draw[|<->|] ({0},{-z - 0.2}) -- node[below] {{{strNW(a+h)} cm}} ++({a+h},0);')
        tikzcommand.append(F'\\draw[dashed]  (A) -- ++({0},{-z - 0.2}) ;')
        tikzcommand.append(F'\\draw[dashed]  (D) -- ++({0},{-g/2 - 0.2}) ;')
        tikzcommand.append(F'\\draw[|<->|] ({a+h+0.2},{-z}) -- node[right] {{{strNW(g)} cm}} ++(0,{g});')
        tikzcommand.append(F'\\draw[|<->|] ({a-0.2},{-z}) -- node[left] {{{strNW(z)} cm}} ++(0,{z});')
        tikzcommand.append(F'\\draw[|<->|] ({a-0.2},{g-2*z}) -- node[left] {{{strNW(z)} cm}} ++(0,{z});')

    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
