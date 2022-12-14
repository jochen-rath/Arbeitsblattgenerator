#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import math


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
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')    
    tikzcommand.append('\\draw ('+str(ursprung[0])+','+str(ursprung[1]+h)+') ellipse ('+str(R)+' and '+str(R/2)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]-R)+','+str(ursprung[1])+') -- ('+str(ursprung[0]-R)+','+str(ursprung[1]+h)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]-R)+','+str(ursprung[1])+') arc (180:360:'+str(R)+' and '+str(R/2)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]-R)+','+str(ursprung[1])+') --  node[below]{'+rName+'}('+str(ursprung[0])+','+str(ursprung[1])+');')
    tikzcommand.append('\\draw [dashed] ('+str(ursprung[0]-R)+','+str(ursprung[1])+') arc (180:360:'+str(R)+' and '+str(-R/2)+');')
    tikzcommand.append('\\draw ('+str(ursprung[0]+R)+','+str(ursprung[1])+') --  node[right]{'+hName+'}('+str(ursprung[0]+R)+','+str(ursprung[1]+h)+');')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

def quaderMitLoch(a=6, b=4, c=9,R=1.5, ursprung=[0,0],buchstabe='Q',aName='a',bName='b',cName='c',rName='r'):
#Diese Funktion erzeugt einen Tikz-code mit dem man einen Quader darstellen.
#Aufruf:
#        tikzcommand=quaderMitLoch(a, b, c,R,ursprung,buchstabe)
#
    cPers=c/2/math.sqrt(2)
    katheteCMP=math.sqrt(1/2)*c/4
    mittelpunkt=[a/2+katheteCMP,katheteCMP]
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    R1=R
    R2=R/2
    tikzcommand.append('\\coordinate ('+buchstabe+'1) at ('+str(ursprung[0])+','+str(ursprung[1])+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'2) at ('+str(ursprung[0]+a)+','+str(ursprung[1])+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'3) at ('+str(ursprung[0]+a)+','+str(ursprung[1]+b)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'4) at ('+str(ursprung[0])+','+str(ursprung[1]+b)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'5) at ('+str(ursprung[0]+cPers)+','+str(ursprung[1]+cPers)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'6) at ('+str(ursprung[0]+a+cPers)+','+str(ursprung[1]+cPers)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'7) at ('+str(ursprung[0]+a+cPers)+','+str(ursprung[1]+b+cPers)+'); ')
    tikzcommand.append('\\coordinate ('+buchstabe+'8) at ('+str(ursprung[0]+cPers)+','+str(ursprung[1]+b+cPers)+'); ')
    tikzcommand.append('\\draw[thick,dashed] ('+buchstabe+'5) -- ('+buchstabe+'6);')
    tikzcommand.append('\\draw[thick,dashed] ('+buchstabe+'5) -- ('+buchstabe+'8);')
    tikzcommand.append('\\draw[thick,dashed] ('+buchstabe+'1) -- ('+buchstabe+'5);')
    tikzcommand.append('\\fill[gray!60]  ('+str(mittelpunkt[0]-R)+','+str(mittelpunkt[1])+') --  ('+str(mittelpunkt[0]+R)+','+str(mittelpunkt[1])+') -- ('+str(mittelpunkt[0]+R)+','+str(mittelpunkt[1]+b)+') --  ('+str(mittelpunkt[0]-R)+','+str(mittelpunkt[1]+b)+') ;')
    tikzcommand.append('\\draw [dashed,fill=gray!60] ('+str(mittelpunkt[0])+','+str(mittelpunkt[1])+') ellipse ('+str(R1)+' and '+str(R2)+');')
    tikzcommand.append('\\draw [thick,fill=gray!60] ('+str(mittelpunkt[0])+','+str(mittelpunkt[1]+b)+') ellipse ('+str(R1)+' and '+str(R2)+');')
    tikzcommand.append('\\draw  ('+str(mittelpunkt[0]-R)+','+str(mittelpunkt[1])+') --  node[below]{'+rName+'} ('+str(mittelpunkt[0])+','+str(mittelpunkt[1])+');')  
    tikzcommand.append('\\draw[thick] ('+buchstabe+'1) -- node[below]{'+aName+'} ('+buchstabe+'2);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'2) -- node[above,right]{'+bName+'} ('+buchstabe+'3);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'3) -- ('+buchstabe+'4);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'4) -- ('+buchstabe+'1);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'4) -- ('+buchstabe+'8);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'3) -- ('+buchstabe+'7);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'2) -- node[below,right]{'+cName+'} ('+buchstabe+'6);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'7) -- ('+buchstabe+'8);')
    tikzcommand.append('\\draw[thick] ('+buchstabe+'6) -- ('+buchstabe+'7);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand
    