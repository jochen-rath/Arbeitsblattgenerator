#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import math

def quadernetz(a=3, b=2, c=1):
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw (0,0) rectangle ++({a},{b}); ')
    tikzcommand.append(F'\\draw (0,0) rectangle ++({-c},{b}); ')
    tikzcommand.append(F'\\draw ({a},{0}) rectangle ++({c},{b}); ')
    tikzcommand.append(F'\\draw ({0},{b}) rectangle ++({a},{c}); ')
    tikzcommand.append(F'\\draw ({0},{0}) rectangle ++({a},{-c}); ')
    tikzcommand.append(F'\\draw ({a+c},{0}) rectangle ++({a},{b}); ')
    tikzcommand.append(F'\\node[below] at ({a/2},{0}) {{a={a} cm}}; ')
    tikzcommand.append(F'\\node[left] at ({0},{b/2}) {{b={b} cm}}; ')
    tikzcommand.append(F'\\node[below] at ({-c/2},{0}) {{c={c} cm}}; ')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def dreiecksPrismaNetz(a=3, b=3, c=3,hK=4):
    # Beispiel
    #
    #             / \
    #          b /   \a
    #           /     \
    #   ------ ------- ----------
    #  |       |   c   |         |
    #  |       |       |         |
    #  |       |       |         |hK
    #  |       |       |         |
    #   ------ ------- ----------
    #           \    /
    #            \  /
    #             \/
    #
    if abs((a**2-b**2-c**2)/(-2*b*c))>1:
        alpha=-1
    else:
        alpha=math.degrees(math.acos((a**2-b**2-c**2)/(-2*b*c)))
    if alpha<0:
        return ['Dreieck nicht darstellbar.']
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw ({c},{0}) -- ++({-c},{0}) -- ++({alpha}:{b}) -- cycle;')
    tikzcommand.append(F'\\draw (0,0) rectangle ++({c},{-hK}); ')
    tikzcommand.append(F'\\draw (0,0) rectangle ++({-b},{-hK}); ')
    tikzcommand.append(F'\\draw ({c},{0})rectangle ++({a},{-hK}); ')
    tikzcommand.append(F'\\draw ({c},{-hK}) -- ++({-c},{0}) -- ++({-alpha}:{b}) -- cycle;')

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
