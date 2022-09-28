#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Dezimalzahlen/erzeugeDezimalzahlenRunden.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Runden von Dezimalzahlen'
    lsgText='Lösungen '+title
    dateiName='rundenDezimalzahlen'
    datum='22.01.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Runde die Dezimalzahlen auf die angegebene Stelle.'
    auswahl=[[1,3],[3,3],[2,3],[0,3],[2,3],[1,3]]
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,auswahl)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,auswahl):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i,a in enumerate(auswahl):
        a,l,d=dezimalzahlenRunden(a[0],a[1],1)
        afg.append([buchstabenKlein[i]+')',a])
        lsg.append([buchstabenKlein[i]+')',l])
    tabAfg=erzeugeEinfacheTabelle(afg,2)
    tabLsg=erzeugeEinfacheTabelle(lsg,2)
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+tabAfg+seitenwechsel(kopfzeile,lsgText)+tabLsg+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()