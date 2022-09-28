#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Einheiten/erzeugeZeitenUmwandeln.py").read())

exec(open("Funktionen/funktionen.py").read())
def main():
#Setze Variablen:
    title='Wandelt die Zeiten um.'
    lsgText='Loesungen '+title
    dateiName='_ZeitenUmwandeln'
#    datum='31.05.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang=''
    erzeugeArbeitsblatt(title,lsgText,dateiName,'' if not 'datum' in locals() else datum,anfang)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i in range(20):
        a,l,d=rechneEinheitenUm("zeit",einSchritt=True,mitKomma=True,einfach=True,vonObenNachUnten=True)
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
    tabAfg=erzeugeEinfacheTabelle(afg,2)
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,2)
    head=latexHead(arraystretch=True,size=1)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+tabAfg+seitenwechsel(kopfzeile,lsgText)+tabLsg+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
#    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()