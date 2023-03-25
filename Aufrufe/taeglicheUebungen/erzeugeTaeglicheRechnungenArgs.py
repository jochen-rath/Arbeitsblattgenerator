#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	python3 Aufrufe/taeglicheUebungen/erzeugeTaeglicheRechnungenArgs.py Titel Datum anzSpalten SeitenumbruchAfg Auswahl1 Auswahl2 ...

exec(open("Funktionen/startup.py").read())
exec(open("Funktionen/funktionen.py").read())

def main():
#Setze Variablen:
    title,kuerzel=sys.argv[1].split('_')
    anfang=sys.argv[2]
    lsgTitle='Lösungen '+title
    dateiName=title.lower().replace(' ','').replace('ü','ue').replace('ä','ae').replace('ö','oe')+'_'+kuerzel
    datum=sys.argv[3]
    anzSpalten=eval('['+sys.argv[4]+']')
    seitenumbruch=eval(sys.argv[5].split('-')[1])
    mitText=eval(sys.argv[6].split('-')[1])
    karoBereich=eval(sys.argv[7].split('-')[1])
    extraKaroseite=eval(sys.argv[8].split('-')[1])
    agfLsgGetrennt=eval(sys.argv[9].split('-')[1])
    erzeugeArbeit=False
    auswahl=[]
    anzahlRechnungen=26
    for arg in sys.argv[10:anzahlRechnungen+10]:
        auswahl=auswahl+[arg]
    if erzeugeArbeit:
        t=1
    else:
        filename=erzeugeArbeitsblattTaeglicheUebungen(auswahl,title,lsgTitle,dateiName,'' if not 'datum' in locals() else datum ,'' if not 'anfang' in locals() else anfang,2 if not 'anzSpalten' in locals() else anzSpalten,seitenumbruch=seitenumbruch,mitText=mitText,karoBereich=karoBereich,extraKaroseite=extraKaroseite,agfLsgGetrennt=agfLsgGetrennt)
    print('Dateiname:'+filename)
    return 



if __name__ == '__main__':
    main()
