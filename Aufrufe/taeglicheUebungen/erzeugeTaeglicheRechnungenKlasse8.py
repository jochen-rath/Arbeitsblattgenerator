#!/usr/bin/env python
# coding: utf8

#Diese Skript erzeugt 8 verschiedene Rechnungen, die am Anfang der Stunde gerechnet werden sollen.
#Aufruf:
#	exec(open("Aufrufe/taeglicheUebungen/erzeugeTaeglicheRechnungenKlasse8.py").read())
exec(open("Funktionen/funktionen.py").read())



def main():
#Setze Variablen:
    title='Tägliche Übungen'
    lsgTitle='Lösungen '+title
    dateiName='01_'+title.lower().replace(' ','').replace('ü','ue').replace('ä','ae').replace('ö','oe')
#    datum='29.06.2021'    #Wird kein Datum angeben, wird das morgige Datum genommen.
    auswahl=['einfacheFormelUmformen','TagesMonatsZinsen','ProzRechPWert','propFktZeichnen','BruchAddSubBel','zweiBruecheDividieren']
    anzSpalten=[2,2]
    erzeugeArbeitsblattTaeglicheUebungen(auswahl,title,lsgTitle,dateiName,'' if not 'datum' in locals() else datum ,'' if not 'anfang' in locals() else anfang,[2,2] if not 'anzSpalten' in locals() else anzSpalten)



if __name__ == '__main__':
    main()

# auswahlFreiwillieLeistung=['BruchAddSubUngleichAddition','BruchAddSubUngleichSubtraktion','zweiBruecheMulti','zweiBruecheDividieren','rechneLaengenEinheitenUmEinschritt','rechneLaengenEinheitenUmEinschritt',
#             'rechneQuadrateEinheitenUmEinschritt','rechneQuadrateEinheitenUmEinschritt','termeUmformen','termeUmformenKlammer','einfacheGleichung',
#             'einfacheGleichungMitKlammer','QuaderVolOber','ProzRechPWert','ZinsatzBerechnen']