#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def aufgabenZufallsversuch(typ='Münzwurf',werte=['Kopf','Zahl',['1','1']],einstufig=True):
    anzahl=[eval(x) for x in werte[-1]]
    wahrscheinlichkeiten=[F'{x}/{sum(anzahl)}' for x in anzahl]
    print(typ,werte,wahrscheinlichkeiten,anzahl)
    anzahlVersuchsergebnisse=', '.join([F'{"" if anzahl[i]==1 else F"{anzahl[i]} mal "}{x}' for i,x in enumerate(werte[:-1])])
    afgText=F'Erstelle das Baumdiagramm für den {"" if einstufig else "zweistufigen "}Zufallsversuch'
    if typ in ['Münzwurf','Loseziehen']:
        afg = [F'{afgText} {typ} mit {anzahlVersuchsergebnisse}.']
    if typ=='Würfelwurf':
        afg = [F'{afgText} {typ} mit den Zahlen {anzahlVersuchsergebnisse}.']
    if typ=='Beutelziehen':
        afg = [F'{afgText} {typ} mit {"" if einstufig else "zurücklegen und"} {anzahlVersuchsergebnisse}.']
    if 'Drehscheibe' in typ:
        afg = [F'Erstelle das Baumdiagramm {"für folgende" if einstufig else "wenn folgende"} Drehscheibe {"" if einstufig else "zweimal gedreht wird"}:\\\\']
        farben=[]
        for i,n in enumerate(anzahl):
            farben=farben+[werte[i]]*int(n)
        random.shuffle(farben)
        afg=afg+DrehscheibeFarblich(farben=farben)
    return afg,wahrscheinlichkeiten

def zufallsversuch(einstufig=True):
    farben=['Rot','Grün','Blau','Orange','Lila','Pink']
    zufall={'Münzwurf':['Kopf','Zahl',['1','1']]}
    nWuerfel=random.randint(3,(6 if einstufig else 5))
    #Die Zahlen müssen später Strings sein.
    zufall['Würfelwurf']=[str(x) for x in list(range(1,nWuerfel+1))]+[['1']*nWuerfel]
    nFarbe=random.randint(2,5)
    zufall['gleichmäßige Drehscheibe']=random.sample(farben,nFarbe)+[['1']*nFarbe]
    zufall['ungleichmäßige Drehscheibe']=random.sample(farben,nFarbe)+[['random.randint(1,3)' for i in range(nFarbe)]]
    zufall['ungleichmäßige Drehscheibe 2']=random.sample(farben,nFarbe)+[['random.randint(1,3)' for i in range(nFarbe)]]
    zufall['ungleichmäßige Drehscheibe 3']=random.sample(farben,nFarbe)+[['random.randint(1,3)' for i in range(nFarbe)]]
    zufall['Beutelziehen']=random.sample(buchstabenGross,4)+[['random.randint(1,3)','random.randint(1,3)','random.randint(1,3)','random.randint(1,3)']]
    if einstufig:
        zufall['Loseziehen']=['Niete','Kleingewinn','Hauptgewinn',['random.randint(100,150)','random.randint(30,50)','random.randint(5,10)']]
    return zufall

def einOderZweiStufigeZufallsversuche(einstufig=True,anzSpalten=2):
    zufall=zufallsversuch(einstufig=einstufig)
    for i in range(2):
        if zufall=='Münzwurf':
            zufall = zufallsversuch(einstufig=einstufig)
    auswahl=random.choice(list(zufall.keys()))
    gesucht=[random.choice(zufall[auswahl][:-1]) for i in range(1 if einstufig else 2)]
    aufgabe, wahrscheinlichkeiten = aufgabenZufallsversuch(typ=auswahl,werte=zufall[auswahl],einstufig=einstufig)
    afg=[F'\\pbox{{{15 if anzSpalten==1 else 7}cm}}{{']
    afg=afg+aufgabe+['\\\\']
    afg=afg+[F'Berechne die Wahrscheinlichkeit $P({",".join([F"&&mbox{{{x}}}" for x in gesucht])})$.'.replace('&&','\\')]
    afg=afg+['}']
    ergebnis={}
    for i,e in enumerate(zufall[auswahl][:-1]):
        ergebnis[e[0]]=wahrscheinlichkeiten[i]
    lsg = [F'\\pbox{{15 cm}}{{']
    lsg=lsg+baumdiagramm(erg=[ergebnis]*(1 if einstufig else 2))
    lsg=lsg+[F'\\\\']
    lsg=lsg+[F'$P(\\mbox{{{",".join([F"&&mbox{{{x}}}" for x in gesucht])}}})={erzeugeLatexFracAusdruck(ergebnis[gesucht[0][0]])}{"" if einstufig else F"*{erzeugeLatexFracAusdruck(ergebnis[gesucht[1][0]])}"}={strNW(eval(ergebnis[gesucht[0][0]])*(1 if einstufig else eval(ergebnis[gesucht[1][0]]))*100,2)}\\%$'.replace('&&','\\').replace('*','\\cdot ')]
    lsg = lsg+['}']
    return [afg,lsg,[]]
