#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/KoerperUndFlaechen/erzeugeQuaderVolumenBerechnung.py").read())

exec(open("Funktionen/funktionen.py").read())
def main():
#Setze Variablen:
    title='Volumen und Oberflächen Berechnen'
    lsgText='Loesungen '+title
    dateiName='quader'
    datum='25.03.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Berechne das Volumen und die Oberfläche von.'
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i in range(4):
        a,l=erzeugeQuaderOberVolBerech(breitePbox=5,maxDim=5,einheit='cm')
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
    tabAfg=erzeugeEinfacheTabelle(afg,2)
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,2)
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