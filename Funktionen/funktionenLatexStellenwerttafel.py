#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, die zur Erstellung einer Latex tex-Datei benötigt werden.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


buchstaben="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()+"a b c d e f g h i j k l m n o p q e s t u v w x y z".split()

def erzeugeDeziStellenwerttabelle(zahlenliste,mitUmrandung=True):
#Diese Funtion erzeugt eine Latex Tabelle für Stellenwerttabellen.
#Beispiel: zahlenliste=[2.56,3.45,76.543,...]
    lenVorKomma=2
    lenNachKomma=3
    tabelle=[]
    if mitUmrandung:
        tabelle=tabelle+erzeugeStellenwertTabellenKopf()
    for zahl in zahlenliste:
        zerlegt=strNW(zahl).split(',')
        tabelle.append('&'.join([' ']*(lenVorKomma-len(zerlegt[0]))+list(zerlegt[0])+list(zerlegt[1])+[' ']*(lenNachKomma-len(zerlegt[1])))+'& &'+strNW(zahl)+'\\\\\\hline')
    if mitUmrandung:
        tabelle=tabelle+erzeugeStellenwertTabellenAbscluss()
    return tabelle

def erzeugeDeziStellenwerttabelleMehrereAufgaben(aufgabenliste):
#Diese Funtion erzeugt eine Latex Tabelle für Stellenwerttabellen die aus mehreren Aufgaben zusammengesetzt wird.
#Beispiel: zahlenliste=[['Aufgabe 1',33.0,54,23.495],['Aufgabe2',34.76,0.23],...]
    tabelle=erzeugeStellenwertTabellenKopf(eineAufgabe=False)
    for aufgabe in aufgabenliste:
        aufg=aufgabe[0]
        tab2=erzeugeDeziStellenwerttabelle(aufgabe[1:],mitUmrandung=False)
        tab2[0]=aufg+'&'+tab2[0].replace('hline','cline{2-8}')
        tab2[1:-1]=['&'+x.replace('hline','cline{2-8}') for x in tab2[1:-1]]
        tab2[-1]='&'+tab2[-1].replace('hline','Xhline{2\\arrayrulewidth}')
        tabelle=tabelle+tab2
    tabelle=tabelle+erzeugeStellenwertTabellenAbscluss()
    return tabelle

def erzeugeStellenwertTabellenKopf(eineAufgabe=True):
    kopf=[]
    kopf.append('\\centerline{')
    kopf.append('\\begin{tabular}{'+('' if eineAufgabe else '|l') +'|c|c?c|c|c|c|r|} ')
    kopf.append('\\hline')
    kopf.append(('' if eineAufgabe else '&') +'Z & H & z & h & t & & Dezimalzahl\\\\\\hline')
    kopf.append(('' if eineAufgabe else '&') +' 10 & 1 & $\\frac{1}{10}$ & $\\frac{1}{100}$ & $\\frac{1}{100}$ &\\phantom{M)}&  \\\\\\Xhline{2\\arrayrulewidth}')
    return kopf

def erzeugeStellenwertTabellenAbscluss():
    abschluss=[]
    abschluss.append('\\end{tabular}')
    abschluss.append('}')
    return abschluss