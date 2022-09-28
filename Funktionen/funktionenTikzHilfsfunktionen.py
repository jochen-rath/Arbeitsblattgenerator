#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def leereZeilen(groesse=[17,3]):
    x,y=groesse
    latexcommand=[]
    latexcommand.append('\\\begin{tikzpicture}')  
    latexcommand.append('\\\node at (0,0.1) {};')  
    latexcommand.append('\\\foreach \i in {1,2,...,'+str(y)+'}{')  
    latexcommand.append('\\\draw[lightgray] (0,-\i) -- ('+str(x)+',-\i);}')  
    latexcommand.append('\\\end{tikzpicture}')  

def leeresKaro(groesse=[17,4]):
    latexcommand=[]
    latexcommand.append('\\noindent\\tikzstyle{background grid}=[draw, black!30,step=.5cm]')
    latexcommand.append('\\begin{tikzpicture}[show background grid]')  
    latexcommand.append('\\node[] at (0,0) {};') 
    latexcommand.append('\\node[] at ('+str(groesse[0])+','+str(groesse[1])+') {};') 
    latexcommand.append('\\end{tikzpicture}') 
    return latexcommand


def Diagramm(formeln=[['10*x','black']],stepXY=[5,50],sizeXY=[6.5,5.5],mitUmrandung=True,textNode=[],koordinaten=[],labels=['t in s','s in m'],at=[0,0]):
    diagramm=[]
    if mitUmrandung:
        diagramm.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        diagramm.append('\\begin{tikzpicture}[show background grid]')  
    diagramm.append('\\begin{axis}[    axis lines = middle, scale only axis=true, at={('+str(at[0])+'cm,'+str(at[1])+'cm)},')
    diagramm.append('    width='+str(sizeXY[0])+' cm, xmin = 0, xmax = '+str(stepXY[0]*sizeXY[0])+',xtick distance = '+str(stepXY[0])+',')
    diagramm.append('    height='+str(sizeXY[1])+'cm, ymin = 0, ymax = '+str(stepXY[1]*sizeXY[1])+', ytick distance = '+str(stepXY[1])+',')
    diagramm.append('    xlabel = {'+labels[0]+'},x label style={at={(current axis.right of origin)},anchor=north, below=2mm},')
    diagramm.append('    ylabel = {'+labels[1]+'},y label style={at={(current axis.above origin)},anchor=south}]')
    for f,c in formeln:
        diagramm.append('    \\addplot[domain = 0:'+str(stepXY[0]*sizeXY[0])+',samples = 200,smooth,thick,'+c+' ] { ('+f+')};')
    for koord in koordinaten:
        diagramm.append('    \\node[circle,draw=black, fill=white,inner sep=1.5pt] at (axis cs:'+str(koord[0])+','+str(koord[1])+') {};')
    for node in textNode:
        diagramm.append('    \\node['+str(node[3])+'] at (axis cs:'+str(node[0])+','+str(node[1])+') {'+str(node[2])+'};')
    diagramm.append('\\end{axis}')
    if mitUmrandung:
        diagramm.append('\\end{tikzpicture}') 
    return diagramm