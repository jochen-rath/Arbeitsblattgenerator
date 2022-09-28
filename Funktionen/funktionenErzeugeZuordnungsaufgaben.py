#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random

def erzeugeTabelleAusfuellen(komma=False,mitText=True):
    anzSpalten=10
    E = random.choice(einheitspaare())
    xStart=random.randint(10,1000)/100 if komma else random.randint(2,20)
    yStart=random.randint(10,1000)/100 if komma else random.randint(2,10)*xStart


def erzeugeProportionaleDreisatzRechnungen(komma=False,mitText=True):
    # Diese Funktion erzeugt eine proportionale Zuordnungsaufgaben
    # Aufruf:
    #         [afg,lsg]=erzeugeProportionaleDreisatzRechnungen(komma=False,mitText=True)
    E = random.choice(einheitspaare())
#Wenn kein Komma gerechnet werden soll,wähle nur Einheiten ohne Komma
    while (not komma) and (not (E[2][0]==int(E[2][0]))  or not (E[2][1]==int(E[2][1]))):
        E = random.choice(einheitspaare())
    grundwert=random.randint(E[2][0]*100,E[2][1]*100)/100 if komma else random.randint(E[2][0],E[2][1])
    xStart,xZiel=1,1
    while xStart==xZiel:
        xStart=random.randint(10,2000)/100 if komma else random.randint(2,20)
        xZiel=random.randint(10,2000)/100 if komma else random.randint(2,20)
    yStart=grundwert*xStart
    art=E[0].split(" ")[0]
    einh=E[0].split(" ")[1]
    if 'kg' == einh or 'g'==einh:
        afg=F'Berechne den Preis für {strNW(xZiel,True)} {einh} {art}, wenn {strNW(xStart,True)} {einh} {strNW(yStart,True)} \\euro{{}} kosten.'
        afg=afg if mitText else (F'{art}:$${strNW(xStart,True)}~{einh}\hat{{=}} {strNW(yStart,True)}~\\mbox{{\\euro{{}}}} \\rightarrow {strNW(xZiel,True)}~{einh}=\\mbox{{?}}$$')
    elif 'h'==einh:
        afg=F'Welche Streck wurde in  {strNW(xZiel,True)} {einh} zurückgelegt, wenn man in {strNW(xStart,True)} {einh} {strNW(yStart,True)} km schafft.'
        afg=afg if mitText else (F'Bewegung:$${strNW(xStart,True)}~{einh}\hat{{=}} {strNW(yStart,True)}~\\mbox{{km}} \\rightarrow {strNW(xZiel,True)}~{einh}=\\mbox{{?}}$$')
    elif 'Anzahl'==einh:
        xStart=int(xStart)
        xZiel=int(xZiel)
        afg=F'Berechne den Preis für {strNW(xZiel,True)} {art}, wenn {strNW(xStart,True)} {art} {strNW(yStart,True)} \\euro{{}} kosten.'
        afg=afg if mitText else (F'{art}:$${strNW(xStart,True)}\hat{{=}} {strNW(yStart,True)}~\\mbox{{\\euro{{}}}} \\rightarrow {strNW(xZiel,True)}=\\mbox{{?}}$$')
    else:
        afg='Noch nichts.'
    lsg=dreiSatz(links=[strNW(x,True) for x in [xStart,'1',xZiel]],rechts=[strNW(x,True) for x in [yStart,yStart/xStart,yStart/xStart*xZiel]],title=E,breit=True)
    return [afg,lsg,[xStart,xZiel,yStart]]


def einheitspaare():
#Diese Funktion gibt ein Paar der Art aus:
#        ['Tomaten in kg','Preis in €',[0.75,4]]
#       Also: [Typ,Preis, [kleinster Preis, größter Preis]
#Aufruf:
#       paare=einheitspaare()
    preisKg=[['Tomaten',[0.75,4]],['Kartoffeln',[1,4]],['Hackfleisch',[10,20]],['Gummibärchen',[3,8]],['Lakritze',[4,14]]]
    paare=[[F'{art[0]} kg','Preis \\euro{}',art[1]] for art in preisKg]
    paare.append(['Zeit h','Strecke km',[2,200]])
    paare.append(['Eier Anzahl','Preis \\euro{}',[0.25,0.5]])
    return paare

def erzeugeAntiProportionaleDreisatzRechnungen(komma=False,mitText=True):
    # Diese Funktion erzeugt eine Aufgabe zur Prozentrechnung:
    # Aufruf:
    #         rechnung=erzeugeProzentRechnungen()
    #
    #      rechnung=[G,W,pP,Einheit]
    E = ['Anzahl Arbeiter','Arbeitsstunden h',[10,30]]
    grundwert=random.randint(E[2][0]*100,E[2][1]*100)/100 if komma else random.randint(E[2][0],E[2][1])
    xStart,xZiel=1,1
    while xStart==xZiel:
        xStart=random.randint(10,2000)/100 if komma else random.randint(2,20)
        xZiel=random.randint(10,2000)/100 if komma else random.randint(2,20)
#    yStart=grundwert:xStart
    art1,einh1=E[0].split(" ")
    art2,einh2=E[1].split(" ")
    if ein1=='Arbeiter':
        afg=F'Wielange brauchen {strNW(xZiel,True)} {einh} für die Arbeit, wenn {strNW(xStart,True)} {einh} {strNW(yStart,True)} {einh2} brauchen?'
        afg=afg if mitText else (F'{art}:$${strNW(xStart,True)}~{einh}\hat{{=}} {strNW(yStart,True)}~\\mbox{{\\euro{{}}}} \\rightarrow {strNW(xZiel,True)}~{einh}=\\mbox{{?}}$$')
    elif 'h'==einh:
        afg=F'Welche Strecke wurde in  {strNW(xZiel,True)} {einh} zurückgelegt, wenn man in {strNW(xStart,True)} {einh} {strNW(yStart,True)} km schafft.'
        afg=afg if mitText else (F'Bewegung:$${strNW(xStart,True)}~{einh}\hat{{=}} {strNW(yStart,True)}~\\mbox{{km}} \\rightarrow {strNW(xZiel,True)}~{einh}=\\mbox{{?}}$$')
    elif 'Anzahl'==einh:
        xStart=int(xStart)
        xZiel=int(xZiel)
        afg=F'Berechne den Preis für {strNW(xZiel,True)} {art}, wenn {strNW(xStart,True)} {art} {strNW(yStart,True)} \\euro{{}} kosten.'
        afg=afg if mitText else (F'{art}:$${strNW(xStart,True)}\hat{{=}} {strNW(yStart,True)}~\\mbox{{\\euro{{}}}} \\rightarrow {strNW(xZiel,True)}=\\mbox{{?}}$$')
    else:
        afg='Noch nichts.'
    lsg=dreiSatz(links=[strNW(x,True) for x in [xStart,'1',xZiel]],rechts=[strNW(x,True) for x in [yStart,yStart/xStart,yStart/xStart*xZiel]],title=E,breit=True)
    return [afg,lsg,[xStart,xZiel,yStart]]

