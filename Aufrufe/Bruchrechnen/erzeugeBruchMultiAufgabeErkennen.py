#!/usr/bin/env python
# coding: utf8

#	exec(open("Aufrufe/Bruchrechnen/erzeugeBruchMultiAufgabeErkennen.py").read())
exec(open("/home/jochen/Schule/skritpeArbeitsblaetter/Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title='Multiplikationsaufgabe Erkennen'
    lsgText='Lösungen '+title
    dateiName='multiAufgabenErkennen'
    datum='12.01.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    anfang='Schreib rechts nebem dem Zahlenstrahl, welcher Multiplikationsaufgabe gegeben ist. Zeichne über dem zweiten Zahlenstrahl ein Pfeil,'
    anfang=anfang+'der solang ist, wie alle Pfeile zusammen. Schreibe rechts nebem dem zweiten Zahlenstrahl die Lösung aus der Mulitplikationsaufgabe. Siehe Beispiel.\\\\'
    erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang):
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
#Erzeuge Aufgaben:
#if True:
    afg=[]
    lsg=[]
    for i in range(1,5):
        a,l=BruchMitNatuerlicherZahlMultiPfeildarstellung()
        afg=afg+['Aufgabe '+str(i)+': \\\\']+a
        lsg=lsg+['Lösung '+str(i)+': \\\\']+l
    head=latexHead(arraystretch=True)
    begin=beginDoc(kopf=kopfzeile,title=title,anfang=anfang)
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+afg+seitenwechsel(kopfzeile,lsgText)+lsg+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()