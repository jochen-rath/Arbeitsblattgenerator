#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#      exec(open("Funktionen/funktionen.py").read())



def loeseGleichungEinfachMitZweiVariabeln(G="2*x+6=3*y-2", variable='x y', lsgVorgabe=['x=0','y=0','x=1'], mitTikzUmrandung=True):
#Diese Funktion löst ein einfaches Gleichungssystem mit x und y ohne Potenzen
#
#Beispiel:         2*x+6=3*y-2
#Aufruf:   loesung=loeseGleichungEinfachMitZweiVariabeln(G,variabel)
#
#mit G=Gleichung
#    variabel=Variabel, nach der Aufgelöst wird
    latexcommand=[]
    if mitTikzUmrandung:
        latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        latexcommand.append('\\begin{tikzpicture}[show background grid]')
        latexcommand.append('\\node[below right] at (0,0.1) {')
        latexcommand.append('$\\begin{aligned}')
    latexcommand.append(G.replace('*','\\cdot ').replace('=','&=')+'\\\\')
    for i,vorgabe in enumerate(lsgVorgabe):
        latexcommand.append('\\mbox{Lsg '+str(i+1)+': }'+vorgabe+'\\\\')
        Glsg=G.replace(vorgabe.split('=')[0],vorgabe.split('=')[1])
        glLsg=loeseGleichungEinfachMitEinerVariabel(Glsg,variable.replace(vorgabe.split('=')[0],'').replace(' ',''),mitTikzUmrandung=False,latexAusgabe=True)
        print(glLsg)
        latexcommand=latexcommand+glLsg
        latexcommand[-1]=vorgabe+'~\\rightarrow '+latexcommand[-1]+'\\\\'
        latexcommand.append(latexcommand[-1])
        latexcommand[-2]='\\makebox[0pt][l]{\\uline{\phantom{$'+latexcommand[-2].replace('&','')+'$}}}'
    if mitTikzUmrandung:
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')
        latexcommand.append('\\endgroup')
    return latexcommand

def zeichneGleichungEinfachMitZweiVariabeln(G="2*x+6=3*y-2",variable='x y',lsgVorgabe=['x=0','y=0','x=1'],achsenlaenge=10,maxX=5,maxM=None,minX=None,mitTikzUmrandung=True):
#Diese Funktion löst ein einfaches Gleichungssystem mit x und y ohne Potenzen
#
#Beispiel:         2*x+6=3*y-2
#Aufruf:   loesung=loeseGleichungEinfachMitZweiVariabeln(G,variabel)
#
#mit G=Gleichung
#    variabel=Variabel, nach der Aufgelöst wird
    latexcommand=['']
    if mitTikzUmrandung:
        latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        latexcommand.append('\\begin{tikzpicture}[show background grid]')
        latexcommand.append('\\node[below right] at (0,0.1) {')
        latexcommand.append('$\\begin{aligned}')
#Hole dir die Lösung in schriftlicher Form
    loesungen=loeseGleichungEinfachMitZweiVariabeln(G=G,variable=variable,mitTikzUmrandung=False)
    latexcommand=latexcommand+loesungen
    if mitTikzUmrandung:
        latexcommand.append('\\end{aligned}$};')
    punkte=[]
#Hol dir nur die Punkte
    for i,vorgabe in enumerate(lsgVorgabe):
        Glsg=G.replace(vorgabe.split('=')[0],vorgabe.split('=')[1])
        punkte.append([vorgabe,loeseGleichungEinfachMitEinerVariabel(Glsg,variable.replace(vorgabe.split('=')[0],'').replace(' ',''),mitTikzUmrandung=False,latexAusgabe=False)])
#Sortiere die Punkte so, dass die x-Koordinate vorne ist.
    punkte=[[x[0].split('=')[1],x[1].split('=')[1]] if 'x' in x[0] else [x[1].split('=')[1],x[0].split('=')[1]] for x in punkte]
#Erzeuge aus den Lösungen eine lineare Gleichung und plotte dies
    try:
        m=str(eval('('+punkte[1][1]+'-'+punkte[0][1]+')/('+punkte[1][0]+'-'+punkte[0][0]+')'))
    except:
        return 'Error'
    b=str(eval([x[1] for x in punkte if x[0]=='0'][0]))
    term=m+'*x+'+b
    if not minX:
        minX=-maxX
    yAchsenSettings=setzeAchsenEinteilungLaenge(minMaxY(term,'x',maxX)+[achsenlaenge*1.5])[1:-1]
    yLaenge=setzeAchsenEinteilungLaenge(minMaxY(term,'x',maxX)+[achsenlaenge*1.5])[-1]
    xStei=(m[1] if type(m)==list else 1)
    yStei=(evalFunc(term,x=xStei)-evalFunc(term,x=0))
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[term,'black']],xAchse=[minX,maxX,achsenlaenge],yAchse=list(yAchsenSettings)+[achsenlaenge*1.5],koordinaten=[[eval(x[0]),eval(x[1])] for x in punkte],mitUmrandung=False,urspr=[0,-len(loesungen)*0.5-yLaenge-1])
    latexcommand=latexcommand+diagramm
    if mitTikzUmrandung:
        latexcommand.append('\\end{tikzpicture}')
        latexcommand.append('\\endgroup')
    return latexcommand


def loeseZweiGleichungenMitZweiVariablen(G=["4*y+2*x=8","6*y-7*x-6=36"],variable='x y',achsenlaenge=10,maxX=5,maxM=None,minX=None,schub=2,zeichnerisch=True,mitTikzUmrandung=True):
#Diese Funktion löst zeichnerisch ein einfaches Gleichungssystem mit 2 Gleichungen x und y ohne Potenzen
#
#Beispiel:         G=["4*y+2*x=8","6*y-7*x-6=36"]
#Aufruf:   loesung=zeichneZweiGleichungenBestSchnittpunkt(G,variabel)
#
#mit G=Gleichungen
#    variabel=Variabeln, Achtung, die Variabeln müssen mit Leerzeichen getrennt sein und die zweite ist die Koordinate, die nach oben zeigt (y)
    latexcommand=[]
    if mitTikzUmrandung:
        latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[below right] at (0,0.1) {')  
        latexcommand.append('$\\begin{aligned}')  
#Hole dir die 1. Lösung in schriftlicher Form und LaTeX Form
    try:
        geradenFkt1=formeEinfacheFormelNachVorgabenUm(G=G[0],gesucht=variable.split(' ')[1],latexAusgabe=False)
    except:
        return 'Error1'
    if geradenFkt1=='Error':
        return 'Error2'
    geradenFkt1Latex=formeEinfacheFormelNachVorgabenUm(G=G[0],gesucht=variable.split(' ')[1],mitTikzUmrandung=False)
    latexcommand=latexcommand+geradenFkt1Latex
#Unterstreiche die 1. Geradengleichung
    latexcommand.append(latexcommand[-1])
    latexcommand[-2]='\\makebox[0pt][l]{\\uline{\phantom{$'+latexcommand[-2].replace('&','')+'$}}}'
    latexcommand=latexcommand+['\\\\']
#Hole dir die 2. Lösung in schriftlicher Form
    try:
        geradenFkt2=formeEinfacheFormelNachVorgabenUm(G=G[1],gesucht=variable.split(' ')[1],latexAusgabe=False)
    except:
        return 'Error3'
    if geradenFkt2=='Error':
        return 'Error4'
    geradenFkt2Latex=formeEinfacheFormelNachVorgabenUm(G=G[1],gesucht=variable.split(' ')[1],mitTikzUmrandung=False)
    latexcommand=latexcommand+geradenFkt2Latex
#Unterstreiche die 2. Geradengleichung
    latexcommand.append(latexcommand[-1])
    latexcommand[-2]='\\makebox[0pt][l]{\\uline{\phantom{$'+latexcommand[-2].replace('&','')+'$}}}'
    latexcommand=latexcommand+['\\\\']
    if mitTikzUmrandung and zeichnerisch:
        latexcommand.append('\\end{aligned}$};')
#Finde den Schnittpunkt
    try:
        nachXAufl=loeseGleichungEinfachMitEinerVariabel(G=geradenFkt1.split('=')[1] + '=' + geradenFkt2.split('=')[1],variable=variable.split(' ')[0],mitTikzUmrandung=False, latexAusgabe=True,mitProbe=False)
        xSchnittpkt=loeseGleichungEinfachMitEinerVariabel(G=geradenFkt1.split('=')[1]+'='+geradenFkt2.split('=')[1],variable=variable.split(' ')[0],latexAusgabe=False,mitProbe=False).split('=')[1]
    except:
        return 'Error5'
    try:
        nachYAufl=loeseGleichungEinfachMitEinerVariabel(G=geradenFkt1.replace(variable.split(' ')[0],'('+str(xSchnittpkt)+')'),variable=variable.split(' ')[1],mitTikzUmrandung=False, latexAusgabe=True,mitProbe=False)
        ySchnittpkt=geradenFkt1.split('=')[1].replace(variable.split(' ')[0],'('+str(xSchnittpkt)+')')
    except:
        return 'Error6'
#Wenn die Koordinaten der Schnittpunkte kleiner als 0.5 sind, verlange ein neues Gleichungssystem
    if zeichnerisch:
        xSchnittpkt=eval(xSchnittpkt)
        ySchnittpkt=eval(ySchnittpkt)
        if abs((xSchnittpkt))<0.5 or abs((ySchnittpkt))<0.5:
            print('xSchnittpkt='+str(xSchnittpkt)+', ySchnittpkt='+str(ySchnittpkt))
            return 'Error'
    #Bestimme die Dimensionen des Koordinatensystem.
        term1=geradenFkt1.split('=')[1]
        if not minX:
            minX=-maxX
        yAchsenSettings=setzeAchsenEinteilungLaenge(minMaxY(term1,'x',maxX)+[achsenlaenge*1.5])[1:-1]
        yLaenge=setzeAchsenEinteilungLaenge(minMaxY(term1,'x',maxX)+[achsenlaenge*1.5])[-1]
    #Plotte das Koordinatensystem. Verschiebe den Ursprung so, dass es unterhalb der Gleichungen ist. Nutze dazu die Anzahl an Einträgen in den Latex-Geradenfunktionen Listen.
        diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[term1,'black'],[geradenFkt2.split('=')[1],'red']],xAchse=[minX,maxX,achsenlaenge],yAchse=list(yAchsenSettings)+[achsenlaenge*1.5],koordinaten=[[xSchnittpkt,ySchnittpkt]],streckenzug=[[xSchnittpkt,0],[xSchnittpkt,ySchnittpkt],[0,ySchnittpkt]],textNode=[[xSchnittpkt,0,strNW(xSchnittpkt,runden=True),'above'],[0,ySchnittpkt,strNW(ySchnittpkt,runden=True),'right']],mitUmrandung=False,urspr=[0,-(len(geradenFkt1Latex)+len(geradenFkt2Latex))*0.5-yLaenge-schub])
        latexcommand=latexcommand+diagramm
    else:
        latexcommand = latexcommand+['\\\\']+['\\mbox{Gleichsetzen:}& & &\\\\']+nachXAufl
        latexcommand.append(latexcommand[-1])
        latexcommand[-2]='\\makebox[0pt][l]{\\uline{\phantom{$'+latexcommand[-2].replace('&','')+'$}}}'
        latexcommand=latexcommand+['\\\\']
        latexcommand = latexcommand+['\\\\']+['\\mbox{Einsetzen:}& & &\\\\']+nachYAufl
        latexcommand.append(latexcommand[-1])
        latexcommand[-2]='\\makebox[0pt][l]{\\uline{\phantom{$'+latexcommand[-2].replace('&','')+'$}}}'
        latexcommand = latexcommand+['\\end{aligned}$};']
    if mitTikzUmrandung:
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand