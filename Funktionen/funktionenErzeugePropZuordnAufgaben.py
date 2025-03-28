#!/usr/bin/env python
# coding: utf8
import random

def proportionalPaar(anti=False):
    paare=[['Anzahl','Preis in \euro{}'],['Zeit in min','Preis in \euro{}'],['Anzahl','Volumen in l'],['Tage','Strecke in km'],['Kinder','Gruppen'],['Anzahl','Kartons']]#,['Zeit in min','Anzahl']]
    paareAnti=[ ['Stuhlreihen', 'Stühle'], ['Anzahl', 'Stücklänge in cm'],['Arbeiter', 'Zeit in h'], ['Entfernung in km', 'Geschw. in $\\frac{km}{h}$'],['Anzahl Personen', 'Gewinn in €'], ['Schrittlänge in cm', 'Anzahl Schritte']]
    return paareAnti if anti else paare

def erzeugePropTabllenAufgaben(mitPfeilen=True,mitBeschr=True):
    title=random.choice(proportionalPaar())
    op=random.choice(['*','/'])
    d1,d2,multi=[random.randint(1,12),random.randint(1,12),random.randint(1,12)]
    if d1==d2:
        d2=d2*random.randint(2,4)
    if op=='*':
        l=[d1,d1*multi]
        r=[d2,d2*multi]
    else:
        l=[d1*multi,d1]
        r=[d2*multi,d2]
    afg=tikzPropTabelle(l,r,title=title,mitPfeilen=mitPfeilen,mitBeschr=mitBeschr,mitLsg=False)
    lsg=tikzPropTabelle(l,r,title=title,mitLsg=True)
    return [afg,lsg,[[]]]

def erzeugeAntiPropTabllenAufgaben(mitPfeilen=True,mitBeschr=True):
    title=random.choice(proportionalPaar(anti=True))
    op=random.choice(['*','/'])
    d1,d2,multi=[random.randint(1,12),random.randint(1,12),random.randint(2,12)]
    if d1==d2:
        d2=d2*random.randint(2,4)
    if op=='*':
        l=[d1,d1*multi]
        r=[d2*multi,d2]
    else:
        l=[d1*multi,d1]
        r=[d2,d2*multi]
    afg=tikzPropTabelle(l,r,title=title,mitPfeilen=mitPfeilen,mitBeschr=mitBeschr,mitLsg=False,anitProp=True)
    lsg=tikzPropTabelle(l,r,title=title,mitLsg=True,anitProp=True)
    return [afg,lsg,[[]]]

def erzeugePropDiagrammErstellAufgaben(diagrammVorgegeben=True,mitText=True):
    multi=random.randint(1,12)
    xMax=6
    yMax=math.ceil((multi*xMax)/10)*10
    afg=['\\pbox{14cm}{']
    afg=afg+[F'{"Übertrage die Werte" if diagrammVorgegeben else "Erstelle aus den Werten"} {"in das " if diagrammVorgegeben else "ein"} Diagramm.\\\\' if mitText else '\\phantom{e}']
    tabelle=tikzTabelle(tabelle=[['x','y']]+[[strNW(x),strNW(multi*x)]for x in range(xMax+1)],dim=[1.5,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[-4.5,4.5])
    if diagrammVorgegeben:
        diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[0,6,7],yAchse=[0,yMax,11],xlabel='x',ylabel='y',urspr=[0,0],mitUmrandung=False)
    else:
        diagramm=[F'\\node at (7,11) {{ }};']
    afg=afg+(tabelle[:-1]+diagramm+[tabelle[-1]])
    afg=afg+ (['}'])
    tabelle=tikzTabelle(tabelle=[['x','y']]+[[x,multi*x]for x in range(xMax)],dim=[1.5,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[-4.5,4.5])
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{multi}*x','black']],xAchse=[0,6,7],yAchse=[0,yMax,11],xlabel='x',ylabel='y',urspr=[0,0],mitUmrandung=False)
    lsg=tabelle[:-1]+diagramm+[tabelle[-1]]
    return [afg,lsg,[multi]]

def erzeugePropDiagrammAufgaben(diagrammVorgegeben=True,mitText=True):
    nurText=False
    auswahl=random.choice(proportionalPaar())
    multi=random.randint(2,10)
    afg=['\\pbox{14cm}{']
    afg=afg+[F'{"Übertrage die Werte" if diagrammVorgegeben else "Erstelle aus den Werten"} der Tabelle {"in das " if diagrammVorgegeben else "ein"} Diagramm.\\\\' if mitText else '\\phantom{e}']
    xwerte=[1]
    for i in range(4):
        xwerte.append(xwerte[-1]+random.randint(1,3))
    ywerte=[x*multi for x in xwerte]
    ywerteAfg=list(ywerte)
    bleibt=random.randint(0,len(ywerte)-1)
    ywerteAfg=[x if i==bleibt else '' for i,x in enumerate(ywerte)]
    xMax=max(xwerte)
    yMax=max(ywerte)
    #[auswahl]+[[strNW(x),strNW(x*multi)]for x in xwerte]
    tabelle=tikzTabelle(tabelle=[[auswahl[0]]+xwerte,[auswahl[1]]+ywerteAfg,],dim=[2.0,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[0,-1.5])
    tabelleLsg=tikzTabelle(tabelle=[[auswahl[0]]+xwerte,[auswahl[1]]+ywerte,],dim=[2.0,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[0,-1.5])
    if diagrammVorgegeben:
        diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[0,xwerte[-1],xwerte[-1]+1],yAchse=[0,ywerte[-1],11],xlabel=auswahl[0],ylabel=auswahl[1],urspr=[0,0],mitUmrandung=False)
    else:
        diagramm=[F'\\node at (7,11) {{ }};']
    afg=afg+ ([] if nurText else (tabelle[:-1]+diagramm+[tabelle[-1]]))
    afg=afg+ ([] if nurText else ['}'])
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{multi}*x','black']],xAchse=[0,xMax,11],yAchse=[0,yMax,11],xlabel='t in s',ylabel='s in  m',urspr=[0,0],mitUmrandung=False)
    lsg=tabelleLsg[:-1]+diagramm+[tabelle[-1]]
    return [afg,lsg,[multi]]

def propDreisatz():
    auswahl=random.choice(proportionalPaar())
    xStart=random.randint(2,10)
    xZiel=random.randint(2,10)
    while xStart==xZiel:
        xZiel=random.randint(2, 12)
    yStart=random.randint(2,5)
    afg=dreiSatz(links=[strNW(x, True) for x in [xStart, '', xZiel]],rechts=[strNW(yStart*xStart),'',''],title=auswahl, breit=True,ohneKlammernLinks=True,ohneKlammernRechts=True)
    lsg=dreiSatz(links=[strNW(x, True) for x in [xStart, '1', xZiel]],
                 rechts=[strNW(x, True) for x in [yStart*xStart, yStart, yStart*xZiel]],title=auswahl, breit=True)
    return [afg,lsg,[]]

def propAntiDreisatz():
    auswahl=random.choice(proportionalPaar(anti=True))
    xStart=random.randint(2,12)
    xZiel=random.randint(2,12)
    while xStart==xZiel:
        xZiel=random.randint(2, 12)
    yStart=random.randint(2,5)
    afg=dreiSatz(links=[strNW(x, True) for x in [xStart, '',xZiel]],rechts=[strNW(yStart*xZiel),'',''],title=auswahl, breit=True,ohneKlammernLinks=True,ohneKlammernRechts=True,antiProp=True)
    lsg=dreiSatz(links=[strNW(x, True) for x in [xStart,'1',xZiel]],rechts=[strNW(x, True) for x in [yStart*xZiel, yStart*xZiel*xStart, yStart*xStart]],title=auswahl,breit=True,antiProp=True)
    return [afg,lsg,[]]

def erzeugeTabelleAusfuellen(komma=False,mitText=True):
    anzSpalten=10
    E = random.choice(einheitspaare())
    xStart=random.randint(10,1000)/100 if komma else random.randint(2,20)
    yStart=random.randint(10,1000)/100 if komma else random.randint(2,10)*xStart


def erzeugeProportionaleDreisatzRechnungen(einfach=False,komma=False,mitText=True):
    # Diese Funktion erzeugt eine proportionale Zuordnungsaufgaben
    # Aufruf:
    #         [afg,lsg]=erzeugeProportionaleDreisatzRechnungen(komma=False,mitText=True)
    E = random.choice(einheitspaare())
#Wenn kein Komma gerechnet werden soll,wähle nur Einheiten ohne Komma
    while (not komma) and (not (E[2][0]==int(E[2][0]))  or not (E[2][1]==int(E[2][1]))):
        E = random.choice(einheitspaare())
    grundwert=random.randint(E[2][0]*100,E[2][1]*100)/100 if komma else random.randint(E[2][0],E[2][1])
    xStart,xZiel=1,1
    while xStart==xZiel:
        maxWert=10 if einfach else 20
        xStart=random.randint(10,maxWert*100)/100 if komma else random.randint(2,maxWert)
        xZiel=random.randint(10,maxWert*100)/100 if komma else random.randint(2,maxWert)
    yStart=grundwert*xStart
    art=E[0].split(" ")[0]
    einh=E[0].split(" ")[1]
    if 'kg' == einh or 'g'==einh:
        afg=F'Berechne den Preis für {strNW(xZiel,True)} {einh} {art}, wenn {strNW(xStart,True)} {einh} {strNW(yStart,True)} \\euro{{}} kosten.'
        afg=afg if mitText else (F'{art}:$${strNW(xStart,True)}~{einh}\hat{{=}} {strNW(yStart,True)}~\\mbox{{\\euro{{}}}} \\rightarrow {strNW(xZiel,True)}~{einh}=\\mbox{{?}}$$')
    elif 'h'==einh:
        afg=F'Welche Strecke wurde in  {strNW(xZiel,True)} {einh} zurückgelegt, wenn man in {strNW(xStart,True)} {einh} {strNW(yStart,True)} km schafft.'
        afg=afg if mitText else (F'Bewegung:$${strNW(xStart,True)}~{einh}\hat{{=}} {strNW(yStart,True)}~\\mbox{{km}} \\rightarrow {strNW(xZiel,True)}~{einh}=\\mbox{{?}}$$')
    elif 'Anzahl'==einh:
        xStart=int(xStart)
        xZiel=int(xZiel)
        afg=F'Berechne den Preis für {strNW(xZiel,True)} {art}, wenn {strNW(xStart,True)} {art} {strNW(yStart,True)} \\euro{{}} kosten.'
        afg=afg if mitText else (F'{art}:$${strNW(xStart,True)}\hat{{=}} {strNW(yStart,True)}~\\mbox{{\\euro{{}}}} \\rightarrow {strNW(xZiel,True)}=\\mbox{{?}}$$')
    else:
        afg='Noch nichts.'
    lsg=dreiSatz(links=[strNW(x,True) for x in [xStart,'1',xZiel]],rechts=[strNW(x,True) for x in [yStart,yStart/xStart,yStart/xStart*xZiel]],title=E,breit=True)
    return [afg,lsg,[xStart,xZiel,yStart]]


def einheitspaare():
#Diese Funktion gibt ein Paar der Art aus:
#        ['Tomaten in kg','Preis in €',[0.75,4]]
#       Also: [Typ,Preis, [kleinster Preis, größter Preis]
#Aufruf:
#       paare=einheitspaare()
    preisKg=[['Tomaten',[0.75,4]],['Kartoffeln',[1,4]],['Hackfleisch',[10,20]],['Gummibärchen',[3,8]],['Lakritze',[4,14]]]
    paare=[[F'{art[0]} kg','Preis \\euro{}',art[1]] for art in preisKg]
    paare.append(['Zeit h','Strecke km',[2,200]])
    paare.append(['Eier Anzahl','Preis \\euro{}',[0.25,0.5]])
    return paare

def erzeugeAntiProportionaleDreisatzRechnungen(einfach=False,komma=False,mitText=True):
    # Diese Funktion erzeugt eine Aufgabe zur Prozentrechnung:
    # Aufruf:
    #         rechnung=erzeugeProzentRechnungen()
    #
    #      rechnung=[G,W,pP,Einheit]
    maxWert=9 if einfach else 20
    antiPaar=[['Anzahl Arbeiter','Arbeitsstunden h',[2,maxWert]],['Zeit h','Geschw. $\\frac{km}{h}$',[2,maxWert]],['Stuhlreihen Reihen','Anzahl Stühle',[2,maxWert]]]
    E = random.choice(antiPaar)
    grundwert=1000
    if einfach:
        while grundwert>100:
            grundwert=random.randint(E[2][0],E[2][1])
    else:
        grundwert=random.randint(E[2][0]*100,E[2][1]*100)/100 if komma else random.randint(E[2][0],E[2][1])
    xStart,xZiel=1,1
    while xStart==xZiel:
        xStart=random.randint(10,maxWert*100)/100 if komma else random.randint(2,maxWert)
        xZiel=random.randint(10,maxWert*100)/100 if komma else random.randint(2,maxWert)
        if 'Geschw' in E[1]:
            if grundwert*xStart*xZiel > 200:
                xStart=xZiel
    yStart=grundwert*xStart
    art1,einh1=E[0].split(" ")
    art2,einh2=E[1].split(" ")
    if einh1=='Arbeiter':
        afg=F'Wie lange brauchen {strNW(xZiel,True)} {einh1} für die Arbeit, wenn {strNW(xStart,True)} {einh1} {strNW(yStart*xZiel,True)} {einh2} brauchen?'
        afg=afg if mitText else (F'{art1}:$${strNW(xStart,True)}~{einh1}\hat{{=}} {strNW(yStart,True)}~\\mbox{{h}} \\rightarrow {strNW(xZiel,True)}~{einh1}=\\mbox{{?}}$$')
    elif 'h' == einh1:
        afg=F'Du brauchst für {yStart*xZiel*xStart} km {xStart} h, fährst also {yStart*xZiel} $\\frac{{km}}{{h}}$. Welche Geschwindigkeit brauchst du für {yStart*xZiel*xStart} km, wenn du {xZiel} h fahren willst.'
        afg=afg if mitText else (F'Geschwindigkeit:$${strNW(xStart,True)}~{einh1}\hat{{=}} {strNW(yStart*xZiel,True)}~\\frac{{km}}{{h}} \\rightarrow {strNW(xZiel,True)}~{einh1}=\\mbox{{?}}$$')
    elif 'Reihen'==einh1:
        xStart=int(xStart)
        xZiel=int(xZiel)
        afg=F'Wie viele Stühle stehen in {strNW(xZiel,True)} Reihen, wenn {yStart*xZiel} Stühle in {xStart} Stuhlreihen stehen?'
        afg=afg if mitText else (F'{art1}:$${strNW(xStart,True)}~\\mbox{{{einh1}}}\hat{{=}} {strNW(yStart,True)}~\\mbox{{{einh2}}} \\rightarrow {strNW(xZiel,True)}~\\mbox{{{einh1}}}=\\mbox{{?}}$$')
    else:
        afg='Noch nichts.'
    lsg=dreiSatz(links=[strNW(x,True) for x in [xStart,'1',xZiel]],rechts=[strNW(x,True) for x in [yStart*xZiel, yStart*xZiel*xStart, yStart*xStart]],title=E,breit=True,antiProp=True)
    return [afg,lsg,[xStart,xZiel,yStart]]

