#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	python3 Aufrufe/taeglicheUebungen/erzeugeTaeglicheRechnungenArgs.py Titel Datum anzSpalten SeitenumbruchAfg Auswahl1 Auswahl2 ...

exec(open("Funktionen/startup.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    if False:
        with open("debug.txt", "w") as my_file:
            for i in range(12):
                my_file.write(F'{i}: {sys.argv[i]}\n')
    title,kuerzel=sys.argv[1].split('_')
    anfang=sys.argv[2]
    lsgTitle='Lösungen '+title
    dateiName=title.lower().replace(' ','').replace('ü','ue').replace('ä','ae').replace('ö','oe')+'_'+kuerzel
    datum=sys.argv[3]
    anzSpalten=eval('['+sys.argv[4]+']')
#    seitenumbruch=eval(sys.argv[5].split('-')[1])
    mitText=eval(sys.argv[5].split('-')[1])
    karoBereich=eval(sys.argv[6].split('-')[1])
    extraKaroseite=eval(sys.argv[7].split('-')[1])
    agfLsgGetrennt=eval(sys.argv[8].split('-')[1])
    erzArbeit=eval(sys.argv[9].split('-')[1])
    texAusgabe=eval(sys.argv[10].split('-')[1])
    pngAusgabe=eval(sys.argv[11].split('-')[1])
    auswahl=[]
    anzahlRechnungen=26
    startRechnungenIndex=12
#    for arg in sys.argv[startRechnungenIndex:anzahlRechnungen+startRechnungenIndex]:
    for arg in sys.argv[startRechnungenIndex:]:
#Soll ein Kahoot-Arbeitsblatt erzeugt werden?
        if 'kahoot' in arg:
            filename=erzeugeKahootTabellenInhalt(anzahl=10,zeit=20,dateiName=dateiName,datum=datum,typ=arg.replace('kahoot',''))
            print('Dateiname:'+filename)
            return 
        auswahl=auswahl+[arg]
    anzahlGleicherTypen=[]
    vergleich=auswahl[0]
    i=1
    aufgabenNummern=buchstabenKlein
#Die Aufgabennummern sollen so nummeriert sein, dass Aufgaben gleichen Typs die gleiche Nummer haben:
#1a),1b),1c) - 2a),2b),2c) usw.
    if len(auswahl)>1:
#1. Fasse Aufgaben gleichen Typs zusammen und zähle, wieviel davon vorhanden sind.
        for a in auswahl[1:]:
            if a==vergleich:
                i=i+1
            else:
                anzahlGleicherTypen.append(i)
                vergleich=a
                i=1
        anzahlGleicherTypen.append(i)
        if len(list(set(anzahlGleicherTypen)))==1 and len(anzahlGleicherTypen)>1:
            if anzahlGleicherTypen[0] > 1:
                if anzahlGleicherTypen[0]<26:
                    aufgabenNummern=[F'{x}{y}' for x in range(1,len(anzahlGleicherTypen)+1) for y in buchstabenKlein[:anzahlGleicherTypen[0]]]
                else:
                    aufgabenNummern=[F'{x}{y}' for x in range(1, int(len(auswahl) / 26) + 2) for y in buchstabenKlein]
    for a in auswahl:
        if a.startswith('daten') or a.startswith('zeitWegDiagramm') or a=='hebelZeichnen' or a.startswith('datenAuswerten'):
            anzSpalten=[1,1]
    if erzArbeit:
        filename=erzeugeArbeit(auswahl,title,dateiName,datum,anfang)
    else:
        filename=erzeugeArbeitsblattTaeglicheUebungen(auswahl,title,lsgTitle,dateiName,'' if not 'datum' in locals() else datum ,'' if not 'anfang' in locals() else anfang,2 if not 'anzSpalten' in locals() else anzSpalten,mitText=mitText,karoBereich=karoBereich,extraKaroseite=extraKaroseite,agfLsgGetrennt=agfLsgGetrennt,texAusgabe=texAusgabe,pngAusgabe=pngAusgabe,aufgabenNummern=aufgabenNummern)
    print('Dateiname:'+filename)
    return 



if __name__ == '__main__':
    main()
