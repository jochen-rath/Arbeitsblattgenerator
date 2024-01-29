#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import math


def quader3D(a=4,b=2,c=1,ursprung=[0,0],aName='a',bName='b',cName='c',mitBeschriftung=True,mitTikzUmrandung=True):
    if mitTikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=[]
    tikzcommand.append(F'\\draw[canvas is xz plane at y={ursprung[1]},red] ({ursprung[0]},0) rectangle ++({a},{-b});')
    tikzcommand.append(F'\\draw[canvas is xz plane at y={c+ursprung[1]},red] ({ursprung[0]},0) rectangle ++({a},{-b});')
    tikzcommand.append(F'\\draw[canvas is xy plane at z=0] ({ursprung[0]},{ursprung[1]}) rectangle ++({a},{c});')
    tikzcommand.append(F'\\draw[canvas is xy plane at z={-b}] ({ursprung[0]},{ursprung[1]}) rectangle ++({a},{c});')
    if mitBeschriftung:
        tikzcommand.append(F'\\node[below] at ({a/2+ursprung[0]},{ursprung[1]}) {{{aName}}}; ')
        tikzcommand.append(F'\\node[right] at ({ursprung[0]},{ursprung[1]},{-b/2}) {{{bName}}}; ')
        tikzcommand.append(F'\\node[left] at ({ursprung[0]},{c/2+ursprung[1]}) {{{cName}}}; ')
    if mitTikzUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def quader(a=6, b=4, c=9,ursprung=[0,0],buchstabe='Q',aName='a',bName='b',cName='c',textOben='',mitBeschriftung=True,mitTikzUmrandung=True):
#Diese Funktion erzeugt einen Tikz-code mit dem man einen Quader darstellen.
#Aufruf:
#        tikzcommand=quader(a, b, c,ursprung,buchstabe)
#
    cPers=c/2/math.sqrt(2)
    if mitTikzUmrandung:
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    else:
        tikzcommand=[]
    tikzcommand.append('\\coordinate ('+buchstabe+'1) at ('+str(ursprung[0])+','+str(ursprung[1])+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'2) at ('+str(ursprung[0]+a)+','+str(ursprung[1])+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'3) at ('+str(ursprung[0]+a)+','+str(ursprung[1]+b)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'4) at ('+str(ursprung[0])+','+str(ursprung[1]+b)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'5) at ('+str(ursprung[0]+cPers)+','+str(ursprung[1]+cPers)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'6) at ('+str(ursprung[0]+a+cPers)+','+str(ursprung[1]+cPers)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'7) at ('+str(ursprung[0]+a+cPers)+','+str(ursprung[1]+b+cPers)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'8) at ('+str(ursprung[0]+cPers)+','+str(ursprung[1]+b+cPers)+'); ')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'3) -- ('+buchstabe+'4);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'4) -- ('+buchstabe+'1);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'4) -- ('+buchstabe+'8);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'3) -- ('+buchstabe+'7);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'7) -- ('+buchstabe+'8);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'6) -- ('+buchstabe+'7);')
    tikzcommand.append('\\draw[thick,dashed] ('+buchstabe+'5) -- ('+buchstabe+'6);')
    tikzcommand.append('\\draw[thick,dashed] ('+buchstabe+'5) -- ('+buchstabe+'8);')
    tikzcommand.append('\\draw[thick,dashed] ('+buchstabe+'1) -- ('+buchstabe+'5);')
    if len(textOben)>0:
        tikzcommand.append('\\node at (' + str(ursprung[0]+ (a+cPers) / 2.0) + ',' + str(ursprung[1]+b+cPers+0.25) + '){' + str(textOben) + '}; ')
    if mitBeschriftung:
        tikzcommand.append('\\draw[thick] ('+buchstabe+'1) -- node[above]{'+aName+'} ('+buchstabe+'2);')
        tikzcommand.append('\\draw[thick] ('+buchstabe+'2) -- node[right]{'+bName+'} ('+buchstabe+'3);')
        tikzcommand.append('\\draw[thick] ('+buchstabe+'2) -- node[below,right]{'+cName+'} ('+buchstabe+'6);')
    else:
        tikzcommand.append('\\draw[thick] ('+buchstabe+'1) -- ('+buchstabe+'2);')
        tikzcommand.append('\\draw[thick] ('+buchstabe+'2) -- ('+buchstabe+'3);')
        tikzcommand.append('\\draw[thick] ('+buchstabe+'2) -- ('+buchstabe+'6);')
    if mitTikzUmrandung:
        tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def trapezprismaLiegend(Bx=5,Cx=4,Cy=3,Dx=2,hK=5,messen=False):
#Diese Funktion erzeugt ein liegendes Trapezprisma. A liegt im Ursprung und B auf y=0.
#Dy=Cy
    a=Bx
    b=((Bx-Cx)**2+Cy**2)**0.5
    Dy=Cy
    h=Cy
    c=Cx-Dx
    d=(Dx**2+Dy**2)**0.5
    hKSchr=hK/(2*2**0.5)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw (0,0) -- node[below]{{$a{"" if messen else F"={strNW(a,True)} cm"}$}} ({Bx},0);')
    tikzcommand.append(F'\\draw  ({Bx},0)-- node[right]{{$b{"" if messen else F"={strNW(b,True)} cm"}$}}({Cx},{Cy});')
    tikzcommand.append(F'\\draw  ({Cx},{Cy})-- node[below]{{$c{"" if messen else F"={strNW(c,True)} cm"}$}}({Dx},{Dy});')
    tikzcommand.append(F'\\draw  ({Dx},{Dy})-- node[below]{{$d{"" if messen else F"={strNW(d,True)} cm"}$}}(0,0);')
    tikzcommand.append(F'\\draw[dashed] ({hKSchr},{hKSchr}) -- ({Bx+hKSchr},{hKSchr});')
    tikzcommand.append(F'\\draw  ({Bx+hKSchr},{hKSchr})-- ({Cx+hKSchr},{Cy+hKSchr});')
    tikzcommand.append(F'\\draw  ({Cx+hKSchr},{Cy+hKSchr})-- ({Dx+hKSchr},{Dy+hKSchr});')
    tikzcommand.append(F'\\draw[dashed]  ({Dx+hKSchr},{Dy+hKSchr})-- ({hKSchr},{hKSchr});')
    tikzcommand.append(F'\\draw[dashed] ({0},{0}) -- ({hKSchr},{hKSchr});')
    tikzcommand.append(F'\\draw  ({Bx+hKSchr},{hKSchr})-- ({Bx},{0});')
    tikzcommand.append(F'\\draw  ({Cx+hKSchr},{Cy+hKSchr})-- node[right]{{$h_K{"" if messen else F"={strNW(hK,True)} cm"}$}}({Cx},{Cy});')
    tikzcommand.append(F'\\draw  ({Dx+hKSchr},{Dy+hKSchr})-- ({Dx},{Dy});')
    tikzcommand.append(F'\\draw[dashed] ({Dx},{0}) -- node[right]{{$h{"" if messen else F"={strNW(h,True)} cm"}$}} ({Dx},{Dy});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def dreiecksPrimsa3D(a=5,b=3,c=4,hK=5,messen=False):
    alpha=math.acos(-(a**2-b**2-c**2)/(2*b*c))
    Cx=math.cos(alpha)*b
    h=math.sin(alpha)*b
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid, x=1.0cm,y=1.0cm,z=0.3536cm]')
    tikzcommand.append(F'\\draw  (0,0,0) -- node[below]{{$c{"" if messen else F"={strNW(c,True)} cm"}$}} ({c},0,0) -- node[right]{{$a{"" if messen else F"={strNW(a,True)} cm"}$}} ({Cx},0,-{h}) -- node[left]{{$b{"" if messen else F"={strNW(b,True)} cm"}$}} cycle ;')
    tikzcommand.append(F'\\draw  (0,{hK},0) -- ({c},{hK},0) -- ({Cx},{hK},-{h}) --cycle ;')
    tikzcommand.append(F'\\draw  (0,0,0) -- (0,{hK},0);')
    tikzcommand.append(F'\\draw  ({c},0,0) -- node[anchor=south west]{{$h_K{"" if messen else F"={strNW(hK,True)} cm"}$}} ({c},{hK},0);')
    tikzcommand.append(F'\\draw{"[dashed]" if True else ""}  ({Cx},0,-{h}) -- ({Cx},{hK},-{h});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def trapezPrismaLiegend3D(a=5,c=3,hT=4,hK=5,messen=False):
    dx=(a-c)/2
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid, x=1.0cm,y=1.0cm,z=0.3536cm]')
    tikzcommand.append(F'\\draw[thick]  (0,0,0) coordinate(A) --node[below]{{$a{"" if messen else F"={strNW(a,True)} cm"}$}} ++({a},0,0) coordinate(B) -- ++({-dx},{hT},0) coordinate(C)  -- node[above]{{$c{"" if messen else F"={strNW(c,True)} cm"}$}}  ++({-c},0,0) coordinate(D) -- cycle ;')
    tikzcommand.append(F'\\draw[white]  (0,0,{hK}) coordinate(E) -- ++({a},0,0) coordinate(F) -- ++({-dx},{hT},0) coordinate(G) -- ++({-c},0,0) coordinate(H) -- cycle ;')
    tikzcommand.append(F'\\draw[thick] (F) -- (G) -- (H);')
    tikzcommand.append(F'\\draw[thick,dashed] (H) -- (E) -- (F);')
    tikzcommand.append(F'\\draw[thick,dashed] (A)  -- (E); ')
    tikzcommand.append(F'\\draw[thick] (B) --node[right]{{$h_K{"" if messen else F"={strNW(hK,True)} cm"}$}} (F);')
    tikzcommand.append(F'\\draw[thick] (C) -- (G); ')
    tikzcommand.append(F'\\draw[thick] (D) -- (H);')
    if dx>0:
        tikzcommand.append(F'\\draw[thick,gray,text=black] (D) -- node[right]{{$h_T{"" if messen else F"={strNW(hT,True)} cm"}$}} ++(0,{-hT},0);')
    else:
        tikzcommand.append(F'\\draw[thick,gray,text=black] (A) -- node[right]{{$h_T{"" if messen else F"={strNW(hT,True)} cm"}$}} ++(0,{hT},0);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def sechseckPrimsa3D(a=5,hK=5,messen=False):
    c=round(2*a*math.cos(60*math.pi/180)+a,1)
    hHexa=round(a*math.sin(60*math.pi/180),1)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid, x=1.0cm,y=1.0cm,z=0.3536cm]')
    tikzcommand.append(F'\\draw[thick]  (0,0)  coordinate (A) --node[below]{{$a{"" if messen else F"={strNW(a,True)} cm"}$}}  ++(0:{a} cm) coordinate (B) -- ++(60:{a} cm) coordinate (C) -- ++(120:{a} cm) coordinate (D) -- ++(180:{a} cm) coordinate (E) -- ++(240:{a} cm) coordinate (F) --   cycle ;')
    tikzcommand.append(F'\\path   ($(A)+(0,0,{hK})$) coordinate (A2) -- ($(B)+(0,0,{hK})$) coordinate (B2) --  ($(C)+(0,0,{hK})$) coordinate (C2) --  ($(D)+(0,0,{hK})$) coordinate (D2) --  ($(E)+(0,0,{hK})$) coordinate (E2) --  ($(F)+(0,0,{hK})$) coordinate (F2) --    cycle ;')
    tikzcommand.append('\\draw[thick] (B2) -- (C2) -- (D2) -- (E2);')
    tikzcommand.append('\\draw[thick,dashed] (E2) -- (F2) -- (A2) -- (B2);')
    tikzcommand.append(F'\\draw[thick] (B) -- node[right]{{$h_K{"" if messen else F"={strNW(hK,True)} cm"}$}} (B2) ;')
    tikzcommand.append('\\draw[thick] (C) -- (C2) ;')
    tikzcommand.append('\\draw[thick] (D) -- (D2) ;')
    tikzcommand.append('\\draw[thick] (E) -- (E2) ;')
    tikzcommand.append('\\draw[thick,dashed] (A) -- (A2) ;')
    tikzcommand.append('\\draw[thick,dashed] (F) -- (F2) ;')
    tikzcommand.append(F'\\draw[thick,gray] (C) -- node[below,text=black]{{$c{"" if messen else F"={strNW(c,True)} cm"}$}} (F) ;')
    tikzcommand.append('\\coordinate (SP) at (intersection of A--E and C--F);')
    tikzcommand.append(F'\\draw[thick,gray] (A) --node[right,text=black]{{$h_H{"" if messen else F"={strNW(hHexa,True)} cm"}$}}  (SP) ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand


def dreiecksPrimsa(Ax=3,Bx=2,Cx=4,Cy=2,hK=4,ursprung=[0,0],messen=False):
#Diese Funktion erzeugt einen Tikz-code mit dem man einen Zylinder darstellen.
#Aufruf:
#        tikzcommand=dreiecksPrimsa(g, h,hK,ursprung)
#
#Beispiel:
#              C
#              #
#             / \
#          b /   \a
#           /     \
#           -------
#  A=(-Ax,0)   c    B=(Bx,0)
    c=abs(-Ax-Bx)
    a=((Bx-Cx)**2+Cy**2)**0.5
    b=((Ax-Cx)**2+Cy**2)**0.5
    g=c
    h=(Cx**2+Cy**2)**0.5
    Cxrot=Cy/(2**0.5)/2
    Cyrot=Cy/(2**0.5)/2
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw ({ursprung[0]-Ax},{ursprung[1]}) -- node[below]{{$c{"" if messen else F"={strNW(c,True)} cm"}$}} ({ursprung[0]+Bx},{ursprung[1]});')
    tikzcommand.append(F'\\draw[dashed]  ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot})-- node[left]{{$b{"" if messen else F"={strNW(b,True)} cm"}$}}({ursprung[0]-Ax},{ursprung[1]});')
    tikzcommand.append(F'\\draw[dashed]  ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot})-- node[right]{{$a{"" if messen else F"={strNW(a,True)} cm"}$}}({ursprung[0]+Bx},{ursprung[1]});')
    tikzcommand.append(F'\\draw[dashed]  ({ursprung[0]},{ursprung[1]})node[above] {{$h{"" if messen else F"={strNW(h,True)} cm"}$}}  -- ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot});')
    tikzcommand.append(F'\\draw ({ursprung[0]-Ax},{ursprung[1]+hK}) -- ({ursprung[0]+Bx},{ursprung[1]+hK});')
    tikzcommand.append(F'\\draw  ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot+hK})--({ursprung[0]-Ax},{ursprung[1]+hK});')
    tikzcommand.append(F'\\draw  ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot+hK})--({ursprung[0]+Bx},{ursprung[1]+hK});')
    tikzcommand.append(F'\\draw ({ursprung[0]-Ax},{ursprung[1]}) -- ({ursprung[0]-Ax},{ursprung[1]+hK});')
    tikzcommand.append(F'\\draw ({ursprung[0]+Bx},{ursprung[1]}) -- node[anchor=south west]{{$h_K{"" if messen else F"={strNW(hK,True)} cm"}$}}({ursprung[0]+Bx},{ursprung[1]+hK});')
    tikzcommand.append(F'\\draw[dashed]  ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot})-- ({ursprung[0]+Cxrot},{ursprung[0]+Cyrot+hK});')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def zylinder(R=3, h=4, ursprung=[0,0],buchstabe='Z',rName='R',hName='h'):
#Diese Funktion erzeugt einen Tikz-code mit dem man einen Zylinder darstellen.
#Aufruf:
#        tikzcommand=zylinder(R, h, ursprung=[0,0],buchstabe,rName,hName)
#
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid, x=1.0cm,y=1.0cm,z=0.3536cm]')
    tikzcommand.append('\\draw ('+str(ursprung[0])+','+str(ursprung[1]+h)+') ellipse ('+str(R)+' and '+str(R/2)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]-R)+','+str(ursprung[1])+') -- ('+str(ursprung[0]-R)+','+str(ursprung[1]+h)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]-R)+','+str(ursprung[1])+') arc (180:360:'+str(R)+' and '+str(R/2)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]-R)+','+str(ursprung[1])+') --  node[below]{'+rName+'}('+str(ursprung[0])+','+str(ursprung[1])+');')
    tikzcommand.append('\\draw [dashed] ('+str(ursprung[0]-R)+','+str(ursprung[1])+') arc (180:360:'+str(R)+' and '+str(-R/2)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]+R)+','+str(ursprung[1])+') --  node[right]{'+hName+'}('+str(ursprung[0]+R)+','+str(ursprung[1]+h)+');')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def quaderMitLoch(a=6, b=4, c=9,R=1.5, ursprung=[0,0],buchstabe='Q',aName='a',bName='b',cName='c',rName='r'):
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid, x=1.0cm,y=1.0cm,z=0.3536cm]')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\R}}{{{R}}}  ')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\winkelA}}{{160}}  ')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\winkelB}}{{335}}  ')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\a}}{{{a}}}  ')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\b}}{{{c}}} ')
    tikzcommand.append(F'\\pgfmathsetmacro{{\\h}}{{{b}}}')
    tikzcommand.append(F'   \\fill[gray!60] ({{\\R*cos(\\winkelA)}},0,{{\\R*sin(\\winkelA)}} ) -- ({{\\R*cos(\\winkelA)}},\\h,{{\\R*sin(\\winkelA)}} ) -- ({{\\R*cos(\\winkelB)}},\\h,{{\\R*sin(\\winkelB)}} ) --({{\\R*cos(\\winkelB)}},0,{{\\R*sin(\\winkelB)}} );')
    tikzcommand.append(F'\\begin{{scope}}[canvas is xz plane at y=\\h]')
    tikzcommand.append(F'\\draw[fill=gray!60,thick] (0,0) circle (\\R cm);')
    tikzcommand.append(F'\\draw (-\\a/2,-\\b/2) rectangle ++(\\a,\\b);')
    tikzcommand.append(F'\\end{{scope}}')
    tikzcommand.append(F'\\begin{{scope}}[canvas is xz plane at y=0]')
    tikzcommand.append(F'\\draw[fill=gray!60,dashed] (0,0) circle (\\R cm);')
    tikzcommand.append(F'\\draw (-\\a/2,\\b/2) --  node[below] {{a={strNW(a)} cm}} (\\a/2,\\b/2);')
    tikzcommand.append(F'\\draw (\\a/2,\\b/2) -- node[right] {{c={strNW(c)} cm}} (\\a/2,-\\b/2);')
    tikzcommand.append(F'\\draw[dashed] (\\a/2,-\\b/2) -- (-\\a/2,-\\b/2);')
    tikzcommand.append(F'\\draw[dashed] (-\\a/2,-\\b/2) --  (-\\a/2,\\b/2);')
    tikzcommand.append(F'\\draw[dashed] (0,0) -- node[below] {{r={strNW(R)} cm}} (-\\R,0);')
    tikzcommand.append(F'\\end{{scope}}')
    tikzcommand.append(F'\\draw[thick] (-\\a/2,0,\\b/2) -- (-\\a/2,\\h,\\b/2);')
    tikzcommand.append(F'\\draw[thick] (\\a/2,0,-\\b/2) -- node[right] {{b={strNW(b)} cm}} (\\a/2,\\h,-\\b/2);')
    tikzcommand.append(F'\\draw[thick,dashed] (-\\a/2,0,-\\b/2) -- (-\\a/2,\\h,-\\b/2);')
    tikzcommand.append(F'\\draw[thick] (\\a/2,0,\\b/2) --(\\a/2,\\h,\\b/2);')
    tikzcommand.append(F'\\draw[thick] (-\\a/2,\\h,\\b/2) --(\\a/2,\\h,\\b/2);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
