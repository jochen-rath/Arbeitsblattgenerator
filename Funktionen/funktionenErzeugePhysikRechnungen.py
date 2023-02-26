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


def listeDerAtome():
    kuerzel=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Uub','Uut','Uuq','Uup','Uuh','Uus','Uuo']
    namen=['Wasserstoff','Helium','Lithium','Beryllium','Bor','Kohlenstoff','Stickstoff','Sauerstoff','Fluor','Neon','Natrium','Magnesium','Aluminium','Silicium','Phosphor','Schwefel','Chlor','Argon','Kalium','Calcium','Scandium','Titan','Vanadium','Chrom','Mangan','Eisen','Cobalt','Nickel','Kupfer','Zink','Gallium','Germanium','Arsen','Selen','Brom','Krypton','Rubidium','Strontium','Yttrium','Zirconium','Niob','Molybdän','Technetium','Ruthenium','Rhodium','Palladium','Silber','Cadmium','Indium','Zinn','Antimon','Tellur','Iod','Xenon','Cäsium','Barium','Lanthan','Cer','Praseodym','Neodym','Promethium','Samarium','Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium','Lutetium','Hafnium','Tantal','Wolfram','Rhenium','Osmium','Iridium','Platin','Gold','Quecksilber','Thallium','Blei','Bismut','Polonium','Astat','Radon','Francium','Radium','Actinium','Thorium','Protactinium','Uran','Neptunium','Plutonium','Americium','Curium','Berkelium','Californium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium','Rutherfordium','Dubnium','Seaborgium','Bohrium','Hassium','Meitnerium','Darmstadtium','Roentgenium','Ununbium','Ununtrium','Ununquadium','Ununpentium','Ununhexium','Ununseptium','Ununoctium']
    atommassen=[1.01,4.00,6.94,9.01,10.81,12.01,14.01,16.00,19.00,20.18,22.99,24.31,26.98,28.09,30.97,32.07,35.45,39.95,39.10,40.08,44.96,47.87,50.94,52.00,54.94,55.85,58.93,58.69,63.55,65.41,69.72,72.64,74.92,78.96,79.90,83.80,85.47,87.62,88.91,91.22,92.91,95.94,98,101.07,102.91,106.42,107.87,112.41,114.82,118.71,121.76,127.60,126.90,131.29,132.91,137.33,138.91,140.12,140.91,144.24,145,150.36,151.96,157.25,158.93,162.50,164.93,167.26,168.93,173.04,174.97,178.49,180.95,183.84,186.21,190.23,192.22,195.08,196.97,200.59,204.38,207.21,208.98,209,210,222,223,226,227,232.04,231.04,238.03,237,244,243,247,247,251,252,257,258,259,262,267,268,271,272,270,276,281,280,285,284,289,288,293, 294,294]
    anzahlElektroneProSchale=[[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,16],[0,2,8,8,32],[0,2,8,8,32],[0,2,8,9,32],[0,2,8,10,32],[0,2,8,11,32],[0,2,8,12,32],[0,2,8,13,32],[0,2,8,14,32],[0,2,8,15,32],[0,2,8,16,32],[0,2,8,17,32],[0,2,8,18,32],[0,2,8,18,32],[0,2,8,18,32],[0,2,8,18,32],[0,2,8,18,32],[0,2,8,18,32],[0,2,8,18,32],[0,2,8,18,8,50],[0,2,8,18,8,50],[0,2,8,18,9,50],[0,2,8,18,10,50],[0,2,8,18,11,50],[0,2,8,18,12,50],[0,2,8,18,13,50],[0,2,8,18,14,50],[0,2,8,18,15,50],[0,2,8,18,16,50],[0,2,8,18,17,50],[0,2,8,18,18,50],[0,2,8,18,18,50],[0,2,8,18,18,50],[0,2,8,18,18,50],[0,2,8,18,18,50],[0,2,8,18,18,50],[0,2,8,18,18,50],[0,2,8,18,18,8,72],[0,2,8,18,18,8,72],[0,2,8,18,18,9,72],[0,2,8,18,19,9,72],[0,2,8,18,20,9,72],[0,2,8,18,21,9,72],[0,2,8,18,22,9,72],[0,2,8,18,23,9,72],[0,2,8,18,24,9,72],[0,2,8,18,25,9,72],[0,2,8,18,26,9,72],[0,2,8,18,27,9,72],[0,2,8,18,28,9,72],[0,2,8,18,29,9,72],[0,2,8,18,30,9,72],[0,2,8,18,31,9,72],[0,2,8,18,32,9,72],[0,2,8,18,32,10,72],[0,2,8,18,32,11,72],[0,2,8,18,32,12,72],[0,2,8,18,32,13,72],[0,2,8,18,32,14,72],[0,2,8,18,32,15,72],[0,2,8,18,32,16,72],[0,2,8,18,32,17,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,72],[0,2,8,18,32,18,8,98],[0,2,8,18,32,18,8,98],[0,2,8,18,32,18,9,98],[0,2,8,18,32,19,9,98],[0,2,8,18,32,20,9,98],[0,2,8,18,32,21,9,98],[0,2,8,18,32,22,9,98],[0,2,8,18,32,23,9,98],[0,2,8,18,32,24,9,98],[0,2,8,18,32,25,9,98],[0,2,8,18,32,26,9,98],[0,2,8,18,32,27,9,98],[0,2,8,18,32,28,9,98],[0,2,8,18,32,29,9,98],[0,2,8,18,32,30,9,98],[0,2,8,18,32,31,9,98],[0,2,8,18,32,32,9,98],[0,2,8,18,32,32,10,98],[0,2,8,18,32,32,11,98],[0,2,8,18,32,32,12,98],[0,2,8,18,32,32,13,98],[0,2,8,18,32,32,14,98],[0,2,8,18,32,32,15,98],[0,2,8,18,32,32,16,98],[0,2,8,18,32,32,17,98],[0,2,8,18,32,32,18,98],[0,2,8,18,32,32,18,98],[0,2,8,18,32,32,18,98],[0,2,8,18,32,32,18,98],[0,2,8,18,32,32,18,98],[0,2,8,18,32,32,18,98],[0,2,8,18,32,32,18,98]]
    atomDict={}
    for i,k in enumerate(kuerzel):
        atomDict[k]=[namen[i],i+1,atommassen[i],anzahlElektroneProSchale[i]]
    return atomDict

def erkenneDasAtom(ion=0,wenig=False,mitText=True):
    atome=listeDerAtome()
    max=12 if wenig else 19
    atom=random.choice(list(atome.keys())[1:max])
    afg=[F'\\pbox{{6cm}}{{{"Welches Atom ist" if mitText else ""}']+(['\\\\'] if mitText else [])
    afg=afg+erzeugeAtom(n=atome[atom][1],massenzahl=int(round(atome[atom][2])),anzahlElektroneProSchale=atome[atom][3],ion=ion)
    afg=afg+['}']
    lsg=[F'\\pbox{{\\textwidth}}{{Es handelt sich um {atome[atom][0]}: $_{{{atome[atom][1]}}}^{{{int(round(atome[atom][2]))}}}${atom}  {"Ion" if not ion==0 else ""}\\\\']
    lsg=lsg+erzeugeAtom(n=atome[atom][1],massenzahl=int(round(atome[atom][2])),anzahlElektroneProSchale=atome[atom][3],ion=ion,pfeile=True)+['}']
    return [afg, lsg, [atom]]

def zeichneDasAtom(mitText=True):
    atome=listeDerAtome()
    atom=random.choice(list(atome.keys())[0:13])
    afg=[F'{"Zeichne folgendes Atom: " if mitText else ""}$_{{{atome[atom][1]}}}^{{{int(round(atome[atom][2]))}}}${atom}']
    lsg=[F'\\pbox{{\\textwidth}}{{{atome[atom][0]}: \\\\']
    lsg=lsg+erzeugeAtom(n=atome[atom][1],massenzahl=int(round(atome[atom][2])))+['}']
    return [afg, lsg, [atom]]

def schreibeAlleAtomeInDateien():
    atome=listeDerAtome()
    for i,atom in enumerate(list(atome.keys())):
        tikzAtom=erzeugeAtom(atom, ion=0)
        hoehe=[x for x in tikzAtom if 'circle' in x][-1].split('circle')[-1]
        result=re.search('\((.*)\)', hoehe)
        h=eval(result.group(1))
        tikzAtom.insert(4,F'\\node at (0,{h+0.5}) {{{atome[atom][0]}: $_{{{atome[atom][1]}}}^{{{atome[atom][2]}}}${atom}}};')
        erzeugeEinfachesLatexdokument(inhalt=tikzAtom,file=F'Atom_{str(i+1).zfill(3)}_{atome[atom][0]}.tex',standalone=True)
    with zipfile.ZipFile(os.path.join('Ausgabe','alleAtome.zip'), 'w') as myzip:
        for x in [x for x in os.listdir('Ausgabe') if x.startswith('Atom_') and x.endswith('pdf')]:
            myzip.write(os.path.join('Ausgabe',x))
    for x in [x for x in os.listdir('Ausgabe') if x.startswith('Atom_')]:
        os.remove(os.path.join('Ausgabe',x))
    return 'alleAtome.zip'

def zerfallsreihen():
    reihe1=[[238,92,'U','\\alpha'],[234,90,'Th','\\beta'],[234,91,'Pa','\\beta'],[234,92,'U','\\alpha'],[230,90,'Th','\\alpha'],[226,88,'Ra','\\alpha'],[222,86,'Rn','\\alpha'],[218,84,'Po','\\alpha'],[214,82,'Pb','\\beta'],[214,83,'Bi','\\beta'],[214,84,'Po','\\alpha'],[210,82,'Pb','\\beta'],[210,83,'Bi','\\beta'],[210,84,'Po','\\alpha'],[206,82,'Pb','XX']]
    reihe2=[[237,93,'Np','\\alpha'],[233,91,'Pa','\\beta'],[233,92,'U','\\beta'],[229,90,'Th','\\alpha'],[225,88,'Ra','\\beta'],[225,89,'Ac','\\alpha'],[221,87,'Fr','\\alpha'],[217,85,'At','\\alpha'],[213,83,'Bi','\\beta'],[213,84,'Po','\\alpha'],[209,82,'Pb','\\beta'],[209,83,'Bi','\\alpha'],[205,81,'Tl','XX']]
    return random.choice([reihe1,reihe2])

def bestimmeZerfall(n=2):
    r=zerfallsreihen()
    i=random.randint(0,len(r)-n)
    r=r[i:i+n]
    rZufall=copy.deepcopy(r)
    for i in range(n-1):
        zufall=random.choice(['strahlung','gesamtesAtom','Atomname','Atomwert'])
        if zufall=='strahlung':
            rZufall[random.randint(0,len(r)-2)][-1]='?'
        atomwahl=random.randint(0,len(r)-1)
        if zufall=='gesamtesAtom':
            rZufall[atomwahl][0:3]=['?']*3
        if zufall=='Atomname':
            rZufall[atomwahl][2]='?'
        if zufall=='Atomwert':
            rZufall[atomwahl][random.randint(0,1)]='?'
    afg=zeichneZerfallsreihen(reihe=rZufall)
    lsg=zeichneZerfallsreihen(reihe=r)
    return [afg,lsg,[r]]

