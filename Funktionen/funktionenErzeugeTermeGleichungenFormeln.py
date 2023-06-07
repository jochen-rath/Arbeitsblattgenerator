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
        afg=F'Setze für die Variabel {vari} den Wert {wert} ein und berechne den Wert des Terms:'
        afg=afg+F'$${term}$$'.replace("*"," \\cdot ").replace('XX','\\')
    else:
        afg=['$\\begin{aligned}']
#        afg=afg+[F'y=&{term}'.replace("*"," \\cdot ")+'\\\\']
#        afg=afg+[F' {vari}=&{wert}~ XXrightarrow ~ y=?'.replace("*"," \\cdot ").replace('XX','\\')]
        afg=afg+[F' {vari}=&{wert}~ XXrightarrow ~ {term}=?'.replace("*"," \\cdot ").replace('XX','\\')]
        afg=afg+['\\end{aligned}$']
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
    T=T.replace('**','^').replace('*','\\cdot ').replace('/',':')
    T=T.replace('XI','I')
    T=T.replace('Xrho','\\rho')
    T=T.replace('XVm','G_{Vm}')
    T=T.replace('XVp','G_{Vp}')
    return T

def erzeugeEinfacheFormelnUmformen(formel='',gesucht=''):
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
    lsg=formeEinfacheFormelNachVorgabenUm(G=G,gesucht=gesucht)
    return [afg,lsg,G]

def untertermErzeugen(variListe,variMaxAnzProUnterterm=3,maxMulti=5,variMinAnzProUnterterm=0,mitKommazahl=False):
#Diese Funktion erzeugt einen Unterterm, welcher dann mit weiteren Untertermen mit plus und Minus zu einem Term zusammengesetzt werden kann.
    n=random.randint(1,maxMulti) + (random.randint(0,10)/10 if mitKommazahl else 0)
    vari=[random.choice(variListe.split(' ')) for i in range(random.randint(variMinAnzProUnterterm,variMaxAnzProUnterterm))]
    if len(vari)>0:
        return '*'.join(([str(n)] if n>1 else [])+vari)
    else:
        return str(n)

def klammerTermErzeugen(variListe='x',anzInKlammer=2,variMaxAnzProUnterterm=3,maxMulti=5,variVorKlammer=False):
#Diese Funktion erzeugt einen Unterterm, welcher dann mit weiteren Untertermen mit plus und Minus zu einem Term zusammengesetzt werden.
    n=random.randint(1,maxMulti)
    variKlammer=''
    if variVorKlammer:
        variKlammer='*'+random.choice(variListe.split(' '))
    return str(n)+variKlammer+'*('+erzeugeTerm(variListe,anzahl=anzInKlammer,variMaxAnzProUnterterm=variMaxAnzProUnterterm,maxMulti=5)+')'


def erzeugeTerm(variablen='x y z',anzahl=3,variMaxAnzProUnterterm=3,maxMulti=5,mitKlammer=False,variVorKlammer=False,mitKommazahl=False):
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
    return term+unterterme[-1]


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
    afg=[F'{"Vereinfache:" if mitText else ""}$${term}$$'.replace("*"," \\cdot ")]
    lsg=sympy.sympify(term)
#    lsg=['$'+term.replace('*','\\cdot ')+'='+str(lsg).replace('**','^').replace('*','\\cdot ')+'$']
    lsg=['$'+term.replace('*','\\cdot ')+'='+str(lsg).replace('**','^').replace('*','')+'$']
    return [afg,lsg,term]

def erzeugeSehrEinfacheGleichungen(variabel='x',mitText=True,nurPlusMinus=False,PlusMinusVariRechts=False,nurMalGeteilt=False,MalUndPlusMinus=True):
    G=F'3*{variabel}-5=10'
    if nurPlusMinus:
        G = F'{variabel}{random.choice(["+", "-"])}{random.randint(1, 50)} = {random.randint(1, 50)}'
    if nurMalGeteilt:
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        G = F'{a}*{variabel}={a * b}' if bool(random.getrandbits(1)) else F'{variabel}/{a}={b}'
    if PlusMinusVariRechts:
        G = F'{random.randint(1, 50)} = {random.randint(1, 50)}{random.choice(["+", "-"])}{variabel}'
    if MalUndPlusMinus:
        x = random.randint(2, 12)
        b = random.randint(2, 20)
        a = random.randint(2, 10)
        c = a*x-b
        G=F"{a}*{variabel}-{b}={c}"
    afg = F'{"Berechne die Variable $" if mitText else ""}${G.replace("**", "^").replace("*", "&&cdot ").replace("/", ":")}${"$" if mitText else ""}'.replace("&&","\\")
    lsg = loeseGleichungEinfachMitEinerVariabel(G=G, variable=variabel, mitProbe=True)
    return [afg, lsg, G]

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
        afg= F'{"Berechne die Variable $" if mitText else ""}${G.replace("**", "^").replace("*", "&&cdot ").replace("/", ":")}${"$" if mitText else ""}'.replace("&&","\\")
#        print(F'G: {G}')
        lsg=loeseGleichungEinfachMitEinerVariabel(G=G,variable=variabel,mitProbe=True)
        if (not lsg=='Error') and ohneKomma:
            erg=loeseGleichungEinfachMitEinerVariabel(G=G,variable=variabel,mitProbe=True,latexAusgabe=False)
#            print(F'erg: {erg}')
            if ('.' in erg) or ('/' in erg) or int(erg.split('=')[1])==0:
                lsg='Error'
    return [afg,lsg,G]
    
