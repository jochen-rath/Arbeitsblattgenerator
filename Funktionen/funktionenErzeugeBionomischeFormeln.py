#!/usr/bin/env python
# coding: utf8
import random


#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Berechnung von Termen und Gleichungen


#Aufruf:
#		import os
#		os.chdir(f'{os.path.expanduser("~")}/Schule/Arbeitsblattgenerator')
#       exec(open("Funktionen/funktionen.py").read())

def einfachAnwendungBionomischeFormeln(mitText=True):
    vari={'a':[random.randint(1,20),'' if random.randint(0,1)<1 else random.choice(buchstabenKlein)]}
    vari['b']=[random.randint(1,20),'' if random.randint(0,1)<1 else random.choice(buchstabenKlein)]
    bioFormel={1:f'({vari["a"][0]}{vari["a"][1]}+{vari["b"][0]}{vari["b"][1]})^2'}
    bioFormel[2]=f'({vari["a"][0]}{vari["a"][1]}-{vari["b"][0]}{vari["b"][1]})^2'
    bioFormel[3]=f'({vari["a"][0]}{vari["a"][1]}+{vari["b"][0]}{vari["b"][1]})\\cdot({vari["a"][0]}{vari["a"][1]}-{vari["b"][0]}{vari["b"][1]})'
    auswahl=random.randint(1,3)
    op='+' if auswahl==1 else '-'
    afg=f'{"Löse folgende Aufgabe mit Hilfe der Bionomischen Formel: " if mitText else ""} $${bioFormel[auswahl]}$$'
    lsg=['$\\begin{aligned}']
    if auswahl<3:
        lsg.append(f'({vari["a"][0]}{vari["a"][1]}{op}{vari["b"][0]}{vari["b"][1]})^2 & = {vari["a"][0]}^2{vari["a"][1]}{"^2" if len(vari["a"][1])>0 else ""}{op}2\\cdot{vari["a"][0]}{vari["a"][1]}\\cdot{vari["b"][0]}{vari["b"][1]}+{vari["b"][0]}^2{vari["b"][1]}{"^2" if len(vari["b"][1])>0 else ""} \\\\')
        lsg.append(f'&={vari["a"][0]**2}{vari["a"][1]}{"^2" if len(vari["a"][1])>0 else ""}{op}{2*vari["a"][0]*vari["b"][0]}{vari["a"][1]}{vari["b"][1]}+{vari["b"][0]**2}{vari["b"][1]}{"^2" if len(vari["b"][1])>0 else ""} \\\\')
        if len(vari["a"][1])==0 and len(vari["b"][1])==0:
            erg=eval(f'{vari["a"][0]}**2{op}{2*vari["a"][0]*vari["b"][0]}+{vari["b"][0]**2}')
            lsg.append(f'&={erg}')
    else:
        lsg.append(f'({vari["a"][0]}{vari["a"][1]}+{vari["b"][0]}{vari["b"][1]})\\cdot({vari["a"][0]}{vari["a"][1]}-{vari["b"][0]}{vari["b"][1]}) & = {vari["a"][0]}^2{vari["a"][1]}{"^2" if len(vari["a"][1])>0 else ""}-{vari["b"][0]}^2{vari["b"][1]}{"^2" if len(vari["b"][1])>0 else ""}\\\\')
        lsg.append(f'&={vari["a"][0]**2}{vari["a"][1]}{"^2" if len(vari["a"][1])>0 else ""}{op}{vari["b"][0]**2}{vari["b"][1]}{"^2" if len(vari["b"][1])>0 else ""} \\\\')
        if len(vari["a"][1])==0 and len(vari["b"][1])==0:
            erg=eval(f'{vari["a"][0]}**2-{vari["b"][0]**2}')
            lsg.append(f'&={erg}')
    lsg.append('\\end{aligned}$')
    return [afg,lsg,[]]