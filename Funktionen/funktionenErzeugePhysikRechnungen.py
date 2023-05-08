#!/usr/bin/env python
# coding: utf8
import os
#Inhalt

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random


def erzeugeGeschwindigkeitsBerechnungen(typ='',einheit='m/s',umrechnen=False,einfach=True,mitText=True,hauptschule=False):
#Diese Funktion erstellt Aufgaben zur Berechnung der Geschwindigkeit, Zeit oder Strecke bei Gegebenen Strecken, Zeit
#oder Geschwindigkeitsangaben:
#           [afg,lsg,[t,s,v,laenge,zeit]]=erzeugeGeschwindigkeitsBerechnungen(typ='',einheit='m/s',umrechnen=False,einfach=True,mitText=True)
#Mit:
#              typ=['Geschwindigkeit','Zeit','Strecke']
#              einheit='m/s'   --> Sollen die Werte in m/s oder km/h angegeben werden.
#              umrechnen=True, False --> Wenn True, gibt es Längen auch in dm,cm,mm und Zeiten in min.
#              einfach=True, False --> Ob Kommazahlen verwendet werden sollen oder nicht.
#              mitText=True, False --> Man kann den Aufgabentext weg lassen.
    groessen,einheitenZuTimedelta,einheiten=einheitenListe()
    typen=['Geschwindigkeit','Zeit','Strecke']
    if typ not in typen:
        typ=random.choice(typen)
    zukleinOderZuGross=True
#Manchmal entstehen m/s Werte, die kleiner als 0,01 sind. Dann sind die in der Lösung wegen Runden gleich 0.
    while zukleinOderZuGross:
        laenge=random.choice(einheiten['laengen']) if umrechnen else ('m' if einheit=='m/s' else 'km')
        zeit=random.choice(einheiten['zeit'][2:]) if umrechnen else ('s' if einheit=='m/s' else 'h')
        t=random.randint(1,1e3) if umrechnen else random.randint(1,12)
        s=random.randint(1,1e3) if umrechnen else  (((t*random.randint(1,20)) if einfach else  (t+random.randint(50,500)/10.0)) * (1 if typ== 'm/s' else random.randint(1,4)))
        if hauptschule:
            t=random.randint(2,10)
            s=t*random.randint(2,5)
        v=s/t
        v_mps=v*(groessen[laenge]/groessen[zeit])
        v_kmph=v_mps*3.6
        if v_mps > 0.01 and v_mps < 10000: #299792458:
            zukleinOderZuGross=False
#Berechnung der Aufgaben und Lösungen:
    if typ=='Geschwindigkeit':
        afg=F'{"Berechne die Geschwindigkeit für " if mitText else ""}s={strNW(s)} {laenge}{" und" if mitText else ","} t={t} {zeit}{"." if mitText else ""}'
#Berechnung der Einheitenumrechnung
        if laenge=='m' and zeit=='s':
            umrechnentext=F'{strNW(v,True)}\\cdot 3,6~\\frac{{km}}{{h}}={strNW(v*3.6,True)}~\\frac{{km}}{{h}}'
        elif laenge=='km' and zeit=='h':
            umrechnentext=F'{strNW(v,True)}:3,6~\\frac{{m}}{{s}}={strNW(v/3.6,True)}~\\frac{{m}}{{s}}'
        else:
            umrechnentext=F'{strNW(v,True)}\\cdot \\frac{{{strNW(groessen[laenge])}~m}}{{{strNW(groessen[zeit])}~s}}'
            umrechnentext=F'{umrechnentext}={strNW(v_mps,True)}~\\frac{{m}}{{s}}'
            umrechnentext=F'{umrechnentext}={strNW(v_mps,True)}\\cdot 3,6~\\frac{{km}}{{h}}'
            umrechnentext=F'{umrechnentext}={strNW(v_kmph,True)}~\\frac{{km}}{{h}}'
        lsg = ['$\\begin{aligned}']
        lsg=lsg+[F'v&=\\frac{{s}}{{t}}=\\frac{{{strNW(s)}~{laenge}}}{{{t}~{zeit}}}={strNW(v,True)}~\\frac{{{laenge}}}{{{zeit}}} \\\\']
        lsg=lsg+[F'v&={"=".join(umrechnentext.split("=")[0:2])} \\\\']
        lsg=lsg+ ([F'v&={"=".join(umrechnentext.split("=")[2:])} \\\\'] if len(umrechnentext.split("="))>2 else [])
        lsg = lsg + ['\\end{aligned}$']
    elif typ=='Zeit':
        if umrechnen and not (zeit=='s' and laenge=='m'):
            afg = F'{F"Berechne die Zeit in {zeit} für " if mitText else F"t=? {zeit}: "}$s={strNW(s)}~{laenge}${" und" if mitText else ","} $v={strNW(v_mps, True)}~\\frac{{m}}{{s}}${"." if mitText else ""}'
            lsg=['$\\begin{aligned}']
            umrechnenInM=F's&={s}~{laenge}={strNW(s)}\\cdot {strNW(groessen[laenge])}~m={strNW(s*groessen[laenge])}~m \\\\'
            lsg=lsg+([] if laenge=='m' else [umrechnenInM])
            lsg=lsg+[F'\\rightarrow t&=\\frac{{s}}{{v}}=\\frac{{{strNW(s*groessen[laenge])}~m}}{{{strNW(v_mps,True)} \\frac{{m}}{{s}}}}={strNW(t*groessen[zeit])}~s \\\\']
            op=':' if groessen[zeit]>1 else '\\cdot'
            teiler=groessen[zeit] if groessen[zeit]>1 else (1/groessen[zeit])
            lsg=lsg+([F'\\rightarrow t&=({strNW(t*groessen[zeit])}{op}{strNW(teiler)})~{zeit}={t}~{zeit}'] if not zeit=='s' else [])
            lsg = lsg + ['\\end{aligned}$']
        else:
            afg=F'{"Berechne die Zeit für " if mitText else ""}$s={strNW(s)}~{laenge}${" und" if mitText else ","} $v={strNW(v,True)}~\\frac{{{laenge}}}{{{zeit}}}${"." if mitText else ""}'
            lsg=F'$t=\\frac{{s}}{{v}}=\\frac{{{strNW(s)}}}{{{strNW(v,True)}}}={t}~{zeit}$'
    elif typ=='Strecke':
        if umrechnen and not (zeit=='s' and laenge=='m'):
            afg = F'{F"Berechne die Strecke in {laenge} für " if mitText else F"s=? {laenge}: "}$t={strNW(t)}~{zeit}${" und" if mitText else ","} $v={strNW(v_mps, True)}~\\frac{{m}}{{s}}${"." if mitText else ""}'
            lsg=['$\\begin{aligned}']
            umrechnenInS=F't&={t}~{zeit}={strNW(t)}\\cdot {strNW(groessen[zeit])}~s={strNW(t*groessen[zeit])}~s \\\\'
            lsg=lsg+([] if zeit=='s' else [umrechnenInS])
            lsg=lsg+[F'\\rightarrow s&=v\\cdot t= {strNW(v_mps,True)}\\cdot {strNW(t*groessen[zeit])}~s\\frac{{m}}{{s}}={strNW(s*groessen[laenge])}~m \\\\']
            op=':' if groessen[laenge]>1 else '\\cdot'
            teiler=groessen[laenge] if groessen[laenge]>1 else (1/groessen[laenge])
            lsg=lsg+([F'\\rightarrow s&=({strNW(s*groessen[laenge])}{op}{strNW(teiler)})~{laenge}={s}~{laenge}'] if not laenge=='m' else [])
            lsg = lsg + ['\\end{aligned}$']
        else:
            afg=F'{"Berechne die Strecke für " if mitText else ""}$t={t}~{zeit}${" und" if mitText else ","} $v={strNW(v,True)}~\\frac{{{laenge}}}{{{zeit}}}${"." if mitText else ""}'
            lsg=F'$s=v\\cdot t={strNW(v,True)}\\cdot{t}={strNW(s)}~{laenge}$'
    return [afg,lsg,[t,s,v,laenge,zeit]]
#aufruf=0
def erzeugeBeschlBerechnungen(typ='',mitText=True):
#Diese Funktion erstellt Aufgaben zur Berechnung der Geschwindigkeit, Zeit oder Strecke bei Gegebenen Strecken, Zeit
#oder Geschwindigkeitsangaben:
#           [afg,lsg,[t,s,v,laenge,zeit]]=erzeugeGeschwindigkeitsBerechnungen(typ='',einheit='m/s',umrechnen=False,einfach=True,mitText=True)
#Mit:
#              typ=['Geschwindigkeit','Zeit','Strecke']
#              einheit='m/s'   --> Sollen die Werte in m/s oder km/h angegeben werden.
#              umrechnen=True, False --> Wenn True, gibt es Längen auch in dm,cm,mm und Zeiten in min.
#              einfach=True, False --> Ob Kommazahlen verwendet werden sollen oder nicht.
#              mitText=True, False --> Man kann den Aufgabentext weg lassen.
    groessen,einheitenZuTimedelta,einheiten=einheitenListe()
    typen=['Beschleunigung','Geschwindigkeit','Zeit']
    if typ not in typen:
        typ=random.choice(typen)
    a=random.choice([random.randint(1,100)/1000.0,random.randint(1,100)/100.0,random.randint(1,100)/10.0])
    v=random.randint(1,40)
    t=v/a
#Berechnung der Aufgaben und Lösungen:
    if typ=='Beschleunigung':
        afg=F'{"Berechne die Beschleunigung für " if mitText else F"$a=? XXXXfrac{{m}}{{s^2}}$: "}$v={strNW(v,True)} \\frac{{m}}{{s}}${" und" if mitText else ","} $t={strNW(t, True)} s${"." if mitText else ""}'
        lsg = ['$\\begin{aligned}']
        lsg=lsg+[F'a&=\\frac{{v}}{{t}}=\\frac{{{strNW(v,True)}~\\frac{{m}}{{s}}}}{{{strNW(t, True)}~s}}={strNW(a,True)}~\\frac{{m}}{{s^2}} \\\\']
        lsg = lsg + ['\\end{aligned}$']
    elif typ=='Zeit':
        afg = F'{F"Berechne die Zeit in s für " if mitText else F"t=? s: "}$a={strNW(a,True)}~\\frac{{m}}{{s^2}}${" und" if mitText else ","} $v={strNW(v, True)}~\\frac{{m}}{{s}}${"." if mitText else ""}'
        lsg=['$\\begin{aligned}']
        lsg=lsg+[F't&=\\frac{{v}}{{a}}=\\frac{{{strNW(v,True)}~\\frac{{m}}{{s}}}}{{{strNW(a,True)} \\frac{{m}}{{s^2}}}}={strNW(t,True)}~s \\\\']
        lsg = lsg + ['\\end{aligned}$']
    elif typ=='Geschwindigkeit':
        afg=F'{"Berechne die Geschwindigkeit für " if mitText else  F"$v=? XXXXfrac{{m}}{{s}}$: "}$t={strNW(t,True)}~s${" und" if mitText else ","} $a={strNW(a,True)}~\\frac{{m}}{{s^2}}${"." if mitText else ""}'
        afg=afg.replace('XXXX','\\')
        lsg=[F'$v=a\\cdot t={strNW(a,True)}\\cdot{strNW(t,True)}={strNW(v,True)}~\\frac{{m}}{{s}}$']
    return [afg,lsg,[]]


def erzeugeDiagrammErstellAufgaben(typ='Zeit-Weg',diagrammVorgegeben=True,mitText=True,nurText=False):
    v=random.randint(1,20)
#    global  aufruf
#    v=[2,5,10,0.5][aufruf]
#    aufruf=aufruf+1
    tMax=6
    vMax=math.ceil((v*tMax)/10)*10
    if nurText:
        afg=[F'Erstelle die Tabelle und das Diagramm für die Geschwindigkeit v={v} m/s.' if mitText else F'v={v} m/s' ]
    else:
        afg=['\\pbox{14cm}{']
        afg=afg+[F'{"Übertrage die Werte" if diagrammVorgegeben else "Erstelle aus den Werten"} des Weges {"in das " if diagrammVorgegeben else "ein"} Diagramm.\\\\' if mitText else '\\phantom{e}']
    tabelle=tikzTabelle(tabelle=[['t in s','s in m']]+[[strNW(t),strNW(v*t)]for t in range(tMax+1)],dim=[1.5,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[-4.5,4.5])
    if diagrammVorgegeben:
        diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[],xAchse=[0,6,7],yAchse=[0,vMax,11],xlabel='t in s',ylabel='s in  m',urspr=[0,0],mitUmrandung=False)
    else:
        diagramm=[F'\\node at (7,11) {{ }};']
    afg=afg+ ([] if nurText else (tabelle[:-1]+diagramm+[tabelle[-1]]))
    afg=afg+ ([] if nurText else ['}'])
    tabelle=tikzTabelle(tabelle=[['t in s','s in m']]+[[t,v*t]for t in range(tMax)],dim=[1.5,0.5],spaltenBreite=[],zeilenHoehe=[],newCBuchst='A',tabellenPos=[-4.5,4.5])
    diagramm=diagrammTikzVorgBreiteHoehe(zuPlotten=[[F'{v}*x','black']],xAchse=[0,6,7],yAchse=[0,vMax,11],xlabel='t in s',ylabel='s in  m',urspr=[0,0],mitUmrandung=False)
    lsg=tabelle[:-1]+diagramm+[tabelle[-1]]
    return [afg,lsg,[v]]

def hebelAufgaben(anzSpalten=1,mitText=True):
    m1=random.choice([10,50,100,200,400,500])
    faktor=random.choice([0.2,0.5,1,2,3,4,5,6])
    m2=m1*faktor
    if m2<m1:
        if faktor==0.2:
            pos1=1
        else:
            pos1=3
    else:
        if faktor==4:
            pos1=4
        elif faktor==5:
            pos1=5
        else:
            pos1=6
    pos2=pos1/faktor
    afg=[F'\\pbox{{{15 if anzSpalten==1 else 6}cm}}{{']
    afg=afg+[F'Du hast ein Gewicht von {strNW(m2,True)} g, bringe folgenden Hebel ins Gleichgewicht:'+'\\\\']
    afg=afg+hebelTikz(pos1=-pos1,m1=m1,pos2=0,m2=m2,breite='!' if anzSpalten==1 else '6 cm')
    afg=afg+['}']
    lsg=hebelTikz(pos1=-pos1,m1=m1,pos2=pos2,m2=m2,mitResizebox=True)
    return [afg,lsg,[]]