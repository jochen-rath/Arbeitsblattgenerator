#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random

def erzeugeRationaleZahlenKlammerAufloesen(mitText=True):
    zahl=str(random.choice(['+','-']))+'('+str(random.choice(['+','-']))+str(random.randint(1,100))+')'
    afg=[F'{"Löse die Klammer auf: " if mitText else ""}{zahl}=']
    lsg=[F'{zahl}={eval(zahl)}']
    return [afg,lsg,[]]

def erzeugeMittlerenWertBestimmen(mitSchritt=False,mitText=True,breitePbox='\\textwidth'):
    start=(1 if random.getrandbits(1) else -1) * random.randint(0,30)
    sw=random.choice(range(2,20,2))
    afg=[F'\\pbox{{{breitePbox}{"" if "text" in breitePbox else "cm"}}}{{Bestimme die mittlere Zahl:\\\\'] if mitText else []
#    print(F'mitSchritt={mitSchritt}')
    afg=afg+zahlenstrahlBestimmeMitte(start=start,schrittweite=sw,laenge=5,mitLsg=False,mitSchritt=mitSchritt)
    afg=afg+(['}']  if mitText else [])
    lsg=zahlenstrahlBestimmeMitte(start=start,schrittweite=sw,laenge=5,mitLsg=True,mitSchritt=mitSchritt)
    return [afg,lsg,[]]

def erzeugeRationaleZahlenAufgabe(operator='',leicht=True):
#Diese Funktion erzeugt eine Aufgabe zur Berechnung von rationalen Zahlen
#Aufruf:
#            [afg,lsg,zahlen]=erzeugeRationaleZahlenAufgabe
#
#Der Operator ist nicht zufällig, wenn das random.choice in den Funktionsaufruf gestellt wird.
    operator=operator if len(operator)>0 else random.choice(['+','-'])
    zahl1=str(random.choice(['','-']))+'('+str(random.choice(['+','-']))+str(random.randint(1,12))+')'
    zahl1='('+str(random.choice(['+','-']))+str(random.randint(1,12))+')'
    zahl2=operator+'('+str(random.choice(['+','-']))+str(random.randint(1,12))+')'
    afg=zahl1+zahl2+'='
    lsg=afg+strNW(eval(zahl1))+('+' if eval(zahl2)>0 else '')+ strNW(eval(zahl2))+'='+strNW(eval(afg[:-1]))
    return ['$'+ersetzePlatzhalterMitSymbolen(afg)+'$','$'+ersetzePlatzhalterMitSymbolen(lsg)+'$',[zahl1,zahl2]]


def erzeugeRationaleZahlenAufgabeMalGeteilt(operator='',leicht=True):
#Diese Funktion erzeugt eine Aufgabe zur Berechnung von rationalen Zahlen
#Aufruf:
#            [afg,lsg,zahlen]=erzeugeRationaleZahlenAufgabe
#
#Der Operator ist nicht zufällig, wenn das random.choice in den Funktionsaufruf gestellt wird.
    operator=operator if len(operator)>0 else random.choice(['*','/'])
    zahl2='('+str(random.choice(['+','-']))+str(random.randint(1,12))+')'
    zahl1=str(random.choice(['','-']))+'('+str(random.choice(['+','-']))+str(random.randint(1,12))+')'
    zahl1='('+str(random.choice(['+','-']))+str(random.randint(1,12))+')'
    if operator=='/':
        zahl1=str(random.choice(['','-']))+'('+str(random.choice(['+','-']))+str(abs(eval(zahl2)*random.randint(1,12)))+')'
        zahl1='('+str(random.choice(['+','-']))+str(abs(eval(zahl2)*random.randint(1,12)))+')'
    afg=zahl1+operator+zahl2+'='
    lsg=afg+strNW(eval(zahl1))+operator+(strNW(eval(zahl2)) if eval(zahl2)>0 else zahl2)+'='+strNW(eval(afg[:-1]))
    return ['$'+ersetzePlatzhalterMitSymbolen(afg)+'$','$'+ersetzePlatzhalterMitSymbolen(lsg)+'$',[zahl1,zahl2]]