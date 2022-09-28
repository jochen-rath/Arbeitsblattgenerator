#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


            
def erzeugeKlammerrechnungenStellengerecht(rechnungen,tabellenWerte,tabellenWerteNr,anzahlZeilen=None):
#Diese Funktion schreibt in die Tabelle die Lösungen so rein, dass diese folgenden aufbau hat:
#               tabellenWerte[Nr][k]=[... 'a)&', '&', '(9&', '2&', '-&', '7&', '4)&', ... , '\\\\\\cline{1-19}\\arrayrulecolor{black}\\cline{20-21}\\arrayrulecolor{lightgray}\\cline{22-34}']
    k=0
    eS=1    #erste Spalte
    for l in range(len(rechnungen) if anzahlZeilen is None else anzahlZeilen):
        calc=list(rechnungen[l])
        ausgeklammert=list(rechnungen[l][1:])      #ausgeklammert
        iK1=ausgeklammert.index('(')               #Position 1. Klammer = (
        iK2=ausgeklammert.index(')')               #Position 2. Klammer = )
#Lösche Klammer und ersetze durch ergebnis
        klRechnung=ausgeklammert[iK1:iK2+1]
        ergKl=eval(''.join(klRechnung))
        del ausgeklammert[iK1:iK2+1]
        ausgeklammert.insert(iK1,str(ergKl))
#Erzeuge zuerst String mit Rechnung und Lösung
        erg=eval(''.join(ausgeklammert))
        zeile=calc+['=']+ausgeklammert+['=']+[str(erg)]
#Wandel alle Einträge in Listen um, um diese Unterlisten dann zu glätten
        zeile=[[zeile[0]]]+[['']]+[list(x) if len(x) > 1 else [x] for x in zeile[1:]]
        zeile=[x for sublist in zeile for x in sublist]
#Die Klammern sollen keine Einzelplatz haben, sondern bei der Passenden Zahl stehen: ['(','8'] wird zu ['(8'].
        iK1=zeile.index('(')
        iK2=zeile.index(')')
        zeile[iK2-1:iK2+1]=[''.join(zeile[iK2-1:iK2+1])]
        zeile[iK1:iK1+2]=[''.join(zeile[iK1:iK1+2])]
#Füge jedem Eintrag ein "&" hinzu und schreibe dann die die Zeilen in die Tabelle.startEintrag
        if len(zeile)<30:
            tabellenWerte[tabellenWerteNr][k][eS:eS+len(zeile)]=[x+'&'for x in zeile]
            zeilenLaenge=len(zeile)
            startSpalte=eS
        else:
            trennung=zeile.index('=')
            zeile1=zeile[:trennung]
            zeile2=zeile[trennung:]
            tabellenWerte[tabellenWerteNr][k][eS:eS+len(zeile1)]=[x+'&'for x in zeile1]
            k=k+1
            tabellenWerte[tabellenWerteNr][k][eS+5:eS+5+len(zeile2)]=[x+'&'for x in zeile2]
            zeilenLaenge=len(zeile2)
            startSpalte=eS+5
#Unterstreiche das Ergebnis.        
        unterstreichen='\\\\'+'\\cline{'+str(1)+'-'+str(startSpalte+zeilenLaenge-len(str(erg)))+'}\\arrayrulecolor{black}\\cline{'+str(startSpalte+zeilenLaenge-len(str(erg))+1)+'-'+str(startSpalte+zeilenLaenge)+'}\\arrayrulecolor{lightgray}'+'\\cline{'+str(startSpalte+zeilenLaenge+1)+'-'+str(len(tabellenWerte[tabellenWerteNr][0])-1)+'}'
        tabellenWerte[tabellenWerteNr][k][-1]=unterstreichen
        k=k+2
#Füge die Zwischenrechnungen ein.
#Wandel die Klammerrechnung in schriftliche Addition/Subtraktion Format um.
#Finde alle Zahlen im String.
        zwRech=[]
        rechnungenZusammengefasst=[''.join(klRechnung[1:-1]),''.join(ausgeklammert)]
        ergebnisse=[ergKl,erg]
        for i in range(len(rechnungenZusammengefasst)):
            zeichen=''.join(rechnungenZusammengefasst[i])
            zahlen=re.findall(r'\d+', rechnungenZusammengefasst[i])
#Lösche die Zahlen aus dem String. Nur + und - bleiben über
            for x in zahlen:
                zeichen=zeichen.replace(x,'')     
            zwRech.append([['']+list(zeichen)+[''],list(map(int,zahlen))+[ergebnisse[i]]])
        posEintraege=[2,17]
        k=schreibeUeberschlag(zwRech,tabellenWerte,tabellenWerteNr,k,posEintraege)
        k=erzeugeRechnungenStellengerecht(zwRech,tabellenWerte,tabellenWerteNr,mitLoesung=True,startZeile=k, mitUeberschlag=False,rechnungenProReihe=2,startEintrag=posEintraege)


def schreibeRechnungStellengerecht(r=[['','-',''],[465,32,433]],mitLoesung=True, kommastelle=-1,mitUeberschlag=False):
    anzZeilen=len(r[1])
    maxAnzZiff=max([len(str(x)) for x in r[1]])    #+1 für +,- Zeichen
    tab=[['']*(maxAnzZiff-len(str(x)))+list(str(x)) for x in r[1]]
    tab=[[r[0][i]] + x for i,x in enumerate(tab)]
    tab=tab[:-1]+[['']*len(tab[0])]+[tab[-1]]
    linie=[[[0,-0.5*(len(tab)-2)],[0.5*len(tab[0]),-0.5*(len(tab)-2)]]]
    if mitLoesung:
        tab[-2]=bestimmeUebertrag(tab)
#Füge ein Komma an der Kommastelle ein. Diese ist überall gleich
        if kommastelle>0:
            for i,x in enumerate(tab[:2]):
                tab[i][-kommastelle-1]=tab[i][-kommastelle-1]+','
            tab[-1][-kommastelle-1]=tab[-1][-kommastelle-1]+','
#Füge ein unsichtbares Komma ein, damit die Zahl mit Komma nicht verschoben dargestellt wird.
            tab=[[x+'\\phantom{,}' if not ',' in x else x for x in zeile] for zeile in tab]
        stellengerecht=schreibeAufgInTabelleInKaro(tab,linien=linie)
    else:
        stellengerecht=schreibeAufgInTabelleInKaro(tab[:-1],linien=linie)
#Füge ein Komma an der Kommastelle ein. Diese ist überall gleich
        if kommastelle>0:
            for i,x in enumerate(tab[:2]):
                tab[i][-kommastelle-1]=tab[i][-kommastelle-1]+','
#Füge ein unsichtbares Komma ein, damit die Zahl mit Komma nicht verschoben dargestellt wird.
            tab=[[x+'\\phantom{,}' if not ',' in x else x for x in zeile] for zeile in tab]
    return stellengerecht

def bestimmeUebertrag(tab):
    zeile=['']*len(tab[0])
    for i in range(len(tab[0])-1,0,-1):
        erg=eval(''.join([(x[0] if len(x[0])> 0 else '+') +(x[i] if len(x[i]) > 0 else '0') for x in tab[:-2]]))
        uebertrag=erg if erg>0 else 0
        while erg<0:
            uebertrag=uebertrag+10
            erg=erg+uebertrag
        zeile[i-1]=str(int(uebertrag/10)) if int(uebertrag/10)>0 else ''
    return zeile

def schreibeUeberschlag(rechnungenAuswahl,tabellenWerte,tabellenWerteNr,k,startEintrag):
    for j in range(len(rechnungenAuswahl)):
        minZahl=min(rechnungenAuswahl[j][1][:-1])
        maxZahl=max(rechnungenAuswahl[j][1][:-1])
#        rundenAuf=[x for x in [1,10,100,1000,10000,100000,1000000,10000000] if 1<=minZahl/x<10]
#        rundenAuf=rundenAuf[0] if len(rundenAuf)>0 else 100
        rundenAuf=10 if minZahl < 100 else (100 if minZahl<1000 else 1000)
        gerundet=list(map(lambda x: round(x/rundenAuf+1e-15)*rundenAuf,rechnungenAuswahl[j][1]))
        uerbschlagStr=str(gerundet[0])+''.join([rechnungenAuswahl[j][0][i+1]+str(gerundet[i+1]) for i in range(len(gerundet[:-2]))])
        uerbschlagErgebStr='='+str(eval(uerbschlagStr))
        n=int(startEintrag[j])
        if rundenAuf==10:
            tabellenWerte[tabellenWerteNr][k][n:n+len(uerbschlagStr)]=[x+' & ' for x in list(uerbschlagStr)]
            tabellenWerte[tabellenWerteNr][k][n+len(uerbschlagStr):n+len(uerbschlagStr)+len(uerbschlagErgebStr)]=[x+' & ' for x in list(uerbschlagErgebStr)]
        else:
            tabellenWerte[tabellenWerteNr][k][n:n+len(uerbschlagStr)]=[x+' & ' for x in list(uerbschlagStr)]
            tabellenWerte[tabellenWerteNr][k+1][n+5:n+5+len(uerbschlagErgebStr)]=[x+' & ' for x in list(uerbschlagErgebStr)]
    return k+2

def schreibeMultiplikationenStellengerecht(r,mitLsg=True,kommastellen=[]):
#Diese Funktion schreibt die Lösung einer schriftlichen Multiplikationasaufgabe in eine Tabelle
#Das Skript schreibeAufgInTabelleInKaro() überträgt diese Tabelle dann in eine Tikz-zeichnung.
#Welche Zahl ist kleiner?
    f1,f2=r.split('*')
#Tausche die Zahlen, wenn f2>f1 ist.
    if int(f2)>int(f1):
        r=str(f2)+'*'+str(f1)
        if len(kommastellen)==2:
            kommastellen=[kommastellen[1],kommastellen[0]]
    f1,f2=r.split('*')
    if int(f1[1:])==0:
        r=str(f2)+'*'+str(f1)
    f1,f2=r.split('*')
#Ein 2. Faktor mit einer Ziffer oder einer Ziffer mit Null folgend wird als eine Einzelrechnung aufgefasst.
    mehrereRechnungen=False if len(f2)==1 else ( True if int(f2[1:])>0 else False)
#Setzen Zeilen Und Spalten
    anzZeilen=1+len(f2)+2  if mehrereRechnungen else 2  #afg+anzZiffer f2+Ubertrag+Erg
    maxAnzZiff=len(r)    
    tab=[['']*maxAnzZiff]*anzZeilen
    tab[0]=list(r)
    multiPos=tab[0].index('*')
    if len(kommastellen)==2:
        if kommastellen[0]>0:
            kommaPosition=multiPos-kommastellen[0]-1
            tab[0][kommaPosition]=tab[0][kommaPosition]+','
        if kommastellen[1]>0:
            kommaPosition=-1-kommastellen[1]
            tab[0][kommaPosition]=tab[0][kommaPosition]+','
#    tab[0]=[x.replace('*','$\\cdot$') for x in tab[0]]
    tab[0][multiPos]='$\\cdot$'
    if mitLsg:
#Schreibe die Muliplikation
        if mehrereRechnungen:
            for i,f in enumerate(f2):
                p=str(eval(f1+'*'+f+'0'*(len(f2)-i-1)))
                print(f1+'*'+f+'0'*(len(f2)-i-1)+'='+p)
                tab[i+1]=['']*(maxAnzZiff-len(p))+list(p)
            tab[-2]=bestimmeUebertrag(tab[1:])
        p=str(eval(r))
        tab[-1]=['']*(maxAnzZiff-len(p))+list(p)
        if len(kommastellen)==2:
            kommaPosition=-1-(kommastellen[0]+kommastellen[1])
            tab[-1][kommaPosition]=tab[-1][kommaPosition]+','

#Schreibe den Übertrag der Multiplikation.
        f2=f2 if mehrereRechnungen else f2[0]
        for f in f2:
            ueber=[('\\cancel{'+x+'}' if int(x)>0 else '') for x in list(bestimmeUebertragVomProdukt(f1,f)[1:]) ]
            tab=[ueber+['']*(maxAnzZiff-len(ueber))]+tab
    linienYPos=[-0.5*(len(f2)),-0.5*len(tab)+1] if mehrereRechnungen else [-0.5*(len(f2))]
    linien=[[[0,y],[0.5*len(tab[0]),y]] for y in linienYPos]
    stellengerecht=schreibeAufgInTabelleInKaro(tab,linien=linien)
    return stellengerecht

def erzeugeDivisionStellengerecht(r,mitLoesung=False, nurSubtraktion=False, nurMultiplikation=False, nurErgebnisEintragen=False, nurRunterZiehen=False,nurLinien=False,trageRestEin=False,kommarechnung=False):
#
    mitLoesung=True if mitLoesung or nurRunterZiehen or nurErgebnisEintragen or nurMultiplikation or nurSubtraktion or trageRestEin else False
    erg,divSchritte,kommapositionen=divisionsSchritte(r,kommarechnung=kommarechnung)
    print(F'kp={kommapositionen}')
#Entferne führende Nullen im Ergebnis
    if 'Rest' in erg:
        erg=str(int(erg.split('Rest')[0]))+('' if trageRestEin else ' Rest'+erg.split('Rest')[1])
    else:
        erg=str(int(erg))
    tabelle=[list(r.replace('/',':').replace('.','').replace(',',''))+['=']+(list(erg) if mitLoesung and not nurErgebnisEintragen else ['']*len(erg))]
    if kommarechnung:
        if kommapositionen[0]>0:
            tabelle[0][kommapositionen[0]-1]=tabelle[0][kommapositionen[0]-1]+','
        gleichPos=tabelle[0].index('=')
        if kommapositionen[1]>0:
            kompos2=gleichPos+kommapositionen[1]
            print(F'kp2={kompos2}')
            tabelle[0][kompos2]=tabelle[0][kompos2]+','
    print(F'tabelle={tabelle}')
    zeilenLaenge=len(tabelle[0])
#Anpassen der Divisionsschritte an die gewählte Ausgabe:
    if nurRunterZiehen:
        divSchritte[:-1]=[[x[0][0]+ (' ' if len(x[0])>1 else ''),x[1],x[2]] for x in divSchritte[:-1]]
    if nurMultiplikation:
        divSchritte[:-1]=[[x[0],x[1],' '*len(x[2])] for x in divSchritte[:-1]]
    if nurSubtraktion:
        divSchritte[1:-1]=[[' ' + x[0][-1],x[1],x[2]] for x in divSchritte[1:-1]]
    if nurLinien:
        divSchritte=[[' '*len(y) for y in x] for x in divSchritte]
    print(divSchritte)
    print([[len(x) for x in s] for s in divSchritte])
#Schreibe den Loesungsweg
#Bestimme die Maximalanzahl
    linien=[]
    if mitLoesung or nurLinien:
        letztesEnde=0
        for i,divSchritt in enumerate(divSchritte):
            letzter=False
#Bei dem ersten Divisionsschritt ist die Spalte verrutsch, wenn die ersten Ziffer durch den Divisor teilbar ist:
#   z.B. 603:3=201
            m=letztesEnde+1-(1 if len(divSchritt)==1 else 0)
            n1=m-len(divSchritt[0])
            if i==0:
                m=int(letztesEnde+len(divSchritt[0]))
                n1=int(m-len(divSchritt[0]))
#Beim ersten Divisionsschritt wird die Zeile aus der Aufgabe genommen.
            if i>0:
                zeilenInhalt=['']*n1+list(divSchritt[0])
                tabelle.append(zeilenInhalt+['']*(zeilenLaenge-len(zeilenInhalt)))
#Im letzten Divisionsschritt wird nurnoch der Rest ausgeben.
            if len(divSchritt)>1:
                n2=int(m-len(divSchritt[2]))
                zeilenInhalt=['']*n2+list(divSchritt[2])
                tabelle.append(zeilenInhalt+['']*(zeilenLaenge-len(zeilenInhalt)))
            else:
                letzter=True
            letztesEnde=m
            if not letzter:
                linien.append([[n1*0.5,-i*1.0-0.5],[(n1+len(divSchritt[0]))*0.5,-i*1.0-0.5]])
    print(tabelle)
    return schreibeAufgInTabelleInKaro(tabelle,linien=linien)
