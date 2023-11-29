#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenTikzZeichnungen.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
import math
import random


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
