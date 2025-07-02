#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeKahootXlsxDatei(aufgaben=[['']*7]*8,dateiName='newFile',datum=''):
    pfad='Ausgabe'
    dateiName,datum=filename(dateiName,datum=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y") if datum=="KeinDatum" else datum)
    ausgabeName=os.path.join(pfad,F'{dateiName}.xlsx')
    inhalt=[['','Quiz template']+['']*6]
    inhalt.append(['','Add questions, at least two answer alternatives, time limit and choose correct answers (at least one). Have fun creating your awesome quiz!']+['']*6)
    inhalt.append(['','Remember: questions have a limit of 95 characters and answers can have 60 characters max. Text will turn red in Excel or Google Docs if you exceed this limit. If several answers are correct, separate them with a comma.  ']+['']*6)
    inhalt.append(['',"See an example question below (don't forget to overwrite this with your first question!) "]+['']*6)
    inhalt.append(['',"And remember,  if you're not using Excel you need to export to .xlsx format before you upload to Kahoot!"]+['']*6)
    inhalt.append(['','Question - max 95 characters','Answer 1 - max 60 characters','Answer 2 - max 60 characters','Answer 3 - max 60 characters','Answer 4 - max 60 characters','Time limit (sec) - 5,10,20,30,60,90 or 120 secs','Correct answer(s) - choose at least one']+['']*6)
    for i,zeile in enumerate(aufgaben):
        inhalt.append([F'{i+1}']+zeile)
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(ausgabeName)
    worksheet = workbook.add_worksheet()
    for i,zeile in enumerate(inhalt):
        for j,k in enumerate(zeile):
            worksheet.write(i+1, j,     k)
    workbook.close()
    return F'{dateiName}.xlsx'



def kahootAdditionSchaetzen(zeit=10):
    calc=str(random.randint(1000,9999))+' + '+str(random.randint(1000,9999))
    erg=str(eval(calc))
    erg2=str(random.randint(1000,19999))
    while erg2[-1] == erg[-1]:
        erg2=str(random.randint(1000,19999))
    results=[str(random.randint(0,1000)),erg,erg2,str(random.randint(20000,99999))]
    random.shuffle(results)
    return [f'Was ist {calc}?']+results+[zeit,results.index(erg)+1]

def kahootSubtraktionSchaetzen(zeit=10):
    differenz=random.randint(50,1000)
    subtrahend=random.randint(100,1000)
    minuend=differenz+subtrahend
    calc=str(minuend)+' - '+str(subtrahend)
    erg=str(differenz)
    erg2=str(random.randint(1,1000))
    while erg2[-1] == erg[-1]:
        erg2=str(random.randint(1,1000))
    results=[str(random.randint(minuend,3*minuend)),erg,erg2,str(random.randint(minuend-30,minuend))]
    random.shuffle(results)
    return [f'Was ist {calc}?']+results+[zeit,results.index(erg)+1]


def erzeugeKahootKopfrechnen(zeit=10):
    afg,lsg,erg=erzeugeKopfrechenAufgabe()
    results=[erg]
    for j in range(3):
        erg2=random.randint(0 if erg-10<0 else erg-10,erg+10)
        while erg2 in results:
            erg2=(random.randint(0 if erg-10<0 else erg-10,erg+10))
        results.append(erg2)
    random.shuffle(results)
    kahootAfg=[F'Was ist {afg.replace("=","")}?'] +results  + [zeit] + [results.index(erg)+1]
    return kahootAfg

def erzeugeKahootFachwoerter(zeit=10,art=''):
    z1,z2=random.randint(20,30),random.randint(5,19)
    fachwoerter={}
    fachwoerter['Addition']={'Aufgabe':f'{z1} + {z2} = {z1+z2}','Summand1':z1,'Summand2':z2,'Summe':z1+z2}
    fachwoerter['Subtraktion']={'Aufgabe':f'{z1+z2} - {z2} = {z1}','Minuend':z1+z2,'Subtrahend':z2,'Differenz':z1}
    fachwoerter['Multiplikation']={'Aufgabe':f'{z1} · {z2} = {z1*z2}','Faktor1':z1,'Faktor2':z2,'Produkt':z1*z2}    
    fachwoerter['Division']={'Aufgabe':f'{z1*z2} : {z2} = {z1}','Dividend':z1*z2,'Divisor':z2,'Quotient':z1}
    if len(art)<1:
        art=random.choice(list(fachwoerter.keys()))
    if random.randint(1,6)<6:
        ges= random.choice(list(fachwoerter[art].keys())[1:])
        afg=f'{fachwoerter[art]["Aufgabe"]} - Wie lautet das Fachwort für die {fachwoerter[art][ges]}?'
        results=[art]+list(fachwoerter[art].keys())[1:]
    else:
        afg=f'{fachwoerter[art]["Aufgabe"]} - Was für eine Aufgabe ist das?'
        results=list(fachwoerter.keys())
        ges=art
#Entferne die Zahlen
    ges=''.join([i for i in ges if not i.isdigit()])
    results=[''.join([i for i in x if not i.isdigit()]) for x in results]
    if ges=='Summand':
        results[results.index(ges)]='Faktor'
    if ges=='Faktor':
        results[results.index(ges)]='Summand'
    random.shuffle(results)        
    return [afg] + results  + [zeit] + [results.index(ges)+1]
    

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
    frage=f'$${vari}={x}~\\rightarrow~{term.replace("*","·").replace("/",":")}=?$$' if formelSchoen else f'x={x} → {term.replace("*","·").replace("/",":")}=?'
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
    frage=f'$${vari}={x}~\\rightarrow~{term.replace("*","·").replace("/",":")}=?$$' if formelSchoen else f'x={x} → {term.replace("*","·").replace("/",":")}=?'
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
        termList=[(f'{"+" if x>0 else ""}{x}{xes[i]}' if abs(x)>0 else '') for i,x in enumerate(koeffs)]
        random.shuffle(termList)
        term=''.join(termList)
        term=term[1:] if term[0]=='+' else term
        ergKoeffs=[eval(''.join([f'{"+" if koeffs[x] >0 else "" }{koeffs[x]}' for x in xesIndex[k]])) for k in list(xesIndex.keys())]
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
        ergTermListModi=[(f'{"+" if x>0 else ""}{x}{xStr[i]}' if abs(x)>0 else '') for i,x in enumerate(ergKoeffsModi)]
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
        ergTermListModi=[(f'{"+" if x>0 else ""}{x}{xStr[i]}' if abs(x)>0 else '') for i,x in enumerate(ergKoeffsModi)]
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
    gl=f'{f"{e[0]}{e[1]}{e[2]}" if not op=='·' else f"{e[2]}{e[1]}{e[0]}"} = {erg}  |  {e[3]}{e[4]}'
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


def erzeugeKahootTabellenInhalt(anzahl=10,zeit=20,dateiName='newFile',datum='',formelSchoen=False,typ=''):
    aufgaben=[]
    for i in range(anzahl):
#Die Funktionen werden in der For-Schleife gesetzt und nicht davor, da bei jeder neuen
#Aufgabe zwischen + und - große Zahlen schätzen gewählt werden soll.
        kahootFkt=['erzeugeKahootKopfrechnen(zeit=zeit)',
                   random.choice(['kahootAdditionSchaetzen(zeit=zeit)', 'kahootSubtraktionSchaetzen(zeit=zeit)']),
                   'erzeugeKahootFachwoerter(zeit=zeit)',
                    f'erzeugeKahootTermeEinfachEinsetzen(zeit=zeit,HS=True,formelSchoen={formelSchoen})',
                    f'erzeugeKahootTermeEinfachEinsetzen(zeit=zeit,formelSchoen={formelSchoen})',
                    f'erzeugeKahootTermeKombiEinsetzen(zeit=zeit,HS=True,formelSchoen={formelSchoen})',
                    f'erzeugeKahootTermeKombiEinsetzen(zeit=zeit,formelSchoen={formelSchoen})',
                   f'erzeugeKahootTermeZusammenfassen(zeit=zeit,HS=True)',
                   f'erzeugeKahootTermeZusammenfassen(zeit=zeit,HS=False)',
                   f'erzeugeKahootTermeZusammenfassen(zeit=zeit,anzVari=2,HS=False)',
                   f'erzeugeKahootGleichungFehlendEintragen(zeit=zeit)',
                   f'erzeugeKahootGleichungFehlendEintragenKombi(zeit=zeit,formelSchoen={formelSchoen})']
        auswahl=list(kahootFkt)[0:3]
        if typ=='Kopf':
            auswahl=[kahootFkt[0]]
        if typ=='Grossezahlen':
            auswahl=[kahootFkt[1]]
        if typ=='Fachwoerter':
            auswahl=[kahootFkt[2]]
        if typ=='TermeEinsetzenHS':
            auswahl=[kahootFkt[3]]
        if typ=='TermeEinsetzen':
            auswahl=[kahootFkt[4]]
        if typ=='TermeEinsetzenKombiHS':
            auswahl=[kahootFkt[5]]
        if typ=='TermeEinsetzenKombi':
            auswahl=[kahootFkt[6]]
        if typ=='TermeZusammenfassenHS':
            auswahl=[kahootFkt[7]]
        if typ=='TermeZusammenfassenNurX':
            auswahl=[kahootFkt[8]]
        if typ=='TermeZusammenfassenNurXY':
            auswahl=[kahootFkt[9]] 
        if typ=='GleichungFehlend':
            auswahl=[kahootFkt[10]]
        if typ=='GleichungFehlendKombi':
            auswahl=[kahootFkt[11]]
        aufgaben.append(eval(random.choice(auswahl)))
    return erzeugeKahootXlsxDatei(aufgaben,dateiName=dateiName,datum=datum)
    
    