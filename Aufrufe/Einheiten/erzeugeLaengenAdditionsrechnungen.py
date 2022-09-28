#!/usr/bin/env python
# coding: utf8
#	exec(open("Aufrufe/Einheiten/erzeugeLaengenAdditionsrechnungen.py").read())

exec(open("Funktionen/funktionen.py").read())
def main():
#Setze Variablen:
    title='Addiere und Subtrahiere die Längeneinheiten'
    lsgText='Loesungen '+title
    dateiName='LaengenEinheitenAdditionSubtraktion'
    datum='31.05.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Berechne die resultierende Einheit.'
    art='laengen'
    einheiten=['km','m','dm','cm','mm']
#Wähle die Einheiten so, dass diese Maximal 2 Größenordnungen auseinander liegen.
    maxGroessOrd=2
    einheitenPaar=[]
    for i in range(len(einheiten)-maxGroessOrd):
        einheitenPaar.append([art,einheiten[i],einheiten[i+random.randint(1,maxGroessOrd)]])   
        einheitenPaar.append([art,einheiten[-1-i],einheiten[-1-i-random.randint(1,maxGroessOrd)]])   
    einheitenPaar=einheitenPaar*4
    random.shuffle(einheitenPaar)
    erzeugeArbeitsblatt(title,lsgText,dateiName,'' if not 'datum' in locals() else datum,anfang,einheiten=einheitenPaar)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,einheiten=[['laengen','km','m']]*3):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i,einheit in enumerate(einheiten):
        art,E1,E2=einheit
        a,l,d=addiereSubtrahiereEinheiten(art=art,mitKomma=False,einheitPaar=[E1,E2])
        afg.append([buchstabenKlein[i]+')','\n'.join(a)])
        lsg.append([buchstabenKlein[i]+')','\n'.join(l)])
    tabAfg=erzeugeEinfacheTabelle(afg,2)
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