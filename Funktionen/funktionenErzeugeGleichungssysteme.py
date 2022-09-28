#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeGleichungmitZweiVariablen(variabel='x y',mitKlammer=False):
#Aufruf
#           [afg,lsg,G]=erzeugeGleichungmitZweiVariablen(variabel)
#
#   variabel= Variabel der Gleichung, x oder y oder a usw.
    G=''
    while not ((variabel.split(' ')[0] in G) and  (variabel.split(' ')[1] in G)):
        term1=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=12,mitKlammer=False)
        term2=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=12,mitKlammer=False)
        G=term1+'='+term2
    afg=['Gib 3 Lösungen folgender Gleichung an:']+['$$'+G.replace('**','^').replace('*','\\cdot ')+'$$']
    lsg=loeseGleichungEinfachMitZweiVariabeln(G=G,variable=variabel)
    return [afg,lsg,G]

def erzeugeGleichungmitZweiVariablenZeichnen(variabel='x y',mitKlammer=False):
#Diese Funktion erzeugt eine Gleichung mit zwei Varibablen ohne Potenz.
#
#Aufruf
#           [afg,lsg,G]=erzeugeGleichungmitZweiVariablen(variabel)
#
#   variabel= Variabel der Gleichung, x oder y oder a usw.
    lsg='Error'
    while 'Error' in lsg:
        G=''
        while not ((variabel.split(' ')[0] in G) and  (variabel.split(' ')[1] in G)):
            term1=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=12,mitKlammer=False)
            term2=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=12,mitKlammer=False)
            G=term1+'='+term2
        afg=['Bestimme 2 Punkte und zeichne durch diese die Lösunggerade der Gleichung:']+['$$'+G.replace('**','^').replace('*','\\cdot ')+'$$']+['Überprüfe die Gerade mit einem drittem Punkt']
        lsg=zeichneGleichungEinfachMitZweiVariabeln(G=G,variable=variabel)
    return [afg,lsg,G]


def erzeugeZweiGleichungmitZweiVariablen(variabel='x y',mitKlammer=False,zeichnerisch=True):
#Diese Funktion erzeugt zwei Gleichungen mit zwei Variablen
#
#Aufruf
#           [afg,lsg,G]=erzeugeGleichungmitZweiVariablen(variabel)
#
#   variabel= Variabel der Gleichung, x oder y oder a usw.
    lsg='Error'
    while 'Error' in lsg:
        G1=''
        while not ((variabel.split(' ')[0] in G1) and  (variabel.split(' ')[1] in G1)):
            term1=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=4,mitKlammer=False)
            term2=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=4,mitKlammer=False)
            G1=term1+'='+term2
        G2=''
        while not ((variabel.split(' ')[0] in G2) and  (variabel.split(' ')[1] in G2)):
            term1=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=4,mitKlammer=False)
            term2=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=4,mitKlammer=False)
            G2=term1+'='+term2
        afg=['Bestimme den Schnittpunkt der beiden Gleichungen'] if zeichnerisch else ['Löse die beiden Gleichungen durch Gleichsetzen']
        afg=afg+['$$'+G1.replace('**','^').replace('*','\\cdot ')+'$$']
        afg=afg+['$$'+G2.replace('**','^').replace('*','\\cdot ')+'$$']
        lsg=loeseZweiGleichungenMitZweiVariablen(G=[G1,G2],variable=variabel,zeichnerisch=zeichnerisch)
    return [afg,lsg,[G1,G2]]