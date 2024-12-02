#!/usr/bin/env python
# coding: utf8
import math
import random


#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Geomtrieaufgaben darstellen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

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
    

def dreieckSWScBetaa(A=[4,40,"A","a","$\\alpha$"],B=[3,60,"B","b","$\\beta$"],C=[5,80,"C","c","$\\gamma$"]):
#
    x0=random.randint(0,5)/10
    y0=random.randint(0,5)/10
    sW=random.randint(-45,45)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black] ({x0},{y0}) coordinate(A) -- node[below,sloped]{{{C[3]}}} ++({sW}:{C[0]}) coordinate(B) -- node[above,sloped]{{{A[3]}}} ++({180-B[1]+sW}:{A[0]} ) coordinate(C) -- node[above,sloped]{{{B[3]}}} cycle;')
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{A[4]}"] {{angle = B--A--C}};')
    tikzcommand.append(F'\\pic [angle radius=0.3cm, "{A[2]}"] {{angle = C--A--B}};')
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{B[4]}"] {{angle = C--B--A}};')
    tikzcommand.append(F'\\pic [angle radius=0.3cm, "{B[2]}"] {{angle = A--B--C}};')
    tikzcommand.append(F'\\pic [draw,thick, -,angle radius=0.7cm, "{C[4]}"] {{angle = A--C--B}};')
    tikzcommand.append(F'\\pic [angle radius=0.3cm, "{C[2]}"] {{angle = B--C--A}};')
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


def dreieckSSSKonstruktion(a=2,b=3,c=4):
    if abs((a**2-b**2-c**2)/(-2*b*c))>1:
        alpha=-1
    else:
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
    winkelStartUmA=-10
    winkelEndUmA=190 if alpha > 90 or alpha <0 else 100
    winkelStartUmB=-10 if b>c and alpha<45 else 80
    winkelEndUmB=190
    x=c+a*math.cos(winkelStartUmB*math.pi/180)
    y=0+a*math.sin(winkelStartUmB*math.pi/180)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
    if alpha>0:
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b});')
    tikzcommand.append(F'\\draw[thick,red] ({winkelStartUmA}:{b}) arc ({winkelStartUmA}:{winkelEndUmA}:{b} cm);')
    tikzcommand.append(F'\\draw[thick,red] ({x},{y}) arc ({winkelStartUmB}:{winkelEndUmB}:{a} cm);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def planfigur(urspr=[0,0],markieren=['alpha','b','gamma']):
    markierenBefehle={'alpha':F'\\pic [draw,thick, green,angle radius=0.7cm, "$\\alpha$"] {{angle = B--A--C}};'}
    markierenBefehle['beta']=F'\\pic [draw,thick, green,angle radius=0.7cm, "$\\beta$"] {{angle = C--B--A}};'
    markierenBefehle['gamma']=F'\\pic [draw,thick, green,angle radius=0.7cm, "$\\gamma$"] {{angle = A--C--B}};'
    markierenBefehle['a']=F'\\draw[thick,green] (B) -- (C);'
    markierenBefehle['b']=F'\\draw[thick,green] (A) -- (C);'
    markierenBefehle['c']=F'\\draw[thick,green] (A) -- (B);'
    tikzcommand=[]
    tikzcommand.append(f'\\draw[thick,black] ({urspr[0]},{urspr[1]}) coordinate(A) -- node[below,sloped]{{c}} ++(2,0) coordinate(B) -- node[above,sloped]{{a}} ++(-1,2) coordinate(C) -- node[above,sloped]{{b}} cycle; ')
    tikzcommand.append(f'\\node[left] at (A) {{A}};')
    tikzcommand.append(f'\\node[right] at (B) {{B}};')
    tikzcommand.append(f'\\node[above] at (C) {{C}};')
    tikzcommand.append(F'\\pic [draw,thick, black,angle radius=0.7cm, "$\\alpha$"] {{angle = B--A--C}};')
    tikzcommand.append(F'\\pic [draw,thick, black,angle radius=0.7cm, "$\\beta$"] {{angle = C--B--A}};')
    tikzcommand.append(F'\\pic [draw,thick, black,angle radius=0.7cm, "$\\gamma$"] {{angle = A--C--B}};')
    for m in markieren:
        tikzcommand.append(markierenBefehle[m])
    return tikzcommand

def dreieckWSWKonstr(werte=[40,5,80],seite='b',mitLsg=True,zeichnePlanfigur=True):
    markieren={'c':['alpha','c','beta'],'a':['beta','a','gamma'],'b':['gamma','b','alpha']}
    markierenBefehle={'alpha':F'\\pic [draw,thick, angle radius=0.7cm, "$\\alpha$"] {{angle = B--A--C}};'}
    markierenBefehle['beta']=F'\\pic [draw,thick, angle radius=0.7cm, "$\\beta$"] {{angle = C--B--A}};'
    markierenBefehle['gamma']=F'\\pic [draw,thick, angle radius=0.7cm, "$\\gamma$"] {{angle = A--C--B}};'
    urspr={'c':[-3,0],'a':[-6,0],'b':[-4,-3]}
    dR=0#random.randint(-10,10)
    sW={'c':0,'a':90+dR,'b':180+90+dR}
    pktBez={'a':['B','C','A'],'b':['C','A','B'],'c':['A','B','C']}
    seitenBez={'a':['a','b','c'],'b':['b','c','a'],'c':['c','a','b']}
    labelPos={'A':225,'B':315,'C':90}
    seitenPos={'a':'above,sloped','b':'above,sloped','c':'below,sloped'}
#w1 ist immer der Winkel links auf der Strecke, gedreht gegen Uhrzeigersinn.
    w1=sW[seite]+werte[0]
    w2=sW[seite]+180-werte[2]
    l=werte[1]
#Beschriftungen
    pktLabel1=f"[label={labelPos[pktBez[seite][0]]}:{pktBez[seite][0]}]" if mitLsg and pktBez[seite][0] in markieren[seite] else ""
    pktLabel2=f"[label={labelPos[pktBez[seite][1]]}:{pktBez[seite][1]}]" if mitLsg and pktBez[seite][1] in markieren[seite] else ""
    pktLabel3=f"[label={labelPos[pktBez[seite][2]]}:{pktBez[seite][2]}]" if mitLsg and pktBez[seite][2] in markieren[seite] else ""
    seitenLabel1=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[seite][0]]}] {{{seitenBez[seite][0]}}}" if mitLsg and seitenBez[seite][0] in markieren[seite] else "")
    seitenLabel2=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[seite][1]]}] {{{seitenBez[seite][1]}}}" if mitLsg and seitenBez[seite][1] in markieren[seite] else "")
    seitenLabel3=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[seite][2]]}] {{{seitenBez[seite][2]}}}" if mitLsg and seitenBez[seite][2] in markieren[seite] else "")+("  cycle" if mitLsg else "")
#Dreieck zeichnen
    tikzcommand=[f'\\coordinate{pktLabel1} (E) at (0,0);']
    tikzcommand.append(f'\\node (E2) at ($(E)+({w1}:1)$) {{}};')
    tikzcommand.append(f'\\coordinate{pktLabel2} (F) at ({sW[seite]}:{l});')
    tikzcommand.append(f'\\node (F2) at ($(F)+({w2}:1)$) {{}};')
    tikzcommand.append(f'\\coordinate{pktLabel3} (G) at (intersection of E--E2 and F--F2);')
    tikzcommand.append(f'\\draw (E) coordinate ({pktBez[seite][0]}) {seitenLabel1} (F) coordinate ({pktBez[seite][1]})  {seitenLabel2} (G) coordinate ({pktBez[seite][2]})  {seitenLabel3};')    
    if mitLsg:
        tikzcommand.append(markierenBefehle[markieren[seite][0]])
        tikzcommand.append(markierenBefehle[markieren[seite][2]])
    if mitLsg or zeichnePlanfigur:
        tikzcommand=tikzcommand+planfigur(urspr=urspr[seite],markieren=markieren[seite] if mitLsg else [])
    else:
        tikzcommand.append(f'\\node (U) at  ({urspr[seite][0]},{urspr[seite][1]}) {{}};')
    return erzeugeTikzUmrandung(tikzcommand)

def dreieckSWSKonstr(werte=[4,60,5],winkel='gamma',mitLsg=True,zeichnePlanfigur=True):
    markieren={'alpha':['b','alpha','c'],'beta':['c','beta','a'],'gamma':['a','gamma','b']}
    markierenBefehle={'alpha':F'\\pic [draw,thick, angle radius=0.7cm, "$\\alpha$"] {{angle = B--A--C}};'}
    markierenBefehle['beta']=F'\\pic [draw,thick, angle radius=0.7cm, "$\\beta$"] {{angle = C--B--A}};'
    markierenBefehle['gamma']=F'\\pic [draw,thick, angle radius=0.7cm, "$\\gamma$"] {{angle = A--C--B}};'
    urspr={'alpha':[-3,0],'beta':[-3-werte[0],0],'gamma':[-5,-3]}
    dR=0 #random.randint(-10,10)
    sW={'alpha':werte[1],'beta':180,'gamma':270+werte[1]+dR}
    pktBez={'alpha':['A','C','B'],'beta':['B','A','C'],'gamma':['C','B','A']}
    seitenBez={'alpha':['b','a','c'],'beta':['c','b','a'],'gamma':['a','c','b']}
    labelPos={'A':225,'B':315,'C':90}
    seitenPos={'a':'above,sloped','b':'above,sloped','c':'below,sloped'}
#l1 ist immer die Seite links von dem Winkel, gedreht gegen Uhrzeigersinn.
    l1=werte[0]
    l2=werte[2]
#Beschriftungen
    pktLabel1=f"[label={labelPos[pktBez[winkel][0]]}:{pktBez[winkel][0]}]" if mitLsg and pktBez[winkel][0] in markieren[winkel] else ""
    pktLabel2=f"[label={labelPos[pktBez[winkel][1]]}:{pktBez[winkel][1]}]" if mitLsg and pktBez[winkel][1] in markieren[winkel] else ""
    pktLabel3=f"[label={labelPos[pktBez[winkel][2]]}:{pktBez[winkel][2]}]" if mitLsg and pktBez[winkel][2] in markieren[winkel] else ""
    seitenLabel1=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[winkel][0]]}] {{{seitenBez[winkel][0]}}}" if mitLsg and seitenBez[winkel][0] in markieren[winkel] else "")
    seitenLabel2=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[winkel][1]]}] {{{seitenBez[winkel][1]}}}" if mitLsg and seitenBez[winkel][1] in markieren[winkel] else "")
    seitenLabel3=(f" -- " if mitLsg else "") + (f"node[{seitenPos[seitenBez[winkel][2]]}] {{{seitenBez[winkel][2]}}}" if mitLsg and seitenBez[winkel][2] in markieren[winkel] else "")+("  cycle" if mitLsg else "")
#Dreieck zeichnen
    tikzcommand=[f'\\coordinate{pktLabel1} (E) at (0,0);']
    tikzcommand.append(f'\\coordinate{pktLabel2} (F) at ({sW[winkel]}:{l1});')
    tikzcommand.append(f'\\coordinate{pktLabel3} (G) at ({sW[winkel]-werte[1]}:{l2});')
    tikzcommand.append(f'\\draw (E) coordinate ({pktBez[winkel][0]})  {seitenLabel1} (F) coordinate ({pktBez[winkel][1]})  {seitenLabel2} (G) coordinate ({pktBez[winkel][2]})  {seitenLabel3};')
    if mitLsg:
        tikzcommand.append(markierenBefehle[winkel])
    if mitLsg or zeichnePlanfigur:
        tikzcommand=tikzcommand+planfigur(urspr=urspr[winkel],markieren=markieren[winkel] if mitLsg else [])
    else:
        tikzcommand.append(f'\\node (U) at  ({urspr[winkel][0]},{urspr[winkel][1]}) {{}};')
    return erzeugeTikzUmrandung(tikzcommand)

