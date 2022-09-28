#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeProzentRechnungen(E='',kapital=False):
#Diese Funktion erzeugt eine Aufgabe zur Prozentrechnung:
#Aufruf:
#         rechnung=erzeugeProzentRechnungen()
#
#      rechnung=[G,W,pP,Einheit]
    einheiten=['\euro{}','km','m','g','l','kg','cm','Schüler','Schülerinnen','Mädchen','Jungs','Autos','LKW','Bleistifte','Buntstifte','Knöpfe','Tickets']
    E=E if len(E)>0 else random.choice(einheiten)
    G=1.1
    while G-int(G)>0:
        pP=random.randint(1,99)+ (random.randint(1,10)/10 if random.randint(1,10)<5 else 0.0)
        if kapital:
            pP=random.randint(1,20)+ (random.randint(1,10)/10 if random.randint(1,10)<5 else 0.0)
        W=random.randint(1,300) if random.randint(1,10)<3 else random.randint(1,100)
        if kapital:
            W=random.randint(20,300)
        G=W*100/pP
    return [int(G),W,pP,E]


def erzeugeProzentwertAufgaben(n=12,lsgMitDreisatz=True,bez=['Grundwert','Prozentsatz'],einheit=''):
#Aufruf 
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    benennung=['G','W','p'] if ('Grundwert' in bez) or ('Prozentsatz' in bez) else ['K','Z','p']
    for i in range(n):
        r=erzeugeProzentRechnungen(E=einheit,kapital=True if 'K' in benennung else False)
        rechnungen.append(bez[0]+'~'+strNW(r[0])+'~'+r[3]+';  '+bez[1]+'~'+strNW(r[2])+'~\%')
        lsgen=ausgabeProzentwertBerechnenFuerTabelle(inhalte=[['',r[0],r[2],r[3]]],mitDreisatz=lsgMitDreisatz,bez=benennung)
    return [rechnungen,lsgen,dezi]

def erzeugeProzentsatzAufgaben(n=12,lsgMitDreisatz=True,bez=['Grundwert','Prozentwert'],einheit=''):
#Aufruf 
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    benennung=['G','W','p'] if ('Grundwert' in bez) or ('Prozentsatz' in bez) else ['K','Z','p']
    for i in range(n):
        r=erzeugeProzentRechnungen(E=einheit,kapital=True if 'K' in benennung else False)
        rechnungen.append(bez[0]+'~'+strNW(r[0])+'~'+r[3]+';  '+bez[1]+'~'+strNW(r[1])+'~'+r[3])
        lsgen=ausgabeProzentsatzBerechnenFuerTabelle(inhalte=[['',r[0],r[1],r[3]]],mitDreisatz=lsgMitDreisatz,bez=benennung)
    return [rechnungen,lsgen,dezi]

def erzeugeGrundwertAufgaben(n=12,lsgMitDreisatz=True,bez=['Prozentwert','Prozentsatz'],einheit=''):
#Aufruf 
#     ausgabe=erzeugeProzentsatzAufgaben(Anzahl)
#
#ausgabe=[rechnungen,lsgen]
    rechnungen=[]
    dezi=[]
    benennung=['G','W','p'] if ('Grundwert' in bez) or ('Prozentsatz' in bez) else ['K','Z','p']
    for i in range(n):
        r=erzeugeProzentRechnungen(E=einheit,kapital=True if 'K' in benennung else False)
        rechnungen.append(bez[0]+'~'+strNW(r[1])+'~'+r[3]+';  '+bez[1]+'~'+strNW(r[2])+'~\%')
        lsgen=ausgabeGrundwertBerechnenFuerTabelle(inhalte=[['',r[1],r[2],r[3]]],mitDreisatz=lsgMitDreisatz,bez=benennung)
    return [rechnungen,lsgen,dezi]

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
    afg=['Berechne den '+art+' für '+strNW(zeit)+' '+zeitEinheit+' und K='+str(K)+'\\euro{} bei $p~\\%='+strNW(pP)+'~\\%$.']
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