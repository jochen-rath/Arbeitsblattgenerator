#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import math


def quadernetz(a=3, b=2, c=1,ursprung=[0,0],buchstabe='Q',aName='a',bName='b',cName='c',mitTikzUmrandung=True):
#
    if mitTikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=[]
    tikzcommand.append(F'\\coordinate ({buchstabe}1) at ({ursprung[0]},{ursprung[1]}); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}2) at ($({buchstabe}1)+({a},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}3) at ($({buchstabe}2)+({c},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}4) at ($({buchstabe}3)+({a},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}5) at ($({buchstabe}4)+({0},{b})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}6) at ($({buchstabe}5)+({-a},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}7) at ($({buchstabe}6)+({-c},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}8) at ($({buchstabe}7)+({-a},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}9) at ($({buchstabe}8)+({-c},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}10) at ($({buchstabe}9)+({0},{-b})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}11) at ($({buchstabe}1)+({0},{-c})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}12) at ($({buchstabe}2)+({0},{-c})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}13) at ($({buchstabe}7)+({0},{c})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}14) at ($({buchstabe}8)+({0},{c})$); ')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- node[below] {{{aName}}} ({buchstabe}2);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}2) -- node[below] {{{cName}}} ({buchstabe}3);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}3) -- ({buchstabe}4);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}4) -- ({buchstabe}5);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}5) -- ({buchstabe}6);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}6) -- ({buchstabe}7);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}7) -- ({buchstabe}8);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}8) -- ({buchstabe}9);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}9) -- ({buchstabe}10);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}10) -- ({buchstabe}1);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- ({buchstabe}8);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}2) -- node[left] {{{bName}}} ({buchstabe}7);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}3) -- ({buchstabe}6);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- ({buchstabe}11);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}2) -- ({buchstabe}12);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}11) -- ({buchstabe}12);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}7) -- ({buchstabe}13);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}8) -- ({buchstabe}14);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}13) -- ({buchstabe}14);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand




def dreiecksPrismaNetz(a=3, b=3, c=3,hK=4,ursprung=[0,0],buchstabe='Q',aName='a',bName='b',cName='c',hkName='$h_K$',mitTikzUmrandung=True):
    # Beispiel:
    #              Q3
    #              #
    #             / \
    #          b /   \a
    #           /     \
    #  Q9------ ------- ---------Q7
    #  |      Q1  c    Q2        |
    #  |       |       |         |
    #  |       |       |         |
    #  |      Q4       Q5        |
    #  Q10----- ------- ---------Q8
    #           \    /
    #            \  /
    #             \/
    #              Q6
    if abs((a**2-b**2-c**2)/(-2*b*c))>1:
        alpha=-1
    else:
        alpha=math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c)))
    if alpha<0:
        return ['Dreieck nicht darstellbar.']
    if mitTikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=[]
    tikzcommand.append(F'\\coordinate ({buchstabe}1) at ({ursprung[0]},{ursprung[1]}); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}2) at ($({buchstabe}1)+({c},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}3) at ($({buchstabe}1)+({alpha}:{b})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}4) at ($({buchstabe}1)+({0},{-hK})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}5) at ($({buchstabe}2)+({0},{-hK})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}6) at ($({buchstabe}4)+({-alpha}:{b})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}7) at ($({buchstabe}2)+({a},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}8) at ($({buchstabe}5)+({a},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}9) at ($({buchstabe}1)+({-b},{0})$); ')
    tikzcommand.append(F'\\coordinate ({buchstabe}10) at ($({buchstabe}4)+({-b},{0})$); ')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- node[below] {{{cName}}} ({buchstabe}2);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}2) -- node[midway, sloped, above] {{{aName}}} ({buchstabe}3);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- node[midway, sloped, above] {{{bName}}} ({buchstabe}3);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}2) -- node [left] {{{hkName}}}({buchstabe}5);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- ({buchstabe}4);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}4) -- ({buchstabe}5);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}4) -- ({buchstabe}6);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}5) -- ({buchstabe}6);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}2) -- ({buchstabe}7);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}7) -- ({buchstabe}8);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}5) -- ({buchstabe}8);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}1) -- ({buchstabe}9);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}4) -- ({buchstabe}10);')
    tikzcommand.append(F'\\draw[thick] ({buchstabe}9) -- ({buchstabe}10);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def gleichseitigesPrismaNEcken(l=3,n=5,hK=5):
    if n<3:
        return ['Zu wenige Ecken']
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw [thick] ({l},0) -- ++{"-- ++".join([F"({i}*{360/n}:{l})" for i in range(1,n)])};')
    tikzcommand.append(F'\\draw [thick] ({l},{-hK}) -- ++{"-- ++".join([F"({-i}*{360/n}:{l})" for i in range(1,n)])};')
    for i in range(n):
        tikzcommand.append(F'\\draw [thick] ({(i-int(n/2))*l},0) -- ++({l},0)-- ++(0,{-hK}) --++({-l},0);')
    tikzcommand.append(F'\\draw [thick] ({(-int(n/2))*l},0) -- node[left] {{$h_K$}} ++(0,{-hK});')
    tikzcommand.append(F'\\draw [thick] (0,0) -- node[below] {{l}} ({l},0);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
