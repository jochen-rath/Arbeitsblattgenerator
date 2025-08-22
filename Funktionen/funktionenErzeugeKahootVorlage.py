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


def zufallAddSubSchaetzen(zeit=10):
    return random.choice([eval('kahootAdditionSchaetzen(zeit=zeit)'), eval('kahootSubtraktionSchaetzen(zeit=zeit)')])

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
    


def erzeugeKahootTabellenInhalt(kahoots=['Grossezahlen','TermeEinsetzenHS'],zeit=20,dateiName='newFile',datum='',formelSchoen=False):
    aufgaben=[]
    kahootFkt={'Kopf':'erzeugeKahootKopfrechnen(zeit=zeit)'}
    kahootFkt['Grossezahlen']='zufallAddSubSchaetzen(zeit=zeit)'
    kahootFkt['Fachwoerter']='erzeugeKahootFachwoerter(zeit=zeit)'
    kahootFkt['BruechekuerzenHS']= f'erzeugeKahootBruecheKuerzenMitVorg(zeit=10,HS=True)'
    kahootFkt['BruecheErweiternHS']= f'erzeugeKahootBruecheErweiternMitVorg(zeit=10,HS=True)'
    kahootFkt['TermeEinsetzenHS']=f'erzeugeKahootTermeEinfachEinsetzen(zeit=zeit,HS=True,formelSchoen={formelSchoen})'
    kahootFkt['TermeEinsetzen']=f'erzeugeKahootTermeEinfachEinsetzen(zeit=zeit,formelSchoen={formelSchoen})'
    kahootFkt['TermeEinsetzenKombiHS']= f'erzeugeKahootTermeKombiEinsetzen(zeit=zeit,HS=True,formelSchoen={formelSchoen})'
    kahootFkt['TermeEinsetzenKombi']=f'erzeugeKahootTermeKombiEinsetzen(zeit=zeit,formelSchoen={formelSchoen})'
    kahootFkt['TermeZusammenfassenHS']= f'erzeugeKahootTermeZusammenfassen(zeit=zeit,HS=True)'
    kahootFkt['TermeZusammenfassenNurX']=f'erzeugeKahootTermeZusammenfassen(zeit=zeit,HS=False)'
    kahootFkt['TermeZusammenfassenNurXY']=f'erzeugeKahootTermeZusammenfassen(zeit=zeit,anzVari=2,HS=False)'
    kahootFkt['GleichungFehlend']=f'erzeugeKahootGleichungFehlendEintragen(zeit=zeit)'
    kahootFkt['GleichungFehlendKombi']=f'erzeugeKahootGleichungFehlendEintragenKombi(zeit=zeit,formelSchoen={formelSchoen})'
    kahootFkt['RatAddSub']=f'erzeugeKahootRationaleZahlenAddSub(zeit=zeit)'
    kahootFkt['RatAddSubHS']=f'erzeugeKahootRationaleZahlenAddSub(zeit=zeit,HS=True)'
    kahootFkt['RatMulDiv']=f'erzeugeKahootRationaleZahlenMultiDiv(zeit=zeit)'
    for typ in kahoots:
        aufgaben.append(eval(kahootFkt[typ.replace('kahoot','')]))
    random.shuffle(aufgaben)
    return erzeugeKahootXlsxDatei(aufgaben,dateiName=dateiName,datum=datum)
    
    
def kahootAenderung():
    for i in range(anzahl):
#Die Funktionen werden in der For-Schleife gesetzt und nicht davor, da bei jeder neuen
#Aufgabe zwischen + und - große Zahlen schätzen gewählt werden soll.

        auswahl=list(kahootFkt)[0:3]
    return erzeugeKahootXlsxDatei(aufgaben,dateiName=dateiName,datum=datum)
    