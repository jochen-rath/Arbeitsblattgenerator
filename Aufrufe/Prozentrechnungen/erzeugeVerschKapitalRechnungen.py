#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	exec(open("Aufrufe/Prozentrechnungen/erzeugeVerschKapitalRechnungen.py").read())
exec(open("Funktionen/funktionen.py").read())


def main():
#Setze Variablen:
    title='Kapital, Zinsen und Zinssatzberechnungen'
    datum=''    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang=''
    lsgTitle='Lösungen '+title
    dateiName='01_'+title.lower().replace(' ','').replace('ü','ue').replace('ä','ae').replace('ö','oe')
#    datum='02.06.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    auswahl=['ZinsenBerechnen','ZinsatzBerechnen','KapitalBerechnen']*6
    random.shuffle(auswahl)
    anzLsgSpalten=2
    erzeugeArbeitsblatt(auswahl,title,lsgTitle,dateiName,'' if not 'datum' in locals() else datum ,'' if not 'anfang' in locals() else anfang,2 if not 'anzLsgSpalten' in locals() else anzLsgSpalten)


def erzeugeArbeitsblatt(auswahl,title,lsgTitle,dateiName,datum,anfang,anzLsgSpalten):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i,aus in enumerate(auswahl):
        print(aus)
        a,l,d=erzeuge10minRechnung(aus)
        if isinstance(a,list):
            a='\n'.join(a)
        if isinstance(l,list):
            l='\n'.join(l)
        afg.append([buchstabenKlein[i]+')',a])
        lsg.append([buchstabenKlein[i]+')',l])
    tabAfg=erzeugeEinfacheTabelle(afg,2)
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,anzLsgSpalten)
#Erzeuge eine Leere Karo Tabelle, in der die SuS was schreiben können.
    karoTabelle=initialisiereTabellenwerte([[10,34]])
    tabelleLeer=erzeugeLatexTabelleMitRechnungen(karoTabelle[0])
#Erzeuge das LaTeX Dokument in Ausgabe
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    writeLatexDoc(head+begin+tabAfg+tabelleLeer+seitenwechsel(kopfzeile,lsgTitle)+tabLsg+['\\end{document}'],os.path.join('Ausgabe',ausgabeName+'.tex'))
    os.chdir('Ausgabe')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
#    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()
