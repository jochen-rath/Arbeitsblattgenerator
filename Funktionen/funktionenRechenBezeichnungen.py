#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeuge10minRechnung(art,mitText=True):
#Diese Funktion erzeugt eine Liste von verschiedenen Aufgaben. 
#Welche Aufgaben, ist in der Liste "art" angegeben.
#art = 'ggT','kgV','Basis','Kopf','erweitern','kuerzen'
#      'kuerzMit','reihe','reihePosZufaellig'
    rechnungsFunktionen={'ggT':'erzeugeGgt()','kgV':'erzeugeKgv()',
                          'Basis':'erzeugePlusMinusMalGeteiltAufgabe()','Kopf':'erzeugeKopfrechenAufgabe()',
                          'addSchriftLeicht':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=0,operator="+")',
                          'addSchrift':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=1,operator="+")',
                          'addSchriftSchwer':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=2,operator="+")',
                          'subSchriftLeicht':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=0,operator="-")',
                          'subSchrift':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=1,operator="-")',
                          'subSchriftSchwer':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=2,operator="-")',
                          'addSubSchriftLeicht':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=0,operator=random.choice(["-","+"]))',
                          'addSubSchrift':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=1,operator=random.choice(["-","+"]))',
                          'addSubSchriftSchwer':'erzeugeSchrAdditionsSubtraktionsRechnung(differenzierung=2,operator=random.choice(["-","+"]))',
                          'multiSchrEinFaktorOhneUbertrag':'erzeugeMultiplikationen(maxStellenFaktorZwei=1,ohneUebertrag=True,normal=False,schwer=False)',
                          'multiSchrEinFaktorMitUbertrag':'erzeugeMultiplikationen(maxStellenFaktorZwei=1,ohneUebertrag=False,normal=False,schwer=False)',
                          'multiSchr':'erzeugeMultiplikationen(maxStellenFaktorZwei=2,ohneUebertrag=False,normal=False,schwer=False)',
                          'multiSchrSchwer':'erzeugeMultiplikationen(maxStellenFaktorZwei=3,ohneUebertrag=False,normal=False,schwer=True)',
                          'diviSchr':'erzeugeDivision()',
                          'diviSchr2stellig':'erzeugeDivision(zweiStellig=True)',
                          'diviSchrMitRest':'erzeugeDivision(mitRest=True)',
                          'diviSchrLinienVorg':'erzeugeDivision(nurLinien=True)',
                          'diviSchrSubtrSchritt':'erzeugeDivision(nurSubtraktion=True)',
                          'diviSchrMultiSchritt':'erzeugeDivision(nurMultiplikation=True)',
                          'diviSchrErgEintrSchritt':'erzeugeDivision(nurErgebnisEintragen=True)',
                          'diviSchrRunterzSchritt':'erzeugeDivision(nurRunterZiehen=True)',
                          'diviSchrResteintr':'erzeugeDivision(trageRestEin=True)',
                          'erweitern':'erzeugeErweitern()','kuerzen':'erzeugeKuerzen()','kuerzenMitTeiler':'erzeugeKuerzen(mitTeiler=True)',
                          'reihe':'BruchReiheAufgabe()','reihePosZufaellig':'BruchReiheAufgabe(faktorenBeliebig=True)','bruchVergleichen':'erzeugeBruchVergleichen()',
        'BruchzuGemischteZahl':'erzeugeBruchzuGemischteZahl()', 'GemischteZahlzuBruch':'erzeugeGemischteZahlZuBruch()',
        'Bruchteil':'erzeugeBruchteileBerechnen()','GanzesBerechnen':'erzeugeGemischteZahlZuBruch()',
        'BruchAddSubGleichAddition':"erzeugeBruchAddition(gleichnamig=True,operator='+')",'BruchAddSubGleichSubtraktion':"erzeugeBruchAddition(gleichnamig=True,operator='-')",
        'BruchAddSubUngleichAddition':"erzeugeBruchAddition(gleichnamig=False,operator='+')",'BruchAddSubUngleichSubtraktion':"erzeugeBruchAddition(gleichnamig=False,operator='-')",
        'BruchAddSubBel':"erzeugeBruchAddition(gleichnamig=False,operator=random.choice(['+','-']))",
        'BruchMultiNat':'BruchMitNatuerlicherZahlMulti()',#'BruchDiviNat',
        'zweiBruecheMulti':'zweiBruecheMulti()','zweiBruecheDividieren':'zweiBruecheDividieren()',
        'deziVergl':'deziZahlenVergleichen(nachkommestellen=random.randint(2,5),mitText='+str(mitText)+')',
        'deziStrahl':'erzeugeZahlenstrahleDezimalzahlenEinteilungTikz(laenge=5,anzPfeile=2,zufall=True)',
        'deziRunden':'dezimalzahlenRunden(random.randint(1,4),2,mitText='+str(mitText)+')',
        'deziAddSubEinfach':'deziZahlenAddierenSubtrahieren(1,operator=random.choice(["+","-"]),mitText='+str(mitText)+')',
        'deziAddSub':'deziZahlenAddierenSubtrahieren(random.randint(1,4),operator=random.choice(["+","-"]),mitText='+str(mitText)+')',
        'deziAddSubSchwer':'deziZahlenAddierenSubtrahieren(random.randint(2,5),operator=random.choice(["+","-"]),mitText='+str(mitText)+')',
        'deziMulti1Stelle':'deziZahlenMultiDivi(nachkommastellen=1,operator="*")',
        'deziDivi1Stelle':'deziZahlenMultiDivi(nachkommastellen=1,operator="/")',
        'deziMulti3Stellen': 'deziZahlenMultiDivi(nachkommastellen=3,operator="*")',
        'deziDivi3Stellen': 'deziZahlenMultiDivi(nachkommastellen=3,operator="/")',
        'deziMultiDivi3Stellen': 'deziZahlenMultiDivi(nachkommastellen=3,operator="")',
        'rechneLaengenEinheitenUm':'rechneEinheitenUm(art="laengen")',
        'rechneLaengenEinheitenUmEinschritt':'rechneEinheitenUm(art="laengen",einSchritt=True)',
        'rechneLaengenEinheitenUmEinschrittmitKomma':'rechneEinheitenUm(art="laengen",mitKomma=True)',
        'rechneLaengenEinheitenUmMitKomma':'rechneEinheitenUm(art="laengen",mitKomma=True)',
        'rechneQuadrateEinheitenUm':'rechneEinheitenUm(art="flaechen")','rechneQuadrateEinheitenUmEinschritt':'rechneEinheitenUm(art="flaechen",einSchritt=True)',
        'rechneGewichtEinheitenUmEinschritt':'rechneEinheitenUm(art="gewicht",einSchritt=True)',
        'rechneZeitEinheitenUmEinfachMitKommaEinschrittObenNachUnten':'rechneEinheitenUm("zeit",einSchritt=True,mitKomma=True,einfach=True)',
        'rechneZeitEinheitenUmEinfachMitKomma':'rechneEinheitenUm("zeit",einSchritt=False,mitKomma=True,einfach=True)',
        'rechneZeitEinheitenUmEinfachMitKommaOhneTagUsw':'rechneEinheitenUm("zeitOhne",einSchritt=False,mitKomma=True,einfach=True)',
        'rechneFlaechenEinheitenUmEinfachMitKomma':'rechneEinheitenUm("flaechen",einSchritt=False,mitKomma=True,einfach=False)',
        'GemischteEinheitenAddierenSubtrahieren':'addiereSubtrahiereEinheiten()','LaengenEinheitenAddierenSubtrahieren':'addiereSubtrahiereEinheiten(art="laengen")',
        'GewichtEinheitenAddierenSubtrahieren':'addiereSubtrahiereEinheiten(art="gewicht")','ZeitEinheitenAddierenSubtrahieren':'addiereSubtrahiereEinheiten(art="zeit")',
        'bestimmeUhrzeit':'erzeugeZeitBestimmenAfg()','addiereUhrzeit':'erzeugeAddiereUhrzeit(schwer=False)','addiereUhrzeitSchwer':'erzeugeAddiereUhrzeit(schwer=True)',
        'bestimmeMitteMitSchritt':F'erzeugeMittlerenWertBestimmen(mitSchritt=True,mitText={mitText})',
        'bestimmeMitte':F'erzeugeMittlerenWertBestimmen(mitText={mitText})',
        'loeseKlammerAufRatZahlen':F'erzeugeRationaleZahlenKlammerAufloesen(mitText={mitText})',
        'addRatioZahlen':'erzeugeRationaleZahlenAufgabe(operator="+")','subRatioZahlen':'erzeugeRationaleZahlenAufgabe(operator="-")','addSubRatioZahlen':'erzeugeRationaleZahlenAufgabe()',
        'multiRatioZahlen':'erzeugeRationaleZahlenAufgabeMalGeteilt(operator="*")','diviRatioZahlen':'erzeugeRationaleZahlenAufgabeMalGeteilt(operator="/")','multiDiviRatioZahlen':'erzeugeRationaleZahlenAufgabeMalGeteilt()',
        'zahlenStrahlGanzeZahlen':F'erzeugeZahlenstrahlGanzeZahlen(laenge=4,nurNatuerlich=False,anzPfeile=-1,ohneKammazahlen=True,mitText={mitText})',
        'zahlenStrahlRationaleZahlenEinfach':F'erzeugeZahlenstrahlGanzeZahlen(laenge=4,nurNatuerlich=False,anzPfeile=-1,ohneKammazahlen=True,mitText={mitText})',
        'zahlenStrahlRationaleZahlenSchwer':F'erzeugeZahlenstrahleDezimalzahlenEinteilungTikz(laenge=5,anzPfeile=2,zufall=True,mitText={mitText},rational=True)',
        'UmfangMessen':'erzeugeUmfangRechnung(mitText='+str(mitText)+')' ,
        'FlaecheMessen':'erzeugeFlaechenberechnung(mitText='+str(mitText)+')',
        'FlaecheUmfang':'erzeugeUmfangFlaechenBerechnung(mitText='+str(mitText)+')',
        'propZuordDreisatz':'erzeugeProportionaleDreisatzRechnungen(mitText='+str(mitText)+')',
        'propZuordDreisatzKomma':'erzeugeProportionaleDreisatzRechnungen(komma=True,mitText='+str(mitText)+')',
        'ZusGesetztFlaeche':'erzeugeZusammengesetzRechtecke(n=3,gesamtlaenge=5,hoehe=5,mitText='+str(mitText)+')',
        'ZusGesetztFlaecheSchw':'erzeugeZusammengesetzRechteckeSchwer(n=3,gesamtlaenge=5,maxHoehe=5,mitText='+str(mitText)+')',
        'ProzRechPWert':'erzeugeProzentwertAufgaben(n=1)','ProzRechPsatzWert':'erzeugeProzentsatzAufgaben(n=1)','ProzRechGWert':'erzeugeGrundwertAufgaben(n=1)',
        'ZinsenBerechnen':'erzeugeProzentwertAufgaben(n=1,bez=["Kapital","Zinssatz"],einheit="\\euro{}")',
        'ZinsatzBerechnen':'erzeugeProzentsatzAufgaben(n=1,bez=["Kapital","Zinsen"],einheit="\\euro{}")',
        'KapitalBerechnen':'erzeugeGrundwertAufgaben(n=1,bez=["Zinsen","Zinssatz"],einheit="\\euro{}")',
        'verminderterGrundwert':'erzeugeVerminderteGrundwertAufgaben(1)','vermehrterGrundwert':'erzeugeVermehrterGrundwertAufgaben(1)',
        'verminderterGrundwertMitQ':'erzeugeVerminderteGrundwertAufgaben(1,lsgMitDreisatz=False)','vermehrterGrundwertMitQ':'erzeugeVermehrterGrundwertAufgaben(1,lsgMitDreisatz=False)',
        'TagesMonatsZinsen':'erzeugeTagesMonatsZinsberechnung()',
        'QuaderVolOber':'erzeugeQuaderOberVolBerech(breitePbox=5,maxDim=5,einheit="cm")','ZylinderVolOber':'erzeugeZylibderOberVolBerech(breitePbox=5,maxDim=5,einheit="cm")',
        'QuaderMitLoch':'erzeugeQuaderMitLochBerech(breitePbox=5,maxDim=5)',
        'Dreiecksprisma':'erzeugeDreiecksPrismaOberVolBerech(breitePbox="5",maxDim=5,mitText='+str(mitText)+')',
        'DreiecksprismaMessen':'erzeugeDreiecksPrismaOberVolBerech(breitePbox="5",maxDim=5,mitText='+str(mitText)+',messen=True)',
        'termeUmformen':'erzeugeTermAufgaben(variablen=random.choice(["a","b","x","y","a b","x y"]),anzahl=random.randint(2,4),variMaxAnzProUnterterm=2)',
        'termeUmformenKlammer':'erzeugeTermAufgaben(variablen=random.choice(["a","b","x","y","a b","x y"]),anzahl=random.randint(2,4),variMaxAnzProUnterterm=2,mitKlammer=True)',
        'einfacheGleichung':'erzeugeEinfacheGleichung(variabel=random.choice(["a","b","x","y"]))', 
        'einfacheGleichungOhneKomma':'erzeugeEinfacheGleichung(variabel=random.choice(["a","b","x","y"]),ohneKomma=True)',
        'einfacheGleichungMitKlammer':'erzeugeEinfacheGleichung(variabel=random.choice(["a","b","x","y"]),mitKlammer=True)',
        'einfacheGleichungMitQuadrat':'erzeugeEinfacheGleichung(variabel=random.choice(["a","b","x","y"]),mitKlammer=True,mitQuadrat=True)',
        'einfacheFormelUmformen':'erzeugeEinfacheFormelnUmformen()',
        'propFktZeichnen':'erzeugeAfgLineareFunktionZeichnen(art="prop",steigung=random.choice(["bruch","dezi","nat"]),achsenlaenge=7,maxX=3)',
        'propFktErkennen':'erzeugeAfgLineareFktErkennen(art="prop",steigung="bruch",achsenlaenge=7,maxX=3)',
        'lineareFktZeichnen':'erzeugeAfgLineareFunktionZeichnen(art="linear",steigung=random.choice(["bruch","dezi","nat"]),achsenlaenge=7,maxX=3)',
        'lineareFktErkennen':'erzeugeAfgLineareFktErkennen(art="linear",steigung="bruch",achsenlaenge=7,maxX=3)',
        'umfangsFunktionRechteck':F'erzeugeUmfangsFunktion(typ="Rechteck",mitText={mitText})',
        'umfangsFunktionDreieck':F'erzeugeUmfangsFunktion(typ="Dreieck",mitText={mitText})',
        'einfacheGleichungZweiVariablen':'erzeugeGleichungmitZweiVariablen()',
        'einfacheGleichungZweiVariablenZeichnen':'erzeugeGleichungmitZweiVariablenZeichnen()',
        'ZweiGleichungmitZweiVariablenZeichnen':'erzeugeZweiGleichungmitZweiVariablen(zeichnerisch=True)',
        'ZweiGleichungmitZweiVariablenGleichsetzen':'erzeugeZweiGleichungmitZweiVariablen(zeichnerisch=False)',
        'quadratwurzelEinfach':'erzeugeWurzelRechnungen(typ="Einfach")',
        'quadratwurzelBruchEinzeln':'erzeugeWurzelRechnungen(typ="Bruch Einzeln")',
        'quadratwurzelBruch':'erzeugeWurzelRechnungen(typ="Bruch")',
        'quadratwurzelDezimalzahlenEinfach':'erzeugeWurzelRechnungen(typ="Dezimalwurzel Einfach")',
        'quadratwurzelDezimalzahlen':'erzeugeWurzelRechnungen(typ="Dezimalwurzel")',
        'quadratwurzelBeliebig':'erzeugeWurzelRechnungen(typ="")',
        'quadratwurzelUmfangBerechnen':'erzeugeWurzelUmfangsberechnungVomQuadrat()',
        'quadratwurzelZwischenNatZahl':'zwischenWelcheNatZahlen(mitText='+str(mitText)+')',
        'quadratwurzelQuaderOberfl':'wurzelOberflaecheWurfel()',
        'quadratwurzelQuaderZusammengesOberfl':'wurzelOberflaecheWurfel(zusammengesetzt=True)',
        'quadratwurzelTeilweise':'teilweiseWurzelziehen(mitText='+str(mitText)+')',
        'quadratwurzelTeilweiseSchwer':'teilweiseWurzelziehen(mitText='+str(mitText)+',einfach=False)',
        'quadratwurzelZusammenziehen':'wurzelnZusammenZiehen()',
        'quadratwurzelAddieren':'wurzelnAddieren(anzahl=random.randint(2,3),mitText='+str(mitText)+')',
        'pythagorasFormulierenSeiten':'erzeugePythagorasFormulieren(seitenBeshr=True,pktBeschr=False,gemischt=False,mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasFormulierenSeitenOhneBogen':'erzeugePythagorasFormulieren(seitenBeshr=True,pktBeschr=False,gemischt=False,mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasFormulierenPunkte':'erzeugePythagorasFormulieren(seitenBeshr=False,pktBeschr=True,gemischt=False,mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasFormulierenPunkteOhneBogen':'erzeugePythagorasFormulieren(seitenBeshr=False,pktBeschr=True,gemischt=False,mitBogen=False,mitText='+str(mitText)+')',
        'pythagorasFormulierenGemischt':'erzeugePythagorasFormulieren(seitenBeshr=False,pktBeschr=False,gemischt=True,mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasFormulierenGemischtOhneBogen':'erzeugePythagorasFormulieren(seitenBeshr=False,pktBeschr=False,gemischt=True,mitBogen=False,mitText='+str(mitText)+')',
        'pythagorasHypBerechnenMitBogen':'erzeugePythagorasBerechnen(seitenwahl=2,mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasKathBerechnenMitBogen':'erzeugePythagorasBerechnen(seitenwahl=random.randint(0,1),mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasHypBerechnenOhneBogen':'erzeugePythagorasBerechnen(seitenwahl=2,mitBogen=False,mitText='+str(mitText)+')',
        'pythagorasKathBerechnenOhneBogen':'erzeugePythagorasBerechnen(seitenwahl=random.randint(0,1),mitBogen=False,mitText='+str(mitText)+')',
        'pythagorasBerechnenMitBogen':'erzeugePythagorasBerechnen(seitenwahl=-1,mitBogen=True,mitText='+str(mitText)+')',
        'pythagorasBerechnenOhneBogen':'erzeugePythagorasBerechnen(seitenwahl=-1,mitBogen=False,mitText='+str(mitText)+')',
        'pythagorasUmfangTrapezEinfach':'erzeugeTrapezUmfangBerechnung(mitText='+str(mitText)+')',
        'kreisRadius':F'erzeugeKreisberechnungen(typ="Radius",mitText={mitText})',
        'kreisUmfang':F'erzeugeKreisberechnungen(typ="Umfang",mitText={mitText})',
        'kreisFlaeche':F'erzeugeKreisberechnungen(typ="Flaeche",mitText={mitText})',
        'kreisUmfangFlaeche':F'erzeugeKreisberechnungen(typ="UmfangFlaeche",mitText={mitText})',
        'kreisUmfangNachFlaeche':F'erzeugeKreisberechnungen(typ="UmfachNachFlaeche",mitText={mitText})',
        'kreisFlaecheNachUmfang':F'erzeugeKreisberechnungen(typ="FlaecheNachUmfang",mitText={mitText})',
        'kreisFlaecheUmfKreisabschnitt':F'erzeugeUmfangFlaecheKreisabschnitt(mitText={mitText})',
        'kreisUmfangDreieckHalbkreis':F'umfangDreieckMitHalbkreis(mitText={mitText})',
        'strahlensatzFarbig':F'erzeugeStrahlensaetzeAufgaben(mitText={mitText})',
        'geschwGeschwBerechnen':F'erzeugeGeschwindigkeitsBerechnungen(typ="Geschwindigkeit",einheit=random.choice(["m/s","km/h"]),umrechnen=False,mitText={mitText})',
        'geschwGeschwBerechnenHS':F'erzeugeGeschwindigkeitsBerechnungen(typ="Geschwindigkeit",einheit=random.choice(["m/s","km/h"]),umrechnen=False,mitText={mitText},hauptschule=True)',
        'geschwGeschwBerechnenSchwer':F'erzeugeGeschwindigkeitsBerechnungen(typ="Geschwindigkeit",einheit=random.choice(["m/s","km/h"]),umrechnen=False,einfach=False,mitText={mitText})',
        'geschwBeliebigBerechnen':F'erzeugeGeschwindigkeitsBerechnungen(typ="",einheit=random.choice(["m/s","km/h"]),umrechnen=False,mitText={mitText})',
        'geschwBeliebigBerechnenHS':F'erzeugeGeschwindigkeitsBerechnungen(typ="",einheit=random.choice(["m/s","km/h"]),umrechnen=False,mitText={mitText},hauptschule=True)',
        'geschwBeliebigBerechnenSchwer':F'erzeugeGeschwindigkeitsBerechnungen(typ="",einheit=random.choice(["m/s","km/h"]),umrechnen=False,einfach=False,mitText={mitText})',
        'geschwGeschwBerechnenEinheitBeliebig':F'erzeugeGeschwindigkeitsBerechnungen(typ="Geschwindigkeit",einheit=random.choice(["m/s","km/h"]),umrechnen=True,mitText={mitText})',
        'geschwBeliebigBerechnenEinheitBeliebig':F'erzeugeGeschwindigkeitsBerechnungen(typ="",einheit=random.choice(["m/s","km/h"]),umrechnen=True,mitText={mitText})',
        'zeitWegDiagramm':F'erzeugeDiagrammErstellAufgaben(typ="Zeit-Weg",mitText={mitText})',
        'zeitWegDiagrammOhneDiaVorgabe':F'erzeugeDiagrammErstellAufgaben(typ="Zeit-Weg",diagrammVorgegeben=False,mitText={mitText})',
        'zeitWegDiagrammNurText':F'erzeugeDiagrammErstellAufgaben(typ="Zeit-Weg",diagrammVorgegeben=False,mitText={mitText},nurText=True)',
        'beschlBeliebigBerechnen':F'erzeugeBeschlBerechnungen(typ="",mitText={mitText})',
    }
    return eval(rechnungsFunktionen[art])


def MoeglicheRechnungen(auswahl='keys'):
    listeRechnungen={'Basisaufgaben':[('Basis','Plus, Minus, Mal, Geteil'),('Kopf','Kopfrechenaufgaben')],
                     'Schriftliche Add-Sub':[('addSchriftLeicht','Addition Leicht'),('addSchrift','Addition Normal'),('addSchriftSchwer','Addition Schwer'),('subSchriftLeicht','Subtraktion Leicht'),('subSchrift','Subtraktion Normal'),('subSchriftSchwer','Subtraktion Schwer'),('addSubSchriftLeicht','Zufällig Leicht'),('addSubSchrift','Zufällig Normal'),('addSubSchriftSchwer','Zufällig Schwer')],
                     'Schriftl. Multi.-Division':[('multiSchrEinFaktorOhneUbertrag','Multi. Fakt einstellig ohne Übertrag'),('multiSchrEinFaktorMitUbertrag','Multi. Fakt einstellig mit Übertrag'),('multiSchr','Schriftliche Multiplikation'),('multiSchrSchwer','Schrft. Multiplikation Schwer'),('diviSchr','Division'),('diviSchr2stellig','Division 2 Stellig'),('diviSchrMitRest','Division mit Rest'),('diviSchrLinienVorg','Div. Linien Vorgegeben'),('diviSchrSubtrSchritt','Division Subtraktionsschritt'),('diviSchrMultiSchritt','Division Multiplikationsschritt'),('diviSchrRunterzSchritt','Division Runterziehen'),('diviSchrResteintr','Division Rest eintragen'),('diviSchrErgEintrSchritt','Division Ergebnis Eintragen')],
                     'Bruch-Grundlagenaufgaben': [('ggT','Größter gemeinsamer Teiler'),('kgV','Kleinstes gemeinsames Vielfache'),('erweitern','Erweitern'),('kuerzen','Kürzen'),('kuerzenMitTeiler','Kürzen mit Teiler'),('reihe','Bruch in einer Reihe'),('reihePosZufaellig','Bruch in Reihe Position Zufällig'),('bruchVergleichen','Brüche Vergleichen'),('BruchzuGemischteZahl','Bruch zur gemischten Zahl'),('GemischteZahlzuBruch','Gemischte Zahl zu Bruch')],
                     'Bruchrechen':[('BruchAddSubGleichAddition','Brüche Addieren gleicher Nenner'),('BruchAddSubGleichSubtraktion','Brüche Subtraktion gleicher Nenner'),('BruchAddSubUngleichAddition','Brüche Addition Ungleicher Nenner'),('BruchAddSubUngleichSubtraktion','Brüche Subtraktion ungleicher Nenner'),('BruchAddSubBel','Brüche Addieren/Subtrahieren'),('BruchMultiNat','Bruch mit natürlicher Zahle multiplizieren'),('zweiBruecheMulti','Zwei Brüche multiplizieren'),('zweiBruecheDividieren','Zwei Brüche dividieren')],
                     'Dezimalzahlen':[('deziVergl','Vergleichen'),('deziStrahl','Zahlenstrahl'),('deziRunden','Runden'),('deziAddSubEinfach','Addieren/Subtrahieren leicht'),('deziAddSub','Addieren/Subtrahieren'),('deziAddSubSchwer','Addieren/Subtrahieren schwer'),('deziMulti1Stelle','Multiplizieren 1 Stelle'),('deziDivi1Stelle','Dividieren 1 Stelle'),('deziMulti3Stellen','Multiplizieren 3 Stellen'),('deziDivi3Stellen','Dividieren 3 Stellen'),('deziMultiDivi3Stellen','Multi/Divi 3 Stellen')],
                     'Quadratwurzeln':[('quadratwurzelEinfach','Einfach'),('quadratwurzelBruchEinzeln','Wurzel nur im Nenner'),('quadratwurzelBruch','Wurzel im Bruch'),('quadratwurzelDezimalzahlenEinfach','Dezimalzahlen Einfach'),('quadratwurzelDezimalzahlen','Dezimalzahlen'),('quadratwurzelBeliebig','Gemischt'),('quadratwurzelUmfangBerechnen','Umfang berechnen'),('quadratwurzelQuaderOberfl','Kantlaenge vom Quader'),('quadratwurzelQuaderZusammengesOberfl','Kantlaenge vom zusammenges. Quader'),('quadratwurzelZwischenNatZahl','Zwischen welcher Nat. Zahl liegt?'),('quadratwurzelAddieren','Wurzeln Addieren/Subtrahieren'),('quadratwurzelZusammenziehen','Wurzel erst vereinen'),('quadratwurzelTeilweise','Wurzel Teilweise ziehen'),('quadratwurzelTeilweiseSchwer','Wurzel Teilweise ziehen Schwer')],
                     'Pythagoras': [('pythagorasFormulierenSeiten','Formulieren Seiten Beschr. mit recht. Winkel.'),('pythagorasFormulierenSeitenOhneBogen','Formulieren Seiten Beschr.'),('pythagorasFormulierenPunkte','Formulieren Punkte Beschr. mit recht. Winkel'),('pythagorasFormulierenPunkteOhneBogen','Formulieren Punkte Beschr.'),('pythagorasFormulierenGemischt','Formlieren Gemischt mit recht. Winkel'),('pythagorasFormulierenGemischtOhneBogen','Formlieren Gemischt'),('pythagorasHypBerechnenMitBogen','Hyp. berechnen mit recht. Winkel'),('pythagorasHypBerechnenOhneBogen','Hyp. berechnen ohne recht. Winkel'),('pythagorasKathBerechnenMitBogen','Kath. berechnen mit recht. Winkel'),('pythagorasKathBerechnenOhneBogen','Kath. berechnen ohne recht. Winkel'),('pythagorasBerechnenMitBogen','Bel. berechnen mit recht. Winkel'),('pythagorasBerechnenOhneBogen','Bel. berechnen ohne recht. Winkel'),('pythagorasUmfangTrapezEinfach','Ber. Umfang vom Trapez')],
                     'Kreis':[('kreisUmfang','Umfang Berechnen'),('kreisFlaeche','Fläche Berechnen'),('kreisUmfangFlaeche','Umfang/Fläche Berechnen'),('kreisRadius','Radius Berechnen'),('kreisUmfangNachFlaeche','Umfang nach Flaeche'),('kreisFlaecheNachUmfang','Fläche nach Umfang'),('kreisFlaecheUmfKreisabschnitt','Kreisabschnitt'),('kreisUmfangDreieckHalbkreis','Umfang Berechnen von Dreieck mit Halbkreis')],
                     'Geometrie':[('strahlensatzFarbig','Strahlensatz Farbig')],
                     'Einheiten':[('rechneLaengenEinheitenUm','Längen umrechnen'),('rechneLaengenEinheitenUmEinschritt','Längeneinheiten umrechnen nur eine Größenordnung'),('rechneLaengenEinheitenUmEinschrittmitKomma','Längeneinheiten, eine Größenordnung, mit Komma'),('rechneLaengenEinheitenUmMitKomma','Längen umrechnen mit Komma'),('rechneQuadrateEinheitenUm','Flächeneinheiten Umrechnen'),('rechneQuadrateEinheitenUmEinschritt','Flächeneinheiten umrechnen nur eine Größenordnung'),('rechneFlaechenEinheitenUmEinfachMitKomma','Flächeneinheiten Umrechnen mit Komma'),('rechneGewichtEinheitenUmEinschritt','Gewichtseinheiten umrechnen'),('rechneZeitEinheitenUmEinfachMitKommaEinschrittObenNachUnten','Zeiteinheiten umrechnen nur eine Größenordnung Mit Komma'),('rechneZeitEinheitenUmEinfachMitKomma','Zeiteinheiten umrechnen mit Komma'),('rechneZeitEinheitenUmEinfachMitKommaOhneTagUsw','Zeiteinheiten umrechnen ohne Tag, Woche usw.'),('GemischteEinheitenAddierenSubtrahieren','Gemischte Einheiten Addieren'),('LaengenEinheitenAddierenSubtrahieren','Längeneinheiten Addieren/Subtrahieren'),('GewichtEinheitenAddierenSubtrahieren','Gewichtseinheiten Addieren/Subtrahieren'),('ZeitEinheitenAddierenSubtrahieren','Zeiteinheiten Addieren/Subtrahieren')],
                     'Zeiten':[('bestimmeUhrzeit','Uhrzeit ablesen'),('addiereUhrzeit','Zeiten addieren'),('addiereUhrzeitSchwer','Zeiten addieren Schwer')],
                     'Rationale Zahlen':[('bestimmeMitteMitSchritt','Bestimme den mittleren Wert mit vorg. Schritt'),('bestimmeMitte','Bestimme den mittleren Wert'),('loeseKlammerAufRatZahlen','loese Klammer auf'),('addRatioZahlen','Rat. Zahl. Addieren'),('subRatioZahlen','Rat. Zahl. Subtrahieren'),('addSubRatioZahlen','Rat. Zahl. Add oder Sub Zufällig'),('multiRatioZahlen','Rat. Zahl. Multiplizieren'),('diviRatioZahlen','Rat. Zahl. Dividieren'),('multiDiviRatioZahlen','Rat. Zahl. Mult. oder Divi Zufällig'),('zahlenStrahlGanzeZahlen','Zahlenstrahl Ganze Zahlen'),('zahlenStrahlRationaleZahlenEinfach','Zahlenstrahl einfach Rat. Zahlen'),('zahlenStrahlRationaleZahlenSchwer','Zahlenstrahl Rat. Zahlen')],
                     'Rechteck Flächen und Umfänge':[('UmfangMessen','Umfänge bestimmen'),('FlaecheMessen','Flächen bestimmen'),('FlaecheUmfang','Fläche und Umfänge bestimmen'),('ZusGesetztFlaeche','Zusammengesetzte Flächen bestimmen'),('ZusGesetztFlaecheSchw','Zusammengesetzte Flächen bestimmen Schwer')],
                     'Zuordnungen':[('propZuordDreisatz','Dreisatz'),('propZuordDreisatzKomma','Dreisatz mit Komma')],
                     'Prozent- und Zinsrechnung':[('ProzRechPWert','Prozentwert berechnen'),('ProzRechPsatzWert','Prozentsatz berechnen'),('ProzRechGWert','Grundwert berechnen'),('ZinsenBerechnen','Zinsen berechnen'),('ZinsatzBerechnen','Zinsatz berechnen'),('KapitalBerechnen','Kapital berechnen'),('verminderterGrundwert','verminderten G-Wert berechnen'),('vermehrterGrundwert',' vermehrten G-Wert berechnen'),('verminderterGrundwertMitQ','vermin. G-Wert mit q berechnen'),('verminderterGrundwertMitQ','vermehr. G-Wert mit q berechnen'),('TagesMonatsZinsen','Tages- Monatszinsen berechnen')],
                     'Prismen':[('QuaderVolOber','Vol., Oberfl. Quader'),('ZylinderVolOber','Vol., Oberfl. Zylinder'),('QuaderMitLoch','Vol., Oberfl. Quader Mit Loch'),('Dreiecksprisma','Dreiecksprisma'),('DreiecksprismaMessen','Dreiecksprisma Seiten messen')],
                     'Terme und Gleichungen':[('termeUmformen','Terme umformen'),('termeUmformenKlammer','Terme mit Klammern umformen'),('einfacheGleichung','einfache Gleichung lösen'),('einfacheGleichungOhneKomma','einfache Gleichung lösen Ohne Komma'),('einfacheGleichungMitKlammer','einf. Gleichung mit Klammer lösen'),('einfacheGleichungMitQuadrat','einf. Gl. mit Kl. und Quadrat lösen'),('einfacheFormelUmformen','Einfache Formeln umformen')],
                     'Gleichungssysteme':[('einfacheGleichungZweiVariablen','einf. Gl. mit 2 Variablen'),('einfacheGleichungZweiVariablenZeichnen','einf. Gl. mit 2 Vari. Zeichnen'),('ZweiGleichungmitZweiVariablenZeichnen','2 Gl. durch zeichnen loesen'),('ZweiGleichungmitZweiVariablenGleichsetzen','2 Gl. durch gleichsetzen loesen')],
                     'Funktionen':[('propFktZeichnen','Proportionale Fkten zeichnen'),('propFktErkennen','Proportionale Fkten erkennen'),('lineareFktZeichnen','Lineare Fkten zeichnen'),('lineareFktErkennen','Lineare Fkten erkennen'),('umfangsFunktionRechteck','Bestimme Rechteck Umfangsfunktion'),('umfangsFunktionDreieck','Bestimme Dreieck Umfangsfunktion')],
                     'Physik': [('geschwGeschwBerechnen', 'Berechne die Geschw.'),('geschwGeschwBerechnenHS', 'Berechne die Geschw. für HS'),('geschwBeliebigBerechnen', 'Berechne fehl. Wert Geschw.'),('geschwBeliebigBerechnenHS', 'Berechne fehl. Wert Geschw. für HS'),('geschwGeschwBerechnenSchwer', 'Berechne die Geschw. mit Komma'),('geschwBeliebigBerechnenSchwer', 'Berechne fehl. Wert Geschw. mit Komma'),('geschwGeschwBerechnenEinheitBeliebig', 'Berechne Gesch. mit bel. Einheiten.'),('geschwBeliebigBerechnenEinheitBeliebig', 'Berechne fehl. Wert mit bel. Einheiten.'),('zeitWegDiagramm','Zeit Weg Diagramm'),('zeitWegDiagrammOhneDiaVorgabe','Zeit Weg Dia ohne Dia. Vorgabe'),('zeitWegDiagrammNurText','Zeit Weg Dia ohne Vorgabe'),('beschlBeliebigBerechnen', 'Berechne fehl. Wert Beschl.')]
    }
    if auswahl in listeRechnungen.keys():
        return listeRechnungen[auswahl]
    else:
        if auswahl=='keys':
            return list(listeRechnungen.keys())
        else:
            return []