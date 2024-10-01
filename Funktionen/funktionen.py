#!/usr/bin/env python
# coding: utf8

#Die Funktion in diesem Skript vereint die Würfel, Stäbe und Scheiben Bilder zu der Zahl,
#die der Funktion übergeben wird. Gespeichert wird das Ergebnis unter "test.png"
#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
#
#       exec(open("/home/jochen/Schule/skripteArbeitsblaetter/Funktionen/funktionen.py").read())
#    
#  funktionenpfad='/home/jochen/Schule/skripteArbeitsblaetter/Funktionen/'

buchstabenKlein=[chr(i) for i in range(97,97+26)]
grBuchst=['\u03B1','\u03B2','\u03B3','\u03B4','\u03B5','\u03B6']
funktionenpfad= 'Funktionen' if not 'funktionenpfad' in locals() else funktionenpfad
import os

for file in os.listdir(funktionenpfad):
    if ('funktionen' in file or 'startup' in file) and not (file  == 'funktionen.py') and (os.path.isfile(os.path.join(funktionenpfad,file))):
        print(file)
        exec(open(os.path.join(funktionenpfad,file)).read())

