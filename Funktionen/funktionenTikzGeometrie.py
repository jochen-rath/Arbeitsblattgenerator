#!/usr/bin/env python
# coding: utf8
import math
import random


#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Geomtrieaufgaben darstellen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

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

def dreieckSWSKonstruktion(l1=4,winkel=55,l2=3,winkelBei='alpha'):
    l3=(l1**2+l2**2-2*l1*l2*math.cos(winkel*math.pi/180))**0.5
    if winkelBei not in ['alpha','beta','gamma']:
        return []
    if winkelBei=='alpha':
        alpha=winkel
        a,b,c=l3,l2,l1
        beta=math.acos((b**2-a**2-c**2)/(-2*a*c))*180/math.pi
        gamma=180-alpha-beta
    if winkelBei=='beta':
        beta=winkel
        a,b,c=l1,l3,l2
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
        gamma=180-alpha-beta
    if winkelBei=='gamma':
        gamma=winkel
        a,b,c=l2,l1,l3
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
        beta=180-alpha-gamma
    bogenR=0.75
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    if winkelBei=='alpha':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{{strNW(c)} cm}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{{strNW(b)} cm}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{alpha}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({alpha/2}:{bogenR*0.75}) {{${alpha}^\\circ$}} ;')
    if winkelBei=='beta':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{{strNW(c)} cm}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  -- node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{{strNW(a)} cm}} ({alpha}:{b}) ;')
        x=c+bogenR*0.75*math.cos((180-beta/2)*math.pi/180)
        y=0+bogenR*0.75*math.sin((180-beta/2)*math.pi/180)
        tikzcommand.append(F'\\draw[thick,red] ({c-bogenR},0) arc (180:{180-beta}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({x},{y}) {{${beta}^\\circ$}} ;')
    if winkelBei=='gamma':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{{strNW(b)} cm}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{{strNW(a)} cm}} ({alpha}:{b}) ;')
        xBogen=(b-bogenR)*math.cos(alpha*math.pi/180)
        yBogen=(b-bogenR)*math.sin(alpha*math.pi/180)
        tikzcommand.append(F'\\draw[thick,red] ({xBogen},{yBogen}) arc ({180+alpha}:{180+alpha+gamma}:{bogenR} cm) ;')
        xZahl=b*math.cos(math.radians(alpha))+bogenR*0.75*math.cos((180+alpha+gamma/2)*math.pi/180)
        yZahl=b*math.sin(math.radians(alpha))+bogenR*0.75*math.sin((180+alpha+gamma/2)*math.pi/180)
        tikzcommand.append(F'\\node[red] at ({xZahl},{yZahl}) {{${gamma}^\\circ$}} ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def dreieckWSWKonstruktion(w1=40,l=5,w2=110,seite='c'):
    bogenR=0.75
    if seite not in ['a','b','c']:
        return []
    if w1+w2>180:
        x=l+l*math.cos(math.radians(180-w2))
        y=0+l*math.sin(math.radians(180-w2))
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  -- node[below]{{{l} cm}}({l},0) ;')
        tikzcommand.append(F'\\draw[thick,black] (0,0)--({w1}:{l}) ;')
        tikzcommand.append(F'\\draw[thick,black] ({l},0) --({x},{y}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{w1}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({w1/2}:{bogenR*0.75}) {{${w1}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({l-bogenR},0) arc ({180}:{180-w2}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({l+bogenR*0.75*math.cos(math.radians(180-w2/2))},{bogenR*0.75*math.sin(math.radians(180-w2/2))}) {{${w2}^\\circ$}} ;')
        tikzcommand.append('\\end{tikzpicture}')
        return tikzcommand
    if seite=='a':
        a=l
        beta=w1
        gamma=w2
        alpha=180-beta-gamma
        b=a/math.sin(math.radians(alpha))*math.sin(math.radians(beta))
        c=a/math.sin(math.radians(alpha))*math.sin(math.radians(gamma))
    if seite=='b':
        b=l
        gamma=w1
        alpha=w2
        beta=180-alpha-gamma
        a=b/math.sin(math.radians(beta))*math.sin(math.radians(alpha))
        c=b/math.sin(math.radians(beta))*math.sin(math.radians(gamma))
    if seite=='c':
        c=l
        alpha=w1
        beta=w2
        gamma=180-alpha-beta
        a=c/math.sin(math.radians(gamma))*math.sin(math.radians(alpha))
        b=c/math.sin(math.radians(gamma))*math.sin(math.radians(beta))
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    x=c+bogenR*0.75*math.cos((180-beta/2)*math.pi/180)
    y=0+bogenR*0.75*math.sin((180-beta/2)*math.pi/180)
    xBogen=(b-bogenR)*math.cos(alpha*math.pi/180)
    yBogen=(b-bogenR)*math.sin(alpha*math.pi/180)
    xZahl=b*math.cos(math.radians(alpha))+bogenR*0.75*math.cos((180+alpha+gamma/2)*math.pi/180)
    yZahl=b*math.sin(math.radians(alpha))+bogenR*0.75*math.sin((180+alpha+gamma/2)*math.pi/180)
    if seite=='c':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{{strNW(c)} cm}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{alpha}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({alpha/2}:{bogenR*0.75}) {{${alpha}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({c-bogenR},0) arc (180:{180-beta}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({x},{y}) {{${beta}^\\circ$}} ;')
    if seite=='a':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  -- node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{{strNW(a)} cm}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({c-bogenR},0) arc (180:{180-beta}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({x},{y}) {{${beta}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({xBogen},{yBogen}) arc ({180+alpha}:{180+alpha+gamma}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({xZahl},{yZahl}) {{${gamma}^\\circ$}} ;')
    if seite=='b':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{{strNW(b)} cm}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({xBogen},{yBogen}) arc ({180+alpha}:{180+alpha+gamma}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({xZahl},{yZahl}) {{${gamma}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{alpha}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({alpha/2}:{bogenR*0.75}) {{${alpha}^\\circ$}} ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand