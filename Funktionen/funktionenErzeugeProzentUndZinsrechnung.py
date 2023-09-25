#!/usr/bin/env python
# coding: utf8
import random


#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
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

def erkenneProzentKreis(mitText=True,bruch=False):
    teile=random.choice([2,3,4,5,8,10,20,25])
    anzahl=random.randint(0,teile)
    if mitText:
        afg=[F'\\pbox{{5cm}}{{{"Wieviel Prozent sind schraffiert?" if not bruch else "Gib den Bruch an:"} \\\\']
        afg=afg+kreisTeilsGefuelt(teile=teile,anzahl=anzahl,mitSchraffur=True)
        afg=afg+['}']
    else:
        afg=kreisTeilsGefuelt(teile=teile, anzahl=anzahl, mitSchraffur=True)
    lsg=F'$$\\frac{{{anzahl}}}{{{teile}}}{"$$" if bruch else F"={strNW(anzahl/teile,True)}={strNW(anzahl/teile*100,True)}§§%$$"}'.replace('§§','\\')
    return [afg,lsg,[teile,anzahl]]
def erzeugeProzentRechnungen(E='',kapital=False,HS=False,G=False):
#Diese Funktion erzeugt eine Aufgabe zur Prozentrechnung:
#Aufruf:
#         rechnung=erzeugeProzentRechnungen()
#
#      rechnung=[G,W,pP,Einheit]
    einheiten=['\euro{}','km','m','g','l','kg','cm','Schüler','Schülerinnen','Mädchen','Jungs','Autos','LKW','Bleistifte','Buntstifte','Knöpfe','Tickets']
    E=E if len(E)>0 else random.choice(einheiten)
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
                pP=random.randint(1,20)+ (random.randint(1,10)/10 if random.randint(1,10)<5 else 0.0)
            W=random.randint(1,300) if random.randint(1,10)<3 else random.randint(1,100)
            if kapital:
                W=random.randint(20,300)
            G=W*100/pP
    return [int(G),W,pP,E]

def erzeugeProzentwertAufgaben(n=12,lsgMitDreisatz=True,bez=['Grundwert','Prozentsatz'],einheit='',HS=False):
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


def zufaelligeProzentaufgabe(HS=False):
    aufgaben=[F'erzeugeProzentwertAufgaben(n=1,HS={HS})',F'erzeugeProzentsatzAufgaben(n=1,HS={HS})',F'erzeugeGrundwertAufgaben(n=1,HS={HS})']
    return eval(random.choice(aufgaben))


def erzeugeVerminderteGrundwertAufgaben(n=12,lsgMitDreisatz=True):
#Aufruf 
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    for i in range(n):
        r=erzeugeProzentRechnungen(E='\euro{}')
        rechnungen.append('Grundwert~'+strNW(r[0])+'~'+r[3]+';  Verminderung~um~'+strNW(r[2])+'~\\%')
        if lsgMitDreisatz:
            lsgen=ausgabeVerminderteGrundwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=lsgMitDreisatz)
        else:
            lsgen=ausgabeVerminderteGrundwertAusgebenMitQ(inhalte=[['',r[0],r[2],r[3]]])
    return [rechnungen,lsgen,dezi]

def erzeugeTagesMonatsZinsberechnung(art='',gesucht=''):
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
    lsg=tagesMonatsZinsenBerechnen(inhalt=[K,pP,zeit],art=art)
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

def erzeugeVermehrterGrundwertAufgaben(n=12,lsgMitDreisatz=True):
#Aufruf 
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    for i in range(n):
        r=erzeugeProzentRechnungen(E='\euro{}')
        rechnungen.append('Grundwert~'+strNW(r[0])+'~'+r[3]+';  Vermehrung~um~'+strNW(r[2])+'~\\%')
        if lsgMitDreisatz:
            lsgen=ausgabeVermehrterGrundwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=lsgMitDreisatz)
        else:
            lsgen=ausgabeVermehrterGrundwertAusgebenMitQ(inhalte=[['',r[0],r[2],r[3]]])
    return [rechnungen,lsgen,dezi]