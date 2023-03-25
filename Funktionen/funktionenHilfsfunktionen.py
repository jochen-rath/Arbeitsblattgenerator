#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Hilfsfunktionen zum Darstellen und lösen von Rechnungen und ergebnissen.

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


buchstabenGross=[chr(i) for i in range(65,65+26)]
buchstabenKlein=[chr(i) for i in range(97,97+26)]

tikzFarben=['black','red','green','blue','yellow','cyan','magenta','olive','orange','pink','purple','brown','darkgray','gray','lightgray','lime','teal','violet','white']
zahlenWoerter=['Null','Eins','Zwei','Drei','Vier','Fuenf','Sechs','Sieben','Acht','Neun','Zehn','Elf','Zwoelf']
def spliteSeiteAddSub(S):
#Am Anfang der Gleichung muss ein Plus oder Minus stehen, damit bei der Termumformung die richtige Operation gewählt werden kann.
    if not (S[0]=='-' or S[0]=='+'):
        S='+'+S
    if not '(' in S:
        pmSPos=[i for i in range(len(S)) if '+'==S[i] or '-'==S[i]]+[len(S)]
        Ssplit=[S[pmSPos[i]:pmSPos[i+1]] for i in range(len(pmSPos[:-1]))]
    else:
        KlOffenPos=[i for i in range(len(S)) if '('==S[i]]
        KlGeschlPos=[i for i in range(len(S)) if ')'==S[i]]
#Es sollen nur die Plus-Minus Positionen gesucht werden, die nicht von einer Klammer umrandet werden.
        pmSPos=[i for i in range(len(S)) if ('+'==S[i] or '-'==S[i]) and (True not in [(KlOffenPos[j]<i and KlGeschlPos[j]>i) for j in range(len(KlOffenPos))])]+[len(S)]
        Ssplit=[S[pmSPos[i]:pmSPos[i+1]] for i in range(len(pmSPos[:-1]))]
    return Ssplit

def entferneEinzelKlammer(term):
    term = [(x.replace('(', '') if ('(' in x) and (not ')' in x) else x) for x in term]
    term = [(x.replace(')', '') if (')' in x) and (not '(' in x) else x) for x in term]
    return term

def erzeugeLatexFracAusdruck(term,operator=False):
#Diese Funktion wandelt einen Term so um, dass Latex ihn als Bruch darstellt. Dazu werden / durch frac ersetzt.
#Die Funktion entfernt zuerst die Klammern, rekursiv von aussen nach innen, und ersetzt diese durch Platzhalter.
#Am Ende werden diese Platzhalten wieder ausgetauscht.
#
#Aufruf:
#           fracTerm=erzeugeLatexFracAusdruck(term,operator=False)
#       term= umzuwandelnder Term
#       operator --> Wenn Gleichungen umgeformt werden, soll das geteilt-Zeichen am Anfang entfernt werden, um es
#                    Am ende wieder einzufügen. Dies soll nicht durch ein Frac ersetzt werden.
    geteilt=term[0] if operator else ''
    term=term[1:] if operator else term
#Finde und entferne zuerst die äußeren Klammern
    klPos=[]
    aussenKlOffen=False
    innenKlZaehler=0
    for i,c in enumerate(term):
        if c=='(' and not aussenKlOffen:
            aussenKlOffen=True
            klPos.append(i)
        elif c==')' and innenKlZaehler==0:
            aussenKlOffen=False
            klPos.append(i+1)
        elif c=='(' and aussenKlOffen:
            innenKlZaehler=innenKlZaehler+1
        elif c==')' and innenKlZaehler>0:
            innenKlZaehler=innenKlZaehler-1
    klammerInhalte=[]
    for i in range(int(len(klPos)/2)):
        klammerInhalte.append(['klammer'+str(i).zfill(2),term[klPos[2*i]:klPos[2*i+1]]])
    for klammer in klammerInhalte:
        term=term.replace(klammer[1],klammer[0])
#Wandel die Klammerausdrücke in frac um.
    for i,klammer in enumerate(klammerInhalte):
        print(klammer)
        klammerInhalte[i][1]='\\left('+erzeugeLatexFracAusdruck(klammer[1][1:-1])+'\\right)'
#Trenne den Term an + oder - auf.
    termSplit=spliteSeiteAddSub(term)
#Wenn der erste Term kein Vorzeichen hat, fuege es ein.
    termSplit[0]=termSplit[0][1:] if termSplit[0][0]=='+' else termSplit[0]
#Ersetze für jeden getrennten Unterterm ein frac ein.
    for i,uT in enumerate(termSplit):
        vorzeichen=uT[0] if (uT[0]=='+' or uT[0]=='-') else ''
        if uT.count('/')==1:
#Ein Plus oder Minus zeichen wird auf den Bruch und nicht vor dem Bruch gezogen, wenn dies nicht abgefangen wird.
            termSplit[i]=vorzeichen+'{'+(frac(uT[1:].split('/')) if len(vorzeichen)>0 else frac(uT.split('/')))+'}'
        elif uT.count('/')>1:
#Wenn mehrer Geteiltzeichen, Splite den Unterterm am Malzeichen. Beispiel 4/8*2/2 oder 2*6/7
            if '*' in uT:
                multiSplit=uT[1:].split('*') if len(vorzeichen)>0 else uT.split('*')
                termSplit[i]=vorzeichen+'{'+'*'.join([erzeugeLatexFracAusdruck(x) for x in multiSplit])+'}'
            else:
#Wandel rekursiv von Hintern nach vorne mehrere Aufeinanderfolgende geteiltzeichen in frac um. Bsp: 7/8/9
                diviSplit=uT[1:].split('/') if len(vorzeichen)>0 else uT.split('/')
                termSplit[i]=vorzeichen+'{'+frac(erzeugeLatexFracAusdruck('/'.join(diviSplit[:-1])),diviSplit[-1])+'}'
    term=geteilt + ''.join(termSplit)
#Ersetze die entfernten Klammern wieder durch deren Inhalte
    for klammer in klammerInhalte:
        term=term.replace(klammer[0],klammer[1])
    return term



def konvertZuFracBeiAddInFormelZuLoeschenDaAlt(term,operator=False):
#Diese Funktion konvertiert eine 6:2 darstellung zu einem LateX Bruch. Bei Gleichungsumformungen soll der Operator, d.h. das erste Zeichen, nicht verändert werden.
#Wenn erstes Zeichen geteilt ist, entferne es:
    geteilt=term[0] if operator else ''
    term=term[1:] if operator else term
#Trenne den Term an + oder - auf.
    Tsplit=spliteSeiteAddSub(term)
#Wenn der erste Term kein Vorzeichen hat, fuege es ein.
    Tsplit[0]=Tsplit[0][1:] if Tsplit[0][0]=='+' else Tsplit[0]
#Ersetze für jeden getrennten Unterterm ein frac ein. 
    for i,uT in enumerate(Tsplit):
#Kommt in einem Unterterm nur ein '/' vor?
        vorzeichen=uT[0] if (uT[0]=='+' or uT[0]=='-') else ''
        if uT.count('/')==1:
#Ein Plus oder Minus zeichen wird auf den Bruch und nicht vor dem Bruch gezogen, wenn dies nicht abgefangen wird.
            Tsplit[i]=frac(entferneEinzelKlammer(uT[1:].split('/'))) if len(vorzeichen)>0 else frac(entferneEinzelKlammer(uT.split('/')))
            Tsplit[i]=vorzeichen+'{'+Tsplit[i]+'}'
        else:
#Wenn nicht, Splite ihn am Malzeichen. Beispiel 4/8*2/2
            if '*' in uT:
                multiSplit=uT[1:].split('*') if len(vorzeichen)>0 else uT.split('*')
                for j,ms in enumerate(multiSplit):
                    if ms.count('/') > 1:
                        diviSplit=entferneEinzelKlammer(ms.split('/'))
                        latexFrac=frac(diviSplit[0],diviSplit[1])
                        for i in range(len(diviSplit)-2):
                            latexFrac=frac(latexFrac,diviSplit[i+2])
                        multiSplit[j]=latexFrac
                    else:
                        multiSplit[j]=frac(ms.split('/')) if '/' in ms else ms
                Tsplit[i]=vorzeichen+'{'+'*'.join(multiSplit)+'}'
#Wenn nicht, Splite ihn am Geteilzeichen. 6/6/4
            else:
                if uT.count('/') > 1:
                    diviSplit=entferneEinzelKlammer(uT[1:].split('/')) if len(vorzeichen)>0 else entferneEinzelKlammer(uT.split('/'))
                    latexFrac=frac(diviSplit[0],diviSplit[1])
                    for k in range(len(diviSplit)-2):
                        latexFrac=frac(latexFrac,diviSplit[k+2])
                    Tsplit[i]=vorzeichen+'{'+latexFrac+'}'
#    TsplitFrac=[frac(x.split('/')) if '/' in x else x for x in Tsplit]
    return geteilt+''.join(Tsplit)

def filename(dateiName,datum=''):
#Wenn kein Datum angeben wird, wird das morgige Datum erzeugt.
    if 'Woche'in datum:
        datumFilename=datum.replace(' ','_')
    else:
        if len(datum)==0:
            datum=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
            datumFilename=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y.%m.%d")
        else:
            if '\\rule' in datum:
                datumFilename=''
            else:
                m_split=datum.split('.')
                datumFilename=m_split[2]+'.'+m_split[1]+'.'+m_split[0]
    dateiName=datumFilename+('_' if len(datumFilename)> 1 else '')+dateiName
    return dateiName,datum

def ggt(a, b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

def kgV(a, b):
    av=[a*x for x in range(1,b+1)]
    bv=[b*x for x in range(1,a+1)]
    return [x for i,x in enumerate(bv) if x in av][0]

def divisionsSchritte(rechnungen,kommarechnung=False):
#Diese Funktion berechnet die Divisionsschrifte einer Divisionsaufgabe.
#
#           erg,divSchr= divisionsSchritte(rechnungen)
#
#       erg=String mit den Ergebnis der Division
#       divSchr= Für jeden Divisionschritt: [Rest, Erg Multi, Subtrahent]
    dividend,divisor=rechnungen.split('/')
    if kommarechnung:
        kommapos=-1 if not ',' in dividend else dividend.index(',')
        kommapos=kommapos if not '.' in dividend else dividend.index('.')
        dividend=dividend.replace(',','').replace('.','')
    rest=''
    divSchr=[]
    erg=''
    ende=False
    i=0
    while not ende:
        zif = '0' if i>=len(dividend) else dividend[i]
        rest=rest+zif
        calc=str(int(math.floor(eval(str(int(float(rest)))+'/'+divisor))))
        erg=erg+calc
        subtrahent=str(eval(calc+'*'+divisor))
        if int(float(erg))>0:
            divSchr.append([rest,calc,subtrahent])
        rest=str(eval(str(int(rest))+'-'+subtrahent))
        i=i+1
        if (i>=len(dividend) and not kommarechnung):
            ende=True
        elif (i>len(dividend) and rest=='0'):
            ende=True
        elif i>10:
            ende=True
    erg=erg+(' Rest '+rest if (int(rest)>0 and not kommarechnung) else '')
    divSchr.append([rest])
    print(rechnungen)
    kommapositionen=[kommapos,strNW(eval(rechnungen.replace('.','').replace(',','.'))).index(',')] if kommarechnung else []
    return erg,divSchr,kommapositionen

def fuegePunkteEin(a):
#Drehe den String um und dann gehe den String in dreier Schritten durch.
#Erzeuge eine Liste mit je drei Elementen.
#Vereine die Liste zum Schluss mit einem Punkt
    return '.'.join(a[::-1][i:i+3] for i in range(0, len(a), 3))[::-1]

def strNW(a,runden=False):
#Schreibe die Zahl nicht wissenschaftlich und mit einem Komma anstatt Punkt.
    if type(a)==str:
        return a
    a_str=str(round(a,10)) if not runden else str(round(a,2))
    if 'e-' in a_str:
        if '.' in a_str:
            n=int(a_str.split('.')[1].split('e-')[1])+len(a_str.split('.')[1].split('e-')[0])
        else:
            n=int(a_str.split('e-')[1])
        a_str=eval('"{:.'+str(int(n))+'f}".format(a)')
    if 'e+' in a_str:
        if '.' in a_str:
            n=int(a_str.split('.')[1].split('e+')[1])+len(a_str.split('.')[1].split('e+')[0])
        else:
            n=int(a_str.split('e+')[1])
        a_str=eval('"{:'+str(int(n))+'.0f}".format(a)')
    if '.' in a_str:
        if int(a_str.split('.')[1])==0:
            a_str=a_str.split('.')[0]
            a_str=fuegePunkteEin(a_str)
        else:
            a_str=fuegePunkteEin(a_str.split('.')[0])+','+a_str.split('.')[1]
    else:
        a_str=fuegePunkteEin(a_str)
    return a_str

def prim(n):
    '''Calculates all prime factors of the given integer.'''
    pfactors = []
    limit = int(math.sqrt(n)) + 1
    check = 2
    num   = n
    if n == 1:
        return [1]
    for check in range(2, limit):
        while num % check == 0:
            pfactors.append(check)
            num /= check
    if num > 1:
        pfactors.append(num)
    return pfactors

def frac(z,n=1):
    if isinstance(z,list):
       n=z[1]
       z=z[0]
    return ('{\\frac{'+z+'}{'+n+'}}' if isinstance(z,str) else '\\frac{'+strNW(z)+'}{'+strNW(n)+'}')

def schreibeBruchundGemZahl(z,n):
    if z%n ==0:
       return strNW(z/n)
    ausgabe=frac(z,n)
    if z>n:
       ausgabe=ausgabe+'='+strNW(int(z/n))+frac(str(int(z)-int(z/n)*n),str(int(n)))
    return ausgabe
  
def schreibeGemZahl(z,n):
    if z%n ==0:
       return strNW(z/n)
    ausgabe=frac(z,n)
    if abs(z)>n:
       ausgabe=strNW(int(z/n))+frac(abs(int(z)-int(z/n)*n),int(n))
    return ausgabe

def konvertiereRechnungenFuerFunktion(rechnungen):
    konv=[]
    for c in rechnungen:
        r1=[c[0]] + c[1].split(' ')[1::2]
        r1=r1+[r1[-1]]
        r2=list(map(int,c[1].split(' ')[0::2]))+[eval(c[1])]
        konv.append([r1,r2])
    return konv

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False 


malZeichen='·'

def cm2inch(*tupl):
    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)

def schreibIntIfFloatIsInt(x):
    return str(int(x)) if int(x)-x==0 else str(x)

def zerschneidePDF(anzahlSeiten,anzahlSchueler,ausgabenName,seitenLsgen=1):
#Beispeil: Anzahl Seiten=2, Anzahl Lösungseiten=2
#Erzeuge Liste mit [1,2,5,6,9,10,... für Aufgabeseiten
#und Liste mit [3,4,7,8,11,12,... für Lösungeseiten
#Beispeil: Anzahl Seiten=3, Anzahl Lösungseiten=1
#Erzeuge Liste mit [1,2,3,5,6,7,9,10,... für Aufgabeseiten
#und Liste mit [4,8,12,... für Lösungeseiten
    anzGesSeiten=anzahlSeiten*anzahlSchueler+1
    aS=[x+1 for x in list(range(anzahlSeiten-seitenLsgen))]   #--> aS=[1,2]
    aSL=[x+1+anzahlSeiten-seitenLsgen for x in list(range(seitenLsgen))]   #--> aSL=[3]
    pages=[y for sublist  in [[x+i*anzahlSeiten] for x in aS for i in range(int(anzGesSeiten/anzahlSeiten))] for y in sublist]
    pages.sort()
    pagesLSG=[y for sublist  in [[x+i*anzahlSeiten] for x in aSL for i in range(int(anzGesSeiten/anzahlSeiten))] for y in sublist]
    pagesLSG.sort()
    os.system('pdftk '+ausgabenName+'.pdf cat '+' '.join([str(x) for x in pages])+' output '+ ausgabenName+'Aufgaben.pdf')
    os.system('pdftk '+ausgabenName+'.pdf cat '+' '.join([str(x) for x in pagesLSG])+' output '+ ausgabenName+'LSG.pdf')
    os.system('rm '+ausgabenName+'.pdf')

def zerschneidePDFVariabel(anzahlSeiten,anzahlVariationen,ausgabenName,inhalt,seitenEinteilung):
#Beispeil: Anzahl Seiten=2,
#Erzeuge Liste mit [1,2,5,6,9,10,... für Aufgabeseiten
    anzGesSeiten=anzahlSeiten*anzahlVariationen+1
    for k in range(len(inhalt)):
        pages=[y for sublist  in [[x+i*anzahlSeiten] for x in seitenEinteilung[k] for i in range(int(anzGesSeiten/anzahlSeiten))] for y in sublist]
        pages.sort()
        os.system('pdftk '+ausgabenName+'.pdf cat '+' '.join([str(x) for x in pages])+' output '+ ausgabenName+inhalt[k]+'.pdf')
#    os.system('rm '+ausgabenName+'.pdf')



def openSchuelerName(schuelerNamenListe):
    with open(schuelerNamenListe,'r') as f:
        namen=f.read()
    return namen.split('\n')

def openSchuelerNameDifferenziert(schuelerNamenListe):
    with open(schuelerNamenListe,'r') as f:
        namen=csv.reader(f)
        namen=list(namen)
    return namen[4:]

def openSchuelerName(schuelerNamenListe):
    with open(schuelerNamenListe,'r') as f:
        namen=csv.reader(f)
        namen=list(namen)
    return namen
