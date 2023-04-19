#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeArbeitsblattTaeglicheUebungen(auswahl,title,lsgTitle,dateiName,datum,anfang,anzSpalten=[2,2],seitenumbruch=False,mitText=True,karoBereich=0,extraKaroseite=False,agfLsgGetrennt=False,texAusgabe=False):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y") if datum=="KeinDatum" else datum)
    ausgabeName=dateiName
    kopfzeile='' if datum=="KeinDatum" else ('Datum: '+datum)
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    if 'erzeugeAlleAtome' in auswahl:
        return schreibeAlleAtomeInDateien()
    for i,aus in enumerate(auswahl):
        a,l,d=erzeuge10minRechnung(aus,mitText,anzSpalten[1])
        if isinstance(a,list):
            a='\n'.join(a)
        if isinstance(l,list):
            l='\n'.join(l)
        afg.append([buchstabenKlein[i]+')',a])
        lsg.append([buchstabenKlein[i]+')',l])
    tabAfg=erzeugeEinfacheTabelle(afg,anzSpalten[0]) if not seitenumbruch else erzeugeEinfacheTabelleMitSeitenumbruch(afg,anzSpalten[0])
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,anzSpalten[1])
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
    for endung in ['aux','log','out']:
        os.remove(ausgabeName+'.'+endung)
    os.chdir('..')
    return F'{dateiName}.{"zip" if agfLsgGetrennt or texAusgabe else "pdf"}'
