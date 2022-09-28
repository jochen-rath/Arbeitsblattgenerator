#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Prozentrechnungen/erzeugeGrundwertrechnungen.py").read())
exec(open("Funktionen/funktionen.py").read())
def main():
#Setze Variablen:
    Kapital=False
    title='Grundwert Berechnen'
    lsgText='Loesungen '+title
    dateiName='grundwert'
    datum=''    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Berechne den Grundwert'
    bez=['Zinsen','Zinssatz'] if Kapital else ['Prozentwert','Prozentsatz']
    einheit='\euro{}' if Kapital else ''
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,bez=bez,einheit=einheit)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,bez=['Prozentwert','Prozentsatz'],einheit=''):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i in range(8):
        a,l,d=erzeugeGrundwertAufgaben(n=1,lsgMitDreisatz=True,bez=bez,einheit=einheit)
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
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