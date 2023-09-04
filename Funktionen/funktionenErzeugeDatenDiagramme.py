#!/usr/bin/env python
# coding: utf8
#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random
#import names

def datenliste(anzahl=6):
    daten={'Lob von Lehrern am Tag':['Gut', 'Schön', 'Toll', 'andere',[120,'Lob','Lobs']]}
    daten['Autos pro Stunde gezählt'] = ['VW', 'Audi', 'Fiat', 'Mercedes', 'Honda','Dacia',[400,'Auto','Autos']]
    daten['Seitenaufrufe aus Ländern pro Minute'] = ['Amerika', 'China', 'Deutschland', 'Frankreich', 'Japan', 'Schweiz', [200,'Aufruf','Aufrufe']]
    groessen=[]
    while len(groessen)<(anzahl if anzahl < 50 else 20):
        groessen=list(set([random.randint(150,200) for i in range(anzahl)]))
    daten['Schülergrößen an der Schule'] = [F'{i} cm' for i in groessen] + [[300,'cm','cm']]
    alter=[]
    while len(alter)<(anzahl if anzahl< 100 else 40):
        alter=list(set([random.randint(0,100) for i in range(anzahl)]))
    daten['Alter von Einwohnern in einer Stadt'] = [F'{i} Jahre' for i in alter] + [[100,'Jahr','Jahre']]
    daten['Anzahl an Whatsapp pro Tag'] = ['Peter','Kevin','Erika','Thomas','Marta','Cleopatra','Zeus','Anastasia','Thor','Theresa',[150,'Nachricht','Nachrichten']]
#    daten['T-Shirt Farben gewaschen']=['Schwarz','Orange','Gelb','Blau','Grün',300]
    auswahl = random.choice(list(daten.keys()))
    eigenschaften=daten[auswahl][-1]
    werte = [daten[auswahl][0:-1]]
    werte.append([random.randint(int(daten[auswahl][-1][0]/3),daten[auswahl][-1][0]) for i in enumerate(werte[0])])
    return auswahl,werte,eigenschaften

def erzeugeDatenKennwerteBestimmen(mitText=True,RS=True):
    auswahl, werte, eigenschaften = datenliste(anzahl=random.randint(10,20))
    anzahl=len(werte[0])
    afgText=[F'Bestimme das Maximum, Minimun, die Spannweite{", den Mittelwert und die Quartilwerte" if RS else " und den Mittelwert"} folgender Daten:\\\\']
    afg = ['\\pbox{15 cm}{']
    if mitText:
        afg=afg+afgText
    afg = afg + [F'{auswahl}\\\\']
    i=0
    n=7
    while i<len(werte[0])-1:
        afg=afg+tikzTabelle(tabelle=[x[i:i+n if i+n<len(werte[0]) else len(werte[0])] for x in werte],dim=[2.0,0.5],newCBuchst=buchstabenGross[int(i/n)])
        i=i+n
    afg=afg+['}']
    lsg=['\\parbox{15 cm}{']
    lsg=lsg+[F'Thema: {auswahl} \\\\']
    lsg=lsg+['1. Sortieren: \\\\']
    werteLsg=[list(range(1,len(werte[0])+1)),list(werte[1])]
    werteLsg[1].sort()
    lsg=lsg+([F'\\resizebox{{15 cm}}{{!}}{{'] if anzahl>14 else [])
    lsg=lsg+datenQuartilAuswertung(werte=werteLsg,RS=RS)
    lsg=lsg+(['}'] if anzahl>14 else [])
    #    i=0
#    n=14
#    while i<len(werte[0]):
#        lsg=lsg+tikzTabelle(tabelle=[x[i:i+n if i+n<len(werteLsg[0]) else len(werteLsg[0])] for x in werteLsg],dim=[1.0,0.5],newCBuchst=buchstabenGross[int(i/n)])
#        i=i+n
    lsg.append('\\begin{itemize}')
    lsg.append(F'\\item Minium = {werteLsg[1][0]} {eigenschaften[2]}')
    lsg.append(F'\\item Maximun = {werteLsg[1][-1]} {eigenschaften[2]}')
    lsg.append(F'\\item Spannweite = {werteLsg[1][-1]}-{werteLsg[1][0]}={werteLsg[1][-1] -werteLsg[1][0]} {eigenschaften[2]}')
    lsg.append(F'\\item Mittelwert:')
    lsg.append(F'\\ $$\\mu = \\frac{{\\mbox{{Summe der Werte}}}} {{\\mbox{{Anzahl der Werte}}}}=\\frac{{{"+".join([strNW(x) for x in werteLsg[1][0:4]])}{"+..." if len(werteLsg[0])>4 else ""}}}{{{len(werteLsg[0])}}}=\\frac{{{sum(werteLsg[1])}}}{{{len(werteLsg[0])}}}={strNW(sum(werteLsg[1])/len(werteLsg[0]),2)}\\mbox{{ {eigenschaften[2]}}}$$')
    if RS:
        lsg.append(F'\\item Zentralwert, Median (genau der mittlere Wert): ')
        n1=int(len(werteLsg[0])/2)-1
        if len(werte[0])%2 <1:
            lsg.append(F' Zwischen {werteLsg[1][n1]} und {werteLsg[1][n1+1]}')
            lsg.append(F'$$\\rightarrow Z=\\frac{{1}}{{2}}\\cdot ({strNW(werteLsg[1][n1])}+{strNW(werteLsg[1][n1+1])})={strNW((werteLsg[1][n1]+werteLsg[1][n1+1])/2)}\\mbox{{ {eigenschaften[2]}}}$$')
        else:
            lsg.append(F'$$\\rightarrow Z={werteLsg[1][n1+1]}$$')
        lsg.append(F'\\item Untere Quartil, Hälfte der unteren Hälfte:')
        if len(werte[0])%4 <2:
            n1,n2=int(len(werteLsg[0])/4)-1,int(len(werteLsg[0])/4)
            lsg.append(F' Zwischen {werteLsg[1][n1]} und {werteLsg[1][n2]}')
            lsg.append(F'$$\\color{{blue}}\\rightarrow q_u=\\frac{{1}}{{2}}\\cdot ({strNW(werteLsg[1][n1])}+{strNW(werteLsg[1][n2])})={strNW((werteLsg[1][n1]+werteLsg[1][n2])/2)}\\mbox{{ {eigenschaften[2]}}}$$')
        else:
            lsg.append(F'$$\\color{{blue}}\\rightarrow q_u={werteLsg[1][int(len(werteLsg[0])/4)]}\\mbox{{ {eigenschaften[2]}}}$$')
        lsg.append(F'\\item Oberes Quartil, Hälfte der oberen Hälfte:')
        if len(werte[0])%4 <2:
            n1,n2=int(len(werteLsg[0])*3/4)-1,int(len(werteLsg[0])*3/4)
            lsg.append(F' Zwischen {werteLsg[1][n1]} und {werteLsg[1][n2]}')
            lsg.append(F'$$\\color{{violet}}\\rightarrow q_o=\\frac{{1}}{{2}}\\cdot ({strNW(werteLsg[1][n1])}+{strNW(werteLsg[1][n2])})={strNW((werteLsg[1][n1]+werteLsg[1][n2])/2)}\\mbox{{ {eigenschaften[2]}}}$$')
        else:
            lsg.append(F'$$\\color{{violet}}\\rightarrow q_o={werteLsg[1][int(len(werteLsg[0])*3/4)]}\\mbox{{ {eigenschaften[2]}}}$$')
    lsg.append('\\end{itemize}')
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeSaeulenStreifenKreisDiagramm(typ='ZeichnenUndBerechnen',mitText=True,streifen=False):
    #Diese Funktion erzeugt eine Tabelle,zu der SuS ein Säulen- und Kreisdiagramm erzeugen sollen.
    auswahl, werte, eigenschaften = datenliste()
    afg=[F'\\pbox{{15 cm}}{{']
    if mitText:
        if typ=='zuordnen':
            afg = afg + [F'Ordne die Daten den Diagrammen zu.\\\\']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenKreisStreifenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl,streifen=streifen)
        if typ=='ZeichnenUndEinfaerben':
            afg = afg + [F'Zeichne das Säulendiagramm und färbe das {"Streifen" if streifen else "Kreis"}diagramm korrekt ein.\\\\ ']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenKreisStreifenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl,streifen=streifen)
        if typ=='Zeichnen':
            afg = afg + [F'Zeichne das Säulen und das {"Streifen" if streifen else "Kreis"}diagramm.\\\\ ']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenKreisStreifenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl,streifen=streifen)
        if typ=='ZeichnenUndBerechnen':
            afg = afg + [F'Zeichne das Säulen und das {"Streifen" if streifen else "Kreis"}diagramm. Berechne dazu die Prozentwerte.\\\\ ']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenKreisStreifenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl,streifen=streifen)
        if typ=='alles':
            afg = afg+ [F'Berechne die relative Häufigkeiten (Prozentwerte) folgender Daten und zeichne die absoluten Werte in ein Säulen und die relativen Werte in ein {"Streifen" if streifen else "Kreis"}diagramm.\\\\']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenKreisStreifenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl,streifen=streifen)
    afg=afg+['}']
    lsg=saeulenKreisStreifenDiagrammeZeichnen(werte=werte,typ='LSG',titel=auswahl,streifen=streifen)
    return [afg,lsg,[]]