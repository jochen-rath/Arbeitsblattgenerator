#!/usr/bin/env python
# coding: utf8

#Inhalt
#Diese Skript erzeugt skripte, aus denen das LaTeX Paket Tikz Zahlenstrahle erzeugen kann.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeWurzelRechnungen(typ=''):
#Diese Funktion erzeugt eine Aufgaben, zum Lösen von Wurzelrechnungen
    typen=['Einfach','Bruch Einzeln','Bruch','Dezimalwurzel Einfach','Dezimalwurzel']
    if typ not in typen:
        typ=random.choice(typen)
    quadratwurzel=random.randint(2,20)
    if typ=='Einfach':
        afg='$\\sqrt{'+strNW(quadratwurzel**2)+'}=$'
        lsg='$\\sqrt{'+strNW(quadratwurzel**2)+'}='+strNW(quadratwurzel)+'$'
        return [afg,lsg,quadratwurzel]
    if typ=='Bruch Einzeln':
        afg='$\\sqrt{\\frac{1}{'+strNW(quadratwurzel**2)+'}}=$'
        lsg='$\\sqrt{\\frac{1}{'+strNW(quadratwurzel**2)+'}}=\\frac{1}{'+strNW(quadratwurzel)+'}$'
        return [afg,lsg,quadratwurzel]
    if typ=='Bruch':
        zaehlerwurzel=random.randint(2,12)
        afg='$\\sqrt{\\frac{'+strNW(zaehlerwurzel**2)+'}{'+strNW(quadratwurzel**2)+'}}=$'
        lsg='$\\sqrt{\\frac{'+strNW(zaehlerwurzel**2)+'}{'+strNW(quadratwurzel**2)+'}}=\\frac{'+strNW(zaehlerwurzel)+'}{'+strNW(quadratwurzel)+'}$'
        return [afg,lsg,quadratwurzel]
    if typ=='Dezimalwurzel Einfach':
        quadratwurzel=quadratwurzel*(random.choice([1e-1,1e-2,1e-3,1e-4]))
        afg='$\\sqrt{'+strNW(quadratwurzel**2)+'}=$'
        lsg='$\\sqrt{'+strNW(quadratwurzel**2)+'}='+strNW(quadratwurzel)+'$'
        return [afg,lsg,quadratwurzel]
    if typ=='Dezimalwurzel':
        quadratwurzel=random.randint(2,40)*(random.choice([1e-1,1e-2,1e-3,1e-4]))
        afg='$\\sqrt{'+strNW(quadratwurzel**2)+'}=$'
        lsg='$\\sqrt{'+strNW(quadratwurzel**2)+'}='+strNW(quadratwurzel)+'$'
        return [afg,lsg,quadratwurzel]


def erzeugeWurzelUmfangsberechnungVomQuadrat():
#Diese Funktion erzeugt eine Aufgaben, zum Berechnen der Umfangs eines Quadrates, bei
#einem vorgegebenen Flächeninhalt.
    quadratwurzel=random.randint(20,50)/10.0
    afg=['Berechne den Umfang des Quadrates:']
    a=quadratwurzel
    afg=afg+rechteckTikz(a,a,beschrSeiten=False,beschrPunkte=False,textMitte='$A='+strNW(quadratwurzel**2)+'cm^2$')
    lsg=['\\pbox{6cm}{']+['$A='+strNW(quadratwurzel**2)+'cm^2$']+['\\\\']
    lsg=lsg+['$a=\\sqrt{A}=\\sqrt{'+strNW(quadratwurzel**2)+'cm^2}='+strNW(quadratwurzel)+'$']+['\\\\']
    lsg=lsg+['$U=4\\cdot a=4 \\cdot'+strNW(quadratwurzel)+'='+strNW(4*quadratwurzel)+'cm$']+['\\\\']
    lsg=lsg+['}']
    return [afg,lsg,quadratwurzel]


def wurzelOberflaecheWurfel(zusammengesetzt=False):
#Diese Funktion erzeugt eine Aufgaben, zum Berechnen der Kantenlänge eines Quaders, bei
#einer vorgegebenen Oberfläche
    zusammengesetzt=1 if not zusammengesetzt else random.randint(2,4)
    a=random.randint(20,50)/10.0
    if zusammengesetzt>1:
        a=random.randint(int(50 / zusammengesetzt),int(100 / zusammengesetzt))/10.0 / zusammengesetzt
    afg=['\\pbox{6cm}{']+['Berechne die Kantenlänge der zusammmengesetzen Würfel: \\\\']
    afg=afg if zusammengesetzt> 1 else (['\\pbox{6cm}{']+['Berechne die Kantenlänge des Würfels: \\\\'])
    multi=6*zusammengesetzt-(zusammengesetzt-1)*2
    O=multi*a**2
    afg=afg+quader(a,a,a,mitBeschriftung=False,textOben='$O='+strNW(O)+'cm^2$')
    for i in range(zusammengesetzt-1):
        afg=afg[:-1]+quader(a,a,a,ursprung=[(i+1)*a,0],mitBeschriftung=False,mitTikzUmrandung=False)+[afg[-1]]
    afg=afg+['}']
    lsg=['\\pbox{6cm}{']+['$O='+strNW(O)+'cm^2$']+['\\\\']
    lsg=lsg+['$O='+strNW(multi)+'\\cdot A \\rightarrow A=O:'+strNW(multi)+'$']+['\\\\']
    lsg=lsg+['$a=\\sqrt{A}=\\sqrt{'+strNW(O)+':'+strNW(multi)+' cm^2}$']+['\\\\']
    lsg=lsg+['$a=\\sqrt{'+strNW(O/multi)+'cm^2}='+strNW(a)+'$']+['\\\\']
    lsg=lsg+['}']
    return [afg,lsg,a]


def zwischenWelcheNatZahlen(mitText=True):
    quadratzahlen=np.array([x**2 for x in range(50)])
    zahl=random.choice([random.randint(1,100)]*4+[random.randint(100,400)]*3+[random.randint(400,700)])
    afg='Zwischen welchen natürlichen Zahlen liegt die Quadratwurzel von $\\sqrt{'+strNW(zahl)+'}$?'
    afg=afg if mitText else '$\\sqrt{'+strNW(zahl)+'}$'
    lsg='$'+strNW(int(zahl**0.5))+' < \\sqrt{'+str(zahl)+'} < '+strNW(int(zahl**0.5)+1)+'$'
    lsg=('$\\sqrt{'+strNW(zahl)+'}='+strNW(zahl**0.5)+'$') if zahl in quadratzahlen else lsg
    return [afg,lsg,zahl]

def teilweiseWurzelziehen(mitText=True,einfach=True):
    qua=[]
    quadratzahlen=np.array([x**2 for x in range(50)])
    while len(qua)==0:
        radikand=random.choice([random.randint(1,100)]*3+[random.randint(100,400)]*2+[random.randint(400,1000)])
        radikand= random.randint(2,4)**2*random.randint(1,3)**2*random.randint(1,7) if einfach else radikand
        if mitText:
            afg=['\\pbox{6cm}{']+['Zerlege den Radikand in eine Quadratzahl und einem Rest. Ziehe dann die Wurzel: \\\\']
            afg=afg +['$\\sqrt{'+strNW(radikand)+'}$']+['}']
        else:
            afg='$\\sqrt{'+strNW(radikand)+'}$'
        if radikand in quadratzahlen:
            qua=[0]
            lsg='$\\sqrt{'+strNW(radikand)+'}='+strNW(radikand**0.5)+'$'
        else:
            rest=radikand
            primzer=prim(radikand)
            qua=[]
            for p in list(set([x for x in primzer if primzer.count(x)>1])):
                potenz=primzer.count(p) if primzer.count(p)%2==0 else (primzer.count(p)-1)
                qua.append(p**potenz)
                rest=rest/qua[-1]
            quaStr=[strNW(x) for x in qua]
            quaSqrStr=['\\sqrt{'+strNW(x)+'}' for x in qua]
            sqrtStr=[strNW(x**0.5) for x in qua]
            lsg='$\\sqrt{'+strNW(radikand)+'}=\\sqrt{'+'\\cdot'.join(quaStr)+'\\cdot'+strNW(rest)+'}'
            lsg=lsg+'='+'\\cdot'.join(quaSqrStr)+'\\cdot\\sqrt{'+strNW(rest)+'}='+'\\cdot'.join(sqrtStr)+'\\cdot\\sqrt{'+strNW(rest)+'}'
            lsg=lsg+(('='+strNW((radikand/rest)**0.5)+'\\cdot\\sqrt{'+strNW(rest)+'}') if len(qua)>1 else '')+'$'
    return [afg,lsg,radikand]

def wurzelnZusammenZiehen():
    quadratzahlen=np.array([x**2 for x in range(20)])
    radikand=random.choice(quadratzahlen[3:])
    primzer=prim(radikand)
    anzfakt=random.randint(2,4)
    faktoren=[]
    n=anzfakt if anzfakt < len(primzer) else len(primzer)
    for i in range(n-1):
        faktoren.append(primzer[i])
    faktoren.append(math.prod(primzer[i+1:]))
    afg='$'+'\\cdot'.join(['\\sqrt{'+strNW(x)+'}' for x in faktoren])+'=$'
    lsg=afg[:-1]+'\\sqrt{'+'\\cdot'.join([strNW(x) for x in faktoren])+'}=\\sqrt{'+strNW(radikand)+'}='+strNW(radikand**0.5)+'$'
    return [afg,lsg,radikand]

def wurzelnAddieren(anzahl=2,mitText=True):
    quadratzahlen=np.array([x**2 for x in range(20)])
    radikant=[]
    for i in range(anzahl):
        r=random.randint(2,20)
        while r in quadratzahlen or r in radikant:
            r=random.randint(2,20)
        radikant.append([r,buchstabenKlein[i]])
    anzSummanden=[random.randint(2,4) for i in range(anzahl)]
    rechnung=[random.choice(['+','-'])+str(random.randint(1,10))+'*'+radikant[i][1] for j in range(anzSummanden[i]) for i in range(anzahl)]
    random.shuffle(rechnung)
    rechnung=''.join(rechnung)
    rechnung=rechnung.replace('1*','')
    rechnung= rechnung[1:] if rechnung[0]=='+' else rechnung
    rechnungAfg=rechnung
    lsg=str(sympy.simplify(rechnung))
    for i in range(anzahl):
        rechnungAfg=rechnungAfg.replace(radikant[i][1],'\\sqrt{'+strNW(radikant[i][0])+'}')
        lsg=lsg.replace(radikant[i][1],'\\sqrt{'+strNW(radikant[i][0])+'}')
    afg=('Fasse zusammen: $' if mitText else '$') +rechnungAfg.replace('*','')+'=$'
    lsg='$'+rechnungAfg.replace('*','')+'='+lsg.replace('*','')+'$'
    return [afg,lsg,rechnung]



