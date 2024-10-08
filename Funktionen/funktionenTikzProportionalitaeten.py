#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Proportionalitätsrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def tikzPropTabelle(l=[4,8],r=[5,10],title=['Anzahl','\euro{}'],tikzUmrandung=True,mitPfeilen=True,mitBeschr=True,mitLsg=True,anitProp=False):
#Diese Funktion erzeugt eine Tikz-Zeichnung.
#Aufruf:
#   tikzPropTabelle(l,r,title,tikzUmrandung,mitPfeilen,mitBeschr,mitLsg):
    if tikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=['']
    op1='\\cdot' if l[1]/l[0] > 1 else ':'
    op2=op1 if not anitProp else ('\\cdot' if op1==':' else ':')
    wert= strNW(l[1]/l[0] if l[1]/l[0] > 1 else l[0]/l[1])

    tikzcommand.append('\\draw[black] (0cm,0cm) -- (0cm,-2cm);')
    tikzcommand.append('\\draw[black] (-2.5 cm,-0.5cm) -- (2.5cm,-0.5cm);')
    tikzcommand.append(F'\\node[below] at (-1.5 cm,0cm) {{{title[0]}}};')
    tikzcommand.append(F'\\node[below] at  (1.5 cm,0cm) {{{title[1]}}};')
    tikzcommand.append(F'\\node[circle] (A) at (-0.75 cm,-0.75cm) {{{l[0]}}};')
    tikzcommand.append(F'\\node[circle] (B) at (-0.75 cm,-1.75cm) {{{l[1]}}};')
    tikzcommand.append(F'\\node[circle] (C) at (0.75 cm,-0.75cm) {{{r[0]}}};')
    tikzcommand.append(F'\\node[circle] (D) at (0.75 cm,-1.75cm) {{{r[1] if mitLsg else "$~$"}}};')
    if mitPfeilen or mitLsg:
        tikzcommand.append(F'\\draw[->] (A) to [out=190,in=170] node[left] {{${(op1+wert) if mitBeschr or mitLsg else ""}$}}  (B) ;')
        tikzcommand.append(F'\\draw[->] (C) to  [out=350,in=10] node[right]  {{${(op2+wert) if mitBeschr or mitLsg else ""}$}}  (D) ;')
    if tikzUmrandung:
            tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def dreiSatz(links=['50','1','100'],rechts=['50','$\ $','$\ $'],title=['\%','\euro{}'],startPos=[0,0],operationLinks=[],tikzUmrandung=True,ohneKlammernRechts=False,ohneKlammernLinks=False,breit=False,antiProp=False):
#Diese Funktion erzeugt eine Tikz-Zeichnung zum Dreisatz.
#Aufruf:
#     tikzcommand=dreiSatz(links=['50','1','100'],rechts=['50','$\ $','$\ $'],title=['\%','\euro{}'],startPos=[0,0])
    if tikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=['']
    if len(operationLinks)==0:
        operationLinks=[links[0],links[2]]
    breite=2.5 if breit else 1.5
    tikzcommand.append(F'\\draw[black] ({startPos[0]}cm,{startPos[1]}cm) -- ({startPos[0]}cm,{startPos[1]-3}cm); ')
    tikzcommand.append(F'\\draw[black] ({startPos[0]-breite} cm,{startPos[1]-0.5}cm) -- ({startPos[0]+breite}cm,{startPos[1]-0.5}cm); ')
    if breit:
        tikzcommand.append(F'\\node[left] at ({startPos[0]} cm,{startPos[1]-0.25}cm) {{{title[0]}}};')
        tikzcommand.append(F'\\node[right] at ({startPos[0]} cm,{startPos[1]-0.255}cm) {{{title[1]}}};')
    else:
        tikzcommand.append('\\node[below] at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1])+'cm) {'+title[0]+'};')
        tikzcommand.append('\\node[below] at  ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1])+'cm) {'+title[1]+'};')
    tikzcommand.append('\\node[circle] (1) at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1]-0.75)+'cm) {'+links[0]+'};')
    tikzcommand.append('\\node[circle] (2) at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1]-1.75)+'cm) {'+links[1]+'};')
    tikzcommand.append('\\node[circle] (3) at ('+str(startPos[0]-0.75)+' cm,'+str(startPos[1]-2.75)+'cm) {'+links[2]+'};')
    tikzcommand.append('\\node[circle] (4) at ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1]-0.75)+'cm) {'+rechts[0]+'};')
    tikzcommand.append('\\node[circle] (5) at ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1]-1.75)+'cm) {'+rechts[1]+'};')
    tikzcommand.append('\\node[circle] (6) at ('+str(startPos[0]+0.75)+' cm,'+str(startPos[1]-2.75)+'cm) {'+rechts[2]+'};')
    if not ohneKlammernLinks:
        tikzcommand.append(F'\\draw[->] (1) to [out=190,in=170] node[left] {{$:{operationLinks[0]}$}}  (2) ;')
        tikzcommand.append(F'\\draw[->] (2) to [out=190,in=170] node[left] {{$XXcdot {operationLinks[1]}$}}  (3) ;'.replace('XX','\\'))
    if not ohneKlammernRechts:
        tikzcommand.append(F'\\draw[->] (4) to [out=350,in=10] node[right] {{${":" if not antiProp else "XXcdot"}{operationLinks[0]}$}}  (5) ;'.replace('XX','\\'))
        tikzcommand.append(F'\\draw[->] (5) to [out=350,in=10] node[right] {{${"XXcdot" if not antiProp else ":"}{operationLinks[1]}$}}  (6) ;'.replace('XX','\\'))
    if tikzUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    for i in range(len(tikzcommand)):
        tikzcommand[i].replace('XX','\\')
    return tikzcommand
