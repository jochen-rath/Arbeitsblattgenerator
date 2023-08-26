#!/usr/bin/env python
# coding: utf8
#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random


def datenliste():
    daten={'Lob von Lehrern am Tag':['Gut', 'Schön', 'Toll', 'andere',120]}
    daten['Autos pro Stunde gezählt'] = ['VW', 'Audi', 'Fiat', 'Mercedes', 'Honda','Dacia',400]
#    daten['T-Shirt Farben gewaschen']=['Schwarz','Orange','Gelb','Blau','Grün',300]
    return daten

def erzeugeSaeulenKreisDiagramm(typ='ZeichnenUndBerechnen',mitText=True):
    #Diese Funktion erzeugt eine Tabelle,zu der SuS ein Säulen- und Kreisdiagramm erzeugen sollen.
    auswahl=random.choice(list(datenliste().keys()))
    werte=[datenliste()[auswahl][0:-1]]
    werte.append([random.randint(int(datenliste()[auswahl][-1]/3),datenliste()[auswahl][-1]) for i in enumerate(werte[0])])
    afg=[F'\\pbox{{15 cm}}{{']
    if mitText:
        if typ=='zuordnen':
            afg = afg + [F'Ordne die Daten den Diagrammen zu.\\\\']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl)
        if typ=='ZeichnenUndEinfaerben':
            afg = afg + [F'Zeichne das Säulendiagramm und färbe das Kreisdiagramm korrekt ein.\\\\ ']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl)
        if typ=='Zeichnen':
            afg = afg + [F'Zeichne das Säulen und das Kreisdiagramm.\\\\ ']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl)
        if typ=='ZeichnenUndBerechnen':
            afg = afg + [F'Zeichne das Säulen und das Kreisdiagramm. Berechne dazu die Prozentwerte.\\\\ ']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl)
        if typ=='alles':
            afg = afg+ [F'Berechne die relative Häufigkeiten (Prozentwerte) folgender Daten und zeichne die absoluten Werte in ein Säulen und die relativen Werte in ein Kreisdiagramm.\\\\']
            afg = afg + [F'Inhalt der Daten: {auswahl}\\\\']
            afg = afg + saeulenDiagrammeZeichnen(werte=werte,typ=typ,titel=auswahl)
    afg=afg+['}']
    lsg=saeulenDiagrammeZeichnen(werte=werte,typ='LSG',titel=auswahl)
    return [afg,lsg,[]]