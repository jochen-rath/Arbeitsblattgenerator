#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenErzeugeGeometrieAufgaben.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
import math
import random
#    farben={"magenta":"Magenta","darkgray":"Dunkelgrau", "violet":"Violett","blue":"Blau","gray":"Grau","green":"Green","brown":"Braun","black":"Schwarz","pink":"Rosa","red":"Rot","yellow":"Gelb","orange":"Orange"}

def erzeugeStrahlensaetzeAufgaben(mitText=True):
    k=random.randint(14,21)/10
    k=k*random.choice([1,-1])
    einheit=random.choice(['mm', 'cm', 'dm', 'm', 'km'])
#Erzeuge Zufällige Positionen für die Zeichnung
    m1=1
    m2=1
    while abs(m1-m2)<3:
        A=[random.randint(5,25)/10,random.randint(5,25)/10]
        B=[random.randint(5,25)/10,A[1]+random.randint(10,20)/10]
        m1=A[1]/A[0]
        m2=B[1]/B[0]
    Astr=[x*k for x in A]
    Bstr=[x*k for x in B]
#Erzeuge die zu berechenden Werte aus den Zeichhnungswerten durch Multiplikation mit einem Faktor
    fZA=random.randint(10,100)/10    #faktor von der Zeichnung zur Aufgabe
    SAWert=math.dist([0,0],A)*fZA
    SBWert=math.dist([0,0],B)*fZA
    SAstrWert=math.dist([0,0],Astr)*fZA
    SBstrWert=math.dist([0,0],Bstr)*fZA
    ABWert=math.dist(A,B)*fZA
    AstrBstrWert=math.dist(Astr,Bstr)*fZA
    streckenLaengen=[SAWert,SAstrWert,SBWert,SBstrWert,ABWert,AstrBstrWert]
    streckenLaengenIndexe=list(range(len(streckenLaengen)))
#Gib den Punkten zufällige Bezeichnungen
    punkte=random.sample(buchstabenGross,5)
    p=punkte
#Und bastel die daraus die Streckenbezeichnungen
    strecken=[p[0]+p[1],p[0]+p[2],p[0]+p[3],p[0]+p[4],p[1]+p[3],p[2]+p[4]]
#Für den Strahlensatz braucht man nur 4 der 6 Strecken
    entferntPos=random.randint(0,2)
    entfernt=[2*entferntPos,2*entferntPos+1]
    streckenLaengenRed=list(streckenLaengen)
    del streckenLaengenRed[entfernt[0]:entfernt[1]+1]
    del streckenLaengenIndexe[entfernt[0]:entfernt[1]+1]
    streckenRed=list(strecken)
    del streckenRed[entfernt[0]:entfernt[1]+1]
#    auswahlFarben=random.sample(list(farben.keys()),6)
    auswahlFarben=['black']*6
#    auswahlFarben[entfernt[0]:entfernt[1]+1]=['black']*2
#Es bleiben vier Strecken ueber. Eine davon muss berechnet werden.
    xNr=random.randint(0,3)
    afg=['\\pbox{5cm}{']
    afg=afg+(['Zeichne die angegebenen Strecken farbig nach und berechne die fehlende Seite.\\\\'] if mitText else [])
    afg=afg+strahlensatz(A=A, B=B,k=k, farben=['black']*6,punkte=punkte,strecken=['']*len(strecken))
    afg=afg+['$\\begin{aligned}']
    for i,l in enumerate(streckenLaengenRed):
        if not i==xNr:
            afg=afg+[F'\\overline{{{streckenRed[i]}}}&={strNW(l,True)}~{einheit}\\\\']
    afg=afg+['\\end{aligned}$']
    afg=afg+['}']
#Entnehme dir die Indexe nach dem Motto: Groß zu klein ist gleich Groß zu klein.
#Die Strecken sind so angeordnet: [klein,groß,klein,groß]
    zaehler1='x'        #red
    nenner1Nr= xNr-1 if xNr in [1,3] else xNr+1     #blue
    zaehler2Nr=xNr+2 if xNr in [0,1] else xNr-2     #olive
    nenner2Nr= 3 if xNr==0 else ( 2 if  xNr==1 else  ( 1 if xNr==2  else 0))    #orange
    farben=['red','blue','green','orange']
    auswahlFarben[streckenLaengenIndexe[xNr]]=farben[0]
    auswahlFarben[streckenLaengenIndexe[nenner1Nr]]=farben[1]
    auswahlFarben[streckenLaengenIndexe[zaehler2Nr]]=farben[2]
    auswahlFarben[streckenLaengenIndexe[nenner2Nr]]=farben[3]
    lsg=['\\pbox{5cm}{']
    lsg=lsg+strahlensatz(A=A,B=B,k=k,farben=auswahlFarben,punkte=punkte,strecken=['']*len(strecken))
    lsg=lsg+['$\\begin{aligned}']
    lsg=lsg+[F'\\frac{{\\color{{{farben[0]}}}{{x}}}}{{\\overline{{\\color{{{farben[1]}}}{{{streckenRed[nenner1Nr]}}}}}}}&=\\frac{{\\overline{{\\color{{{farben[2]}}}{{{streckenRed[zaehler2Nr]}}}}}}}{{\\overline{{\\color{{{farben[3]}}}{{{streckenRed[nenner2Nr]}}}}}}} \\quad &  \\\\']
    lsg=lsg+[F'\\frac{{x}}{{{strNW(streckenLaengenRed[nenner1Nr],True)}}}&=\\frac{{{strNW(streckenLaengenRed[zaehler2Nr],True)}}}{{{strNW(streckenLaengenRed[nenner2Nr],True)}}} \\quad &  | \\cdot {strNW(streckenLaengenRed[nenner1Nr],True)} \\\\']
    lsg=lsg+[F'x&=\\frac{{{strNW(streckenLaengenRed[zaehler2Nr],True)}}}{{{strNW(streckenLaengenRed[nenner2Nr],True)}}} \\cdot {strNW(streckenLaengenRed[nenner1Nr],True)} \\quad &   \\\\']
    lsg=lsg+[F'x&={strNW(streckenLaengenRed[xNr],True)}~{einheit}&']
    lsg=lsg+['\\end{aligned}$']
    lsg=lsg+['}']
    return [afg,lsg,[]]