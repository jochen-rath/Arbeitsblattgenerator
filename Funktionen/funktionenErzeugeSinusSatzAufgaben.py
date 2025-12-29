#!/usr/bin/env python
# coding: utf8

#Aufruf:
#		import os
#		os.chdir(f'{os.path.expanduser("~")}/Schule/Arbeitsblattgenerator')
#       exec(open("Funktionen/funktionen.py").read())
#Aufruf:
#       exec(open("Funktionen/funktionenErzeugeGeometrieAufgaben.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())
import math
import random
#    farben={"magenta":"Magenta","darkgray":"Dunkelgrau", "violet":"Violett","blue":"Blau","gray":"Grau","green":"Green","brown":"Braun","black":"Schwarz","pink":"Rosa","red":"Rot","yellow":"Gelb","orange":"Orange"}

def erzeugeSinussatzRechtwBenennen(sinKosTan='',mitText=True,anzSpalten=[2,2]):
    wBez=random.sample(list(abcZuGr.keys()),3)
    rechtWinkelNr=random.randint(0,2)
    seiten=list(wBez)
    rechterWinkelBei=wBez[rechtWinkelNr].upper()
    hyp=wBez[rechtWinkelNr].lower()
    del seiten[rechtWinkelNr]
    gesucht=[random.choice(seiten),random.choice(['Sinus','Kosinus','Tangens']) if len(sinKosTan)<1 else sinKosTan]
    gegKat=gesucht[0].lower()
    anKat=[x for x in seiten if not x==gegKat][0]
    afgText=f'Formuliere den {gesucht[1]} und markiere die benötigten Seiten zur Berechnung des roten Winkels von folgendem Dreieck\\\\'
    afg=['\\pbox{\\linewidth}{']+([afgText] if mitText else [f'{gesucht[1]}:\\\\'])
    afg=afg+planfigurRWSinusKosinus(rW=rechterWinkelBei,wBez=wBez,ges=gesucht[0])
    afg=afg+['}']
    loesung={'Sinus':['\\sin','gegKat','hyp'],'Kosinus':['\\cos','anKat','hyp'],'Tangens':['\\tan','gegKat','anKat']}
    lsg=['\\pbox{\\linewidth}{']+[f'${loesung[gesucht[1]][0]}({abcZuGr[gesucht[0]]})=\\left(\\frac{{{eval(loesung[gesucht[1]][1])}}}{{{eval(loesung[gesucht[1]][2])}}}\\right)$\\\\']
    lsg=lsg+planfigurRWSinusKosinus(rW=rechterWinkelBei,wBez=wBez,ges=gesucht[0],markieren=[eval(loesung[gesucht[1]][2]),eval(loesung[gesucht[1]][1])])
    lsg=lsg+['}']    
    return [afg,lsg,[]]

def erzeugeSinussatzRechtwBerechnen(sinKosTan='',mitWinkel=True,mitText=True,anzSpalten=[2,2]):
    wBez=random.sample(list(abcZuGr.keys()),3)    #3 kleine Buchstaben
    werte={}
    laengenBez=[]
    for s in wBez:
        werte[s]=random.randint(20,50)/10
    rechtWinkelNr=random.randint(0,2)
    seiten=list(wBez)
    rechterWinkelBei=wBez[rechtWinkelNr].upper()
    hyp=wBez[rechtWinkelNr].lower()
    del seiten[rechtWinkelNr]
    gesucht=[random.choice(seiten),random.choice(['Sinus','Kosinus','Tangens']) if len(sinKosTan)<1 else sinKosTan]
    gegKat=gesucht[0].lower()
    anKat=[x for x in seiten if not x==gegKat][0]
    werte[hyp]=(werte[anKat]**2+werte[gegKat]**2)**0.5
    coordinaten=[(0,0)]*3
    coordinaten[1]=f'({werte[wBez[2]]},0)'
    if rechtWinkelNr==0:
        coordinaten[2]=f'(0,{werte[wBez[1]]})'
    if rechtWinkelNr==1:
        coordinaten[2]=f'({werte[wBez[2]]},{werte[wBez[0]]})'
    if rechtWinkelNr==2:
        coordinaten[2]=f'({math.degrees(math.asin(werte[wBez[0]]/werte[wBez[2]]))}:{werte[wBez[1]]})'
    for s in wBez:
        laengenBez.append(f'{s}={strNW(werte[s],2)} cm')
    afgText=f'Berechne den {gesucht[1]} des roten Winkels{", den Winkel" if mitWinkel else ""} und markiere die benötigten Seiten. Überprüfe die Werte mit einer Messung.\\\\'
    afg=['\\pbox{\\linewidth}{']+([afgText] if mitText else [f'{gesucht[1]}:\\\\'])
    afg=afg+planfigurRWSinusKosinus(rW=rechterWinkelBei,wBez=wBez,ges=gesucht[0],laengenBez=laengenBez,coordinaten=coordinaten)
    afg=afg+['}']
    loesung={'Sinus':['\\sin',gegKat,hyp],'Kosinus':['\\cos',anKat,hyp],'Tangens':['\\tan',gegKat,anKat]}
    lsg=['\\pbox{\\linewidth}{']+['$\\begin{aligned}']
    lsg.append(f'{loesung[gesucht[1]][0]}({abcZuGr[gesucht[0]]})&=\\left(\\frac{{{loesung[gesucht[1]][1]}}}{{{loesung[gesucht[1]][2]}}}\\right) & &\\\\')
    lsg.append(f'&=\\left(\\frac{{{strNW(werte[loesung[gesucht[1]][1]],2)}~cm}}{{{strNW(werte[loesung[gesucht[1]][2]],2)}~cm}}\\right) & & \\\\')
    lsg.append(f'{loesung[gesucht[1]][0]}({abcZuGr[gesucht[0]]})&={strNW(werte[loesung[gesucht[1]][1]]/werte[loesung[gesucht[1]][2]],2)} & {("\\mid \\mbox{a"+loesung[gesucht[1]][0][1:]+"}") if mitWinkel else ""}&\\\\')
    if mitWinkel:
        lsg.append(f'{abcZuGr[gesucht[0]]}&={strNW(eval("math.degrees(math.a"+loesung[gesucht[1]][0][1:]+"("+str(werte[loesung[gesucht[1]][1]]/werte[loesung[gesucht[1]][2]])+"))"),0)}^\\circ & &\\\\')
    lsg.append('\\end{aligned}$')
    lsg=lsg+planfigurRWSinusKosinus(rW=rechterWinkelBei,wBez=wBez,ges=gesucht[0],markieren=[loesung[gesucht[1]][2],loesung[gesucht[1]][1]],laengenBez=laengenBez,coordinaten=coordinaten)
    lsg=lsg+['}']    
    return [afg,lsg,[]]