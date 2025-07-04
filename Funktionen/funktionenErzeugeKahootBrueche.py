#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeKahootBruecheKuerzenMitVorg(zeit=10,HS=False):
    a,b=random.randint(1,10 if HS else 15),random.randint(1,10 if HS else 15)
    while a>=b:
        a,b=random.randint(1,10),random.randint(1,10)
    f=random.randint(2,10  if HS else 12)
    results=[f'$$\\frac{{{x}}}{{{y}}}$$' for x,y in [[a,b],[b,a],[a+1,b],[a*f-f,b*f-f]]]
    random.shuffle(results)
    frage=f'$$\\text{{Kürze mit Faktor {f}:}}~\\frac{{{a*f}}}{{{b*f}}}$$'
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == f'$$\\frac{{{a}}}{{{b}}}$$'])
    return [frage]+results+[zeit,ergIndizes]