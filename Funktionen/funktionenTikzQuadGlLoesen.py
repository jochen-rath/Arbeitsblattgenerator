#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, die zur Erstellung einer Latex tex-Datei benötigt werden.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def quadFktnullStellenBerechPQFormel(fkt='2*(x-2)**2-5',vari='x',mitTikzUmrandung=True,scheitelform=True):
    pL=gebePolynomVarisAus(poly=fkt,x=vari)
    latexcommand=[]
    if mitTikzUmrandung:
        latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[below right] at (0,0.1) {')  
        latexcommand.append('$\\begin{aligned}')
    if scheitelform:
        latexcommand.append(F'{ersetzePlatzhalterMitSymbolen(str(fkt).replace(".",","))}&=0 & \quad & \\mid \\mbox{{Vereinfachen}} \\\\')
    fkt=str(sympy.expand(fkt))
    if not eval(pL[0])==1:
        latexcommand.append(F'{ersetzePlatzhalterMitSymbolen(setzePolyListeZusammenLatexAusgabe(pL))}&=0 & \quad & \\mid~:{"" if pL[0][0]=="+" else "("}{pL[0][1:].replace(".",",") if pL[0][0]=="+" else pL[0].replace(".",",")}{"" if pL[0][0]=="+" else ")"} \\\\')
#p,q Formel
    pL=[str(eval(F'{x}/{pL[0]}')) for x in pL]
    latexcommand.append(F'{ersetzePlatzhalterMitSymbolen(setzePolyListeZusammenLatexAusgabe(pL))}&=0 & \quad & \\mid \\mbox{{p,q Formel}}\\\\')
    latexcommand.append(F'x_{{1,2}}&=-\\frac{{{strNW(float(pL[1]),True)}}}{{2}} \\pm\\sqrt{{\\left(\\frac{{{strNW(float(pL[1]),True)}}}{{2}}\\right)^2{"+" if float(pL[2])<0 else "-"}{strNW(abs(float(pL[2])),True)}}} & & \\\\')
    latexcommand.append(F'x_{{1}}&={strNW(eval(f"-{pL[1]}/2+(({pL[1]}/2)**2-{pL[2]})**0.5"),True)} && \\\\')
    latexcommand.append(F'x_{{2}}&={strNW(eval(f"-{pL[1]}/2-(({pL[1]}/2)**2-{pL[2]})**0.5"),True)} && \\\\')
    if mitTikzUmrandung:
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand