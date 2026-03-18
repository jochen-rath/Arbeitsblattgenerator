#!/usr/bin/env python
# coding: utf8
import math
import random


#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Geomtrieaufgaben darstellen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def einfacheLinie(l=4,breite=6):
    rot=random.randint(0,359)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black,rotate={rot},|-|] (0,0) node[left]{{A}} -- ({l},0) node[right] {{B}};')
    tikzcommand.append(F'\\node at ({breite/2},{breite/2}) {{}};')
    tikzcommand.append(F'\\node at ({-breite/2},{-breite/2}) {{}};')
    
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
    

def scheitelNebenStufenWechselWinkel(w1='0',w2='0',laenge=5):
    import numbers
    w1=w1 if isinstance(w1, numbers.Number) else random.randint(-44,44)
    w2=w2 if isinstance(w2, numbers.Number) else random.randint(46,134)
    tikzcommand=['\\begin{tikzpicture}']
    tikzcommand.append(F'\\draw[thick,black] (0,0) coordinate(S) --  ++({w1}:{laenge/2} ) coordinate(B) ;')
    tikzcommand.append(F'\\draw[thick,black] (0,0) --  ++({w1+180}:{laenge/2} ) coordinate(A) ;')
    tikzcommand.append(F'\\draw[thick,black] (0,0) --  ++({w2}:{laenge/2} ) coordinate(D) ;')
    tikzcommand.append(F'\\draw[thick,black] (0,0) --  ++({w2+180}:{laenge/2} ) coordinate(C) ;')
    tikzcommand.append(F'\\pic [draw,thick, black,fill=red,angle radius=0.7cm, " "] {{angle = B--S--D}};')    
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.6cm, " "] {{angle = D--S--A}};')    
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, " "] {{angle = A--S--C}};')    
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.6cm, " "] {{angle = C--S--B}};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
    

def winkelZeichnen(winkel=[34,'34'],laenge=5,LSG=True):
    sW=0 if LSG else random.randint(-45,45)
    tikzcommand=['\\begin{tikzpicture}']
    tikzcommand.append(F'\\draw[thick,black] (0,0) coordinate(A) --  ++({sW}:{laenge if winkel[0]<110 else laenge/2} ) coordinate(B) ;')
    tikzcommand.append(F'\\draw[thick,black] (A) --  ++({winkel[0]+sW}:{laenge} ) coordinate(C) ;') 
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{winkel[1]}"] {{angle = B--A--C}};')    
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
    



def zeichneRechtwinklLinien(linienWinkel=[[2,4,89,[93,'red']],[[3,'red'],0,91,95]],laenge=6):
    tikzcommand=['\\begin{tikzpicture}']
    for i,winkel in enumerate(linienWinkel):
        if i==0:
            for j,w in enumerate(winkel):
                if isinstance(w, list):
                    farbe=w[1]
                    w=w[0]
                else:
                    farbe='black'
                pos='left' if w<45 else 'below'
                tikzcommand.append(F'\\draw[thick,{farbe}] {f"(-0.5,{j*0.3})" if w<45 else f"({j*0.3},-0.5)"} node[{pos}] {{{chr(65+i*len(winkel)+j)}}}  -- ++({w}:{laenge});')
        elif i==1:
            for j,w in enumerate(winkel):
                if isinstance(w, list):
                    farbe=w[1]
                    w=w[0]
                else:
                    farbe='black'
                pos='left' if w<45 else 'below'
                tikzcommand.append(F'\\draw[thick,{farbe}] {f"(-0.5,{laenge-1-j*0.3})" if w<45 else f"({laenge-0.5-j*0.3},-0.5)"} node[{pos}] {{{chr(65+i*len(winkel)+j)}}}  -- ++({w}:{laenge});')        
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def zeichneLinienMitVorgWinkel(linienWinkel=[5,[2,'red'],0,7,[2,'red'],10],laenge=6):
    tikzcommand=['\\begin{tikzpicture}']
    for i,w in enumerate(linienWinkel):
        if isinstance(w, list):
            farbe=w[1]
            w=w[0]
        else:
            farbe='black'
        tikzcommand.append(F'\\draw[thick,{farbe}] (0,{i*0.5}) node[left] {{{chr(65+i)}}}  -- ++({w}:{laenge});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def mittelsenkrechte(l=random.randint(5,10)):
    R=0.6*l
    winkelDiff=60
    winkelStartUmB=180-winkelDiff
    winkelEndUmB=180+winkelDiff
    x=l+R*math.cos(winkelStartUmB*math.pi/180)
    y=0+R*math.sin(winkelStartUmB*math.pi/180)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black,|-|] (0,0) node[left]{{A}} -- ({l},0) node[right] {{B}};')
    tikzcommand.append(F'\\draw[thick,red] (-{winkelDiff}:{R}) arc (-{winkelDiff}:{winkelDiff}:{R} cm);')
    tikzcommand.append(F'\\draw[thick,red] ({x},{y}) arc ({winkelStartUmB}:{winkelEndUmB}:{R} cm);')
    tikzcommand.append(F'\\draw[thick,blue] ({l/2},{-1.1*R}) -- ({l/2},{1.1*R})  ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def winkelhalbierende(winkel=random.randint(20,160),mitLsg=True):
    l=5
    R=l*0.7
    winkelDiff=10
    winkelStartUnten=winkel/2
    winkelEndUnten=winkel/2+winkel
    xUnten=R+R*math.cos(winkelStartUnten*math.pi/180)
    yUnten=0+R*math.sin(winkelStartUnten*math.pi/180)
    winkelStartOben=-10
    winkelEndOben=winkel/2+winkelStartOben
    xSchnittOben=R*math.cos(winkel*math.pi/180)
    ySchnittOben=R*math.sin(winkel*math.pi/180)
    xOben=xSchnittOben+R*math.cos(winkelStartOben*math.pi/180)
    yOben=ySchnittOben+R*math.sin(winkelStartOben*math.pi/180)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{S}} -- ({l},0);')
    tikzcommand.append(F'\\draw[thick,black] (0,0) -- ({winkel}:{l});')
    if mitLsg:
        tikzcommand.append(F'\\draw[thick,gray] (-{winkelDiff}:{R}) arc (-{winkelDiff}:{winkel}+{winkelDiff}:{R} cm);')
        tikzcommand.append(F'\\draw[thick,blue] ({xUnten},{yUnten}) arc ({winkelStartUnten}:{winkelEndUnten}:{R} cm);')
        tikzcommand.append(F'\\draw[thick,dashed,blue] ({R},0) -- ({xUnten},{yUnten});')
        tikzcommand.append(F'\\draw[thick,blue] ({xOben},{yOben}) arc ({winkelStartOben}:{winkelEndOben}:{R} cm);')
        tikzcommand.append(F'\\draw[thick,dashed,blue] ({xSchnittOben},{ySchnittOben}) -- ({xOben},{yOben});')
        tikzcommand.append(F'\\draw[thick,red] (0,0) -- ({winkel/2}:{1.5*l});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def dreieckMarkieren(seiteWinkel="",farbe='green'):
    markierenBefehle={'alpha':F'\\pic [draw,thick, {farbe},angle radius=0.7cm, "$\\alpha$"] {{angle = B--A--C}};'}
    markierenBefehle['beta']=F'\\pic [draw,thick, {farbe},angle radius=0.7cm, "$\\beta$"] {{angle = C--B--A}};'
    markierenBefehle['gamma']=F'\\pic [draw,thick, {farbe},angle radius=0.7cm, "$\\gamma$"] {{angle = A--C--B}};'
    markierenBefehle['a']=F'\\draw[thick,{farbe}] (B) -- (C);'
    markierenBefehle['b']=F'\\draw[thick,{farbe}] (A) -- (C);'
    markierenBefehle['c']=F'\\draw[thick,{farbe}] (A) -- (B);'
    return markierenBefehle[seiteWinkel] if seiteWinkel in list(markierenBefehle.keys()) else ""

def planfigur(urspr=[0,0],markieren=['alpha','b','gamma']):
    tikzcommand=[]
    tikzcommand.append(f'\\draw[thick,black] ({urspr[0]},{urspr[1]}) coordinate(A) -- node[below,sloped]{{c}} ++(2,0) coordinate(B) -- node[above,sloped]{{a}} ++(-1,2) coordinate(C) -- node[above,sloped]{{b}} cycle; ')
    tikzcommand.append(f'\\node[left] at (A) {{A}};')
    tikzcommand.append(f'\\node[right] at (B) {{B}};')
    tikzcommand.append(f'\\node[above] at (C) {{C}};')
    tikzcommand.append(F'\\pic [draw,thick, black,angle radius=0.7cm, "$\\alpha$"] {{angle = B--A--C}};')
    tikzcommand.append(F'\\pic [draw,thick, black,angle radius=0.7cm, "$\\beta$"] {{angle = C--B--A}};')
    tikzcommand.append(F'\\pic [draw,thick, black,angle radius=0.7cm, "$\\gamma$"] {{angle = A--C--B}};')
    for m in markieren:
        tikzcommand.append(dreieckMarkieren(m))
    return tikzcommand

