#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/TermeGleichungen/erzeugeEinfachGleichungMitQuadrat.py").read())

exec(open("Funktionen/funktionen.py").read())
def main():
#Setze Variablen:
    title='Löse folgende Gleichungen'
    lsgText='Loesungen '+title
    dateiName='gleichungenMitQuadrat'
    datum='31.05.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Berechne die Variabel.'
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
        a,l,d=erzeugeEinfacheGleichung(variabel=random.choice(["a","b","x","y"]),mitKlammer=True,mitQuadrat=True)
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
    tabAfg=erzeugeEinfacheTabelle(afg,1)
    tabLsg=erzeugeEinfacheTabelleMitSeitenumbruch(lsg,1)
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