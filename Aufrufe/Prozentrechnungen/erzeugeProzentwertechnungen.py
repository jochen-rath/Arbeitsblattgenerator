#!/usr/bin/env python
# coding: utf8

#	exec(open("Aufrufe/Prozentrechnungen/erzeugeProzentwertechnungen.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Prozentwert Berechnen'
    lsgText='Lösungen '+title
    dateiName='prozentwert'
    datum=''    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Berechne den Prozentwert'
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i in range(8):
        a,l=erzeugeProzentwertAufgaben(n=1,lsgMitDreisatz=False)
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l[0])])
    tabAfg=erzeugeEinfacheTabelle(afg,1)
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,2)
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