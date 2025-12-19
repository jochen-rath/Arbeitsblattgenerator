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

def erzeugeSinussatzRechtwBenennen(mitText=True,anzSpalten=[2,2]):
    wBez=random.sample(list(abcZuGr.keys()),3)
    rechtWinkelNr=random.randint(0,2)
    seiten=list(wBez)
    rechterWinkelBei=wBez[rechtWinkelNr].upper()
    hyp=wBez[rechtWinkelNr].lower()
    del seiten[rechtWinkelNr]
    gesucht=[random.choice(seiten),random.choice(['Sinus','Kosinus'])]
    gegKat=gesucht[0].lower()
    anKat=[x for x in seiten if not x==gegKat][0]
    afgText=f'Formuliere den {gesucht[1]} und markiere die benötigten Seiten zur Berechnung des roten Winkels von folgendem Dreieck\\\\'
    afg=['\\pbox{\\linewidth}{']+([afgText] if mitText else [f'{gesucht[1]}:\\\\'])
    afg=afg+planfigurRWSinusKosinus(rW=rechterWinkelBei,wBez=wBez,ges=gesucht[0])
    afg=afg+['}']
    loesung={'Sinus':['\\sin','gegKat','hyp'],'Kosinus':['\\cos','anKat','hyp']}
    lsg=['\\pbox{\\linewidth}{']+[f'${loesung[gesucht[1]][0]}({abcZuGr[gesucht[0]]})=\\left(\\frac{{{eval(loesung[gesucht[1]][1])}}}{{{eval(loesung[gesucht[1]][2])}}}\\right)$\\\\']
    lsg=lsg+planfigurRWSinusKosinus(rW=rechterWinkelBei,wBez=wBez,ges=gesucht[0],markieren=[hyp,eval(loesung[gesucht[1]][1])])
    lsg=lsg+['}']    
    return [afg,lsg,[]]
