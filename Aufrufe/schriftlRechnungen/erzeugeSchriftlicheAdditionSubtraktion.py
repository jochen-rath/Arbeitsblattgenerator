#!/usr/bin/env python
# coding: utf8

#Aufruf:
#exec(open("Aufrufe/schriftlRechnungen/erzeugeSchriftlicheAdditionSubtraktion.py").read())

exec(open("Funktionen/funktionen.py").read())

def main():
    title='Schriftliches Addieren und Subtrahieren'
    anfang='Schreibe die Aufgaben stellenwertgerecht untereinander auf und berechne die Lösungen.'
    lsgTitle='Loesungen '+title
    dateiName='schrifftAddSub'
    datum='31.05.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    schwierigkeit='Normal'
    dateiName='schriftlicheAdditionSubtraktion'
    erzeugeArbeitsblatt(title,lsgTitle,dateiName,datum,anfang,schwierigkeit)

def erzeugeArbeitsblatt(title,lsgText,dateiName,datum,anfang,schwierigkeit):
    anzZeilenSpaltenProTabelle=[[2,5],[30,34],[46,34],[46,34]]
    ausgabeName='newFile'
    dateiName,datum=filename(dateiName,datum=datum)
    kopfzeile='Datum: '+datum
    differenzierung={'Einfach':0,'Normal':1,'Schwierig':2}
#Erzeuge Aufgaben:
    rechnungen=erzeugeAdditionsSubtraktionsRechnungen(anzZeilenSpaltenProTabelle[0],differenzierung[schwierigkeit],zufaellig=True)
    tabellenWerte=initialisiereTabellenwerte(anzZeilenSpaltenProTabelle)
#1. Tabelle, schreibe Aufgaben
    aufgaben=erzeugeTabelleMitAufgaben(rechnungen)
#2. Tabelle Schwach Schüler = erste Zeile; Normal, Starke Schüler  Leer -- 
    if schwierigkeit=='Einfach':
        erzeugeRechnungenStellengerecht(rechnungen,tabellenWerte,1,2,False)
#3. Tabelle Leer
#4. Tabelle Loesungen
    erzeugeRechnungenStellengerecht(rechnungen,tabellenWerte,3,0,True)
    head=latexHead()
    kopf=datum+' '+schwierigkeit
    begin=beginDoc(kopf=kopf,title=title,anfang=anfang)
    tabelleDifferenziert=erzeugeLatexTabelleMitRechnungen(tabellenWerte[1])
    tabelleLeer=erzeugeLatexTabelleMitRechnungen(tabellenWerte[2])
    loesungen=erzeugeLatexTabelleMitRechnungen(tabellenWerte[3])
    os.chdir('Ausgabe')
    writeLatexDoc(head+begin+aufgaben+tabelleDifferenziert+seitenwechsel(kopf)+tabelleLeer+seitenwechsel(kopf,'Lösungen von '+title)+loesungen+['\\end{document}'],ausgabeName+'.tex')
    os.system('xelatex '+ausgabeName+'.tex')
    os.rename(ausgabeName+'.pdf',dateiName+'.pdf')
    [os.remove(file) for file in os.listdir() if ausgabeName in file]
    os.chdir('..')



if __name__ == '__main__':
    main()