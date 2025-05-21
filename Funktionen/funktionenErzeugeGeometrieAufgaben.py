#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenErzeugeGeometrieAufgaben.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
import math
import random
#    farben={"magenta":"Magenta","darkgray":"Dunkelgrau", "violet":"Violett","blue":"Blau","gray":"Grau","green":"Green","brown":"Braun","black":"Schwarz","pink":"Rosa","red":"Rot","yellow":"Gelb","orange":"Orange"}

def erzeugeWinkelZeichnenMessen(zeichnen=True,mitText=True,anzSpalten=[2,2]):
    winkel=random.randint(20,180)
    name=random.choice(['\\alpha','\\beta','\\gamma','\\delta'])
    afg=[f'{"Zeichne " if zeichnen else "Miss folgen"}den Winkel{f" ${name}$={winkel}°:" if zeichnen else ":"}']
    if not zeichnen:
        afg=['\\pbox{\\linewidth}{']+afg+winkelZeichnen(winkel=[winkel,f'${name}$'])+['}']
    lsg=winkelZeichnen(winkel=[winkel,f'{winkel}°'],LSG=True)
    lsg=['\\pbox{\\linewidth}{']+[f'${name}$={winkel}° \\\\']+lsg+['}']
    return [afg,lsg,[]]
    

def erzeugeFindeParallelLinien(anzahl=6,mitText=True,anzSpalten=[2,2]):
    winkel=random.sample(list(range(-anzahl,anzahl)),anzahl)
    gleich=random.sample(list(range(0,anzahl)),2)
    winkel[gleich[0]]=winkel[gleich[1]]
    aufg=['Finde die zwei parallele Linien']
    afg=['\\pbox{\\linewidth}{']+ (aufg if mitText else [])+ zeichneLinienMitVorgWinkel(linienWinkel=winkel)+['}']
    winkel[gleich[0]]=[winkel[gleich[0]],'red']
    winkel[gleich[1]]=[winkel[gleich[1]],'red']
    lsg=zeichneLinienMitVorgWinkel(linienWinkel=winkel)
    return [afg,lsg,[]]

def erzeugeSenkrechteLinien(anzahlProEcke=2,mitText=True,anzSpalten=[2,2]):
    winkel=random.sample(list(range(-4*anzahlProEcke,4*anzahlProEcke)),4*anzahlProEcke)
    gleich=random.sample(list(range(0,len(winkel))),2)
#Setze eine horizontale Linie und eine Senkrechte Linie genau Senkrecht zueinander,
#indem sie den gleichen Winkel haben.
    indi0=random.choice([j*anzahlProEcke+i for j in range(4) for i in range(anzahlProEcke) if j%2==0])
    indi90=random.choice([j*anzahlProEcke+i for j in range(4) for i in range(anzahlProEcke) if j%2==1])
    winkel[indi90]=winkel[indi0]
    winkel0=winkel[indi0]
    winkel90=90+winkel[indi0]
#Winkel nach den 4 Ecken sortieren und um 90° drehen
    winkel=[winkel[:int(len(winkel)/4)]+[x+90 for x in winkel[int(len(winkel)/4):2*int(len(winkel)/4)]]]+[winkel[2*int(len(winkel)/4):3*int(len(winkel)/4)]+[x+90 for x in winkel[3*int(len(winkel)/4):]]]
    aufg=['Finde die zwei senkrechten Linien']
    afg=['\\pbox{\\linewidth}{']+ (aufg if mitText else [])+ zeichneRechtwinklLinien(linienWinkel=winkel)+['}']
    for x in winkel:
        if winkel0 in x:
            x[x.index(winkel0)]=[x[x.index(winkel0)],'red']
        if winkel90 in x:
            x[x.index(winkel90)]=[x[x.index(winkel90)],'red']
    lsg=zeichneRechtwinklLinien(linienWinkel=winkel)
    return [afg,lsg,[]]

def erzeugeStreckungsaufgaben(mitText=True,anzSpalten=[2,2],mitKoord=False):
    xyMax=5 if anzSpalten[0]==2 else 12
    n=random.randint(2,3)
    art={2:'Gerade',3:'Dreieck',4:'Viereck'}
    k=random.choice([0.5,2,3])
    punkte={'Z':[random.randint(0,int(xyMax/2)),random.randint(0,int(xyMax/2))]}
    for i in range(n):
        exec(f'punkte[buchstabenGross[i]]=[random.randint(1,int(xyMax/2)),random.randint(1,int(xyMax/2))]')
        while punkte[buchstabenGross[i]] in [punkte[x] for x in list(punkte.keys()) if not x==buchstabenGross[i]] or len(set([punkte[x][0] for x in list(punkte.keys())]))==1 or len(set([punkte[x][1] for x in list(punkte.keys())]))==1:
            exec(f'punkte[buchstabenGross[i]]=[random.randint(1,int(xyMax/2)),random.randint(1,int(xyMax/2))]')
    afg=[f'{f"Strecke folgende{"" if n==2 else"s" } {art[n]} mit den Punkten " if mitText else ""}{", ".join([f"{x}	({punkte[x][0]}|{punkte[x][1]})" for x in list(punkte.keys())])}{" und dem Faktor" if mitText else ","} k={k}']
    if mitKoord:
        afg=['\\pbox{\\linewidth}{']+ afg+['\\\\']+ diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[0,xyMax,xyMax+1],yAchse=[0,xyMax,xyMax+1])+['}']
    lsg=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[0,xyMax,xyMax+1],yAchse=[0,xyMax,xyMax+1])
    for i,pkt in enumerate(list(punkte.keys())):
#        lsg.insert(-1,f'\\node ({pkt}) at ({punkte[pkt][0]},{punkte[pkt][1]})  {{•}};')
        lsg.insert(-1,f'\coordinate[label={315 if punkte[pkt][1]==0 else 270}:${pkt}$] ({pkt}) at ({punkte[pkt][0]},{punkte[pkt][1]}) ;')
        lsg.insert(-1,f'\\fill[black] ({pkt}) circle (2pt);')
        if not pkt=='Z':
            lsg.insert(-1,f"\\coordinate[label={315 if punkte[pkt][1]==0 else 270}:${pkt}$'] ({pkt}2) at ($(Z)!{k}!({pkt})$);")
            lsg.insert(-1,f'\\fill[red] ({pkt}2) circle (2pt);')
    for i,pkt in enumerate(list(punkte.keys())):
        if not pkt=='Z':
            lsg.insert(-1,f'\\draw[blue] (Z) -- ({pkt});')
            lsg.insert(-1,f'\\draw[red] ({pkt}) -- ({pkt}2);')
            if i==len(list(punkte.keys()))-1:
                lsg.insert(-1,f'\\draw[black] (A) -- ({pkt});')
                lsg.insert(-1,f'\\draw[green] (A2) -- node[above,black,sloped]{{k={k}}} ({pkt}2);')
            if n>2 and i<len(list(punkte.keys()))-1:
                lsg.insert(-1,f'\\draw[black] ({pkt}) -- ({list(punkte.keys())[i+1]});')
                lsg.insert(-1,f'\\draw[green] ({pkt}2) -- ({list(punkte.keys())[i+1]}2);')
    return [afg,lsg,[]]

def erzeugeStrahlensaetzeAufgaben(mitText=True,anzSpalten=[2,2]):
    k=random.randint(14,21)/10
    k=k*random.choice([1,-1])
    einheit=random.choice(['mm', 'cm', 'dm', 'm', 'km'])
#Erzeuge Zufällige Positionen für die Zeichnung
    m1=1
    m2=1
    while abs(m1-m2)<3:
        A=[random.randint(5,25)/10,random.randint(5,25)/10]
        B=[random.randint(5,25)/10,A[1]+random.randint(10,20)/10]
        m1=A[1]/A[0]
        m2=B[1]/B[0]
    Astr=[x*k for x in A]
    Bstr=[x*k for x in B]
#Erzeuge die zu berechenden Werte aus den Zeichhnungswerten durch Multiplikation mit einem Faktor
    fZA=random.randint(10,100)/10    #faktor von der Zeichnung zur Aufgabe
    SAWert=math.dist([0,0],A)*fZA
    SBWert=math.dist([0,0],B)*fZA
    SAstrWert=math.dist([0,0],Astr)*fZA
    SBstrWert=math.dist([0,0],Bstr)*fZA
    ABWert=math.dist(A,B)*fZA
    AstrBstrWert=math.dist(Astr,Bstr)*fZA
    streckenLaengen=[SAWert,SAstrWert,SBWert,SBstrWert,ABWert,AstrBstrWert]
    streckenLaengenIndexe=list(range(len(streckenLaengen)))
#Gib den Punkten zufällige Bezeichnungen
    punkte=random.sample(buchstabenGross,5)
    p=punkte
#Und bastel die daraus die Streckenbezeichnungen
    strecken=[p[0]+p[1],p[0]+p[2],p[0]+p[3],p[0]+p[4],p[1]+p[3],p[2]+p[4]]
#Für den Strahlensatz braucht man nur 4 der 6 Strecken
    entferntPos=random.randint(0,2)
    entfernt=[2*entferntPos,2*entferntPos+1]
    streckenLaengenRed=list(streckenLaengen)
    del streckenLaengenRed[entfernt[0]:entfernt[1]+1]
    del streckenLaengenIndexe[entfernt[0]:entfernt[1]+1]
    streckenRed=list(strecken)
    del streckenRed[entfernt[0]:entfernt[1]+1]
#    auswahlFarben=random.sample(list(farben.keys()),6)
    auswahlFarben=['black']*6
#    auswahlFarben[entfernt[0]:entfernt[1]+1]=['black']*2
#Es bleiben vier Strecken ueber. Eine davon muss berechnet werden.
    xNr=random.randint(0,3)
    groesse='{17 cm}' if anzSpalten[0] == 1 else '{7 cm}'
    afg=[f'\\pbox{groesse}{{']
    afg=afg+(['Zeichne die angegebenen Strecken farbig nach und berechne die fehlende Seite.\\\\'] if mitText else [])
    afg=afg+strahlensatz(A=A, B=B,k=k, farben=['black']*6,punkte=punkte,strecken=['']*len(strecken))
    afg=afg+['$\\begin{aligned}']
    for i,l in enumerate(streckenLaengenRed):
        if not i==xNr:
            afg=afg+[F'\\overline{{{streckenRed[i]}}}&={strNW(l,True)}~{einheit}\\\\']
    afg=afg+['\\end{aligned}$']
    afg=afg+['}']
#Entnehme dir die Indexe nach dem Motto: Groß zu klein ist gleich Groß zu klein.
#Die Strecken sind so angeordnet: [klein,groß,klein,groß]
    zaehler1='x'        #red
    nenner1Nr= xNr-1 if xNr in [1,3] else xNr+1     #blue
    zaehler2Nr=xNr+2 if xNr in [0,1] else xNr-2     #olive
    nenner2Nr= 3 if xNr==0 else ( 2 if  xNr==1 else  ( 1 if xNr==2  else 0))    #orange
    farben=['red','blue','green','orange']
    auswahlFarben[streckenLaengenIndexe[xNr]]=farben[0]
    auswahlFarben[streckenLaengenIndexe[nenner1Nr]]=farben[1]
    auswahlFarben[streckenLaengenIndexe[zaehler2Nr]]=farben[2]
    auswahlFarben[streckenLaengenIndexe[nenner2Nr]]=farben[3]
    groesse='{17 cm}' if anzSpalten[1] == 1 else '{7 cm}'
    lsg=[f'\\pbox{groesse}{{']
    lsg=lsg+strahlensatz(A=A,B=B,k=k,farben=auswahlFarben,punkte=punkte,strecken=['']*len(strecken))
    lsg=lsg+['$\\begin{aligned}']
    lsg=lsg+[F'\\frac{{\\color{{{farben[0]}}}{{x}}}}{{\\overline{{\\color{{{farben[1]}}}{{{streckenRed[nenner1Nr]}}}}}}}&=\\frac{{\\overline{{\\color{{{farben[2]}}}{{{streckenRed[zaehler2Nr]}}}}}}}{{\\overline{{\\color{{{farben[3]}}}{{{streckenRed[nenner2Nr]}}}}}}} \\quad &  \\\\']
    lsg=lsg+[F'\\frac{{x}}{{{strNW(streckenLaengenRed[nenner1Nr],True)}}}&=\\frac{{{strNW(streckenLaengenRed[zaehler2Nr],True)}}}{{{strNW(streckenLaengenRed[nenner2Nr],True)}}} \\quad &  | \\cdot {strNW(streckenLaengenRed[nenner1Nr],True)} \\\\']
    lsg=lsg+[F'x&=\\frac{{{strNW(streckenLaengenRed[zaehler2Nr],True)}}}{{{strNW(streckenLaengenRed[nenner2Nr],True)}}} \\cdot {strNW(streckenLaengenRed[nenner1Nr],True)} \\quad &   \\\\']
    lsg=lsg+[F'x&={strNW(streckenLaengenRed[xNr],True)}~{einheit}&']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeMittelsenkrechteAufgabe(mitText=True):
    laenge=random.randint(30,90)/10
    afg=F'Zeichne die Mittelsenkrechte durch eine Linie der Länge von {strNW(laenge)} cm' if mitText else F'l={strNW(laenge)} cm'
    lsg=mittelsenkrechte(laenge)
    return [afg,lsg,[]]

def erzeugeWinkelhalbbierendeAufgabe(mitText=True,anzSpalten=[2,2]):
    alpha=random.randint(20,160)
    groesse='{17 cm}' if anzSpalten[1] == 1 else '{7 cm}'
    afg=[f'\\pbox{groesse}{{']
    afg=afg+([F'Zeichne die Winkelhalbierende für:\\\\']  if mitText else [])
    afg=afg+winkelhalbierende(winkel=alpha,mitLsg=False)+['}']
    lsg=winkelhalbierende(alpha)
    return [afg,lsg,[]]

def erzeugeDreieckWSWKonstrukt(planfigur=False,mitHilfe=False,mitText=True,anzSpalten=[2,2]):
    WSW=[['alpha','c','beta'],['beta','a','gamma'],['gamma','b','alpha']]
    auswahl=random.choice(WSW)
    w1,w2=90,80
    minWinkel=20 if anzSpalten[0] < 2 else 40
    while abs(180-(w1+w2))<minWinkel:
        w1=random.choice(list(range(20,120,10)))
        w2=random.choice(list(range(20,180-w1,10)))
    l=random.randint(40,80)/10 if anzSpalten[0] < 2 else random.randint(20,40)/10 
    afg=['\\pbox{\\linewidth}{']
    afg=afg+([F'{"Markiere" if planfigur else "Zeichne"} die Planfigure und Konstruiere das Dreieck für folgende Werten:\\\\']  if mitText else [])
    afg=afg+[F'$\\begin{{aligned}}']
    afg.append(f'\\{auswahl[0]}&={strNW(w1)}^\\circ \\\\')
    afg=afg+[F'{auswahl[1]}&={strNW(l)}~cm\\\\']
    afg=afg+[F'\\{auswahl[2]}&={strNW(w2)}^\\circ  \\\\']
    afg=afg+[F'\\end{{aligned}}$ \\\\']
    afg=afg+dreieckWSWKonstr(werte=[w1,l,w2],seite=auswahl[1],mitLsg=False,zeichnePlanfigur=planfigur,mitHilfe=mitHilfe)
    afg=afg+['}']
    lsg=dreieckWSWKonstr(werte=[w1,l,w2],seite=auswahl[1],mitLsg=True,zeichnePlanfigur=True)
    return [afg,lsg,[]]

def erzeugeDreieckSWSKonstrukt(planfigur=False,mitHilfe=False,mitText=True,anzSpalten=[2,2]):
    SWS=[['b','alpha','c'],['c','beta','a'],['a','gamma','b']]
    auswahl=random.choice(SWS)
    l1=random.randint(40,80)/10 if anzSpalten[0] < 2 else random.randint(20,40)/10
    l2=random.randint(40,80)/10 if anzSpalten[0] < 2 else random.randint(20,40)/10 
    w=random.choice(list(range(30,120,10)))
    afg=['\\pbox{\\linewidth}{']
    afg=afg+([F'{"Markiere" if planfigur else "Zeichne"} die Planfigure und Konstruiere das Dreieck für folgende Werten:\\\\']  if mitText else [])
    afg=afg+[F'$\\begin{{aligned}}']
    afg.append(f'{auswahl[0]}&={strNW(l1)}~cm \\\\')
    afg=afg+[F'\\{auswahl[1]}&={strNW(w)}^\\circ \\\\']
    afg=afg+[F'{auswahl[2]}&={strNW(l2)}~cm  \\\\']
    afg=afg+[F'\\end{{aligned}}$ \\\\']
    afg=afg+dreieckSWSKonstr(werte=[l1,w,l2],winkel=auswahl[1],mitLsg=False,zeichnePlanfigur=planfigur,mitHilfe=mitHilfe)
    afg=afg+['}']
    lsg=dreieckSWSKonstr(werte=[l1,w,l2],winkel=auswahl[1],mitLsg=True,zeichnePlanfigur=True)
    return [afg,lsg,[]]


def erzeugeDreieckSSSKonstrukt(planfigur=False,mitHilfe=False,mitText=True,anzSpalten=[2,2]):
    minL,maxL=[15,30] if anzSpalten[0]>1 else [30,80]
    a,b,c=random.randint(minL,maxL)/10,random.randint(minL,maxL)/10,random.randint(minL,maxL)/10
    afg=['\\pbox{\\linewidth}{']
    afg=afg+([F'{"Markiere" if planfigur else "Zeichne"} die Planfigure und Konstruiere das Dreieck für folgende Werten:\\\\']  if mitText else [])
    afg=afg+[F'$\\begin{{aligned}}']
    afg=afg+[F'a&={strNW(a)}~cm \\\\']
    afg=afg+[F'b&={strNW(b)}~cm \\\\']
    afg=afg+[F'c&={strNW(c)}~cm \\\\']
    afg=afg+[F'\\end{{aligned}}$']
    afg=afg+dreieckSSSKonstr(werte=[a,b,c],mitLsg=False,zeichnePlanfigur=planfigur,mitHilfe=mitHilfe)
    afg=afg+['}']
    lsg=dreieckSSSKonstr(werte=[a,b,c],mitLsg=True,zeichnePlanfigur=True)
    return [afg,lsg,[]]
