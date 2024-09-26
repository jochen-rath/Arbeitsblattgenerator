#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeArbeitsblattTaeglicheUebungen(auswahl,title,lsgTitle,dateiName,datum,anfang,anzSpalten=[2,2],mitText=True,karoBereich=0,extraKaroseite=False,agfLsgGetrennt=False,texAusgabe=False,pngAusgabe=False,aufgabenNummern=buchstabenKlein):
    temperaturRatAbfrage=list(set([True if x.startswith('temperaturRat') else False for x in auswahl]))
    nurThermometerAufgaben=True if len(temperaturRatAbfrage)<2 and temperaturRatAbfrage[0]==True else False
    ausgabeName='newFile'
    datumAuswahl=datum
    dateiName,datum=filename(dateiName,datum=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y") if datum=="KeinDatum" else datum)
    ausgabeName=dateiName
    kopfzeile=F'Datum: {"%%rule{3cm}{0.15mm}" if datumAuswahl=="KeinDatum" else datum}'.replace('%%','\\')
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
#    aufgabenNummern=buchstabenKlein if len(auswahl)<27 else [F'{x}{y}' for x in range(1,int(len(auswahl)/26)+2) for y in buchstabenKlein]
    if 'erzeugeAlleAtome' in auswahl:
        return schreibeAlleAtomeInDateien()
    for i,aus in enumerate(auswahl):
        a,l,d=erzeuge10minRechnung(aus,mitText,anzSpalten[1],anzSpalten[0])
        if isinstance(a,list):
            a='\n'.join(a)
        if isinstance(l,list):
            l='\n'.join(l)
        afg.append([aufgabenNummern[i]+')',a])
        lsg.append([aufgabenNummern[i]+')',l])
    tabAfg=erzeugeEinfacheTabelle(afg,anzSpalten[0],nurThermometerAufgaben)
    tabLsg=erzeugeEinfacheTabelle(lsg,anzSpalten[1],nurThermometerAufgaben)
#Erzeuge eine Leere Karo Tabelle, in der die SuS was schreiben können.
    karoTabelle=initialisiereTabellenwerte([[10,34]])
    tabelleLeer=erzeugeLatexTabelleMitRechnungen(karoTabelle[0])
#Erzeuge das LaTeX Dokument in Ausgabe
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    karo=(leeresKaro(groesse=[16,karoBereich]) +['\\\\'] ) if karoBereich>0 else []
    extraKaro=leeresKaro(groesse=[16,25]) if extraKaroseite else []
#    with open('readme.txt', 'a') as f:
#        f.write(F'In {inspect.currentframe().f_code.co_name}: Vor writeLatexDoc\n')
    if not agfLsgGetrennt:
        writeLatexDoc(head+begin+tabAfg+karo+extraKaro+seitenwechsel(kopfzeile,lsgTitle)+tabLsg+['\\end{document}'],os.path.join('Ausgabe',ausgabeName+'.tex'))
    else:
        writeLatexDoc(head+begin+tabAfg+karo+['\\end{document}'],os.path.join('Ausgabe',ausgabeName+'.tex'))
        writeLatexDoc(head+beginDoc(kopf=kopfzeile,title=lsgTitle)+tabLsg+['\\end{document}'],os.path.join('Ausgabe',ausgabeName+'_lsg.tex'))
    os.chdir('Ausgabe')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    if agfLsgGetrennt:
        os.system(F'xelatex {ausgabeName}_lsg.tex')
        os.rename(F'{ausgabeName}_lsg.pdf',F'{dateiName}_lsg.pdf')
        os.system(F'zip {dateiName}.zip {dateiName}.pdf {dateiName}_lsg.pdf')
        for endung in ['aux','log','out']:
            os.remove(ausgabeName+'_lsg.'+endung)
    if texAusgabe:
        os.system(F'zip {dateiName}.zip {dateiName}.pdf {dateiName}.tex')
    if pngAusgabe:
        os.system(F'pdftoppm -png {dateiName}.pdf {dateiName}')
        os.system(F'zip {dateiName}.zip {dateiName}.pdf {dateiName}*.png')
    for endung in ['aux','log','out']:
        os.remove(ausgabeName+'.'+endung)
    os.chdir('..')
    return F'{dateiName}.{"zip" if agfLsgGetrennt or texAusgabe or pngAusgabe else "pdf"}'
