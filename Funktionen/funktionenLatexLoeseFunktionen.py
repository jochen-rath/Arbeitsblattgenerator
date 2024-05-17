#!/usr/bin/env python
# coding: utf8
import random


#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Berechnung von Termen und Gleichungen


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def loeseFunktion(formel='W=G*p/100',varis={'W':[16,'Autos'],'G':[200,'Autos'],'p':[8,'\\%']},ges='p',breite=12,kommaAusgabe=False):
    geg=list(varis.keys())
    geg.remove(ges)
    lsg=[F'\\pbox{{{ breite} cm}}{{']
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,-0.25) {Geg.: };')
    nLsg=len(lsg)
    for x in geg:
        lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{${x}={strNW(varis[x][0],2)}~\\mbox{{{varis[x][1]}}}$}};')
    lsg.append(F'\\node[left] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{Ges.: }};')
    nLsg = nLsg+1
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{${ges} {"§§%" if ges=="p" else ""} = ?~\\mbox{{{varis[ges][1]}}} $}};'.replace('§§','\\'))
    lsg.append(F'\\node[below right] at (0,{-0.25-0.5*(len(lsg)-nLsg)}) {{')
    lsg.append('$\\begin{aligned}')
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1]} & &§§mid~\\mbox{{Einsetzen}} \\\\')
    for x in list(geg):
        formelStrNw=formel.replace(x,strNW(varis[x][0],True))
        formel=formel.replace(x,str(varis[x][0]))
#Steht der gesuchte Werte Links oder Rechts?
    if ges==formel.split("=")[0].replace(" ",""):
        lsg.append(F'{formelStrNw.split("=")[0]}&={formelStrNw.split("=")[1]} & & \\\\')
        lsg.append(F'{formelStrNw.split("=")[0]}&={strNW(eval(formel.split("=")[1]))}~\\mbox{{{varis[ges][1]}}}& &')
    else:
        if not str(sympy.sympify(formel.split("=")[1]))==formelStrNw.split("=")[1]:
            lsg.append(F'{formelStrNw.split("=")[0]}&={formelStrNw.split("=")[1]} & &§§mid~\\mbox{{Zusammenfassen}} \\\\')
            R=str(sympy.sympify(formel.split("=")[1]).evalf()) if kommaAusgabe else str(sympy.sympify(formel.split("=")[1]))
            formel=formel if not kommaAusgabe else F'{formel.split("=")[0]}={R}'
        lsg.append(F'{formelStrNw.split("=")[0]}&={str(sympy.sympify(formel.split("=")[1])).replace(".",",")} & &§§mid~\\mbox{{Umdrehen}} \\\\')
    #    lsg.append(F'{sympy.sympify(formelStrNw.split("=")[1])}&={formelStrNw.split("=")[0]} & & \\\\')
        glLsg = loeseGleichungEinfachMitEinerVariabel(G=F'{sympy.sympify(formel.split("=")[1])} = {formelStrNw.split("=")[0].replace(".","").replace(",",".")}', variable=ges, latexAusgabe=True,fracAmEnde=False)
        glLsg=glLsg[6:-3]
        glLsg[-1]=F'{glLsg[-1].split("&")[0]} {"§§%" if ges=="p" else ""}&{glLsg[-1].split("&")[1]}~\\mbox{{{varis[ges][1]}}}&{glLsg[-1].split("&")[2]}&{glLsg[-1].split("&")[3]}'.replace('§§','\\')
        lsg=lsg+glLsg
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    lsg.append('}')
    return lsg