#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	exec(open("Aufrufe/funktionen/erzeugeLineareFunktionenErkennen.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Proportionale Funktionen Bestimmen'
    anfang='Bestimme die Funktionsgleichung der Form $y=M\\cdot x+b$.'
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
    auswahl=['nat']*2+['bruch']*4+['dezi']*2
    dSamm=[]
    for i,ausw in enumerate(auswahl):
        a,l,d=erzeugeAfgLineareFktErkennen(art='linear',steigung=ausw,achsenlaenge=12,maxX=5,maxM=3,mitText=False)
        while d in dSamm:
            a,l,d=erzeugeAfgLineareFktErkennen(art='linear',steigung=ausw,achsenlaenge=12,maxX=5,maxM=3,mitText=False)
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
        dSamm.append(d)
    tabAfg=erzeugeEinfacheTabelleMitSeitenumbruch(afg,spalten=1,anzZeilen=1)
    tabLsg=erzeugeEinfacheTabelle(lsg)
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