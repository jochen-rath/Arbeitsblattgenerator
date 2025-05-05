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
    tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] (0,0) -- node[below,rotate={drehung}] {{{F"g={strNW(g)} cm" if mitBeschr else ""}}} ++({g},0) -- ++({dx},{h}) coordinate(C) --cycle;')
#    tikzcommand.append(F'\\draw[thick,black] ({drehung}:{dx}) -- node{{{F"g={strNW(g)} cm" if mitBeschr else "" }}} ({drehung}:{dx+g});')
#    tikzcommand.append(F'\\draw[thick,black] ({drehung}:{dx})  -- ({drehung+90}:{h});')
#    tikzcommand.append(F'\\draw[thick,black] ({drehung}:{dx+g})  -- ({drehung+90}:{h});')
    if mitBeschr:
        tikzcommand.append(F'\\draw[dashed,black] (C)  -- node[rotate={drehung}]{{h={strNW(h)} cm}} ++({drehung-90}:{h}) coordinate(H);')
        tikzcommand.append(F'\\draw[dashed,black] (H)  -- ++({drehung}:{-dx});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def dracheFuerFlaechenBer(e=4,f=2,dx=1,drehung=0,mitBeschr=True,mitEundF=True):
#rotate in draw geht nur mit relativen Koordinaten und nicht, wenn die Koordinaten mit
#\cordinate (A) at (0,0);vorher definiert werden.
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    if mitEundF:
        tikzcommand.append(F'\\draw[thick,dashed,black,rotate={drehung}] (0,0) -- node[rotate={drehung}]{{{F"e={strNW(e)} cm" if mitBeschr else ""}}} ++({e},0);')
        tikzcommand.append(F'\\draw[thick,dashed,rotate={drehung}] ({dx},{f/2}) -- node[above,rotate={drehung}]{{{F"f={strNW(f)} cm" if mitBeschr else ""}}} ++(0,{-f});')
    tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] (0,0) -- ++({dx},{f/2}) -- ++({e-dx},{-f/2}) -- ++({-e+dx},{-f/2}) --cycle;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def parallogrammFuerFlaechenBer(g=4,h=2,dx=2,drehung=0,mitBeschr=True):
#rotate in draw geht nur mit relativen Koordinaten und nicht, wenn die Koordinaten mit
#\cordinate (A) at (0,0);vorher definiert werden.
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(
        F'\\draw[thick,black,rotate={drehung}] (0,0) -- node[below,rotate={drehung}] {{{F"g={strNW(g)} cm" if mitBeschr else ""}}} ++({g},0) -- ++({dx},{h}) -- ++({-g},0) --cycle;')
    if mitBeschr:
        tikzcommand.append(F'\\draw[dashed,black,rotate={drehung}] ({g/2},0)  -- node[right,rotate={drehung}]{{h={strNW(h)} cm}} ++(0,{h});')
        if dx>g/2:
            tikzcommand.append(F'\\draw[dashed,black,rotate={drehung},red] ({g/2},{h})  -- ++({dx-g/2},0);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def trapezFuerFlaechenBer(a=5,c=2,h=3,dx=1,drehung=0,mitBeschr=True):
#rotate in draw geht nur mit relativen Koordinaten und nicht, wenn die Koordinaten mit
#\cordinate (A) at (0,0);vorher definiert werden.
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] (0,0) -- node[below,rotate={drehung}]{{{F"a={strNW(a)} cm" if mitBeschr else ""}}} ++({a},{0}) -- ++({-dx},{h}) --node[below,rotate={drehung}]{{{F"c={strNW(c)} cm" if mitBeschr else ""}}} ++({-c},{0}) --cycle;')
    if mitBeschr:
        tikzcommand.append(F'\\draw[thick,black,rotate={drehung}] ({a-c-dx},0) --node[left,rotate={drehung}]{{{F"h={strNW(h)} cm" if mitBeschr else ""}}}  ++(0,{h});')
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

def trapezMitTrapezenUmrandet(R=50,h=25,LSG=False):
    tikzcommand=[]
    tikzcommand.append("\\begin{tikzpicture}")
    tikzcommand.append("%Ich rechne mal sqrt(0.75) da hier ein gleichseitiges Dreieck vorliegt, bei dem man die Höhe berechnen muss.")
    tikzcommand.append("%Dies geht mit dem Pythagoras, wobei der durch die Hälfte der Seite geht:")
    tikzcommand.append("%               a²+b²=c² mit a=c/2 --> b²=c²-(c/2)²=c²-c²/4=3/4*c² --> b=c*sqrt(3/4)")
    tikzcommand.append("%Flächenberechnung grün-blau in Python:")
    tikzcommand.append("%R,h=50,25")
    tikzcommand.append("%2*((2*R-R)*R*(0.75**0.5)/2)-6*((R+h*(0.75**0.5))-R)*h/2")
    tikzcommand.append(F"  \\pgfmathsetmacro{{\\hWert}}{{{h}}}")
    tikzcommand.append(F"  \\pgfmathsetmacro{{\\RWert}}{{{R}}}")
    tikzcommand.append("  \\pgfmathsetmacro{\\dh}{\\hWert/100*4}")
    tikzcommand.append("  \\pgfmathsetmacro{\\R}{\\RWert/100*4}")
    tikzcommand.append("  \\pgfmathsetmacro{\\dR}{\\dh/sqrt(0.75)}")
    tikzcommand.append("  \\pgfmathsetmacro{\\hges}{(\\R+\\dR)*sqrt(0.75)}")
    tikzcommand.append("  \\pgfmathsetmacro{\\h}{\\hges-\\dh}")
    tikzcommand.append("%Schreibe ohne Komma")
    tikzcommand.append("  \\pgfmathtruncatemacro\\gesamthoehe{2*(\\RWert*sqrt(0.75)+\\hWert)}")
    tikzcommand.append("  \\pgfmathtruncatemacro\\aussenlaenge{\\RWert+\\hWert/sqrt(0.75)}")
    tikzcommand.append("  \\pgfmathtruncatemacro\\innenlaenge{2*\\RWert}")
    tikzcommand.append("  \\pgfmathtruncatemacro\\innenhoehe{\\RWert*sqrt(0.75)}")
    tikzcommand.append("\\foreach \\rot in  {0,60,...,360}{")
    tikzcommand.append("\\draw[black,rotate=\\rot,fill=blue!60] (\\R,0) -- ++(\\dR,0) -- ++(120:\\R+\\dR) -- ++(60:-\\dR) -- cycle;")
    tikzcommand.append("}")
    tikzcommand.append("\\draw[black,fill=green] (\\R,0) -- ++(120:\\R) -- ++(180:\\R) -- ++(240:\\R) -- ++(120:-\\R) -- ++(0:\\R) -- cycle ;")
    if LSG:
        tikzcommand.append("\\draw[thick,<->] (-\\R,0) --node[below] {$a_1=\\innenlaenge~cm$} (\\R,0);")
        tikzcommand.append("\\draw[thick,<->] (240:\\R+\\dR+0.1) --node[below] {$a_2=\\aussenlaenge~cm$}  (300:\\R+\\dR+0.1);")
        tikzcommand.append("\\draw[thick,<->] (0,-\\h) --node[right] {$h_2=\\hWert~cm$} (0,-\\hges);")
        tikzcommand.append("\\draw[thick,<->] (0,0) --node[right] {$h_1=\\innenhoehe~cm$} (0,\\h);")
        tikzcommand.append("\\draw[thick,<->] (240:\\R-0.1) --node[above] {$c_2=\\RWert cm$}  (300:\\R-0.1);")
        tikzcommand.append("\\draw[thick,<->] (60:\\R-0.1) --node[above] {$c_1=\\RWert cm$}  (120:\\R-0.1);")
    else:
        tikzcommand.append("\\draw[thick,<->] (-\\R,0) --node[below] {\\innenlaenge~cm} (\\R,0);")
        tikzcommand.append("\\draw[thick,<->] (\\R+\\dR+0.2,\\hges) --node[right] {\\gesamthoehe~cm} (\\R+\\dR+0.2,-\\hges) ;")
        tikzcommand.append("\\draw[thick,<->] (240:\\R-0.1) --node[above] {\\RWert cm}  (300:\\R-0.1);")
        tikzcommand.append("\\draw[thick,<->] (240:\\R+\\dR+0.1) --node[below] {\\aussenlaenge~cm}  (300:\\R+\\dR+0.1);")
        tikzcommand.append("\\draw[thick,<->] (0,\\h) --node[right] {\\hWert~cm} (0,\\hges);")
    tikzcommand.append("\\end{tikzpicture}")
    return tikzcommand

def halbkreisAufQuadrat(a=4,einheit='cm',mitLsg=False):
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(f"\\draw[thick] (0,0) coordinate(A) -- node[below]{{$a={strNW(a)}~{einheit}$}} ({a},0) coordinate(B) -- ({a},{a}) coordinate(C)  (0,{a}) coordinate (D) -- node[left]{{a}} (0,0);")
    tikzcommand.append(f"\\draw[thick] (D) arc (180:0:{a/2});")
    if mitLsg:
        tikzcommand.append(f"\\draw[thick] (D) -- (C);")
        tikzcommand.append(f"\\draw[thick,red] ({a/2},{a}) -- node[below]{{r={strNW(a/2)}~{einheit}}} (C);")
    tikzcommand.append("\\end{tikzpicture}")
    return tikzcommand
