#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeKahootBruecheKuerzenMitVorg(zeit=10,HS=False):
    a,b=random.randint(1,10 if HS else 15),random.randint(1,10 if HS else 15)
    while a>=b:
        a,b=random.randint(1,10),random.randint(1,10)
    f=random.randint(2,10  if HS else 12)
    results=[f'$$\\frac{{{x}}}{{{y}}}$$' for x,y in [[a,b],[b,a],[a*f,b],[a,b*f]]]
    random.shuffle(results)
    frage=f'$$\\text{{Kürze mit {f}:}}~\\frac{{{a*f}}}{{{b*f}}}$$'
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == f'$$\\frac{{{a}}}{{{b}}}$$'])
    return [frage]+results+[zeit,ergIndizes]

def erzeugeKahootBruecheErweiternMitVorg(zeit=10,HS=False):
    a,b=random.randint(1,10 if HS else 15),random.randint(1,10 if HS else 15)
    while a>=b:
        a,b=random.randint(1,10),random.randint(1,10)
    f=random.randint(2,10  if HS else 12)
    results=[f'$$\\frac{{{x}}}{{{y}}}$$' for x,y in [[a*f,b*f],[b*f,a*f],[a*f,b],[a,b*f]]]
    random.shuffle(results)
    frage=f'$$\\text{{Erweiter mit {f}:}}~\\frac{{{a}}}{{{b}}}$$'
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == f'$$\\frac{{{a*f}}}{{{b*f}}}$$'])
    return [frage]+results+[zeit,ergIndizes]


def erzeugeKahootRationaleZahlenAddSub(zeit=10,HS=False):
    a,b=(random.randint(1,20),random.randint(1,20)) if HS else (random.randint(1,100),random.randint(1,100))
    pMlinks=random.choice(['+','-'])
    pMmitte=random.choice(['+','-'])
    pMrechts=random.choice(['+','-'])
    gegenPM={'+':'-','-':'+'}
    term=f'{a}{pMmitte}({pMrechts}{b})' if HS else f'({pMlinks}{a}){pMmitte}({pMrechts}{b})'
    if HS:
        while eval(term)<0:
            a,b=(random.randint(1,20),random.randint(1,20)) if HS else (random.randint(1,100),random.randint(1,100))
            pMmitte=random.choice(['+','-'])
            pMrechts=random.choice(['+','-'])
            term=f'{a}{pMmitte}({pMrechts}{b})'
    frage=f'Berechne: {term}='
    results=[eval(term),eval(f'{a}{gegenPM[pMmitte]}({pMrechts}{b})') if HS else eval(f'({pMlinks}{a}){gegenPM[pMmitte]}({pMrechts}{b})'),
             (1 if random.getrandbits(1) else -1)*random.randint(1,10)+eval(term),
             (1 if random.getrandbits(1) else -1)*random.randint(1,10)+(eval(f'{a}{gegenPM[pMmitte]}({pMrechts}{b})') if HS else eval(f'({pMlinks}{a}){gegenPM[pMmitte]}({pMrechts}{b})'))]
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == eval(term)])
    return [frage]+results+[zeit,ergIndizes]



def erzeugeKahootRationaleZahlenMultiDiv(zeit=10,HS=False):
    a,b=random.randint(1,12),random.randint(2,12)
    pMlinks=random.choice(['+','-'])
    malGeteilt=random.choice(['*','/'])
    a,b=(a*b,b) if malGeteilt=='/' else (a,b)
    pMrechts=random.choice(['+','-'])
    gegenPM={'+':'-','-':'+'}
    term=f'({pMlinks}{a}){malGeteilt}({pMrechts}{b})'
    frage=f'Berechne: {term}='
    results=[eval(term),eval(f'({pMlinks}{a}){malGeteilt}({gegenPM[pMrechts]}{b})'),
             eval(f'({pMlinks}{a}){malGeteilt}({pMrechts}{b-1})'),eval(f'(a){malGeteilt}({gegenPM[pMrechts]}{b-1})')]
    if malGeteilt=='/':
        results=[eval(term),eval(f'({pMlinks}{a})/({gegenPM[pMrechts]}{b})'),eval(term)+(1 if random.getrandbits(1) else -1),
             eval(f'({pMlinks}{a})/({gegenPM[pMrechts]}{b})')+(1 if random.getrandbits(1) else -1),]
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == eval(term)])    
    return [frage.replace('/',':').replace('*','·')]+results+[zeit,ergIndizes]

def erzeugeKahootProzentwert(zeit=10):
    ges=''
    werte=erzeugeProzentRechnungen(HS=True)
    art=werte[3]
    varis={'G':[werte[0],art],'W':[werte[1],art],'p':[werte[2],'\\%']}
    geg=list(varis.keys())
    if len(ges)<1:
        ges=random.choice(geg)
    geg.remove(ges)
    formel='W=G*p/100'
    if ges=='W':
        frage=F'{strNW(varis[geg[1]][0])} {varis[geg[1]][1]} von {strNW(varis[geg[0]][0])} {varis[geg[0]][1]}'
    if ges=='G':
        frage=F'{strNW(varis[geg[0]][0])} {varis[geg[0]][1]} sind {strNW(varis[geg[1]][0])} {varis[geg[1]][1]}'
    if ges=='p':
        frage=F'{strNW(varis[geg[1]][0])} {varis[geg[1]][1]} von {strNW(varis[geg[0]][0])} {varis[geg[0]][1]}'
    einheiten=erzeugeProzentEinheiten()+['\\%']
    del einheiten[einheiten.index(varis[ges[0]][1])]
    results=[F'{ges}={strNW(varis[ges[0]][0])} {varis[ges[0]][1]}',F'{ges}={strNW(varis[ges[0]][0])} {varis[geg[0]][1] if varis[ges[0]][1]==chr(37) else "&&%"}'.replace('&&','\\')]
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == F'{ges}={strNW(varis[ges[0]][0])} {varis[ges[0]][1]}'])
    return [frage]+results+[zeit,ergIndizes]