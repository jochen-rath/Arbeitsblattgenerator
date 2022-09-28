#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	exec(open("Aufrufe/taeglicheUebungen/erzeugeTaeglicheRechnungenKlasse6.py").read())
exec(open("Funktionen/funktionen.py").read())



def main():
#Setze Variablen:
    title='Tägliche Übungen'
    title='Einheiten'
    lsgTitle='Lösungen '+title
    dateiName='einheiten'
    datum='07.07.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    auswahl=['bestimmeUhrzeit']*6
    auswahl=['GemischteEinheitenAddierenSubtrahieren']*12+['ZeitEinheitenAddierenSubtrahieren']*12
    auswahl=['BruchAddSubGleichAddition']*3+['BruchAddSubGleichSubtraktion']*3+['BruchAddSubBel']*2+['deziVergl']*2+['deziRunden']*2+['deziAddSubEinfach']*2+['deziAddSub']*3+['deziAddSubSchwer']*3
#    random.shuffle(auswahl)
    auswahl=[random.choice(['rechneLaengenEinheitenUm','rechneQuadrateEinheitenUm']) for i in range(20)]
    erzeugeArbeitsblatt(auswahl,title,lsgTitle,dateiName,'' if not 'datum' in locals() else datum ,'' if not 'anfang' in locals() else anfang)


def erzeugeArbeitsblatt(auswahl,title,lsgTitle,dateiName,datum,anfang,anzLsgSpalten=2):
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
    tabelleLeer=[] #erzeugeLatexTabelleMitRechnungen(karoTabelle[0])
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
