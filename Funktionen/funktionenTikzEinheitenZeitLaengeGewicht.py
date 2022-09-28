#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, die zur Erstellung einer Latex tex-Datei benötigt werden.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())




def tikzAnalogeUhr(stunde=6,minute=25,radius=2.5,mitZeiger=True):
#Quelle:%https://tex.stackexchange.com/questions/132321/generate-analog-clock-with-numbered-face
    if minute>59:
        return tikzAnalogeUhr(stunde=stunde+1,minute=minute-60,radius=2.5)
    latexcommand=[]
    latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
    latexcommand.append('\\begin{tikzpicture}[show background grid]')  
    latexcommand.append('\\draw[line width=2pt] (0,0) circle [radius='+str(radius)+'cm];') 
    latexcommand.append('\\filldraw [fill=black] (0,0) circle [radius=0.1cm];') 
    latexcommand.append('\\foreach \\angle [count=\\xi] in {60,30,...,-270}') 
    latexcommand.append('{') 
    latexcommand.append('  \\draw[line width=1pt] (\\angle:'+str(radius-0.2)+'cm) -- (\\angle:'+str(radius)+'cm);') 
    latexcommand.append('  \\node[font=\\large] at (\\angle:'+str(radius-0.64)+'cm) {\\textsf{\\xi}};') 
    latexcommand.append('}') 
    latexcommand.append('\\foreach \\angle in {0,90,180,270}') 
    latexcommand.append('  \\draw[line width=2pt] (\\angle:'+str(radius-0.4)+'cm) -- (\\angle:'+str(radius)+'cm);') 
    latexcommand.append('\\foreach \\angle in {0,6,...,360}') 
    latexcommand.append('  \\draw[line width=1pt] (\\angle:'+str(radius-0.1)+'cm) -- (\\angle:'+str(radius)+'cm);') 
    if mitZeiger:
        latexcommand.append('\\draw[line width=2pt] (0,0) -- ('+str(-minute*6+90)+':'+str(radius/2)+'cm);') 
        latexcommand.append('\\draw[line width=2pt] (0,0) -- ('+str(-stunde*30+90-minute/2)+':'+str(radius*0.3)+'cm);') 
    latexcommand.append('\\end{tikzpicture}') 
    return latexcommand
