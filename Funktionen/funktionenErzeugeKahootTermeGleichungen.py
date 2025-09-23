#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeKahootTermeEinfachEinsetzen(zeit=10,HS=False,formelSchoen=False):
    alleVaris=['x','y','z','a','b']
    vari=random.choice(alleVaris)
    op=random.choice(['+','-','*','/'])    
    x=random.randint(1,100) if op in ['+','-'] else random.randint(1,15)
    zahl=random.randint(1,100) if op in ['+','-'] else random.randint(1,15)
    variZuerst=bool(random.getrandbits(1)) or op=='/'
    term=f'{vari}{op}{zahl}' if variZuerst else f'{zahl}{op}{vari}'
    erg=eval(term.replace(f'{vari}',str(x)))
    if HS:
        while erg<0:
            x=random.randint(1,100) if op in ['+','-'] else random.randint(1,15)
            zahl=random.randint(1,100) if op in ['+','-'] else random.randint(1,15)     
            term=f'{zahl}{op}{vari}' if variZuerst else f'{vari}{op}{zahl}'
            erg=eval(term.replace(f'{vari}',str(x)))
    if  op=='/' and formelSchoen:
        term=f'\\frac{{{vari}}}{{{zahl}}}'
    x,erg=(x*zahl,x) if op=='/' else (x,erg)
    auswahl=random.sample(range(1, 5 if erg<10 else 10), 3)
    results=[erg,erg+(1 if bool(random.getrandbits(1)) else -1)*auswahl[0],erg+(1 if bool(random.getrandbits(1)) else -1)*auswahl[1],erg+(1 if bool(random.getrandbits(1)) else -1)*auswahl[2]]
    random.shuffle(results)
    frage=f'$${vari}={x}~\\rightarrow~{term.replace("*","·").replace("/",":")}=?$$' if formelSchoen else f'{vari}={x} → {term.replace("*","·").replace("/",":")}=?'
    return [frage]+results+[zeit,results.index(erg)+1]

def erzeugeKahootTermeKombiEinsetzen(zeit=10,HS=False,formelSchoen=False):
    alleVaris=['x','y','z','a','b']
    vari=random.choice(alleVaris)
    op=random.choice(['+','-'])
    op2=random.choice(['*','/'])
    Z1=random.randint(1,10 if HS else 14)
    x=random.randint(0,10  if HS else 14)
    x=x if op2=='*' else x*Z1
    ergTerm1=x*Z1 if op2=='*' else int(x/Z1)
#Keine negativen Ergebnisse für die HS
    erg=(1 if bool(random.getrandbits(1)) or HS else -1)*random.randint((ergTerm1+1) if HS and op=='+' else 1,  (ergTerm1+1) if HS and op=='-' else 150)
    Z2=(erg-ergTerm1) if op=='+' else (ergTerm1-erg)
    term=f'{Z1}*{vari}{op}{Z2}' if op2=='*' else (f'\\frac{{{vari}}}{{{Z1}}}{op}{Z2}' if formelSchoen else f'{vari}/{Z1}{op}{Z2}')
    term=term.replace('--','+').replace('+-','-')
    auswahl=random.sample(range(1, 5 if erg<10 else 10), 3)
    results=[erg,erg+(1 if bool(random.getrandbits(1)) else -1)*auswahl[0],erg+(1 if bool(random.getrandbits(1)) else -1)*auswahl[1],erg+(1 if bool(random.getrandbits(1)) else -1)*auswahl[2]]
    random.shuffle(results)
    frage=f'$${vari}={x}~\\rightarrow~{term.replace("*","·").replace("/",":")}=?$$' if formelSchoen else f'{vari}={x} → {term.replace("*","·").replace("/",":")}=?'
    return [frage]+results+[zeit,results.index(erg)+1]


def erzeugeKahootTermeZusammenfassen(zeit=10,anzVari=1,anzKoeffProVari=2,HS=False,rekursion=False):
    alleVaris=['x','y','z','a','b']
    random.shuffle(alleVaris)
    xStr=alleVaris[0:anzVari]+['']
    xes=[val for val in xStr for _ in range(anzKoeffProVari)]
    xesIndex={}
    for l in xStr:
        xesIndex[l]=[i for i, x in enumerate(xes) if x == l]
    ergTerm=''
    while len(ergTerm)<2:
        koeffs=[(1 if bool(random.getrandbits(1)) or HS else -1) * random.randint(0,10) for i in range((anzVari+1)*anzKoeffProVari)]
        print(koeffs)
        termList=[(f'{"+" if x>0 else ""}{x}{xes[i]}' if abs(x)>0 else '') for i,x in enumerate(koeffs)]
        print(termList)
        random.shuffle(termList)
        term=''.join(termList)
        term=term[1:] if term[0]=='+' else term
        ergKoeffs=[eval(''.join([f'{"+" if koeffs[x] >0 or koeffs[x]==0  else "" }{koeffs[x]}' for x in xesIndex[k]])) for k in list(xesIndex.keys())]
        print(ergKoeffs)
        ergTermList=[(f'{"+" if x>0 else ""}{x}{xStr[i]}' if abs(x)>0 else '') for i,x in enumerate(ergKoeffs)]
        ergTerm=''.join(ergTermList)
    ergTerm=ergTerm[1:] if ergTerm[0]=='+' else ergTerm
    results=[ergTerm]
#Erzeuge 3 Modifizierte Lösungen
#1. Buchstabe ändern
    ergTermModi=ergTerm
    for k in range(anzVari):
        ergTermModi=ergTermModi.replace(alleVaris[k],f'{alleVaris[-k-1]}{alleVaris[-k-1]}')
    for k in range(anzVari):
        ergTermModi=ergTermModi.replace(f'{alleVaris[-k-1]}{alleVaris[-k-1]}',alleVaris[-k-1])
    results.append(ergTermModi)
#2. Zahlen ändern.
    ergTermModi=''
    while len(ergTermModi)<2:
        ergKoeffsModi=[sum(x) for x in zip([(1 if bool(random.getrandbits(1)) else -1)*x for x in random.sample(range(0, 3), anzVari+1)],   ergKoeffs )]
        ergTermListModi=[(f'{"+" if x>0 or x==0 else ""}{x}{xStr[i]}' if abs(x)>0 else '') for i,x in enumerate(ergKoeffsModi)]
        ergTermModi=''.join(ergTermListModi)
    ergTermModi=ergTermModi[1:] if ergTermModi[0]=='+' else ergTermModi
    results.append(ergTermModi)
#3. Wenn die Koeffizienten unterschiedlich sind, verstausche sie. Ansonsten wie 2.
    results.append(ergTermModi)
    zaehler=0
    rekur=['']
    while len(results)>len(list(set(results))):
        if len(ergKoeffs)==len(list(set(ergKoeffs))):
            ergKoeffsModi=list(reversed(ergKoeffs))
        else:
            ergKoeffsModi=[sum(x) for x in zip([(1 if bool(random.getrandbits(1)) else -1)*x for x in random.sample(range(0, 3), anzVari+1)],   ergKoeffs )]
        ergTermListModi=[(f'{"+" if x>0 or x==0  else ""}{x}{xStr[i]}' if abs(x)>0 else '') for i,x in enumerate(ergKoeffsModi)]
        ergTermModi=''.join(ergTermListModi)
        ergTermModi=ergTermModi[1:] if ergTermModi[0]=='+' else ergTermModi
        results[-1]=ergTermModi
        zaehler=zaehler+1
#Ich nutze Rekursion, um die Whileschleife zu beenden. Leider entsteht ein Fehler, den ich so schnell nicht nachvollziehen konnte.
#Durch die Rekursion erhalte ich ein brauchbares Ergebnis.
        if zaehler>5:
            rekur=erzeugeKahootTermeZusammenfassen(zeit=zeit,anzVari=anzVari,anzKoeffProVari=anzKoeffProVari,HS=HS,rekursion=True)
            break
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == ergTerm])
    return [f'Fasse zusammen: {term}']+results+[zeit,ergIndizes] if not rekursion else rekur

def erzeugeKahootKlammerEinfachAufloesen(zeit=10):
    gegenPM={'+':'-','-':'+'}
    alleVaris=['x','y','z','a','b']
    var=random.choice(alleVaris)
    w=[random.randint(1,10) for x in range(3)]
    while w[1]==w[2]:
        w=[random.randint(1,10) for x in range(3)]
    vZ=[random.choice(['-','+']) for x in range(3)]
    vZd=['-' if x=='-' else '' for x in vZ]
    varPos=random.randint(0,1)
    vari=['','']
    vari[varPos]=var
    term=f'{vZd[0]}{w[0]}({vZd[1]}{w[1]}{vari[0]}{vZ[2]}{w[2]}{vari[1]})'   #Bsp: 5(3a+5)
    erg=f'{eval(f"{vZ[0]}{w[0]}*{vZ[1]}{w[1]}")}{vari[0]}{"+" if vZ[0]==vZ[2] else ""}{eval(f"{vZ[0]}{w[0]}*{vZ[2]}{w[2]}")}{vari[1]}'
    f1=f'{eval(f"{vZ[0]}{w[0]}*{vZ[1]}{w[1]}")}{vari[1]}{"+" if vZ[0]==vZ[2] else ""}{eval(f"{vZ[0]}{w[0]}*{vZ[2]}{w[2]}")}{vari[0]}'
    f2=f'{eval(f"{vZ[0]}{w[0]}*{vZ[1]}{w[1]}")}{vari[0]}{"+" if gegenPM[vZ[0]]==vZ[2] else ""}{eval(f"{gegenPM[vZ[0]]}{w[0]}*{vZ[2]}{w[2]}")}{vari[1]}'    
    alleVaris.remove(var)
    vari[varPos]=random.choice(alleVaris)    
    f3=f'{eval(f"{vZ[0]}{w[0]}*{vZ[1]}{w[1]}")}{vari[0]}{"+" if vZ[0]==vZ[2] else ""}{eval(f"{vZ[0]}{w[0]}*{vZ[2]}{w[2]}")}{vari[1]}'
    results=[erg,f1,f2,f3]
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == erg])    
    return [f'Löse die Klammer auf: {term}']+results+[zeit,ergIndizes]


def erzeugeKahootEinfachAusklammern(zeit=10):
    gegenPM={'+':'-','-':'+'}
    alleVaris=['x','y','z','a','b']
    var=random.choice(alleVaris)
    w=[random.randint(1,10) for x in range(3)]
    while ggt(w[1],w[2])>1:
        w=[random.randint(1,10) for x in range(3)]
    vZ=[random.choice(['-','+']) for x in range(3)]
    vZd=['-' if x=='-' else '' for x in vZ]
    varPos=random.randint(0,1)
    vari=['','']
    vari[varPos]=var
    term=f'{eval(f"{vZd[0]}{w[0]}*{vZd[1]}{w[1]}")}{vari[0]}{"+" if vZ[0]==vZ[2] else ""}{eval(f"{vZd[0]}{w[0]}*{vZd[2]}{w[2]}")}{vari[1]}'   #Bsp: 5*3a+5*1)
    erg=f'{vZd[0]}{w[0]}({vZd[1]}{w[1]}{vari[0]}{vZ[2]}{w[2]}{vari[1]})'
    f1=f'{vZd[0]}{w[0]}{var}({vZd[1]}{w[1]}{vZ[2]}{w[2]})'
    f2=f'{vZd[0]}{w[0]}({vZd[1]}{w[1]}{vari[0]}{gegenPM[vZ[2]]}{w[2]}{vari[1]})'
#    alleVaris.remove(var)
#    vari[varPos]=random.choice(alleVaris)
    f3=f'{vZd[0]}{w[0]+(1 if bool(random.getrandbits(1)) else -1)}({vZd[1]}{w[1]}{vari[0]}{vZ[2]}{w[2]}{vari[1]})'
    results=[erg,f1,f2,f3]
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == erg])  
    return [f'Klammer aus: {term}']+results+[zeit,ergIndizes]

def erzeugeKahootGleichungFehlendEintragen(zeit=10,formelSchoen=False):
    alleVaris=['x','y','z','a','b']
    op=random.choice(['+','-','·',':'])
    opGegen={'·':':',':':'·','+':'-','-':'+'}
    erg,zahl=random.randint(1,50),random.randint(1,50)
#    form=f'{zahl}{op}x = {erg}   |   {opGegen[op]} {zahl}' if not op=='/' else f'x{op}{zahl} = {erg}   |   {opGegen[op]} {zahl}'
#Einsetzen:
    einsetzen=['x',op,zahl,opGegen[op],zahl]
    e=list(einsetzen)
    auswahl=random.randint(0,len(einsetzen)-1)
    e[auswahl]='◻'
    gl=f'{f"{e[0]}{e[1]}{e[2]}" if not op=="·" else f"{e[2]}{e[1]}{e[0]}"} = {erg}  |  {e[3]}{e[4]}'
    if formelSchoen and op2==':': 
        gl=f'\\frac{{x}}{{{e[2]}}} = {erg} |  {e[3]}{e[4]}'
    if formelSchoen: 
        gl=gl.replace('◻','\\textcolor{red}{\square}').replace('|', '\\quad\\mid\\quad')
    del e[auswahl]
    results=[einsetzen[auswahl]]+random.sample(e,3)
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == einsetzen[auswahl]])
    frage=f'$$\\text{{Was fehlt: \\quad}}{gl}$$' if formelSchoen else f'Was fehlt: {gl}'
    return [frage]+results+[zeit,ergIndizes]

def erzeugeKahootGleichungFehlendEintragenKombi(zeit=10,formelSchoen=False):
    alleVaris=['x','y','z','a','b']
    op,op2=random.choice(['+','-']),random.choice([':','·'])
    opGegen={'·':':',':':'·','+':'-','-':'+'}
    erg,z1,z2=random.randint(1,50),random.randint(1,50),random.randint(1,50)
    while z1==z2 or z1==erg or z2==erg:
        erg,z1,z2=random.randint(1,50),random.randint(1,50),random.randint(1,50)
#    gleichung=f'{f"{z1}x" if op2=="·" f"x:{z1}{"} {op}{z2} = {erg}   |   {opGegen[op]}{z2}' 
#Einsetzen:
    einsetzen=[f'{op}{z2}',f'{opGegen[op]}{z2}']
    e=list(einsetzen)
    auswahl=random.randint(0,len(einsetzen)-1)
    e[auswahl]='◻'
    gl=f'{f"{z1}x" if op2=="·" else f"x:{z1}"} {e[0]} = {erg}   |  {e[1]}'
    if formelSchoen and op2==':': 
        gl=f'\\frac{{x}}{{{z1}}} {e[0]} = {erg} | {e[1]}'
    if formelSchoen: 
        gl=gl.replace('◻','\\textcolor{red}{\square}').replace('|', '\\quad\\mid\\quad')
    del e[auswahl]
    results=[einsetzen[auswahl]]+[e[0]]+random.sample([f"{op}{z1}",f"{opGegen[op]}{z1}",f"{op}{erg}",f"{opGegen[op]}{erg}",f"{op2}{z1}",f"{opGegen[op2]}{z1}",f"{op2}{z2}",f"{opGegen[op2]}{z2}",f"{op2}{erg}",f"{opGegen[op2]}{erg}"],2)
    random.shuffle(results)
    ergIndizes=','.join([str(i+1) for i, x in enumerate(results) if x == einsetzen[auswahl]])
    frage=f'$$\\text{{Was fehlt: \\quad}}{gl}$$' if formelSchoen else f'Was fehlt: {gl}'
    return [frage]+results+[zeit,ergIndizes]
