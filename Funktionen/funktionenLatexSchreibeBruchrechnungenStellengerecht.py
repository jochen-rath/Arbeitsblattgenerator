#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def schreibeBruchErweitern(rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[]):
#Diese Funktion schreibt eine Bruchrechnung zum Erweitern stellengerecht in ein Karopapier. Jeder Zahl in ein Karo.
#
#       startzeile=schreibeBruchErweitern(rechnungen,tabellenWerte,tabellenWerteNr,startZeile)
#
#               rechnung: Rechenaufgabe, Bsp: Erweiter mit dem Faktor 5:\frac{5}{6}
#                         Wichtige Zahlenreihenfolge: Erst Faktor, dann Zähler, dann Nenner.
#          tabellenWerte: Liste mit Tabellen
#        tabellenWerteNr: tabellennummer, in welche Tablle das Ergebniss kommt.
#             startzeile: Ab welcher Zeile soll die Erweiterung geschrieben werden?
#
#Achtung: Derzeit wird kein Gleichheitszeichen eingefügt. Das muss nachträglich mit xournallpp eingefügt werden.
    k=0 if startZeile is None else startZeile 
    gz='\\Rnode{marker}{} &'  #gleichheitszeichen
    spalte1=3
    tabellenLinie='\\\\'
    n=spalte1
    faktor=rechnungen[1][0]
    zaehler=rechnungen[1][1]
    nenner=rechnungen[1][2]
    print(faktor)
    zf=str(int(zaehler)*int(faktor))
    nf=str(int(nenner)*int(faktor))
    bruch=[[zaehler,nenner],[zaehler+'*'+faktor,nenner+'*'+faktor],[zf,nf]]
    return schreibeReihenBruchInStellenAusListe(bruch,rechnungen,tabellenWerte,tabellenWerteNr,startZeile=k,markers=markers)

def schreibeBruchKuerzen(rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[]):
#Diese Funktion schreibt eine Bruchrechnung zum Kürzen stellengerecht in ein Karopapier. Jeder Zahl in ein Karo.
#
#       startzeile=schreibeBruchErweitern(rechnungen,tabellenWerte,tabellenWerteNr,startZeile)
#
#               rechnung: Rechenaufgabe, Bsp: Kuerze:\frac{4}{8}
#                         Wichtige Zahlenreihenfolge: Erst Zähler, dann Nenner.
#          tabellenWerte: Liste mit Tabellen
#        tabellenWerteNr: tabellennummer, in welche Tablle das Ergebniss kommt.
#             startzeile: Ab welcher Zeile soll die Erweiterung geschrieben werden?
#
#Achtung: Derzeit wird kein Gleichheitszeichen eingefügt. Das muss nachträglich mit xournallpp eingefügt werden.
    gz='\\Rnode{marker}{} &'  #gleichheitszeichen
    spalte1=3
    tabellenLinie='\\\\'
    n=spalte1
    zaehler=rechnungen[1][0]
    nenner=rechnungen[1][1]
    teiler=str(ggt(int(zaehler),int(nenner)))
    if 'mit' in rechnungen[1]:
       teiler=rechnungen[1][0]
       zaehler=rechnungen[1][1]
       nenner=rechnungen[1][2]
    zK=str(int(zaehler)/int(teiler))
    nK=str(int(nenner)/int(teiler))
    k=0 if startZeile is None else startZeile     
    bruch=[[zaehler,nenner],[zaehler+':'+teiler,nenner+':'+teiler],[zK,nK]]
    return schreibeReihenBruchInStellenAusListe(bruch,rechnungen,tabellenWerte,tabellenWerteNr,startZeile=k,markers=markers)

def schreibenReihenBruch(rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[]):
#Diese Funktion schreibt eine Bruchrechnung zum Erweitern stellengerecht in ein Karopapier. Jeder Zahl in ein Karo.
#
#       startzeile=schreibeBruchErweitern(rechnungen,tabellenWerte,tabellenWerteNr,startZeile)
#
#               rechnung: Rechenaufgabe, Bsp: Erweiter mit dem Faktor 5:\frac{5}{6}
#                         Wichtige Zahlenreihenfolge: Erst Faktor, dann Zähler, dann Nenner.
#          tabellenWerte: Liste mit Tabellen
#        tabellenWerteNr: tabellennummer, in welche Tablle das Ergebniss kommt.
#             startzeile: Ab welcher Zeile soll die Erweiterung geschrieben werden?
#
#Achtung: Derzeit wird kein Gleichheitszeichen eingefügt. Das muss nachträglich mit xournallpp eingefügt werden.
    gz='\\Rnode{marker}{} &'  #gleichheitszeichen
    k=0 if startZeile is None else startZeile     
    spalte1=3
    tabellenLinie='\\\\'
    n=spalte1
#Finde den kompletten Bruch in der Aufgabe
    bruch=re.findall(r'{\d+}{\d+}',rechnungen[1])
#Finde alle nicht kompletten Brueche
    bruch=map(int,re.findall(r'\d+',bruch[0]))
    print(bruch)
#Berechne jeden Faktor, mit dem der erste Bruch mal genommen wurde.
    print(re.findall(r'{}{\d+}',rechnungen[1]))
    faktoren=[int(int(re.findall(r'\d+',x)[0])/bruch[1]) for x in re.findall(r'{}{\d+}',rechnungen[1])]
#Schreibe alle Brueche in eine Liste
    lsg=[map(str,bruch)]
    for f in faktoren:
        lsg.append([str(bruch[0]*f),str(bruch[1]*f)])
    return schreibeReihenBruchInStellenAusListe(lsg,rechnungen,tabellenWerte,tabellenWerteNr,startZeile=k,markers=markers)

def schreibenReihenBruchListe(rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[]):
#Diese Funktion schreibt eine Bruchrechnung zum Erweitern stellengerecht in ein Karopapier. Jeder Zahl in ein Karo.
#
#       startzeile=schreibeBruchErweitern(rechnungen,tabellenWerte,tabellenWerteNr,startZeile)
#
#               rechnung: Rechenaufgabe, Bsp: Erweiter mit dem Faktor 5:\frac{5}{6}
#                         Wichtige Zahlenreihenfolge: Erst Faktor, dann Zähler, dann Nenner.
#          tabellenWerte: Liste mit Tabellen
#        tabellenWerteNr: tabellennummer, in welche Tablle das Ergebniss kommt.
#             startzeile: Ab welcher Zeile soll die Erweiterung geschrieben werden?
#
#Achtung: Derzeit wird kein Gleichheitszeichen eingefügt. Das muss nachträglich mit xournallpp eingefügt werden.
#Finde den kompletten Bruch in der Aufgabe
    bruch=[map(int,x) for x in rechnungen[1] if len(x[0])>0][0]
    print(bruch)
    teiler=1.0*bruch[0]/bruch[1]
#Berechne jeden Bruch, mit dem der erste Bruch mal genommen wurde.
    lsg=[[str(int(int(x[1])*teiler)),x[1]] for x in rechnungen[1]]
    return schreibeReihenBruchInStellenAusListe(lsg,rechnungen,tabellenWerte,tabellenWerteNr,startZeile=startZeile,markers=markers)

def schreibeBruchVergleichenAufgabe(rechnung,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[],markerNr='a',mitLSG=False):
    tabellenLinie='\\\\'
    k=0 if startZeile is None else startZeile
    spalte1=3
    aufgabenAbstand=4
    vzMarker='\\Rnode{marker}{} &'  #vergleichszeichen
    count=1
    for r in rechnung:
        zaehlerZeile=[]
        nennerZeile=[]
        for buchstabe,b1,vz,b2 in r:
            if len(b1)>2 and mitLSG:
                zaehlerZeile=zaehlerZeile+[buchstabe+' &']+[x+'&' for x in b1[0]]+[' &']+[x+'&' for x in b1[2]]+[' &']+[x+'&' for x in b2[2]]+[' &']+[x+'&' for x in b2[0]]+[' &']*aufgabenAbstand
            else:
                zaehlerZeile=zaehlerZeile+[buchstabe+' &']+[x+'&' for x in b1[0]]+[' &']+[x+'&' for x in b2[0]]+[' &']*aufgabenAbstand
            markers.append([markerNr+str(count),vz])
            count=count+1
            if len(b1)>2 and mitLSG:   
                markers.append([markerNr+str(count),'='])
                count=count+1
                markers.append([markerNr+str(count),'='])
                count=count+1
                nennerZeile=nennerZeile+[' &']+  [x+'&' for x in b1[1]]+[vzMarker.replace('marker',markers[-2][0])]+[x+'&' for x in b1[3]]+[vzMarker.replace('marker',markers[-3][0])]+[x+'&' for x in b2[3]]+[vzMarker.replace('marker',markers[-1][0])]+[x+'&' for x in b2[1]]+[' &']*aufgabenAbstand
            else:
                nennerZeile=nennerZeile+[' &']+  [x+'&' for x in b1[1]]+[vzMarker.replace('marker',markers[-1][0])]+[x+'&' for x in b2[1]]+[' &']*aufgabenAbstand
#Schreibe die Zeilen in die Tabelle
        m=len(zaehlerZeile)
        tabellenWerte[tabellenWerteNr][k][spalte1-1:spalte1+m]=zaehlerZeile
        m=len(nennerZeile)
        tabellenWerte[tabellenWerteNr][k+1][spalte1-1:spalte1+m]=nennerZeile #Bruchstriche: LaengeStrich=lS
        lS=[1,spalte1-1]
        for i,b in enumerate(r):
            b=b[1:] #Entferne den Buchstaben aus b,damit die Linien wieder passen
            lS[1]=lS[1]+1
            tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[0][:2])))+'}\\arrayrulecolor{lightgray}'
            lS=[lS[1]+max(map(len,b[0][:2]))+1,lS[1]+1+max(map(len,b[0][:2]))]
            if len(b[0])>2 and mitLSG:
                tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[0][2:])))+'}\\arrayrulecolor{lightgray}'
                lS=[lS[1]+max(map(len,b[0][2:]))+1,lS[1]+1+max(map(len,b[0][2:]))]  
            if len(b[2])>2 and mitLSG:
               tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[2][2:])))+'}\\arrayrulecolor{lightgray}'
               lS=[lS[1]+1+max(map(len,b[2][2:])),lS[1]+max(map(len,b[2][2:]))+1]   
            tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[2][:2])))+'}\\arrayrulecolor{lightgray}'
            lS=[lS[1]+1+max(map(len,b[2][:2])),lS[1]+aufgabenAbstand+max(map(len,b[2][:2]))]
        tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(len(tabellenWerte[tabellenWerteNr][0])-1)+'}'
        tabellenWerte[tabellenWerteNr][k][-1]=tabellenLinie
        k=k+3
    return markers

def schreibeBruchVergleichenAufgabeNebeneinander(rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,anzNeben=3):
    tabellenLinie='\\\\'
    k=2 if startZeile is None else startZeile
    spalte1=2
    aufgabenAbstand=3
    count=1
    anzReihen=int(len(rechnungen)/anzNeben)
    print('anzReihen='+str(anzReihen))
    for i in range(anzReihen):
        zaehlerZeile=[]
        nennerZeile=[]
        for r in rechnungen[i*anzNeben:i*anzNeben+anzNeben]:
            print('rechnungen Auswahl='+str(r[0]))
            buchstabe,b1,vz,b2 = r[0]
            zaehlerZeile=zaehlerZeile+[buchstabe+' &']+[x+'&' for x in b1[0]]+[' &']+[x+'&' for x in b2[0]]+[' &']*aufgabenAbstand
            count=count+1
            nennerZeile=nennerZeile+[' &']  +[x+'&' for x in b1[1]]+[' &']+[x+'&' for x in b2[1]]+[' &']*aufgabenAbstand
#Schreibe die Zeilen in die Tabelle
        m=len(zaehlerZeile)
        tabellenWerte[tabellenWerteNr][k][spalte1-1:spalte1+m]=zaehlerZeile
        m=len(nennerZeile)
        tabellenWerte[tabellenWerteNr][k+1][spalte1-1:spalte1+m]=nennerZeile #Bruchstriche: LaengeStrich=lS
        lS=[1,spalte1-1]
        for j,b in enumerate(rechnungen[i*anzNeben:i*anzNeben+anzNeben]):
            b=b[0][1:] #Entferne den Buchstaben aus b,damit die Linien wieder passen
            lS[1]=lS[1]+1
            print('b='+str(b))
            tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[0][:2])))+'}\\arrayrulecolor{lightgray}'
            lS=[lS[1]+max(map(len,b[0][:2]))+1,lS[1]+1+max(map(len,b[0][:2]))]  
            tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[2][:2])))+'}\\arrayrulecolor{lightgray}'
            lS=[lS[1]+1+max(map(len,b[2][:2])),lS[1]+aufgabenAbstand+max(map(len,b[2][:2]))]
        tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(len(tabellenWerte[tabellenWerteNr][0])-1)+'}'
        tabellenWerte[tabellenWerteNr][k][-1]=tabellenLinie
        k=k+10
    return

def schreibeReihenBruchInStellenAusListe(lsg,rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[],markerNr='g'):
#Diese Funktion bekommt eine Liste mit Bruechen in Stringformat:
#lsg=[['4','5'],['8','10'],['40','50']....
#Und schreibt diese Korrekt in ein Karopapiert.
    tabellenLinie='\\\\'
    k=0 if startZeile is None else startZeile
    spalte1=3
    gz='\\Rnode{marker}{} &'  #gleichheitszeichen
#Zeichenlaenge
    zLen=[max(map(len,x)) for x in lsg]
#Erzeuge die Zaehler und Nennerzeile
    zaehlerZeile=[rechnungen[0]+'&']+[' &']*(zLen[0]-len(lsg[0][0]))+[x+'&' for x in lsg[0][0]]
    nennerZeile=               ['&']+[' &']*(zLen[0]-len(lsg[0][1]))+[x+'&' for x in lsg[0][1]]
    count=1
    for i in range(1,len(lsg)):
        zaehlerZeile=zaehlerZeile+['&']+[' &']*(zLen[i]-len(lsg[i][0]))+[x+'&' for x in lsg[i][0]]
        markers.append(markerNr+rechnungen[0][0]+str(count))
        nennerZeile=nennerZeile+[gz.replace('marker',markers[-1])]+[' &']*(zLen[i]-len(lsg[i][1]))+[x+'&' for x in lsg[i][1]]
        count=count+1    
#Schreibe die Zeilen in die Tabelle
    m=len(zaehlerZeile)
    tabellenWerte[tabellenWerteNr][k][spalte1-1:spalte1+m]=zaehlerZeile
    m=len(nennerZeile)
    tabellenWerte[tabellenWerteNr][k+1][spalte1-1:spalte1+m]=nennerZeile
#Bruchstriche: LaengeStrich=lS
    lS=[1,spalte1]
    for i in range(len(lsg)):
        tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+zLen[i])+'}\\arrayrulecolor{lightgray}'
        lS=[lS[1]+1+zLen[i],lS[1]+1+zLen[i]]
    tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(len(tabellenWerte[tabellenWerteNr][0])-1)+'}'
    tabellenWerte[tabellenWerteNr][k][-1]=tabellenLinie
    return k+3,markers

def schreibenReihenBruchBeliebig(rechnungen,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[]):
#Diese Funktion schreibt eine Bruchrechnung zum Erweitern stellengerecht in ein Karopapier. Jeder Zahl in ein Karo.
#
#       startzeile=schreibeBruchErweitern(rechnungen,tabellenWerte,tabellenWerteNr,startZeile)
#
#               rechnung: Rechenaufgabe, Bsp: Erweiter mit dem Faktor 5:\frac{5}{6}
#                         Wichtige Zahlenreihenfolge: Erst Faktor, dann Zähler, dann Nenner.
#          tabellenWerte: Liste mit Tabellen
#        tabellenWerteNr: tabellennummer, in welche Tablle das Ergebniss kommt.
#             startzeile: Ab welcher Zeile soll die Erweiterung geschrieben werden?
#
#Achtung: Derzeit wird kein Gleichheitszeichen eingefügt. Das muss nachträglich mit xournallpp eingefügt werden.
    k=0 if startZeile is None else startZeile     
    spalte1=3
    n=spalte1
#Finde den kompletten Bruch in der Aufgabe
    bruch=[x for x in rechnungen[1] if len(x[0])>0][0]
    print(bruch)
    zaehler=int(bruch[0])
    nenner=int(bruch[1])
    bruch=(1.0*zaehler)/nenner
#Finde alle nicht kompletten Brueche
    nennerGesamt=[int(x[1]) for x in rechnungen[1]] + [nenner]
    nennerGesamt.sort()
    zaehlerGesamt=[n*bruch for n in nennerGesamt]
#Schreibe alle Brueche in eine Liste
    lsg=[]
    for i in range(len(nennerGesamt)):
        lsg.append([str(int(zaehlerGesamt[i])),str(int(nennerGesamt[i]))])
    startzeile,markers=schreibeReihenBruchInStellenAusListe(lsg,rechnungen,tabellenWerte,tabellenWerteNr,startZeile=k,markers=markers)
    return startzeile,markers


def schreibeBruchGemischtZahl(rechnung,tabellenWerte,tabellenWerteNr,startZeile=None,markers=[],markerNr='a',mitLSG=False):
    tabellenLinie='\\\\'
    k=0 if startZeile is None else startZeile
    spalte1=3
    aufgabenAbstand=8
    vzMarker='\\Rnode{marker}{} &'  #vergleichszeichen
    count=1
    for r in rechnung:
        zaehlerZeile=[]
        nennerZeile=[]
        for b in r:
            print('b='+str(b))
            if mitLSG:
                zaehlerZeile=zaehlerZeile+[x+'&' for x in b[0]]+[' &']+[' &']+[x+'&' for x in b[3]]+[' &']*(aufgabenAbstand-3)
            else:
                zaehlerZeile=zaehlerZeile+[x+'&' for x in b[0]]+[' &']*aufgabenAbstand
            if mitLSG:  
                markers.append([markerNr+str(count),'='])
                count=count+1 
                markers.append([markerNr+str(count),b[2]])
                count=count+1
                print('markers[-2]'+str(markers[-2]))
                nennerZeile=nennerZeile+  [x+'&' for x in b[1]]+[vzMarker.replace('marker',markers[-2][0])]+[vzMarker.replace('marker',markers[-1][0])]+[x+'&' for x in b[4]]+[' &']*(aufgabenAbstand-3)
            else:
                nennerZeile=nennerZeile+  [x+'&' for x in b[1]]+[' &']*aufgabenAbstand
#Schreibe die Zeilen in die Tabelle
        m=len(zaehlerZeile)
        tabellenWerte[tabellenWerteNr][k][spalte1:spalte1+m]=zaehlerZeile
        m=len(nennerZeile)
        tabellenWerte[tabellenWerteNr][k+1][spalte1:spalte1+m]=nennerZeile #Bruchstriche: LaengeStrich=lS
        lS=[1,spalte1]
        for b in r:
            tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+1+max(map(len,b[:2])))+'}\\arrayrulecolor{lightgray}'
            lS=[lS[1]+max(map(len,b[:2]))+1,lS[1]+aufgabenAbstand if not mitLSG else 2 +max(map(len,b[:2]))]
            if mitLSG:
                tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(lS[1])+'}\\arrayrulecolor{black}\\cline{'+str(lS[1]+1)+'-'+str(lS[1]+max(map(len,b[3:])))+'}\\arrayrulecolor{lightgray}'
                lS=[lS[1]+max(map(len,b[3:]))+1,lS[1]+1+max(map(len,b[3:]))]  
        tabellenLinie=tabellenLinie+'\\cline{'+str(lS[0])+'-'+str(len(tabellenWerte[tabellenWerteNr][0])-1)+'}'
        tabellenWerte[tabellenWerteNr][k][-1]=tabellenLinie
        k=k+3
    return markers
