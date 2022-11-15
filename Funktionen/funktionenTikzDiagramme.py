#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def bestimmeTickAbstand(dx):
#Die Tick-Abstände bei den Diagrammen sollen nicht beliebig sein. sondern sie sollen einen Wert wie 0.1, 0.2, 0.5 usw. annehmen. Dazu erstelle ich hier eine
#Liste mit erlaubten Tick-Werten und die Diagramme fragen ihren nächst höheren Tickwert hier ab.
     zugelasseneAbstaende=[x*10**i for i in range(5) for x in [0.01,0.02,0.025,0.05] ]
     zugelasseneAbstaende=[x*10**i for i in range(5) for x in [0.01,0.02,0.05] ]
     zugelasseneAbstaende=[x*10**i for i in range(5) for x in [0.01,0.02] ]
     return zugelasseneAbstaende[next(x[0] for x in enumerate(zugelasseneAbstaende) if x[1] >= dx)]

def setzeAchsenEinteilungLaenge(achse):
#Wenn ein gewuenschte Min, Max und Achsenlaenge gegeben ist, dann passt diese Funktion diese Werte an die vorgebenen Tick-Werte aus bestimmeTickAbstand an.
#    achse=[xMin,xMax,Laenge]
#       min=Minimaler Wert
#       max=Maximaler Wert
#       Laenge=Laenge der Achse
    tickDist=bestimmeTickAbstand((achse[1]-achse[0]+1)/achse[2])
    minimum=math.floor(achse[0]/tickDist)*tickDist
    maximum=math.ceil(achse[1]/tickDist)*tickDist+tickDist/2
    laenge=(maximum-minimum)/tickDist
    return tickDist, minimum, maximum, laenge

def diagrammTikzVorgBreiteHoehe(zuPlotten=['x','black'],koordinaten=[],streckenzug=[],textNode=[],xAchse=[0,9,10],yAchse=[0,9,10],xlabel='x',ylabel='y',urspr=[0,0],mitUmrandung=True):
#Diese Funktion erzeugt einen Tikz-code mit dem man Funktionen darstellen kann.
#Aufruf:
#        tikzcommand=diagrammTikzVorgBreiteHoehe(zuPlotten=[[Funktion,farbe]],xAchse=[xMin,xMax,xTickDist],yAchse=[yMin,yMax,yTickDist],xLabel='',yLabel='')
#
#Leeres Diagramm:
#         erzeugeEinfachesLatexdokument(diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[0,6,8],yAchse=[0,10,12],xlabel='t in s',ylabel='s in cm'))
#    zuPlotten=[Funktion,farbe]
#       Funktion=String mit der Funktion, Beispiel: x,x^2,sqrt(x),x+x^2
#       Farbe=String mit Farbe: 'blue','black','red'
#       oder
#       Funktion=Liste mit Coordinaten
#       Farbe=Liste mit Eigenschaften für die Marker: [farbe,markerOptions]
#    streckenzug=[Liste mit Coordinaten]  oder [anzZuege,[streckenzug1, streckenzug2,...]]    Bsp: [[1,0],[1,1],[0,1]]
#    textNode=[[posX,posY,'Text','below' (or 'right', 'above' ...],...]
#    xAchse=[xMin,xMax,Laenge]
#       xMin=Minimaler x Wert
#       xMax=Maximaler x Wert
#       Laenge=Laenge der Achse
#    yAchse=[yMin,yMax,Laenge]
#
#Beispiele:
#coords=[[x,0.5*1.6*x**2] for x in [5,10,12.5,15,17.5,20]]
#x=10
#coords2=[[x,0],[x,0.5*1.6*x**2],[0,0.5*1.6*x**2]]
#erzeugeEinfachesLatexdokument(koordinatensystemTikz([['0.5*1.6*x^2','blue'],[coords,'black','mark=*, only marks'],[coords2,'red','no markers']],[0,20,2],[0,300,50],xlabel='Zeit t in s',ylabel='Weg s in m'))
#Testen, ob nur Ein Plot:
    einzelplot=False
    if len(zuPlotten)>1:
        if isinstance(zuPlotten[1], str):
            einzelplot=True
    else:
        einzelplot=True
    tikzcommand=[]
    if mitUmrandung:
        tikzcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')  
##Achseneigenschaften 
#Ich mache die Achsen ein bisschen Größer, damit die Achsenenden und Pfeilspitzen sich nicht überschneiden.
#Außerdem passe ich die Tick-Werte an, dass das Diagramm in der vorgegebenen Größe gut lesbar dargestellt wird.
    xTickDist,xMin,xMax,breite=setzeAchsenEinteilungLaenge(xAchse)
    yTickDist,yMin,yMax,hoehe=setzeAchsenEinteilungLaenge(yAchse)
#    print(urspr)
    tikzcommand.append(F'\\begin{{axis}}[    axis lines = middle, scale only axis=true, at={{({urspr[0]}cm,{urspr[1]}cm)}},')
    tikzcommand.append('    width='+str(breite)+' cm, xmin = '+str(xMin)+', xmax = '+str(xMax)+',xtick distance = '+str(xTickDist)+',')
    tikzcommand.append('    height='+str(hoehe)+'cm, ymin = '+str(yMin)+', ymax = '+str(yMax)+', ytick distance = '+str(yTickDist)+',')
    tikzcommand.append('    xlabel = {'+xlabel+'},x label style={at={(current axis.right of origin)},anchor=north, below=5mm},')
    tikzcommand.append('    ylabel = {'+ylabel+'},y label style={at={(current axis.above origin)},anchor=south}]')
    if einzelplot:
        if len(zuPlotten)>0:
            plot=zuPlotten[0]
            if isinstance(plot, list):
                tikzcommand.append(F'    \\addplot[domain = {xAchse[0]}:{xAchse[1]},samples = 200,smooth,thick,{plot[1]} ] {{ ({plot[0]})}};')
            else:
                tikzcommand.append(F'    \\addplot[domain = {xAchse[0]}:{xAchse[1]},samples = 200,smooth,thick,{zuPlotten[1]} ] {{ ({zuPlotten[0]})}};')
    else:
        for plot in zuPlotten:
            if isinstance(plot[0], str):
                tikzcommand.append('    \\addplot[domain = '+str(xAchse[0])+':'+str(xAchse[1])+',samples = 200,smooth,thick,color='+plot[1]+' ] { ('+plot[0]+')};')
            else:
                tikzcommand.append('    \\addplot[thick,color='+plot[1]+','+plot[2]+' ] coordinates{ '+' '.join(['('+str(p[0])+','+str(p[1])+')' for p in plot[0]])+'};')
    for koord in koordinaten:
        tikzcommand.append('    \\node[circle,draw=black, fill=white,inner sep=1.5pt] at (axis cs:'+str(koord[0])+','+str(koord[1])+') {};')
    pkte=''
    if len(streckenzug)>0:
        if isinstance(streckenzug[0],int):
            for strZug in streckenzug[1:]:
                tikzcommand.append('    \\addplot[thick, color=red] coordinates {  '+' '.join(['('+str(x[0])+','+str(x[1])+')' for x in strZug])+' };')
        else:
            tikzcommand.append('    \\addplot[thick, color=red] coordinates {  '+' '.join(['('+str(x[0])+','+str(x[1])+')'for x in streckenzug])+' };')
    for node in textNode:
#        print(node)
#        tikzcommand.append(F'    \\node[{("" if len(node)<4 else node[3])+("" if len(node)<5 else (",text="+node[4]))}] at (axis cs:{node[0]},{node[1]}) {{{node[2]}}};')
        tikzcommand.append(F'    \\node[{",".join(node[3:])}] at (axis cs:{node[0]},{node[1]}) {{{node[2]}}};')
    tikzcommand.append('\\end{axis}')
    if (yMin < 0 ) and (yMax > 0)  and  (xMin < 0 ) and (xMax > 0):
        tikzcommand.append('\\node[below] at ('+str(urspr[0]-xMin/xTickDist)+','+str(urspr[1]-yMin/yTickDist)+') {0};')
        tikzcommand.append('\\node[left] at ('+str(urspr[0]-xMin/xTickDist)+','+str(urspr[1]-yMin/yTickDist)+') {0};')
    if mitUmrandung:
        tikzcommand.append('\\end{tikzpicture}') 
    return tikzcommand

def koordinatensystemTikz(zuPlotten=[],xAchse=[0,10,1],yAchse=[0,10,1],xlabel='x',ylabel='y'):
#Diese Funktion erzeugt einen Tikz-code mit dem man Funktionen darstellen kann.
#Aufruf:
#        tikzcommand=koordinatensystemTikz(zuPlotten=[[Funktion,farbe]],xAchse=[xMin,xMax,xTickDist],yAchse=[yMin,yMax,yTickDist],xLabel='',yLabel='')
#
#    zuPlotten=[Funktion,farbe]
#       Funktion=String mit der Funktion, Beispiel: x,x^2,sqrt(x),x+x^2
#       Farbe=String mit Farbe: 'blue','black','red'
#       oder
#       Funktion=Liste mit Coordinaten
#       Farbe=Liste mit Eigenschaften für die Marker: [farbe,markerOptions]
#    xAchse=[xMin,xMax,xTickDist]
#       xMin=Minimaler x Wert
#       xMax=Maximaler x Wert
#       xTickDist=Abstand zwischen zwei Werten auf der x-Achse.
#    yAchse=[yMin,yMax,yTickDist]
#
#Beispiele:
#coords=[[x,0.5*1.6*x**2] for x in [5,10,12.5,15,17.5,20]]
#x=10
#coords2=[[x,0],[x,0.5*1.6*x**2],[0,0.5*1.6*x**2]]
#erzeugeEinfachesLatexdokument(koordinatensystemTikz([['0.5*1.6*x^2','blue'],[coords,'black','mark=*, only marks'],[coords2,'red','no markers']],[0,20,2],[0,300,50],xlabel='Zeit t in s',ylabel='Weg s in m'))
#Testen, ob nur Ein Plot:
    einzelplot=False
    if len(zuPlotten)>1:
        if isinstance(zuPlotten[1], str):
            einzelplot=True
    else:
        einzelplot=True
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
##Achseneigenschaften 
#Ich mache die Achsen ein bisschen Größer, damit die Achsenenden und Pfeilspitzen sich nicht überschneiden.
    xTickDist=xAchse[2]
    xMin=xAchse[0]-xTickDist/2.0
    xMax=xAchse[1]+xTickDist/2.0
    breite=(xMax-xMin)/xTickDist
    yTickDist=yAchse[2]
    yMin=yAchse[0]-yTickDist/2.0
    yMax=yAchse[1]+yTickDist/2.0
    hoehe=(yMax-yMin)/yTickDist
    tikzcommand.append('\\begin{axis}[    axis lines = middle, scale only axis=true, at={(0,0)},')
    tikzcommand.append('    width='+str(breite)+' cm, xmin = '+str(xMin)+', xmax = '+str(xMax)+',xtick distance = '+str(xTickDist)+',')
    tikzcommand.append('    height='+str(hoehe)+'cm, ymin = '+str(yMin)+', ymax = '+str(yMax)+', ytick distance = '+str(yTickDist)+',')
    tikzcommand.append('    xlabel = {'+xlabel+'},x label style={at={(current axis.right of origin)},anchor=north, below=5mm},')
    tikzcommand.append('    ylabel = {'+ylabel+'},y label style={at={(current axis.above origin)},anchor=south}]')
    if einzelplot:
        plot=zuPlotten[0]
        tikzcommand.append('    \\addplot[domain = '+str(xAchse[0])+':'+str(xAchse[1])+',samples = 200,smooth,thick,'+plot[1]+' ] { ('+plot[0]+')};')
    else:
        for plot in zuPlotten:
            if isinstance(plot[0], str):
                tikzcommand.append('    \\addplot[domain = '+str(xAchse[0])+':'+str(xAchse[1])+',samples = 200,smooth,thick,color='+plot[1]+' ] { ('+plot[0]+')};')
            else:
                tikzcommand.append('    \\addplot[thick,color='+plot[1]+','+plot[2]+' ] coordinates{ '+' '.join(['('+str(p[0])+','+str(p[1])+')' for p in plot[0]])+'};')
    tikzcommand.append('\\end{axis}')
    tikzcommand.append('\\node[below] at ('+str(0-xMin/xTickDist)+','+str(0-yMin/yTickDist)+') {0};')
    tikzcommand.append('\\node[left] at ('+str(0-xMin/xTickDist)+','+str(0-yMin/yTickDist)+') {0};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand



def koordinatensystemNatuerlicheZahlen(x,y,dx=-1,dy=-1,laenge=-1,hoehe=-1,NullAufNull=False,xlabel='',ylabel=''):
#Diese Funktion
#Erstelle das Koordinatensystem:
    if True:
        xWerte=x
        yWerte=y
        if NullAufNull:
            if not (x[0]==0):
                x=[0]+x
            if not (y[0]==0):
                y=[0]+y
        xPos=range(len(x))
        yPos=range(len(y))
        if dx<0:
            dx=min(np.diff(x))
        print(dx)
        if dy<0:
            dy=min(np.diff(y))
            yEnd=y[-1]
        else:
            yEnd=math.ceil(y[-1]/dy)*dy
        if laenge<0:
            laenge=(x[-1]-x[0])/dx
        if hoehe<0:
            hoehe=(yEnd-y[0])/dy
        xAchszahlenstrahlWerte=np.linspace(x[0],x[-1],(x[-1]-x[0])/dx+1)
        yAchszahlenstrahlWerte=np.linspace(y[0],yEnd,(yEnd-y[0])/dy+1)
        print(yAchszahlenstrahlWerte)
        pos=np.linspace(0 ,laenge,len(xAchszahlenstrahlWerte))
        Mx=(pos[1]-pos[0])/(1.0*xAchszahlenstrahlWerte[1]-xAchszahlenstrahlWerte[0])
        bx=1.0*xAchszahlenstrahlWerte[0]-Mx*pos[0]
        xHT=[[pos[i],xAchszahlenstrahlWerte[i]] for i in range(len(xAchszahlenstrahlWerte))]
        UT=[]
        pos=np.linspace(0 ,hoehe,len(yAchszahlenstrahlWerte))
        My=(pos[1]-pos[0])/(1.0*yAchszahlenstrahlWerte[1]-yAchszahlenstrahlWerte[0])
        by=1.0*yAchszahlenstrahlWerte[0]-My*pos[0]
        yHT=[[pos[i],yAchszahlenstrahlWerte[i]] for i in range(len(yAchszahlenstrahlWerte))]
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand=tikzcommand+zahlenstrahlNatuerlicheZahlenTikz([xHT,UT],beginEnd=False,laenge=laenge+1.5)
    tikzcommand=tikzcommand+zahlenstrahlNatuerlicheZahlenSenkrechtTikz([yHT,UT],beginEnd=False,hoehe=hoehe+1.0)
#Markiere die Punkte:
    if True:
        xWerteAngepasst=[]
        yWerteAngepasst=[]
        for i,x in enumerate(xWerte):
            y=yWerte[i]
            xWerteAngepasst.append(1.0*x*Mx+bx)
            yWerteAngepasst.append(1.0*y*My+by)
            tikzcommand.append('\\node at ('+str(xWerteAngepasst[i])+','+str(yWerteAngepasst[i])+')[circle,fill,inner sep=1.5pt]{};')
        for i in range(len(xWerte)-1):
            tikzcommand.append('\\draw[black] ('+str(xWerteAngepasst[i])+','+str(yWerteAngepasst[i])+') -- ('+str(xWerteAngepasst[i+1])+','+str(yWerteAngepasst[i+1])+');')
#Beschrifte die Achsen:
    if len(xlabel)>0:
        tikzcommand.append('\\node[below right] at ('+str(xHT[-1][0]+0.5)+',0){'+xlabel+'};')
#Beschrifte die Achsen:
    if len(ylabel)>0:
        tikzcommand.append('\\node[above left] at (0,'+str(yHT[-1][0]+0.5)+'){'+ylabel+'};')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand

