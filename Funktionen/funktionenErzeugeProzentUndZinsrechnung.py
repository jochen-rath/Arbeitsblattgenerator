#!/usr/bin/env python
# coding: utf8
import random


#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#		import os
#		os.chdir(f'{os.path.expanduser("~")}/Schule/Arbeitsblattgenerator')
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeProzentzeichnen(mitVorgabe=False,mitText=True):
    laenge=random.randint(3,5 if mitVorgabe else 10)
    prozent=random.randint(1,10)*10
    if mitVorgabe:
        afg=[F'\\pbox{{5cm}}{{Schraffiere {prozent} \% von: \\\\']
        afg=afg+rechteckTeilsGefuelt(laenge,prozent,mitLsg=False)
        afg=afg+['}']
    else:
        afg=F'Zeichne ein {laenge} cm langes und {strNW(laenge/2)} cm hohes Rechtecks. Schraffiere {prozent} \% davon.'
        afg=afg if mitText else F'l={laenge} cm, h={strNW(laenge/2)} cm, p={prozent}\%'
    lsg=rechteckTeilsGefuelt(laenge,prozent,mitLsg=True)
    return [afg,lsg,[laenge,prozent]]

def erkenneProzent(mitText=True):
    laenge=random.randint(3,6)
    prozent=random.randint(1,10)*10
    if mitText:
        afg=[F'\\pbox{{5cm}}{{Wieviel Prozent sind schraffiert?\\\\']
        afg=afg+rechteckTeilsGefuelt(laenge,prozent,mitLsg=True)
        afg=afg+['}']
    else:
        afg=rechteckTeilsGefuelt(laenge, prozent, mitLsg=True)
    lsg=[F'\\pbox{{5cm}}{{']
    lsg=lsg+dreiSatz(links=[strNW(x, True) for x in [laenge*10, laenge, laenge*10*prozent/100]],
                 rechts=[strNW(x, True) for x in [100, 10, prozent]],title=['mm','\%'], operationLinks=['10',strNW(prozent/10,True)],breit=True)
    lsg=lsg+['\\newline']
    lsg=lsg+['Oder: \\newline']
    lsg=lsg+[F'Gesamtlänge: {strNW(laenge*10)}\\,mm, Länge der Schraffur: {strNW(laenge*10*prozent/100)}\\,mm. Das bedeutet: \\newline']
#    lsg=lsg+[F'{strNW(laenge)} mm sind 10 \% und ${strNW(laenge*10*prozent/100)}\\cdot{}']
    lsg=lsg+[F'$\\frac{{{strNW(laenge*10*prozent/100)}}}{{{strNW(laenge*10)}}}={strNW((laenge*10*prozent/100)/(laenge*10),True)}={prozent}\%$']
    lsg=lsg+['}']
    return [afg,lsg,[laenge,prozent]]

def erkenneProzentKreis(mitText=True,bruch=False,einfach=False):
    teile=random.choice([2,4,5,10,20]) if einfach else random.choice([2,3,4,5,8,10,20,25])
    anzahl=random.randint(0,teile)
    if mitText:
        afg=[F'\\pbox{{5cm}}{{{"Wieviel Prozent sind schraffiert?" if not bruch else "Gib den Bruch an:"} \\\\']
        afg=afg+kreisTeilsGefuelt(teile=teile,anzahl=anzahl,mitSchraffur=True)
        afg=afg+['}']
    else:
        afg=kreisTeilsGefuelt(teile=teile, anzahl=anzahl, mitSchraffur=True)
    lsg=F'$$\\frac{{{anzahl}}}{{{teile}}}{"$$" if bruch else F"={strNW(anzahl/teile,True)}={strNW(anzahl/teile*100,True)}§§%$$"}'.replace('§§','\\')
    return [afg,lsg,[teile,anzahl]]


def erzeugeProzentEinheiten():
    einheiten=['\euro{}','km','m','g','l','kg','cm','Schüler','Schülerinnen','Mädchen','Jungs','Autos','LKW','Bleistifte','Buntstifte','Knöpfe','Tickets']
    return einheiten

def erzeugeProzentRechnungen(E='',kapital=False,HS=False,G=False):
#Diese Funktion erzeugt eine Aufgabe zur Prozentrechnung:
#Aufruf:
#         rechnung=erzeugeProzentRechnungen()
#
#      rechnung=[G,W,pP,Einheit]
    einheiten=erzeugeProzentEinheiten()
    E=E if len(E)>0 else random.choice(einheiten)
    E='€' if kapital else E
    G=1.1
    if HS:
        if G:
            HS_GWerte=[20,25,50,200,400,500,1000]
            pP_Werte=[1,2,4,5,10]
            W=1.1
            while W-int(W)>0:
                G=random.choice(HS_GWerte)
                pP=random.choice(pP_Werte)
                W=pP*G/100
            W=int(W)
        else:
            HS_GWerte=[20,25,50,100,200,400,500,1000]
            pP=1.1
            while pP-int(pP)>0:
                G=random.choice(HS_GWerte)
                W=random.randint(1,G)
                pP=W*100/G
    else:
        while G-int(G)>0:
            pP=random.randint(1,99)+ (random.randint(1,10)/10 if random.randint(1,10)<5 else 0.0)
            if kapital:
                pP=random.randint(1,7)+ (random.randint(1,10)/10 if random.randint(1,10)<8 else 0.0)
            W=random.randint(1,300) if random.randint(1,10)<3 else random.randint(1,100)
            if kapital:
                W=random.randint(10,30) * 10 if random.getrandbits(1) else random.randint(10,300)
            G=W*100/pP
    return [int(G),W,pP,E]

def erzeugeProzentwertAufgabenFormel(ges='',HS=False):
    werte=erzeugeProzentRechnungen(HS=HS)
    art=werte[3]
    varis={'G':[werte[0],art],'W':[werte[1],art],'p':[werte[2],'\\%']}
    geg=list(varis.keys())
    if len(ges)<1:
        ges=random.choice(geg)
    geg.remove(ges)
    formel='W=G*p/100'
    if ges=='W':
        afg=F'{strNW(varis[geg[1]][0])} {varis[geg[1]][1]} von {strNW(varis[geg[0]][0])} {varis[geg[0]][1]}'
    if ges=='G':
        afg=F'{strNW(varis[geg[0]][0])} {varis[geg[0]][1]} sind {strNW(varis[geg[1]][0])} {varis[geg[1]][1]}'
    if ges=='p':
        afg=F'{strNW(varis[geg[1]][0])} {varis[geg[1]][1]} von {strNW(varis[geg[0]][0])} {varis[geg[0]][1]}'
    lsg=loeseFunktion(formel=formel,varis=varis,ges=ges,breite=5,kommaAusgabe=True)
    return [[ersetzePlatzhalterMitSymbolen(x) for x in [afg]],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]
def erzeugeProzentwertAufgaben(n=12,lsgMitDreisatz=False,bez=['Grundwert','Prozentsatz'],einheit='',HS=False):
#Aufruf
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    benennung=['G','W','p'] if ('Grundwert' in bez) or ('Prozentsatz' in bez) else ['K','Z','p']
    for i in range(n):
        r=erzeugeProzentRechnungen(E=einheit,kapital=True if 'K' in benennung else False,HS=HS)
        rechnungen.append(bez[0]+'~'+strNW(r[0])+'~'+r[3]+';  '+bez[1]+'~'+strNW(r[2])+'~\%')
        lsgen=ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=lsgMitDreisatz,bez=benennung)
    return [rechnungen,lsgen,dezi]

def erzeugeProzentsatzAufgaben(n=12,lsgMitDreisatz=True,bez=['Grundwert','Prozentwert'],einheit='',HS=False):
#Aufruf
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    benennung=['G','W','p'] if ('Grundwert' in bez) or ('Prozentsatz' in bez) else ['K','Z','p']
    for i in range(n):
        r=erzeugeProzentRechnungen(E=einheit,kapital=True if 'K' in benennung else False,HS=HS)
        rechnungen.append(bez[0]+'~'+strNW(r[0])+'~'+r[3]+';  '+bez[1]+'~'+strNW(r[1])+'~'+r[3])
        lsgen=ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['',r[0],r[1],r[3]]],mitDreisatz=lsgMitDreisatz,bez=benennung)
    return [rechnungen,lsgen,dezi]

def erzeugeGrundwertAufgaben(n=12,lsgMitDreisatz=True,bez=['Prozentwert','Prozentsatz'],einheit='',HS=False):
#Aufruf
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    benennung=['G','W','p'] if ('Grundwert' in bez) or ('Prozentsatz' in bez) else ['K','Z','p']
    for i in range(n):
        r=erzeugeProzentRechnungen(E=einheit,kapital=True if 'K' in benennung else False,HS=HS,G=True)
        rechnungen.append(bez[0]+'~'+strNW(r[1])+'~'+r[3]+';  '+bez[1]+'~'+strNW(r[2])+'~\%')
        lsgen=ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['',r[1],r[2],r[3]]],mitDreisatz=lsgMitDreisatz,bez=benennung)
    return [rechnungen,lsgen,dezi]

def erzeugeGemZinsrechnungenOhneTabelle():
    bez=["Kapital",'Zinsen', "Zinssatz"]
    benennung=['K','Z','p']
    afgBez=list(bez)
    r=erzeugeProzentRechnungen(E='€',kapital=True,HS=False,G=True)
    afgWerte=list(r)
    ausw=random.randint(0,2)
    del afgBez[ausw]
    del afgWerte[ausw]
    afg=F'{afgBez[0]} {strNW(afgWerte[0])} {afgWerte[-1]};  {afgBez[1]} {strNW(afgWerte[1])} {" XXX" if ausw<2 else " €"}'.replace('XXX','\%')
    if ausw==0:
        lsg=ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['',r[1],r[2],r[3]]],mitDreisatz=False,bez=benennung)
    if ausw==1:
        lsg=ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=False,bez=benennung)
    if ausw==2:
        lsg=ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['',r[0],r[1],r[3]]],mitDreisatz=False,bez=benennung)
    return [afg,lsg,[]]


def zufaelligeProzentaufgabe(HS=False):
    aufgaben=[F'erzeugeProzentwertAufgaben(n=1,HS={HS})',F'erzeugeProzentsatzAufgaben(n=1,HS={HS})',F'erzeugeGrundwertAufgaben(n=1,HS={HS})']
    return eval(random.choice(aufgaben))


def erzeugeTagesMonatsZinsberechnung(art='',gesucht='',einfach=False):
#Aufruf
#     ausgabe=erzeugeTagesMonatsZinsberechnung(art='' oder 'Tageszinsen' oder 'Monatszinsen')
#
#ausgabe=[afg,lsg,[ K,Z,pP,zeit]]
    art=art if len(art)>0 else random.choice(['Tageszinsen','Monatszinsen'])
    gesucht=gesucht if len(gesucht)>0 else random.choice(['K','p','Z'])
    K,Z,pP,E=erzeugeProzentRechnungen(E='\euro{}',kapital=True)
    zeit=random.randint(1,11) if art=='Monatszinsen' else random.randint(1,359)
    zeitEinheit=('Monate' if zeit > 1 else 'Monat') if art=='Monatszinsen' else ('Tage' if zeit > 1 else 'Tag')
    zeitAbk='m'if art=='Monatszinsen' else 'd'
    maxT=12if art=='Monatszinsen' else 360
    Z=round(Z*zeit/maxT,2)
    afg=[F'Berechne die {art} für {strNW(zeit)} {zeitEinheit} und $K={strNW(K)}~€$ bei $p~\\%={strNW(pP)}~\\%$.']
    lsg=tagesMonatsZinsenBerechnen(inhalt=[K,pP,zeit],art=art,einfach=einfach)
    if gesucht=='K':
        afg=['Berechne das eingesetze Kapitel, wenn Z='+strNW(Z)+'\\euro{}, $p~\\%='+strNW(pP)+'~\\%$ und '+zeitAbk+' = '+strNW(zeit)+' '+zeitEinheit+'.']
        lsg=tagesMonatsZinsenBerechnenKapitalGesucht(inhalt=[Z,pP,zeit],art=art)
    if gesucht=='p':
        afg=['Berechne den Zinssatz, wenn Z='+strNW(Z)+'\\euro{}, K='+strNW(K)+'\\euro{} und '+zeitAbk+' = '+strNW(zeit)+' '+zeitEinheit+'.']
        lsg=tagesMonatsZinsenBerechnenZinssatzGesucht(inhalt=[K,Z,zeit],art=art)
    return [afg,lsg,[ K,Z,pP,zeit]]


def erzeugeTagesMonatsZinsberechnungKapitalGesucht(art=''):
#Aufruf
#     ausgabe=erzeugeTagesMonatsZinsberechnungKapitalGesucht(art='' oder 'Tageszinsen' oder 'Monatszinsen')
#
#ausgabe=[afg,lsg,[ K,Z,pP,zeit]]
    K,Z,pP,E=erzeugeProzentRechnungen(E='\euro{}',kapital=True)
    art=art if len(art)>0 else random.choice(['Tageszinsen','Monatszinsen'])
    zeit=random.randint(1,11) if art=='Monatszinsen' else random.randint(1,359)
    zeitEinheit=('Monate' if zeit > 1 else 'Monat') if art=='Monatszinsen' else ('Tage' if zeit > 1 else 'Tag')
    return [afg,lsg,[ K,Z,pP,zeit]]

def einfachZinseszinsen(mitText=True,anzSpalten=2):
    K, Z, pP, E = erzeugeProzentRechnungen(E='\euro{}', kapital=True)
    jahre=random.randint(2,4)
    afg=F'Berechne das ersparte Geld nach {jahre} Jahren für K={strNW(K)} € und p\%={strNW(pP)} \%'
    afg=afg if mitText else F'Z=? nach {jahre} Jahren für K={strNW(K)} € und p\%={strNW(pP)} \%'
    Kwerte=[K*(1+pP/100)**(i) for i in range(jahre)]
    lsg=loeseZinseszinsRechnung(Kwerte=Kwerte,pP=pP,jahre=jahre,anzSpalten=anzSpalten)
    return [afg,lsg,[]]

def loeseZinseszinsRechnung(Kwerte=[1100,1110,1111],pP=2,jahre=2,anzSpalten=2):
    lsg=[F'\\pbox{{{15 if anzSpalten==1 else 5}cm}}{{']
    for i in range(jahre):
        lsg.append(F'Nach {i+1} Jahr{"" if jahre<1 else "en"}: \\\\')
        lsg.append('$\\begin{aligned}')
#        lsg.append(F'Z_{i+1}&=K_{i if i>0 else "{start}"}\\cdot p\\% \\\\')
        lsg.append(F'Z_{i+1}&=K_{i if i>0 else "{start}"}\\cdot p : 100 \\\\')
        lsg.append(F'&={strNW(Kwerte[i],True)} € \\cdot {strNW(pP)} : 100 \\\\')
        lsg.append(F'&={strNW(Kwerte[i]*pP/100,True)} €\\\\')
        lsg.append(F'K_{i+1}&=K_{i if i>0 else "{start}"}+Z \\\\')
        lsg.append(F'&={strNW(Kwerte[i],True)} €+ {strNW(Kwerte[i]*pP/100,True)} €\\\\')
        lsg.append(F'K_{i+1}&={strNW(Kwerte[i]+Kwerte[i]*pP/100,True)} €\\\\')
        lsg.insert(-1, F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
        lsg.append('\\end{aligned}$ \\\\')
    lsg.append('}')
    return lsg
def erzeugeVermehrterGrundwertAufgaben(n=12,lsgMitDreisatz=True,HS=False,euro=True):
#Aufruf
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    for i in range(n):
        r=erzeugeProzentRechnungen(E='\euro{}',HS=HS) if euro else  erzeugeProzentRechnungen(E='',HS=HS)
        rechnungen.append('Grundwert~'+strNW(r[0])+'~'+r[3]+';  Vermehrung~um~'+strNW(r[2])+'~\\%')
        if lsgMitDreisatz:
            lsgen=ausgabeVermehrterGrundwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=lsgMitDreisatz)
        else:
            lsgen=ausgabeVermehrterGrundwertAusgebenMitQ(inhalte=[['',r[0],r[2],r[3]]])
    return [rechnungen,lsgen,dezi]



def erzeugeVerminderteGrundwertAufgaben(n=12,lsgMitDreisatz=True,HS=False,euro=True):
#Aufruf
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    for i in range(n):
        r=erzeugeProzentRechnungen(E='\euro{}',HS=HS) if euro else  erzeugeProzentRechnungen(E='',HS=HS)
        rechnungen.append('Grundwert~'+strNW(r[0])+'~'+r[3]+';  Verminderung~um~'+strNW(r[2])+'~\\%')
        if lsgMitDreisatz:
            lsgen=ausgabeVerminderteGrundwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=lsgMitDreisatz)
        else:
            lsgen=ausgabeVerminderteGrundwertAusgebenMitQ(inhalte=[['',r[0],r[2],r[3]]])
    return [rechnungen,lsgen,dezi]

def erzeugeBruttoNettoLohnRechnungen(mitText=True,HS=False):
    r=erzeugeProzentRechnungen(E='\euro{}',HS=HS,G=True)
    afgText=f'Der Bruttolohn  beträgt {r[0]} €. Es werden {r[2]} \\% abgezogen. Berechne die Abzüge und den Nettolon.'
    afg=[afgText] if mitText else [f'Brutto: {r[0]} €, Abzüge: {r[2]} \\%. Gesucht: Nettolon und Abzüge.']
    lsg=ausgabeBruttoNetteLohnBerechnenFuerTabelle(afg=[r[0],r[2],'€'])
    return [afg,lsg,[]]


def erzeugeMehrwertsteuerRechnungen(mitText=True,HS=False):
    breitePbox='\\hsize'
    p=random.choice([7,19])
    n=random.randint(1,10)
    gegenstand={7:[f'{n} {x} kosten' for x in ['Stück Gurken','kg Paprika','kg Tomaten','Stück Zucchinis']],19:[f'Ein {x} kostet' for x in ['Kleid','Hose','Rock','Hemd','Spiel']]}
    if p==7:
        G=random.randint(100,1000)/100 if not HS else random.randint(1,10)
    else:
        G=random.randint(100,1000) if not HS else random.choice(list(range(100,1100,100)))
    afgText=f'{random.choice(gegenstand[p])} {strNW(G)} €. Berechne die Mehrwertsteuer und den Verkaufspreis.'
    afg=[afgText] if mitText else [f'Brutto: {G} €, p \\&: {p} \\%. Gesucht: Mehrwertsteuer und Verkaufspreis.']
    lsg=ausgabeBruttoNetteLohnBerechnenFuerTabelle(afg=[G,p,'€'],V='+')
    return [afg,lsg,[]]

def zinsrechnungen(ges='',einfach=False):
    K=random.choice([random.randint(1000,10000),random.randint(10000,30000)])
    p=random.randint(5,80)/10
    Z=K*p/100
    if einfach:
        K,Z,p,E=erzeugeProzentRechnungen(kapital=True,HS=True,G=True)
    varis=['K','Z','p']
    ges=ges if len(ges)>0 else random.choice(varis)
    geg=list(varis)
    geg.remove(ges)
    einheiten={'K':'~€','Z':'~€','p':'~\\%'}
    prozent={'K':'','Z':'','p':'~\\%'}
    aufgaben={'K':f'{strNW(p)}\\% sind {strNW(Z,2)} €'}
    aufgaben['Z']=f'{strNW(p)}\\% von {strNW(K)} €'
    aufgaben['p']=f'{strNW(Z,2)} € von {strNW(K)} €'
    aufg=aufgaben[ges]
    lsg=[]
    scope = locals()
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,0.25) {Geg.: };')
    for x in geg:
        lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-5)}) {{${x}{prozent[x]}={strNW(eval(x),2)} {einheiten[x]}$}};')
    lsg.append(F'\\node[left] at (0,{-0.25-0.5*(len(lsg)-5)}) {{Ges.: }};')
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-6)}) {{{ges}{prozent[ges]}  = ? {einheiten[ges]} }};')
    lsg.append(F'\\node[below right] at (0,{-0.25-0.5*(len(lsg)-6)}) {{')
    lsg.append('$\\begin{aligned}')
    formel='{{Z}}={{K}}\\cdot \\frac{{{{p}}}}{{100}}'
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1]}& & \\\\')
    for x in geg:
        formel = formel.replace(f'{{{x}}}',f'{{{strNW(eval(x),2)}}}')
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1]}& & \\\\')
    if not ges=='Z':
        geg.remove('Z')
        lsg.append(F'{strNW(Z,2)}&={strNW(eval(geg[0])/100)}\\cdot {strNW(ges)}&\\mid : {strNW(eval(geg[0])/100)}& \\\\')
    lsg.append(F'{ges}{prozent[ges]}&={strNW(eval(ges),2)}{einheiten[ges]}& & \\\\')
#Ergebniss doppelt unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    return [aufg,lsg,[]]


def zinseszinsrechnungen(ges=''):
    K_0=random.choice([random.randint(1000,10000),random.randint(10000,30000)])
    p=random.randint(5,80)/10
    q=1+p/100
    n=random.choice([random.randint(2,10),random.randint(10,30)])
    K_n=K_0*(1+p/100)**n
    varis=['K_0','K_n','p','n']
    ges='K_n'
    geg=list(varis)
    geg.remove(ges)
    einheiten={'K_0':'~€','K_n':'~€','q':'~','p':'~\\%','n':'~\\mbox{Jahre}'}
    prozent={'K_0':'','K_n':'','p':'~\\%','n':''}
    aufgaben={'K_0':f'{strNW(K_n,2)} € Kapital bei {strNW(K_0,2)} \\% nach {strNW(n)} Jahre'}
    aufgaben['K_n']=f'{strNW(p)}\\% von {strNW(K_0)} € für {strNW(n)} Jahre'
    aufg=aufgaben[ges]
    lsg=[]
    scope = locals()
    lsg.append('\\begingroup\\setlength{\\jot}{0.02cm}')
    lsg.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
    lsg.append('\\begin{tikzpicture}[show background grid]')
    lsg.append('\\node[left] at (0,0.25) {Geg.: };')
    for x in geg:
        lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-5)}) {{${x}{prozent[x]}={strNW(eval(x),2)} {einheiten[x]}$}};')
    lsg.append(F'\\node[left] at (0,{-0.25-0.5*(len(lsg)-5)}) {{Ges.: }};')
    lsg.append(F'\\node[right] at (0,{-0.25-0.5*(len(lsg)-6)}) {{${ges}{prozent[ges]}  = ? {einheiten[ges]} $}};')
    lsg.append(F'\\node[below right] at (0,{-0.25-0.5*(len(lsg)-6)}) {{')
    lsg.append('$\\begin{aligned}')
    geg.append('q')
    qformel='{{q}}=1+\\frac{{{{p}}}}{{100}}'
    lsg.append(F'{qformel.split("=")[0]}&={qformel.split("=")[1]}& & \\\\')
    qformel = qformel.replace('{{p}}',f'{{{strNW(p,2)}}}')
    lsg.append(F'{qformel.split("=")[0]}&={qformel.split("=")[1]}& & \\\\')
    lsg.append(F'q&={strNW(q,2)}& & \\\\')
    lsg.insert(-1,'\\makebox[0pt][l]{\\uline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}') 
    formel='{{K_n}}={{K_n}}\\cdot {{q}}^{{n}}'
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1]}& & \\\\')
    for x in geg:
        formel = formel.replace(f'{{{x}}}',f'{{{strNW(eval(x),2)}}}')
    lsg.append(F'{formel.split("=")[0]}&={formel.split("=")[1]}& & \\\\')
    if not ges=='K_n':
        geg.remove('K_n')
        lsg.append(F'{strNW(Z,2)}&={strNW(eval(geg[0])/100)}\\cdot {strNW(ges)}&\\mid : {strNW(eval(geg[0])/100)}& \\\\')
    lsg.append(F'{ges}{prozent[ges]}&={strNW(eval(ges),2)}{einheiten[ges]}& & \\\\')
#Ergebniss doppelt unterstreichen
    lsg.insert(-1,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-1].replace('&', '') + '$}}}')
    lsg.append('\\end{aligned}$};')
    lsg.append('\\end{tikzpicture}')
    lsg.append('\\endgroup')
    return [aufg,lsg,[]]

