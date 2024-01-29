#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())
import random


def dezi(nachkommestellen=3,nullFavourisieren=False,bis10=False):
#Diese Funktion erzeugt eine Dezimalzahl auf diese Weise, damit vermehrt Nullen auftauchen.
#Stellen die Nullen enthalten führen zu Problemen und die SuS sollen diese üben.
    dezi=random.randint(1,10) if (random.randint(1,5)<4 or bis10) else random.randint(1,100)
    for i in range(1,nachkommestellen+1):
        if nullFavourisieren:
            dezi=dezi+ (0 if random.randint(1,4)<2 else random.randint(1,9)) * 10**(-i)
        else:
            dezi=dezi+ (random.randint(1,9)) * 10**(-i)
    return round(dezi,nachkommestellen)

def mehrereDeziZahlen(nachkommestellen=1,anzSummanden=2,bis10=False):
    deziZahlen=[]
    for i in range(anzSummanden):
        deziZahlen.append(dezi(1 if nachkommestellen==1 else random.randint(1,nachkommestellen+1) ,bis10=bis10))
    return deziZahlen

def erzeugeSchrAddSubTabellenzeile(tabelle,i,d,kommaPos):
#Diese Funktion erzeugt eine Eine Zeile in der Form
#   t=['','1','2,','3','']
#     tabelle=erzeugeSchrAddSubTabellenzeile(tabelle,zeile,zahl,kommaPos)
    print(d)
    vorK=strNW(d).split(',')[0]
    nachK=strNW(d).split(',')[1]
    tabelle[i][kommaPos-len(vorK):kommaPos]=list(vorK)
    tabelle[i][kommaPos:kommaPos+len(nachK)]=list(nachK)
    tabelle[i][kommaPos-1]=tabelle[i][kommaPos-1]+','
    return tabelle

def deziZahlenAddierenSubtrahieren(nachkommestellen=1,anzSummanden=2,operator='+',anzahl=1,bis10=False,mitText=False):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [Aufgabe,Lösungen,[zahlen,operator,erg]]=deziZahlenAddierenSubtrahieren(nachkommestellen,operator,anzahl)
    breitePbox='5'
    deziZahlen=mehrereDeziZahlen(nachkommestellen=nachkommestellen,anzSummanden=anzSummanden,bis10=bis10)
    zahlen=[]
    while ((eval(operator.join(map(str,deziZahlen))) <0) or (False if not bis10 else (eval(operator.join(map(str,deziZahlen))) >10))):   #Keine Negativen Ergebnisse
        deziZahlen=mehrereDeziZahlen(nachkommestellen=nachkommestellen,anzSummanden=anzSummanden,bis10=bis10)
#        aufg=('Berechne: ' if mitText else '')+operator.join(map(strNW,deziZahlen))+'='
    aufg=operator.join(map(strNW,deziZahlen))+'='
#Erzeuge eine Lösung mit Schriftlicher Addition, Subktraktion
    zahlenStr=list(map(strNW,deziZahlen+[eval(operator.join(map(str,deziZahlen)))]))
    nKs=[0 if not (',' in x) else len(x[x.index(',')+1:]) for x in zahlenStr]
    maxNK=max(nKs)
    zahlenStr2=[x+'0'*(maxNK-nKs[i])  for i,x in enumerate(zahlenStr)]
    schriftlich=[['',operator,''],[x.replace(',','') for x in zahlenStr2]]
    lsg=schreibeRechnungStellengerecht(schriftlich,mitLoesung=True,kommastelle=maxNK)
#    lsg=operator.join(map(strNW,deziZahlen))+'='+strNW(round(eval(operator.join(map(str,deziZahlen))),nachkommestellen+3))
    zahlen.append(([deziZahlen,operator,round(eval(operator.join(map(str,deziZahlen))),nachkommestellen+3)]))
    return [aufg,lsg,zahlen]

def deziZahlenSchriftAddierenSubtrahieren(nachkommestellen=1,anzSummanden=2,operator='+',bis10=False,name='ausgabeTablle'):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum schritlichen Addieren und Subtrahieren von Dezimalzahlen
#Die Aufgabe und Lösung wird in eine Tabelle geschrieben, welche am Anfang des Latex Dokuments mit 
#      \begin{filecontents*}{tabelle.tex}
#      \end{filecontents*}
#eingebunden werden muss. In einer Tikz Zeichnung wird diese Tabelle mit dem Befehl:
#      \node[black,below right] at (-0.15,0.15) {\input{tabelle.tex}}
#aufgerufen.
#Ausgabe: [aufg,lsg,tabFileCon,tabFileConLSG]=deziZahlenSchriftAddierenSubtrahieren(nachkommestellen=1,operator='+',anzahl=1,bis10=False)
#         tabFileCon=[filecontensCode,name,tabelle,linien,extraBezeichnungen]
#         rechnung=[[zahlen1,operator1,erg1],[zahlen2,operator2,erg2],...]
    aufg,lsg,rechnungen=deziZahlenAddierenSubtrahieren(nachkommestellen=nachkommestellen,anzSummanden=anzSummanden,operator=operator,anzahl=anzahl,bis10=bis10)
#Iteration über alle Rechnungen.
    for i,r in enumerate(rechnungen):
        anzDeziZahlen=len(r[0])
        anzSpalten=max([len(strNW(x)) for x in r[0]+[r[-1]]])      #Beispiel:  +& 3&2,&1&9   --> Das Komma wird mitgezählt, aber als Operator gewertet.
        anzZeilen=len(r[0])+2                              #Dezimalzahlen, plus Leerzeile, plus Ergebniszeile
        tabelle=[['\\phantom{8;}']*anzSpalten for i in range(anzZeilen)] #Tabelle wird über iteration erzeugt, damit jede Zeile eine eigene Liste ist.
        kommaPos=anzSpalten-max([len(strNW(x).split(',')[1]) for x in r[0]])
#Iteriere über die Dezimalzahlen und erzeuge ein Tabelle, die die Rechnung entält
        for i,d in enumerate(r[0]):
            tabelle=erzeugeSchrAddSubTabellenzeile(tabelle,i,d,kommaPos)
            if i>0:
                tabelle[i][0]=operator
        tabelleLSG=[x.copy() for x in tabelle]
#Schreibe bei der Lösung das Ergebnis in die letzte Zeile
        tabelleLSG=erzeugeSchrAddSubTabellenzeile(tabelleLSG,len(tabelleLSG)-1,r[-1],kommaPos)
#SFülle die Lücken in den Nachkommastellen mit Nullen auf.
        for zeile in tabelleLSG:
            kommaPos=max([i if ',' in x else -1 for i,x in enumerate(zeile) ])
            if kommaPos>0:
                zeile[kommaPos:]=['0' if 'phantom' in x else x for x in zeile[kommaPos:]]
#Erzeuge den Tabellen Code der vor begin{document} steht und speicher diesen und den Namen der Tabelle und die Tabelle in eine Variabel
        tabFileCon=[erzeugeTabelleFilecontents(tabelle,name+'_'+str(i)),name+'_'+str(i),tabelle]
        tabFileConLSG=[erzeugeTabelleFilecontents(tabelleLSG,name+'Lsg'+'_'+str(i)),name+'Lsg'+'_'+str(i),tabelleLSG]
#Erzeuge die Trennlinie für die Lösung unter allen Dezimalzahlen und füge sie der vorherigen Variabel hinzu.
        linie=[]
        linieLsg=[[0,-(anzZeilen*0.5-0.5),anzSpalten*0.5,-(anzZeilen*0.5-0.5)]]
        tabFileCon.append(linie)
        tabFileConLSG.append(linieLsg)
#Schreibe die Aufgabennummer als extra Bezeichnung.
        tabFileCon.append([[-0.25,-0.25,name[-1]+')']])
        tabFileConLSG.append([[-0.25,-0.25,name[-1]+')']])
    return [aufg,lsg,tabFileCon,tabFileConLSG]

def deziZahlenMultiDivi(nachkommastellen=3,operator=''):
#Diese Funktion erzeugt eine Dezimalzahlen Multiplikation, Divisionsaufgabe
#Ausgabe: [Aufgabe,Lösungen,[Zahl1,Zahl2]]
    operator='' if not (operator=='*' or operator=='/') else operator
    op=random.choice(['*','/']) if len(operator)==0 else operator
    if op=='*':
        nk1=random.randint(0,nachkommastellen)
        nk2=random.randint(nachkommastellen-nk1,nachkommastellen)
        zahl1=dezi(nachkommestellen=nk1)
        zahl2=dezi(nachkommestellen=nk2)
        while zahl1==1 or zahl2 ==1:
            zahl1=dezi(nachkommestellen=nk1)
            zahl2=dezi(nachkommestellen=nk2)
    else:
        quotient=dezi(nachkommestellen=nachkommastellen)
        zahl2=random.randint(2,12)
        zahl1=quotient*zahl2
    afg=F'${strNW(zahl1)}~{"XXXcdot" if op=="*" else ":"}~{strNW(zahl2)}=$'
    afg=[afg.replace('XXX','\\')]
    lsg=F'${strNW(zahl1)}~{"XXXcdot" if op=="*" else ":"}~{strNW(zahl2)}={strNW((zahl1 * zahl2) if op=="*" else (zahl1/zahl2))}$'
    lsg=[lsg.replace('XXX','\\')]
    if op=='*':
        calc=F'{strNW(zahl1)}*{strNW(zahl2)}'
        lsg=schreibeMultiplikationenStellengerecht(calc.replace(',',''), mitLsg=True,kommastellen=[nk1,nk2])
    else:
        calc=F'{strNW(zahl1)}/{strNW(zahl2)}'
        lsg=erzeugeDivisionStellengerecht(calc, mitLoesung=True,kommarechnung=True)
    return [afg,lsg,[]]

def deziZahlenVergleichen(nachkommestellen=3,mitText=True):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum vergleich von Dezimalzahlen.
#Ausgabe: [Aufgabe,Lösungen,[Zahl1,Zahl2]]
    zahl=dezi(nachkommestellen=nachkommestellen)
    op=random.choice(['+','-'])
    zahl2=round(eval(str(zahl)+op+str(random.randint(1,9)*10**(-random.randint(nachkommestellen-1,nachkommestellen)))),nachkommestellen)
    vergl='<' if zahl<zahl2 else '>'
    aufg=('Vergleiche: ' if mitText else '')+'$'+strNW(zahl)+'~\\square~'+strNW(zahl2)+'$'
    lsg='$'+strNW(zahl)+vergl+strNW(zahl2)+'$'
    return [aufg,lsg,[zahl,zahl2]]

def dezimalzahlenRunden(kommastelle,anzahl=1,zusatz=0,mitText=True):
#Diese Funktion erzeugt eine oder mehrere Rundungsaufgaben für Dezimalzahlen. Die Aufgaben und Lösungen werden in einer pbox geschrieben, wenn mehr als eine Aufgabe geben ist.
#Aufruf: dezimalzahlenRunden(3,1)
#        dezimalzahlenRunden(4,3)
#
#Ausgabe:  [aufg,lsg,deziZahlen]
    breitePbox='5'
    woerter={0:'Einer',1:'Zehntel',2:'Hunderstel',3:'Tausendstel',4:'Zehntausendstel'}
    if anzahl>1:
        aufg=F'\\pbox{{{breitePbox} cm}}{{{F"Runde auf {woerter[kommastelle]}:" if mitText else ""}\\\\'
        lsg='\\pbox{'+breitePbox+'cm}{'
        deziZahl=[]
        for i in range(anzahl):
            zusatz=random.randint(1,3) if zusatz==0 else zusatz
            deziZahl.append(dezi(kommastelle+zusatz,nullFavourisieren=False))
            aufg=aufg+'$'+strNW(round(deziZahl[-1],kommastelle+zusatz))+'~\\approx~$'+'\\\\'
            lsg=lsg+'$'+strNW(round(deziZahl[-1],kommastelle+zusatz))+'~\\approx~'+strNW(round(deziZahl[-1],kommastelle))+'$'+'\\\\'
        aufg=aufg+'}'
        lsg=lsg+'}'
    else:
        zusatz=random.randint(1,3) if zusatz==0 else zusatz
        deziZahl=dezi(kommastelle+zusatz)
        aufg=F'{F"Runde auf {woerter[kommastelle]}: " if mitText else ""}{strNW(round(deziZahl,kommastelle+zusatz))}'
        lsg='$'+strNW(round(deziZahl,kommastelle+zusatz))+'~\\approx~'+strNW(round(deziZahl,kommastelle))+'$'
    return [aufg,lsg,deziZahl]

def deziZahlenAddierenSubtrahierenAlteFunktion(nachkommestellen=1,anzSummanden=2,operator='+',anzahl=1,bis10=False,mitText=False):
#Diese Funktion erzeugt eine Aufgabe und Lösung zum Addieren und Subtrahieren von Dezimalzahlen
#Ausgabe: [Aufgabe,Lösungen,[zahlen,operator,erg]]=deziZahlenAddierenSubtrahieren(nachkommestellen,operator,anzahl)
    breitePbox='5'
    deziZahlen=mehrereDeziZahlen(nachkommestellen=nachkommestellen,anzSummanden=anzSummanden,bis10=bis10)
    zahlen=[]
    if anzahl>1:
        aufg='\\pbox{'+breitePbox+'cm}{Berechne:\\\\'
        lsg='\\pbox{'+breitePbox+'cm}{'
        for i in range(anzahl):
#Keine Negativen Ergebnisse, eventuell keine Ergebnisse größer 10.
            while ((eval(operator.join(map(str,deziZahlen))) <0) or (False if not bis10 else (eval(operator.join(map(str,deziZahlen)) >10)))):
                deziZahlen=mehrereDeziZahlen(nachkommestellen=nachkommestellen,anzSummanden=anzSummanden,bis10=bis10)
            aufg=aufg+operator.join(map(strNW,deziZahlen))+'=\\\\'
            lsg=lsg+operator.join(map(strNW,deziZahlen))+'='+strNW(round(eval(operator.join(map(str,deziZahlen))),nachkommestellen+3))+'\\\\'
            zahlen.append([deziZahlen,operator,round(eval(operator.join(map(str,deziZahlen))),nachkommestellen+3)])
        aufg=aufg+'}'
        lsg=lsg+'}'
    else:
        while ((eval(operator.join(map(str,deziZahlen))) <0) or (False if not bis10 else (eval(operator.join(map(str,deziZahlen))) >10))):   #Keine Negativen Ergebnisse
            deziZahlen=mehrereDeziZahlen(nachkommestellen=nachkommestellen,anzSummanden=anzSummanden,bis10=bis10)
#        aufg=('Berechne: ' if mitText else '')+operator.join(map(strNW,deziZahlen))+'='
        aufg=operator.join(map(strNW,deziZahlen))+'='
        lsg=operator.join(map(strNW,deziZahlen))+'='+strNW(round(eval(operator.join(map(str,deziZahlen))),nachkommestellen+3))
        zahlen.append(([deziZahlen,operator,round(eval(operator.join(map(str,deziZahlen))),nachkommestellen+3)]))
    return [aufg,lsg,zahlen]
