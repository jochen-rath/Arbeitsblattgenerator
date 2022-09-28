#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	exec(open("Aufrufe/funktionen/erzeugePropLinearFunktionenZeichnen.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Proportionale Funktionen Zeichnen'
    anfang='Zeichne die Funktion und das Steigungsdreieck in ein Koordinatensystem.'
    lsgTitle='Lösungen '+title
    dateiName='01_'+title.lower().replace(' ','').replace('ü','ue').replace('ä','ae').replace('ö','oe')
#    datum='29.06.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anzSpalten=[2,2]
    erzeugeArbeitsblatt(title,lsgTitle,dateiName,'' if not 'datum' in locals() else datum ,'' if not 'anfang' in locals() else anfang)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    auswahl=['bruch']*2+['dezi']*2+['bruch']*2+['dezi']*2
    dSamm=[]
    for i,ausw in enumerate(auswahl):
        a,l,d=erzeugeAfgLineareFunktionZeichnen(art='linear',steigung=ausw,achsenlaenge=10,maxX=4,maxM=3,mitText=False)
        while d in dSamm:
            a,l,d=erzeugeAfgLineareFunktionZeichnen(art='linear',steigung=ausw,achsenlaenge=10,maxX=4,maxM=3,mitText=False)
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
        dSamm.append(d)
    tabAfg=erzeugeEinfacheTabelle(afg,2)
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,spalten=1,anzZeilen=1)
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+tabAfg+seitenwechsel(kopfzeile,lsgText)+tabLsg+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
#    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')

if __name__ == '__main__':
    main()

# auswahlFreiwillieLeistung=['BruchAddSubUngleichAddition','BruchAddSubUngleichSubtraktion','zweiBruecheMulti','zweiBruecheDividieren','rechneLaengenEinheitenUmEinschritt','rechneLaengenEinheitenUmEinschritt',
#             'rechneQuadrateEinheitenUmEinschritt','rechneQuadrateEinheitenUmEinschritt','termeUmformen','termeUmformenKlammer','einfacheGleichung',
#             'einfacheGleichungMitKlammer','QuaderVolOber','ProzRechPWert','ZinsatzBerechnen']