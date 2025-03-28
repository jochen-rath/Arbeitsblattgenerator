#!/usr/bin/env python
# coding: utf8
import random


#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Berechnung von Termen und Gleichungen


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def variabelErsetzen(mitText=True):
    vari=random.choice(['a','b','x','z'])
    wert=random.choice([1,-1])*random.randint(1,12)
    term='3+4'
    while not vari in term:
        term=erzeugeTerm(variablen=vari, anzahl=2, variMaxAnzProUnterterm=1)
    if mitText:
#       afg=F'Setze für die Variabel {vari} den Wert {wert} ein und berechne die Lösung für y:'
        afg=['\\pbox{\\linewidth}{']
        afg.append(F'Setze für die Variabel {vari} den Wert {wert} ein und berechne den Wert des Terms:\\\\')
        afg.append(F'${term}$'.replace("*"," \\cdot ").replace('XX','\\'))
        afg.append('}')
    else:
        afg = F' ${vari}={wert}~ XXrightarrow ~ {term}=?$'.replace("*"," \\cdot ").replace('XX','\\')
#        afg=['$\\begin{aligned}']
#        afg=afg+[F'y=&{term}'.replace("*"," \\cdot ")+'\\\\']
#        afg=afg+[F' {vari}=&{wert}~ XXrightarrow ~ y=?'.replace("*"," \\cdot ").replace('XX','\\')]
#        afg=afg+[F' {vari}=&{wert}~ XXrightarrow ~ {term}=?'.replace("*"," \\cdot ").replace('XX','\\')]
#        afg=afg+['\\end{aligned}$']
    lsg=['$\\begin{aligned}']
    lsg=lsg+[F"XXtextcolor{{red}}{{{vari}={strNW(wert,True)}}} & XXrightarrow".replace('XX','\\')+"\\\\"]
    if False:
        lsg=lsg+[F"y&={term}".replace('*',' \\cdot ').replace(vari,'\\textcolor{red}{'+vari+'}')+"\\\\"]
        lsg=lsg+[F"y&={term}".replace(vari,'\\textcolor{red}{'+F"{'(' if wert<0 else ''}{strNW(wert,True)}{')' if wert<0 else ''}"+'}').replace('*',' \\cdot ')+"\\\\"]
        lsg=lsg+[F"y&={eval(term.replace(vari,str(wert)))}"+"\\\\"]
    erg=F"{'(' if wert<0 else ''}{strNW(wert,True)}{')' if wert<0 else ''}"
    lsg=lsg+[F"{term}=&{term.replace(vari,'XXtextcolor{red}{'+erg+'}')}={eval(term.replace(vari,str(wert)))}".replace('*',' \\cdot ').replace('XX','\\')+"\\\\"]
    lsg=lsg+['\\end{aligned}$']
    return [afg,lsg,[]]

def findenEinenTerm(mitText=True):
    vari='x'
    wert=random.randint(1,12)
    term1=F'{vari}{"+" if random.randint(0,1) else "-"}{strNW(wert)}'
    term2=F'{"" if random.randint(0,1) else "-"}{vari} * {strNW(wert)}'
    term=random.choice([term1,term2])
    erg=eval(term.replace(vari,str(wert)))
    afg=F'Bestimme ein Term, wenn {vari}={strNW(wert)} und das Ergebnis gleich {strNW(erg)} ist.'
    lsg='Ein mögliches Ergebnis:'
    lsg=lsg+F'XX[ {vari}={strNW(wert)} ~~ XXrightarrow {term.replace("*","XXcdot")}={erg} XX]'.replace('XX','\\')
    return [afg,lsg,[]]

def ersetzePlatzhalterMitSymbolen(T):
#Achtung, bestimmte Symbole muss ich durch Platzhalter ersetzen. So hat 'I' für sympy eine bedeutung die ich nicht kenne und R=U/I kann sympy nicht lösen
#Auch Griechische Symbole gehen nicht.
# 'Y' = 'I'
# 'X' = '\rho'
    result = re.findall("[0-9]\*[a-z]", T)
#Entferne Mal Zeichen zwischen Zahl und Buchstabe:
    for x in result:
        T=T.replace(x, x.replace('*', ''))
    result = re.findall("[a-z]\*[a-z]", T)
#Entferne Mal Zeichen zwischen Zahl und Buchstabe:
    for x in result:
        T=T.replace(x, x.replace('*', ''))
    T=T.replace('**','^').replace('*','\\cdot ').replace('/',':')
    T=T.replace('XI','I')
    T=T.replace('Xrho','\\rho')
    T=T.replace('XVm','G_{Vm}')
    T=T.replace('XVp','G_{Vp}')
    T=T.replace('§§','\\')
    T=T.replace('variStr','')
    T=T.replace('vari','')
    return T

def erzeugeEinfacheFormelnUmformen(formel='',gesucht='',anzSpalten=[2,2]):
#Diese Funktion erzeugt eine Aufgabe, bei der eine Formel nach einem vorgegebenen Wert umgeformt werden muss. Es gilt:
#
#      [afg,lsg,G]=erzeugeEinfacheFormelnUmformen(formel='',gesucht='')
#
# Wenn formel='' oder gesucht='' wird eine Formel bzw. der gesuchte Wert zufällig gewählt
    Formeln={'Prozentgleichung':['p/100=W/G',['W','G','p']],'Zinsrechnungsgleichung':['p/100=Z/K',['Z','K','p']],'Geschwindigkeitsgleichung':['v=s/t',['s','t']],
             'Rechteck Flaechengleichung':['A=a*b',['a','b']],'Rechteck Umfangsgleichung':['U=2*a+2*b',['a','b']],'Dreieck Umfangsgleichung':['U=a+b+c',['a','b','c']],
             'Dreieck Flaechengleichung':['A=g*h/2',['g','h']], 'Widerstandsgleichung':['R=U/XI',['U','XI']],'Gleichung der Dichte':['Xrho=m/V',['m','V']],
             'Beschleunigungsgleichung':['a=v/t',['v','t']],'Vermehrter Grundwertgleichung':['q/100=XVp/G',['XVp','q','G']],'Vermindeter Grundwertgleichung':['q/100=XVm/G',['XVm','q','G']],
             'Kraft- und Beschleunigungsgleichung':['F=m*a','m','a'],'Monatzinsgleichung':['Z=K*p/100*m/12',['K','p','m']],'Tageszinsgleichung':['Z=K*p/100*t/360',['K','p','t']]}
    formel=formel if len(formel)>0 else random.choice(list(Formeln.keys()))
    G=Formeln[formel][0]
    gesucht=gesucht if len(gesucht)>0 else random.choice(Formeln[formel][1])
    L,R=G.split('=')
    afg='Forme die '+formel+' $'+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(L))+' ='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'$ nach $'+ersetzePlatzhalterMitSymbolen(gesucht)+'$ um.'    
    groesse='{6 cm}{!}' if anzSpalten[1] == 2 else '{!}{!}'
    lsg=[f'\\resizebox{groesse}{{']+formeEinfacheFormelNachVorgabenUm(G=G,gesucht=gesucht)+['}']
    return [afg,lsg,G]


def untertermErzeugen(variListe,variMaxAnzProUnterterm=3,maxMulti=5,variMinAnzProUnterterm=0,mitKommazahl=False):
#Diese Funktion erzeugt einen Unterterm, welcher dann mit weiteren Untertermen mit plus und Minus zu einem Term zusammengesetzt werden kann.
    n=random.randint(1,maxMulti) + (random.randint(0,10)/10 if mitKommazahl else 0)
    vari=[random.choice(variListe.split(' ')) for i in range(random.randint(variMinAnzProUnterterm,variMaxAnzProUnterterm))]
    if len(vari)>0:
        return '*'.join(([str(n)] if n>1 else [])+vari)
    else:
        return str(n)

def klammerTermErzeugen(variListe='x',anzInKlammer=2,variMaxAnzProUnterterm=3,maxMulti=5,variVorKlammer=False,variVorKlammerAnders=False,zwingendMitVari=True):
#Diese Funktion erzeugt einen Unterterm, welcher dann mit weiteren Untertermen mit plus und Minus zu einem Term zusammengesetzt werden.
    n=random.randint(1,maxMulti)
    variKlammer=''
    if variVorKlammer:
        variKlammer='*'+random.choice(variListe.split(' '))
    if variVorKlammer and variVorKlammerAnders and len(variListe.split(' '))>1:
        varis=variListe.split(' ')
        vari=random.choice(varis)
        varis.remove(vari)
        variKlammer='*'+vari
        variListe=' '.join(varis)
    return str(n)+variKlammer+'*('+erzeugeTerm(variListe,anzahl=anzInKlammer,variMaxAnzProUnterterm=variMaxAnzProUnterterm,maxMulti=5,zwingendMitVari=zwingendMitVari)+')'


def erzeugeTerm(variablen='x y z',anzahl=3,variMaxAnzProUnterterm=3,maxMulti=5,mitKlammer=False,variVorKlammer=False,mitKommazahl=False,zwingendMitVari=False):
#Diese Funktion erzeugt einen Term, in der Unterterme mit '+' und '-' verbindet.
#Aufruf:
#    term=erzeugeTerm(variablen,anzahl,variMaxAnzProUnterterm,maxMulti,mitKlammer,variVorKlammer)
#
#         variablen='x y z' usw.
#         anzahl=Anzahl an Untertermen.
#         variMaxAnzProUnterterm=MAxial Anzahl an Variablen im Unterterm. Bei 2: 'x*x' geht aber 'x*x*x*x' nicht
#         maxMulti=Mit welchen Faktor die Variabel Maximal mal genommen wird.

    anzahl=(anzahl-1) if mitKlammer else anzahl
    unterterme=[untertermErzeugen(variListe=variablen,variMaxAnzProUnterterm=variMaxAnzProUnterterm,maxMulti=maxMulti,mitKommazahl=mitKommazahl) for i in range(anzahl)]
    if mitKlammer:
        unterterme.insert(random.randrange(len(unterterme)+1),klammerTermErzeugen(variListe=variablen,anzInKlammer=2,variMaxAnzProUnterterm=variMaxAnzProUnterterm,maxMulti=maxMulti,variVorKlammer=variVorKlammer))
    term=''
    for t in unterterme[:-1]:
        term=term+t+random.choice([' + ',' - '])
    term=term+unterterme[-1]
    if zwingendMitVari:
        if len([1 for x in variablen.split(' ') if x in term])==0:
            term=erzeugeTerm(variablen=variablen,anzahl=anzahl,variMaxAnzProUnterterm=variMaxAnzProUnterterm,maxMulti=maxMulti,mitKlammer=mitKlammer,variVorKlammer=variVorKlammer,mitKommazahl=mitKommazahl,zwingendMitVari=zwingendMitVari)
    return term


def erzeugeTermAusklammernAufgabe(variablen='a b x y z',mitText=True):
    vorzVorKl='-' if random.getrandbits(1) else '+'
    term=klammerTermErzeugen(variListe=variablen,variMaxAnzProUnterterm=1,variVorKlammer=True,variVorKlammerAnders=True)
    inKlammer=term.split('(', 1)[1].split(')')[0]
    vorKlammer=term.split('(')[0][:-1]
    vorzeichen='-' if inKlammer[0]=='-' else ''
    inKlammer=inKlammer[1:] if inKlammer[0]=='-' else inKlammer
    op='+' if '+' in inKlammer else '-'
    wertKl1,wertKl2=inKlammer.split(op)
    afg=F'{"Löse die Klammer auf:$" if mitText else ""}${"-" if vorzVorKl=="-" else ""}{term}=?${"$" if mitText else ""}'
    lsg1=F'§§textcolor{{red}}{{ {"-" if vorzVorKl=="-" else ""}{vorKlammer} }}*({inKlammer})'
    lsg2=F'§§textcolor{{red}}{{ {"-" if vorzVorKl=="-" else ""}{vorKlammer} }}*{"(" if wertKl1[0]=="-" else ""}{vorzeichen}{wertKl1}{")" if wertKl1[0]=="-" else ""}{op}§§textcolor{{red}}{{ {"(" if vorzVorKl=="-" else ""}{"-" if vorzVorKl=="-" else ""}{vorKlammer}{")" if vorzVorKl=="-" else ""} }}*{wertKl2}'
    lsg3=F'{sympy.sympify(F"{vorzeichen}{vorzVorKl}{vorKlammer}*{wertKl1}")}{"-" if eval(F"{op}1{vorzVorKl}1")==0 else "+"}{sympy.sympify(F"{vorKlammer}*{wertKl2}")}'
    lsg=['$\\begin{aligned}']
    lsg.append(F'{lsg1}=&{lsg2} \\\\')
    lsg.append(F'=&{lsg3.replace("*","")} \\\\')
    lsg.append(('\\end{aligned}$'))
    return [[ersetzePlatzhalterMitSymbolen(afg)],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeZweiSummenAusmulti(nMax=2,nurEinBuchstabe=False,mitText=True):
    farben=tikzFarben[1:]
    variablen=['a','b','c','d','x','y','z','']
    if nurEinBuchstabe:
        auswahl = random.choice(variablen[0:-1])
        terme = [F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}',F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}*{auswahl}']
        terme2 = [F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}',F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}*{auswahl}']
        random.shuffle(terme)
        random.shuffle(terme2)
    else:
        auswahl=random.sample(variablen,random.randint(2,nMax))
        auswahl2=random.sample(variablen,random.randint(2,nMax))
        terme=[F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}{F"*" if len(x)>0 else ""}{x}' for x in auswahl]
        terme2=[F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}{F"*" if len(x)>0 else ""}{x}' for x in auswahl2]
    termeFarben=[F'§§textcolor{{{farben[i]}}}{{{x if i>0 else (x if x[0]=="-" else x[1:])}}}' for i,x in enumerate(terme)]
    terme2Farben=[F'§§textcolor{{{farben[len(terme)+j]}}}{{{y if j>0 else (y if y[0]=="-" else y[1:])}}}' for j,y in enumerate(terme2)]
#Entferne das erste Plus, falls vorhanden. beim Term in den Klammer
#    lsg1=[F'{x[0] if x[0]=="+" or x[0]=="-" else ""}{vorKl}*{x[1:] if (x[0]=="+" or x[0]=="-") else x}' for x in terme]
    lsg1=[F'{x}*({y})' for i,x in enumerate(terme)  for j,y in enumerate(terme2)]
    lsg1Farben=[F'§§textcolor{{{farben[i]}}}{{ {x if i>0 or j>0 else (x if x[0]=="-" else x[1:])}}}*(§§textcolor{{{farben[len(terme)+j]}}}{{ {y}}})' for i,x in enumerate(terme) for j,y in enumerate(terme2) ]
    lsg2=[str(sympy.sympify(x)) for x in lsg1]
#Füge ein plus fürs Join hinzu
    lsg2=[x if x[0]=='-' else F'+{x}' for x in lsg2]
    lsg3=str(sympy.sympify("".join(lsg2)))
    terme[0] = terme[0][1:] if terme[0][0] == '+' else terme[0]
    terme2[0] = terme2[0][1:] if terme2[0][0] == '+' else terme2[0]
    afg = 'Multipliziere die Klammern aus:'
    afg=(afg if mitText else "")+ F'${"$" if mitText else ""}({"".join(terme)})*({"".join(terme2)}){"$" if mitText else ""}$'
    lsg = ['$\\begin{aligned}']
    lsg.append(F'(&{"".join(termeFarben)})*({"".join(terme2Farben)}) \\\\')
    lsg.append(F'=&{"".join(lsg1Farben)} \\\\')
    lsg2[0]=lsg2[0][1:] if lsg2[0][0]=='+' else lsg2[0]
    lsg.append(F'=&{"".join(lsg2)} \\\\')
    if nurEinBuchstabe:
        lsg.append(F'=&{lsg3} \\\\')
    lsg.append(('\\end{aligned}$'))
    return [[ersetzePlatzhalterMitSymbolen(afg)],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]


def erzeugeSummenAusmultiAuskl(n=2,ausKlammern=False,mitText=True):
    variablen=['a','b','c','d','x','y','z','']
    auswahl=random.sample(variablen,n)
    vorKlAus=random.choice(variablen)
    vorKl=F'{"" if ausKlammern else ("" if random.getrandbits(1) else "-")}{random.randint(2,9)}{F"*" if len(vorKlAus)>0 else  ""}{vorKlAus}'
    #terme=[F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}{F"*{x}" if random.randint(0,3)<3 else ""}' for x in auswahl]
    faktoren=random.sample([1,2,3,5,7,9,11],n) if ausKlammern else [random.randint(1,9) for x in auswahl]
    terme=[F'{"+" if random.getrandbits(1) else "-"}{faktoren[i]}{F"*" if len(x)>0 else ""}{x}' for i,x in enumerate(auswahl)]
#Entferne das erste Plus, falls vorhanden. beim Term in der Klammer
    terme[0]=terme[0][1:] if terme[0][0]=='+' else terme[0]
    klammer=(F'{vorKl}*({"".join(terme)})')
    afg='Multipliziere die Klammer aus:'
    afg=[(afg if mitText else "")+ F'${"$" if mitText else ""}{klammer}{"$" if mitText else ""}$']
    vorKl=F'({vorKl})' if vorKl[0]=='-' else vorKl
#Schreibe die Lösung auf, indem der Term vor der Klammer zwischen + oder -  und dem dazugehörigen Term geschrieben wird.
#Achtung, der erste Term in der Klammer hat eventuell kein +
    lsgRot=[F'{x[0] if x[0]=="+" or x[0]=="-" else ""}§§textcolor{{red}}{{{vorKl}}}*{x[1:] if (x[0]=="+" or x[0]=="-") else x}' for x in terme]
    lsg1=[F'{x[0] if x[0]=="+" or x[0]=="-" else ""}{vorKl}*{x[1:] if (x[0]=="+" or x[0]=="-") else x}' for x in terme]
#    lsg1=[F'{vorKl}*{F"({x})" if x[0] == "-" else x[1:]}' for x in terme]
    lsg2=[str(sympy.sympify(x)) for x in lsg1]
#Füge ein plus fürs Join hinzu
    lsg2=[x if x[0]=='-' else F'+{x}' for x in lsg2]
    lsg3=str(sympy.sympify("".join(lsg2)))
    lsg = ['$\\begin{aligned}']
    lsg.append(F'{vorKl}*&({"".join(terme)}) \\\\')
    lsg.append(F'=&{"".join(lsgRot)} \\\\')
    lsg2[0]=lsg2[0][1:] if lsg2[0][0]=='+' else lsg2[0]
    lsg.append(F'=&{"".join(lsg2)} \\\\')
    lsg.append(F'=&{lsg3} \\\\')
    lsg.append(('\\end{aligned}$'))
    if ausKlammern:
        afg='Klammer soweit wie möglich aus:\\\\'
        afg=['\\pbox{\\linewidth}{']+[(afg if mitText else "")]+ [F'${"".join(lsg2)}$']+['}']
        lsg = ['$\\begin{aligned}']
        lsg.append(F'{lsg2[0]}&{"".join(lsg2[1:])} \\\\')
        lsg.append(F'=&{"".join(lsgRot)} \\\\')
        klammer=(F'§§textcolor{{red}}{{{vorKl}}}*({"".join(terme)})')
        lsg.append(F'=&{klammer} \\\\')
        lsg.append(('\\end{aligned}$'))
    return [[ersetzePlatzhalterMitSymbolen(x)  for x in afg],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeKlammerAufloesenVereinfachen(mitText=True):
    variablen=['a','b','c','d','x','y','z']
    auswahl=random.choice(variablen)
    vorKl=F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}'
    einzelTerm=F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}{F"*{auswahl}" if random.randint(0,3)<3 else ""}'
    inKlammer=[F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}*{auswahl}',F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}']
    random.shuffle(inKlammer)
#Entferne das erste Plus, falls vorhanden. beim Term in der Klammer
    inKlammer[0]=inKlammer[0][1:] if inKlammer[0][0]=='+' else inKlammer[0]
    klammer=(F'{vorKl}*({"".join(inKlammer)})')
    termVorne=True if random.getrandbits(1) else False
    afg='Multipliziere die Klammer aus und vereinfache:'
    gesTerm= F"{einzelTerm}{klammer}" if termVorne else F"{klammer}{einzelTerm}"
    afg=(afg if mitText else "")+ F'${"$" if mitText else ""}{gesTerm[1:] if gesTerm[0]=="+" else gesTerm}{"$" if mitText else ""}$'
    vorKl=F'({vorKl})' if vorKl[0]=='-' else vorKl[1:]
#Schreibe die Lösung auf, indem der Term vor der Klammer zwischen + oder -  und dem dazugehörigen Term geschrieben wird.
#Achtung, der erste Term in der Klammer hat eventuell kein +
    lsg1=[einzelTerm] +[F'{x[0] if x[0]=="+" or x[0]=="-" else "+"}{x[1:]  if (x[0]=="+" or x[0]=="-") else x}*{vorKl}' for x in inKlammer] if termVorne else [F'{x}*{vorKl}' for x in inKlammer]+[einzelTerm]
    lsgRot=[einzelTerm] +[F'{x[0] if x[0]=="+" or x[0]=="-" else "+"}{x[1:]  if (x[0]=="+" or x[0]=="-") else x}*§§textcolor{{red}}{{{vorKl}}}' for x in inKlammer] if termVorne else [F'{x}*{vorKl}' for x in inKlammer]+[einzelTerm]
    # Entferne das erste Plus, falls vorhanden. beim Term in der Klammer
    lsgRot[0]=lsgRot[0][1:] if lsgRot[0][0]=='+' else lsgRot[0]
    lsg2=[str(sympy.sympify(x)) for x in lsg1]
    lsg2=[F'{"" if x[0]=="-" else "+"}{x}' for x in lsg2]
    lsg3=str(sympy.sympify(''.join(lsg2)))
#Füge ein plus fürs Join hinzu
    lsg = ['$\\begin{aligned}']
#Entferne das erste Plus, falls vorhanden. beim Term in der Klammer
    klammer=(klammer[1:] if klammer[0]=="+" else klammer) if not termVorne else klammer
    klammerMitUndZeichen=F'{klammer.split("(")[0]}(&{klammer.split("(")[1]}'
    lsg.append( F"{einzelTerm[1:] if einzelTerm[0]=='+' else einzelTerm}&{klammer} \\\\" if termVorne else F"{klammerMitUndZeichen}{einzelTerm}  \\\\")
    lsg.append(F'=&{"".join(lsgRot)} \\\\')
    lsg2[0]=lsg2[0][1:] if lsg2[0][0]=='+' else lsg2[0]
    lsg.append(F'=&{"".join(lsg2)} \\\\')
    lsg.append(F'=&{"".join(lsg3)} \\\\')
    lsg.append(('\\end{aligned}$'))
    return [[ersetzePlatzhalterMitSymbolen(afg)],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeTermAufgaben(variablen='x y z',anzahl=3,variMaxAnzProUnterterm=3,mitKlammer=False,mitText=True):
#Diese Funktion erezeugt einen Term, der umgeschrieben und vereinfacht werden soll. Ausgegeben wird auch eine Lösung:
#
#           [afg,lsg,term]=erzeugeTermAufgaben(variablen='x y z',anzahl=3)
#
#Eingabe: variablen: Mit Leerzeichen getrennter String mit den zu verwendenen Variablen
#         anzahl: Wieviel +,- getrennte Unterterme soll der Term enthalten?
#
#Ausgabe: afg: Aufgabe
#         lsg: Lösung
#         term: term ohne Vorwort
    term=erzeugeTerm(variablen=variablen,anzahl=anzahl,variMaxAnzProUnterterm=variMaxAnzProUnterterm,mitKlammer=mitKlammer)
    afg=F'{"Vereinfache:$" if mitText else ""}${term}=?${"$" if mitText else ""}'
    lsg=sympy.sympify(term)
#    lsg=['$'+term.replace('*','\\cdot ')+'='+str(lsg).replace('**','^').replace('*','\\cdot ')+'$']
#    lsg=['$'+term.replace('*','\\cdot ')+'='+str(lsg).replace('**','^').replace('*','')+'$']
    lsg=[F'${term}={str(lsg)}$']
    return [[ersetzePlatzhalterMitSymbolen(afg)],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeSehrEinfacheGleichungen(variabel='x',mitText=True,nurPlusMinus=False,PlusMinusVariImTerm2=False,PlusMinusVariRechtsImTerm1=False,nurMalGeteilt=False,MalUndPlusMinus=False,MalUndPlusMinusAufgeteilt=False,einfKlammer=False):
    G=F'3*{variabel}-5=10'
    if nurPlusMinus:
        G = F'{variabel}{random.choice(["+", "-"])}{random.randint(1, 50)} = {random.randint(1, 50)}'
    if PlusMinusVariImTerm2:
        G = F'{random.randint(1, 50)}={variabel}{random.choice(["+", "-"])}{random.randint(1, 50)}'
    if nurMalGeteilt:
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        G = F'{a}*{variabel}={a * b}' if bool(random.getrandbits(1)) else F'{variabel}/{a}={b}'
    if MalUndPlusMinus:
        x = random.randint(2, 12)
        b = random.randint(2, 20)
        a = random.randint(2, 10)
        c = a*x-b
        G=F"{a}*{variabel}-{b}={c}"
    if MalUndPlusMinusAufgeteilt:
        x = random.randint(2, 12)
        b = random.randint(2, 20)
        a = random.randint(2, 10)
        c = a*x-b
        op1=random.choice(['+','-'])
        op2=random.choice(['+','-'])
        #a=a1 +/- a2
        a2=random.randint(1,a-1)
        a1=eval(F'{a}{ {"+":"-","-":"+"}[op1] }{a2}')
        # b=b1 +/- b2
        b2=random.randint(1,b-1)
        b1=eval(F'{b}{ {"+":"-","-":"+"}[op2] }{b2}')
        werte=[F'+{a1}*{variabel}',F'{op1}{a2}*{variabel}',F'-{b1}',F'{ {"+":"-","-":"+"}[op2] }{b2}']
        random.shuffle(werte)
        G=F'{"".join([werte[0].replace("+","")]+werte[1:])}={c}'
    if PlusMinusVariRechtsImTerm1:
        G = F'{random.randint(1, 50)}{random.choice(["+", "-"])}{variabel}={random.randint(1, 50)}'
    if einfKlammer:
        variabel=random.choice(['a','b','x','y','z'])
        werte={}
        op=random.choice(['+','-'])
        for i in variabel,'h','i','j':
            werte[i]=random.randint(2,8)
        klammer=F"{werte['h']}*({werte['i']}*{variabel}{op}{werte['j']})"
        G= F'{klammer} = {eval(klammer.replace(variabel,str(werte[variabel])))}'
    afg = F'{"Berechne die Variable $" if mitText else ""}${G.replace("**", "^").replace("*", "&&cdot ").replace("/", ":")}${"$" if mitText else ""}'.replace("&&","\\")
    lsg = loeseGleichungEinfachMitEinerVariabel(G=G, variable=variabel, mitProbe=True)
    return [afg, lsg, G]


def erzeugeGleichungMitSummenklammernAusmulti(mitText=True,ohneKomma=False,ergUnter10=False):
    lsg='Error'
    while lsg=='Error':
        gesTerm='x+1'
        while not '**2' in str(sympy.simplify(gesTerm)):
            variablen=['a','b','c','d','x','y','z','']
            auswahl = random.choice(variablen[0:-1])
            terme = [F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}',F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}*{auswahl}']
            terme2 = [F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}',F'{"+" if random.getrandbits(1) else "-"}{random.randint(1,9)}*{auswahl}']
            random.shuffle(terme)
            random.shuffle(terme2)
            terme[0] = terme[0][1:] if terme[0][0] == '+' else terme[0]
            terme2[0] = terme2[0][1:] if terme2[0][0] == '+' else terme2[0]
            gesTerm=F'({"".join(terme)})*({"".join(terme2)})'
        xQuadratFaktor=str(sympy.simplify(gesTerm)).split('**')[0]
        termeR=[F'{xQuadratFaktor}**2',F'{"+" if random.getrandbits(1) else "-"}{random.randint(0,12)}*{auswahl}',F'{"+" if random.getrandbits(1) else "-"}{random.randint(0,12)}']
        termeR=[str(sympy.simplify(x)) for x in termeR]
        random.shuffle(termeR)
        while '0' in termeR: termeR.remove('0')
        termeR=[x if x[0]=='+' or x[0]=='-' else F'+{x}' for x in termeR]
        G=F'({"".join(terme)})*({"".join(terme2)})={"".join(termeR)}'
        afg=F'{"Berechne die Variable $" if mitText else ""}${G.replace("/", ":")}${"$" if mitText else ""}'.replace("&&","\\")
        lsg = loeseGleichungEinfachMitEinerVariabel(G=G, variable=auswahl, mitProbe=True)
        if (not lsg=='Error') and ohneKomma:
            erg=loeseGleichungEinfachMitEinerVariabel(G=G,variable=auswahl,mitProbe=True,latexAusgabe=False)
            if ('.' in erg) or ('/' in erg) or int(erg.split('=')[1])==0:
                lsg='Error'
            if ergUnter10:
                if abs(eval(erg.split('=')[1]))>=10:
                    lsg = 'Error'
    return [[ersetzePlatzhalterMitSymbolen(afg)],[ersetzePlatzhalterMitSymbolen(x) for x in lsg],[]]

def erzeugeEinfacheGleichung(variabel='x',mitKlammer=False,mitQuadrat=False,ohneKomma=False,mitText=True):
#Diese Funktion erzeugt eine Gleichung mit einem x ohne Potenz.
#
#Aufruf 
#           [afg,lsg,G]=erzeugeEinfacheGleichung(variabel)
#
#   variabel= Variabel der Gleichung, x oder y oder a usw.
    lsg='Error'
    while lsg=='Error':
        G=''
        while not (variabel in G):
            if mitKlammer:
                t1Klammer=bool(random.getrandbits(1))
                t2Klammer=True if not t1Klammer else (bool(random.getrandbits(1)))
            else:
                t1Klammer,t2Klammer=False,False
            term1=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=12,mitKlammer=t1Klammer)
            term2=erzeugeTerm(variablen=variabel,anzahl=2,variMaxAnzProUnterterm=1,maxMulti=12,mitKlammer=t2Klammer)
            if mitQuadrat:
                enthaeltNichtGenauEinePotenz=True
                while enthaeltNichtGenauEinePotenz:
                #Erzeuge einen Term mit einer Klammer und x davor
                    klammerTerm=klammerTermErzeugen(variListe=variabel,anzInKlammer=2,variMaxAnzProUnterterm=1,maxMulti=12,variVorKlammer=True)
                #Multipliziere die Klammer aus und extrahiere die Potenz.
                    potenzTerm=[x for x in spliteSeiteAddSub(klammernEntfernen(klammerTerm)) if '**' in x]
                #Addiere die Potenz auf die Linke und Rechte seite.
                    if len(potenzTerm)==1:
                #Wähle zufällig den 1. oder 2. Term.
                        if bool(random.getrandbits(1)):
                            term1=term1+('+' if not (klammerTerm[0]=='+' or klammerTerm[0]=='-')  else '')+klammerTerm
                            term2=term2+('+' if not (potenzTerm[0][0]=='+' or potenzTerm[0][0]=='-') else '')+potenzTerm[0]
                        else:
                            term2=term2+('+' if not (klammerTerm[0]=='+' or klammerTerm[0]=='-')  else '')+klammerTerm
                            term1=term1+('+' if not (potenzTerm[0][0]=='+' or potenzTerm[0][0]=='-') else '')+potenzTerm[0]
                        enthaeltNichtGenauEinePotenz=False
            G=term1+'='+term2
        afg= F'{"Berechne die Variable $" if mitText else ""}${ersetzePlatzhalterMitSymbolen(G)}${"$" if mitText else ""}'.replace("&&","\\")
#        print(F'G: {G}')
        lsg=loeseGleichungEinfachMitEinerVariabel(G=G,variable=variabel,mitProbe=True)
        if (not lsg=='Error') and ohneKomma:
            erg=loeseGleichungEinfachMitEinerVariabel(G=G,variable=variabel,mitProbe=True,latexAusgabe=False)
#            print(F'erg: {erg}')
            if ('.' in erg) or ('/' in erg) or int(erg.split('=')[1])==0:
                lsg='Error'
    return [[afg],[x for x in lsg],[]]
    


def erzeugeFlaechenFormelUmformenUndAnwenden(auswahl='',mitText=True):
    if len(auswahl)==0:
        auswahl=random.choice(['Rechteck','Parallelogramm','RechteckUmfang','ParallelogrammUmfang','Dreieck'])
    if auswahl=='Rechteck':
        gesucht=random.choice(['a','b'])
        gegeben='a' if gesucht=='b' else 'b'
        a=random.randint(10,100)/10
        b=random.randint(10,100)/10
        G='A=a*b'
        afg=F'Stelle die Flächenformel des Rechtecks nach der fehlenden Seite um und berechne diese und den Umfang für'
        afg=(afg if mitText else 'Rechteck: ')+F' $A={strNW(a*b)}~cm^2$ und ${gegeben}={strNW(eval(gegeben))}~cm$.'
        lsg = formeEinfacheFormelNachVorgabenUm(G=G, gesucht=gesucht)
#Schreibe gegeben, gesucht.
        lsg.insert(4,F'geg.: A &={strNW(a*b)}~cm^2& & \\\\')
        lsg.insert(5,F'  {gegeben} &={strNW(eval(gegeben))}~cm& & \\\\')
        lsg.insert(6,F'ges.: {gesucht} &=?~cm& & \\\\')
        lsg.insert(7,F'u &=?~cm& & \\\\')
        lsg.insert(8,F'& & & \\\\')
#Setze die Werte ein.
#        lsgSplit=lsg[-3].split('&')
#        einsetzen=lsgSplit[1].replace('{A}',F'{{{strNW(a*b)}}}').replace(F'{{{gegeben}}}',F'{{{strNW(eval(gegeben))}}}')
#        einsetzen=F'{einsetzen}={strNW(eval(gesucht))}~cm'
#        lsgSplit[1]=F'{lsgSplit[1]}{einsetzen}'
#        lsg[-3]='&'.join(lsgSplit)+'\\\\'
        lsg[-3]=lsg[-3]+'\\\\'
#\makebox[breite] oder \makebox(breite,hoehe). Das Minus schiebt die Box unter den Bruch
        lsg.insert(-3,'\\makebox(0pt,-0.25cm)[l]{\\uline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
        lsg.insert(-2, F'{gesucht}&=\\frac{{{strNW(a*b)}}}{{{strNW(eval(gegeben))}}}& & \\\\')
        lsg.insert(-2, F'&={strNW(eval(gesucht))}~cm& & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
#Berechne den Umfang.
        lsg.insert(-2,F'u&=2a+2b & & \\\\')
        lsg.insert(-2,F'&=2\\cdot{strNW(a)}+2\\cdot{strNW(b)}& & \\\\')
        lsg.insert(-2,F'u&={strNW(2*a+2*b)}~cm   & & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
    if auswahl=='RechteckUmfang' or auswahl=='ParallelogrammUmfang':
        R=True if 'Rechteck' in auswahl else False
        typ="Rechtecks" if R else "Parallelogramm"
        indP1=0 if R else 1
        gesucht=random.choice(['a','b'])
        gegeben='a' if gesucht=='b' else 'b'
        a=random.randint(10,100)/10
        b=random.randint(10,100)/10
        h=random.randint(10,(a if gesucht=='a' else b)*10)/10
        G='u=2*a+2*b'
        afg=F'Stelle die Umfangsformel des {typ} nach der fehlenden Seite um und berechne diese und den Flächeninhalt für'
        afg=(afg if mitText else F'{typ}: ')+F' $u={strNW(2*a+2*b)}~cm${" und" if R else ","} ${gegeben}={strNW(eval(gegeben))}~cm${"" if R else F" und $h_{gesucht}={strNW(h)} cm$"}.'
        lsg = formeEinfacheFormelNachVorgabenUm(G=G, gesucht=gesucht)
#Schreibe gegeben, gesucht.
        lsg.insert(4,F'geg.: u &={strNW(2*a+2*b)}~cm& & \\\\')
        lsg.insert(5,F'  {gegeben} &={strNW(eval(gegeben))}~cm& & \\\\')
        if not R:
            lsg.insert(6, F' h_{gesucht} &={strNW(h)}~cm& & \\\\')
        lsg.insert(6+indP1,F'ges.: {gesucht} &=?~cm& & \\\\')
        lsg.insert(7+indP1,F'A &=?~cm^2& & \\\\')
        lsg.insert(8+indP1,F'& & & \\\\')
#Setze die Werte ein.
        lsg[-3]=lsg[-3]+'\\\\'
#\makebox[breite] oder \makebox(breite,hoehe). Das Minus schiebt die Box unter den Bruch
        lsg.insert(-3,'\\makebox(0pt,-0.25cm)[l]{\\uline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
        lsg.insert(-2, F'{gesucht}&=-{strNW(eval(gegeben))}+\\frac{{{strNW(2*a+2*b)}}}{{2}}& & \\\\')
        lsg.insert(-2, F'&={strNW(eval(gesucht))}~cm& & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
#Berechne den Umfang.
        lsg.insert(-2,F'A&=a\\cdot b & & \\\\' if R else F'A&={gesucht}\\cdot h_{gesucht} & & \\\\')
        lsg.insert(-2,F'&={strNW(a) if R else strNW(eval(gesucht))}\\cdot{strNW(b) if R else strNW(h)}& & \\\\')
        lsg.insert(-2,F'A&={strNW(a*b) if R else strNW(eval(gesucht)*h)}~cm^2   & & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
    if auswahl=='Parallelogramm':
        gesucht=random.choice(['a','b'])
        gegeben='a' if gesucht=='b' else 'b'
        a=random.randint(10,100)/10
        b=random.randint(10,100)/10
        h=random.randint(10,(a if gesucht=='a' else b)*10)/10
        G=F'A={gesucht}*Y'
        A=eval(gesucht)*h
        afg=F'Stelle die Flächenformel des Parallelogramm nach der fehlenden Seite um und berechne diese und den Umfang für'
        afg=(afg if mitText else 'Parallelogramm: ')+F' $A={strNW(A)}~cm^2$, ${gegeben}={strNW(eval(gegeben))}~cm$ und $h_{gesucht}={strNW(h)}~cm$.'
        lsg = formeEinfacheFormelNachVorgabenUm(G=G, gesucht=gesucht)
#Schreibe gegeben, gesucht.
        lsg.insert(4,F'geg.: A &={strNW(A)}~cm^2& & \\\\')
        lsg.insert(5,F'  {gegeben} &={strNW(eval(gegeben))}~cm& & \\\\')
        lsg.insert(6,F'  h_{gesucht} &={strNW(h)}~cm& & \\\\')
        lsg.insert(7,F'ges.: {gesucht} &=?~cm& & \\\\')
        lsg.insert(8,F'u &=?~cm& & \\\\')
        lsg.insert(9,F'& & & \\\\')
#Setze die Werte ein.
#        lsgSplit=lsg[-3].split('&')
#        einsetzen=lsgSplit[1].replace('{A}',F'{{{strNW(a*b)}}}').replace(F'{{{gegeben}}}',F'{{{strNW(eval(gegeben))}}}')
#        einsetzen=F'{einsetzen}={strNW(eval(gesucht))}~cm'
#        lsgSplit[1]=F'{lsgSplit[1]}{einsetzen}'
#        lsg[-3]='&'.join(lsgSplit)+'\\\\'
        lsg[-3]=lsg[-3]+'\\\\'
#\makebox[breite] oder \makebox(breite,hoehe). Das Minus schiebt die Box unter den Bruch
        lsg.insert(-3,'\\makebox(0pt,-0.25cm)[l]{\\uline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
        lsg.insert(-2, F'{gesucht}&=\\frac{{{strNW(A)}}}{{{strNW(h)}}}& & \\\\')
        lsg.insert(-2, F'{gesucht}&={strNW(eval(gesucht))}~cm& & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
#Berechne den Umfang.
        lsg.insert(-2,F'u&=2a+2b & & \\\\')
        lsg.insert(-2,F'&=2\\cdot{strNW(a)}+2\\cdot{strNW(b)}& & \\\\')
        lsg.insert(-2,F'u&={strNW(2*a+2*b)}~cm   & & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
        for i,l in enumerate(lsg):
            lsg[i]=lsg[i].replace('Y',f'h_{gesucht}')
    if auswahl=='Dreieck':
        vari=['a','b','c']
        gegeben=list(vari)
        gesucht=random.choice(vari)
        gegeben.remove(gesucht)
        a=random.randint(10,100)/10
        b=random.randint(10,100)/10
        c=random.randint(10,100)/10
        h=random.randint(9,eval(gesucht)*10)/10
        G=F'A=({gesucht}*Y)/2'
        A=eval(gesucht)*h/2
        afg=F'Stelle die Flächenformel des Dreiecks nach der fehlenden Seite um und berechne diese und den Umfang für'
        afg=(afg if mitText else 'Dreieck: ')+F' $A={strNW(A)}~cm^2$, ${gegeben[0]}={strNW(eval(gegeben[0]))}~cm$, ${gegeben[1]}={strNW(eval(gegeben[1]))}~cm$  und $h_{gesucht}={strNW(h)}~cm$.'
        lsg = formeEinfacheFormelNachVorgabenUm(G=G, gesucht=gesucht)
#Schreibe gegeben, gesucht.
        lsg.insert(4,F'geg.: A &={strNW(A)}~cm^2& & \\\\')
        lsg.insert(5,F'  {gegeben[0]} &={strNW(eval(gegeben[0]))}~cm& & \\\\')
        lsg.insert(6,F'  {gegeben[1]} &={strNW(eval(gegeben[1]))}~cm& & \\\\')
        lsg.insert(7,F'  h_{gesucht} &={strNW(h)}~cm& & \\\\')
        lsg.insert(8,F'ges.: {gesucht} &=?~cm& & \\\\')
        lsg.insert(9,F'u &=?~cm& & \\\\')
        lsg.insert(10,F'& & & \\\\')
#Setze die Werte ein.
        lsg[-3]=lsg[-3]+'\\\\'
#\makebox[breite] oder \makebox(breite,hoehe). Das Minus schiebt die Box unter den Bruch
        lsg.insert(-3,'\\makebox(0pt,-0.25cm)[l]{\\uline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
        lsg.insert(-2, F'{gesucht}&=\\frac{{{strNW(2*A)}}}{{{strNW(h)}}}& & \\\\')
        lsg.insert(-2, F'{gesucht}&={strNW(eval(gesucht))}~cm& & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
#Berechne den Umfang.
        lsg.insert(-2,F'u&=a+b+c& & \\\\')
        lsg.insert(-2,F'&={strNW(a)}+{strNW(b)}+{strNW(c)}& & \\\\')
        lsg.insert(-2,F'u&={strNW(a+b+c)}~cm   & & \\\\')
        lsg.insert(-3,'\\makebox[0pt][l]{\\uuline{\\phantom{$' + lsg[-3].replace('&', '') + '$}}}')
        for i,l in enumerate(lsg):
            lsg[i]=lsg[i].replace('Y',f'h_{gesucht}')
    return [afg,lsg,[]]