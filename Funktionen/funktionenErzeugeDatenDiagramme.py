#!/usr/bin/env python
# coding: utf8
#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random


def datenliste():
    daten={'Lob von Lehrern am Tag':['Gut', 'Schön', 'Toll', 'andere',120]}
    daten['Autos pro Stunde gezählt'] = ['VW', 'Audi', 'Fiat', 'Mercedes', 'Honda','Dacia',400]
    daten['Seitenaufrufe aus Ländern pro Minute'] = ['Amerika', 'China', 'Deutschland', 'Frankreich', 'Japan', 'Schweiz', 200]
    daten['Schülergrößen an der Schule'] = [F'{random.randint(150,190)} cm' for i in range(6)] + [300]
    daten['Alter von Einwohnern in einer Stadt'] = [F'{random.randint(0, 100)} Jahre' for i in range(6)] + [200]
#    daten['T-Shirt Farben gewaschen']=['Schwarz','Orange','Gelb','Blau','Grün',300]
    return daten

def erzeugeSaeulenStreifenKreisDiagramm(typ='ZeichnenUndBerechnen',mitText=True,streifen=False):
    #Diese Funktion erzeugt eine Tabelle,zu der SuS ein Säulen- und Kreisdiagramm erzeugen sollen.
    auswahl=random.choice(list(datenliste().keys()))
    werte=[datenliste()[auswahl][0:-1]]
    werte.append([random.randint(int(datenliste()[auswahl][-1]/3),datenliste()[auswahl][-1]) for i in enumerate(werte[0])])
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