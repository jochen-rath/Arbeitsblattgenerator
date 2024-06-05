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

def erzeugeKahootTabellenInhalt(anzahl=10,zeit=20,dateiName='newFile',datum=''):
    aufgaben=[]
    for i in range(anzahl):
        aufgaben.append(erzeugeKahootKopfrechnen(zeit=zeit))
    return erzeugeKahootXlsxDatei(aufgaben,dateiName=dateiName,datum=datum)
    
    