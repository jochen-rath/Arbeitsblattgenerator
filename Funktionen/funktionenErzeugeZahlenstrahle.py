#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())

def erzeugeTemperaturskalen(parameter=[[1,1,28],[3,0.5,60]],mitHintergrund=True):
#    parameter=[[Nullpunt, Schrittweite, Temperatur],...]
    afg=[]
    lsg=[]
#Initialialisiere die Befhele, um renewcommand nutzen zu koennen.    
    afg.append('\\newcommand\\R{'+str(1)+'}   ')
    afg.append('\\newcommand\\Hoehe{'+str(1)+'}')
    afg.append('\\newcommand\\NP{'+str(1)+'}')
    afg.append('\\newcommand\\SP{'+str(1)+'}')
    afg.append('\\newcommand\\SW{'+str(1)+'}')
    afg.append('\\newcommand\\NPplusSW{'+str(1)+'}')
    afg.append('\\newcommand\\NPplusSWplusSW{'+str(1)+'}')
    afg.append('\\newcommand\\SPminusSW{'+str(1)+'}')
    afg.append('\\newcommand\\TempHoehe{'+str(1)+'}')
#Erstelle die Aufgaben
    for i,para in enumerate(parameter):
        NP,SW,T =para
        if i%4 > 0:
            afg=afg[0:-1]+temperaturSkalaSiedepunkt(NP=NP,SW=SW,T=T,ursprung=[i%4*4,0],mitLsg=False,mitUmrandung=False,mitHintergrund=mitHintergrund)+[afg[-1]]
            lsg=lsg[0:-1]+temperaturSkalaSiedepunkt(NP=NP,SW=SW,T=T,ursprung=[i%4*4,0],mitLsg=True,mitUmrandung=False,mitHintergrund=mitHintergrund)+[lsg[-1]]
        else:
            if i>0:
                afg=afg+['\\newpage']
                lsg=lsg+['\\newpage'] 
            afg=afg+temperaturSkala(NP=NP,SW=SW,T=T,ursprung=[0,0],mitLsg=False,mitUmrandung=True,mitHintergrund=mitHintergrund)
            lsg=lsg+temperaturSkala(NP=NP,SW=SW,T=T,ursprung=[0,0],mitLsg=True,mitUmrandung=True,mitHintergrund=mitHintergrund)
    return [afg,lsg,parameter]

def erzeugeZahlenstrahlGanzeZahlen(laenge=4,nurNatuerlich=False,ohneKomma=False,anzPfeile=-1,ohneKammazahlen=False,mitText=True,breitePbox='\\textwidth'):
#Diese Funktion erzeugt einen Zahlenstrahlen mit Ganzen Zahlen von - nach +
#1. Erzeuge die Werte: startwert, endwert, schrittweite
    if nurNatuerlich:
        startwert=random.randint(0,40)
    else:
        startwert=random.randint(0,40)*(1 if random.getrandbits(1) else -1)
    schrittweiteProCm=random.choice([2,4,10,12,14] if ohneKammazahlen else [1,2,4,5,10])
    laenge=random.randint(4,10) if laenge<0 else laenge
    endwert=startwert+laenge*schrittweiteProCm
#Erzeuge die Haupteinteilung mit linespace: Bsp: [-45,-40,-35]
    HT=np.linspace(startwert, endwert, laenge+1)
#Erzeuge die Nebenunterteilung mit linespace: Bsp: [-45,42.5,-40,37.5,-35]
    UT=np.linspace(startwert, endwert, 2*laenge+1)
#Pfeile
    pfeileAuswahl=[x for x in UT if x not in HT]
    anzPfeile=random.randint(2,len(pfeileAuswahl)) if anzPfeile<1 else min(anzPfeile,len(pfeileAuswahl))
    pfeileId=random.sample(range(len(UT[:-1])),anzPfeile)
#    pfeileWert=[UT[i] for i in pfeileId]
    pfeileWert=random.sample(pfeileAuswahl,anzPfeile)
#    pfeileId=[UT.index(x) for x in pfeileWert]
    pfeileId=[list(UT).index(x) for x in pfeileWert]
#Wandel die Haupteinteilung in einen Liste um, die das Zahlenstrahl skript darstellen kann.
#Dabei wird jeder Zahl eine x-Position zugeordnet
    HT, UT=passeHaupteinteilungAnXXcmZahlenstrahlAn(HT, UT, laenge+2)
    pfeile=[[UT[id],strNW(round(pfeileWert[i],1))] for i,id in enumerate(pfeileId)]
#    tikzZahlenstrahl=zahlenstrahlNatuerlicheZahlenTikz([HT,UT],laenge=laenge+2.5)['']
    afg=[F'\\pbox{{{breitePbox}{"" if "text" in breitePbox else "cm"}}}{{Beschrifte den Zahlenstrahl:\\\\'] if mitText else []
    afg=afg+zahlenstrahlBruchDezimalzahlenTikz([HT,UT],pfeile,laenge+2.5,mitLSG=False)
    afg=afg+(['}']  if mitText else [])
    lsg=zahlenstrahlBruchDezimalzahlenTikz([HT,UT],pfeile,laenge+2.5,mitLSG=True)
    return [afg,lsg,[]]


def erzeugeZahlenstrahleDezimalzahlenEinteilungTikz(startwert=10,endwert=0,laenge=10,anzPfeile=-1,zufall=True,mitText=False,rational=False):
#Diese Skript erzeut einen Zahlenstrahl von Startwert zu Endwert.
#Dazu erzeugt es eine Hauptunterteilung und eine Unterteilung:
#Haupteinteilung
#     HT=[startwert,..,endwert+1]
#Unterteilung zwischen zwei Werten:
#        UT=[0,0.1,0.2 usw
#anzPfeile Wieviel Pfeile sollen in jedem Zahlenstrahl geplottet werden
#pfeilPos: Index wird aus UT genommen
#pfeile=[[Zähler Pfeil1, Nenner Pfeil],[Zähler Pfeil2,Nenner Pfeil2],....
#if True:
    schritteHT=0
#Manche Kombinationen erzeugen eine Schrittweite von 0. Dies führt zu Programmfehlern.
    while schritteHT<1:
        if zufall:
            anzKommast=random.randint(1,3)
            startwert=dezi(anzKommast) * (1 if random.getrandbits(1) else -1) if rational else 1
            endwert=startwert+random.randint(1,3)*10**(-anzKommast)
    #    endwert=endwert if endwert>0 else random.randint(1,12)
    #    startwert=startwert if startwert< endwert else random.randint(0,endwerte[i]-1)
        kommastelle=0 if not ',' in strNW(endwert) else len(strNW(endwert).split(',')[1])
        einteilung=10
        schritteHT=round(endwert-startwert,kommastelle)*eval('1e'+strNW(kommastelle))
        schritteUT=schritteHT*einteilung
    HT=np.linspace(startwert, endwert, int(round(schritteHT+0.00001))+1)
    UT=np.linspace(startwert, endwert, int(round(schritteUT+0.00001))+1)
    pfeileAuswahl=[x for x in UT if x not in HT]
    anzPfeile=random.randint(2,min(5,len(pfeileAuswahl))) if anzPfeile<1 else min(anzPfeile,len(pfeileAuswahl))
    pfeileId=random.sample(range(len(UT[:-1])),anzPfeile)
    pfeileWert=[UT[i] for i in pfeileId]
    pfeileWert=random.sample(pfeileAuswahl,anzPfeile)
    pfeileId=[list(UT).index(x) for x in pfeileWert]
#    laenge=(schritteHT-1)*4 if (schritteHT-1)*4<laenge else laenge
    HT,UT=passeHaupteinteilungAnXXcmZahlenstrahlAn(HT,UT,laenge)
#Entferne Lange Nachkommastellen aus den Dezimalzahlen, z.b. 1.78000000000000000001
    HT=[[x[0],strNW(round(x[1],kommastelle+3))] for x in HT]
    pfeile=[[UT[index],strNW(round(pfeileWert[i],kommastelle+3))] for i,index in enumerate(pfeileId)]
    print(HT)
    afg='\pbox{20cm}{Bestimme die Zahlen an den Pfeilen:\\\\' if mitText else ''
    afg=afg+'\n'.join(zahlenstrahlBruchDezimalzahlenTikz([HT,UT],pfeile,laenge,mitLSG=False))
    afg=afg+('}' if mitText else '')
    zahlenstrahleMitLSG='\n'.join(zahlenstrahlBruchDezimalzahlenTikz([HT,UT],pfeile,laenge,mitLSG=True))
    return [afg,zahlenstrahleMitLSG,[startwert,endwert]]


def passeLaengenAnZahlenstrahlAn(startwert,endwert,Einteilung,laenge=10):
#Will man einen Pfeil in einem Zahlenstrahl zeichnen, so passt dieser eventuell nicht, da die Strecke von 0 bis 1 eventuell nicht 1 cm lang ist.
#Ausgabe:
    startN=int(startwert)
    endN=int(endwert)
    werteZahlenstrahl=[Einteilung,startN,endN]
    HT=range(werteZahlenstrahl[1] if (werteZahlenstrahl[1]-1) >0 else 0,werteZahlenstrahl[2]+1)
    UT=np.linspace(HT[0], HT[-1], (HT[-1]-HT[0])*werteZahlenstrahl[0]+1)
    HT,UT=passeHaupteinteilungAnXXcmZahlenstrahlAn(HT,UT,laenge)
    return HT[1][0]/HT[1][1]

def passeHaupteinteilungAnXXcmZahlenstrahlAn(HT,UT,laenge=10):
#Wähle Werte von 0 oder 1 bis 10, die der Haupteinteilung entsprechen soll.
#Wenn HT[0]=0 ist, soll Zahlenstrahl bei 0 beginnen, ansonsten bei 1
    pos=np.linspace(0 if HT[0]==0 else 1 ,laenge,len(HT))
#Berechne Grade, die Haupteinteilung auf 0 oder 1 bis 10 abbildet.
    M=(1.0*HT[1]-HT[0])/(pos[1]-pos[0])
    b=1.0*HT[0]-M*pos[0]
    HT=[[pos[i],HT[i]] for i in range(len(HT))]
    UT=(UT-b)/M
    return [HT,UT]

def erzeugeDezizahlPfeilmarkierungen(pfeile,HT):
    M=(1.0*HT[1][1]-HT[0][1])/(HT[1][0]-HT[0][0])
    b=1.0*HT[0][1]-M*HT[0][0]
    return [[(p-b)/M,strNW(p)] for i,p in enumerate(pfeile)]

def erzeugeBruchPfeilmarkierungen(pfeile,HT,mitLSG=False):
    M=(1.0*HT[1][1]-HT[0][1])/(HT[1][0]-HT[0][0])
    b=1.0*HT[0][1]-M*HT[0][0]
    pfeilText=[]
    for p in pfeile:
        bruch='$\\frac{'+str(p[0])+'}{'+str(p[1])+'}$'
#        pfeilText.append(('$'+str(int(p[0]/p[1]))+'$' if p[0]%p[1]==0 else bruch) if mitLSG else '')
#        pfeilText.append('$'+str(int(p[0]/p[1]))+'$' if p[0]%p[1]==0 else bruch)
        pfeilText.append('$'+schreibeBruchundGemZahl(p[0],p[1])+'$')
    return [[(1.0*p[0]/p[1]-b)/M,pfeilText[i]] for i,p in enumerate(pfeile)]


#Die Funktionen im Folgenden werden (noch) nicht auf der Webseite verwendet. Sie sind noch von
#Der Zeit, als die Arbeitsblätter direkt ohne Auswahl erzeugt wurden.

def zeichenZahlenstrahleNatuerlicheZahlenTikz(zahlenstrahl):
#Diese Skript plottet einen Zahlenstrahl passend zur Funktion erzeugeZahlenstrahleNatuerlicheZahlen:
    zahlenstrahleLatex=[]
    for z in zahlenstrahl:
#Positionen auf den Zahlenstrahl, der 10 cm lang ist.
#Es werden die Zahlen vom Strahl auf einen Zahlenstrahl abgebildet, der 10cm lang ist.
        HT=[z[0],z[1],int(z[1]+(z[1]-z[0]))]
        UT=np.linspace(HT[0],HT[2],2*z[2]+1)
        zahlenstrahleLatex=zahlenstrahleLatex+zahlenstrahlNatuerlicheZahlenTikz(passeHaupteinteilungAnXXcmZahlenstrahlAn(HT,UT))
    return zahlenstrahleLatex



def zahlenstrahlMitEinteilung(startwert,endwert,Einteilung,laenge=10,mitBeginEnd=True):
#Aufruf:
#        zahlenstrahlMitEinteilung(0,5,4,laenge=10)
#
#werteZahlenstrahl=[Anzahl einteilungen zwischen 0 und 1,startwert,endwert]
#HT=[0,1,2,3,...,endwertN]
#UT=[0.1,0.2,0.3,...]
    startN=int(startwert)
    endN=int(endwert)
    werteZahlenstrahl=[Einteilung,startN,endN]
    HT=range(werteZahlenstrahl[1] if (werteZahlenstrahl[1]-1) >0 else 0,werteZahlenstrahl[2]+1)
    UT=np.linspace(HT[0], HT[-1], (HT[-1]-HT[0])*werteZahlenstrahl[0]+1)
    HT,UT=passeHaupteinteilungAnXXcmZahlenstrahlAn(HT,UT,laenge)
    return zahlenstrahlBruchzahlenTikz([HT,UT],[],laenge,mitLSG=False,mitBeginEnd=mitBeginEnd)

def erzeugeZahlenstrahleBruecheEinteilungTikz(n=8,laenge=10,endWert=12):
#Diese Skript erzeut n zufällige Zahlenstrahle. Dazu erzeugt es eine Hauptunterteilung und Nebenunterteilung:
#werteZahlenstrahl=[[Anzahl einteilungen zwischen 0 und 1,startwert,endwert],[..
#HT=[[1,2,3,4],        [2,3,4],                      [8,9,10],....]
#UT=[[1.2,1.4,1.6,...],[2.3333,2.66666,3,3.333,....],
#anzPfeile Wieviel Pfeile sollen in jedem Zahlenstrahl geplottet werden
#pfeilPos: Index wird aus UT genommen
#pfeile=[[Zähler Pfeil1, Nenner Pfeil],[Zähler Pfeil2,Nenner Pfeil2],....
#if True:
    endwerte=[random.randint(1,endWert) for i in range(n)]
    werteZahlenstrahl=[[random.randint(2,10),random.randint(0,endwerte[i]-1),endwerte[i]] for i in range(n)]
    HT=[range(werteZahlenstrahl[i][1] if (werteZahlenstrahl[i][1]-1) >0 else 0,werteZahlenstrahl[i][2]+1) for i in range(n)]
#    startVorHT=[random.randint(1,HT[i][0]) for i in range(n)]
#    UT=[np.linspace((HT[i][0]-startVorHT[i]/werteZahlenstrahl[i][0]) if (HT[i][0]-startVorHT[i]/werteZahlenstrahl[i][0])>0 else 0, HT[i][-1], (HT[i][-1]-HT[i][0])*werteZahlenstrahl[i][0]+1+(startVorHT[i] if (HT[i][0]-startVorHT[i]/werteZahlenstrahl[i][0])>0 else 0)) for i in range(n)]
    UT=[np.linspace(HT[i][0], HT[i][-1], (HT[i][-1]-HT[i][0])*werteZahlenstrahl[i][0]+1) for i in range(n)]
    anzPfeile=[random.randint(2,5) if len(list(UT[i]))>5 else 1 for i in range(n)]
    pfeilPos=[random.sample(range(len(UT[i][:-1])),anzPfeile[i]) for i in range(n)]
    pfeile=[[[pP+UT[i][0]*werteZahlenstrahl[i][0],werteZahlenstrahl[i][0]] for pP in pfeilPos[i]] for i in range(n)]
    laengen=[(werteZahlenstrahl[i][2]-werteZahlenstrahl[i][1])*4 if (werteZahlenstrahl[i][2]-werteZahlenstrahl[i][1])*4<laenge else laenge for i in range(n)]
    print(laengen)
    for i in range(n):
        HT[i],UT[i]=passeHaupteinteilungAnXXcmZahlenstrahlAn(HT[i],UT[i],laengen[i])
        pfeile[i]=erzeugeBruchPfeilmarkierungen(pfeile[i],HT[i],mitLSG=False)
    print(HT)
    zahlenstrahleOhneLSG=[zahlenstrahlBruchzahlenTikz([HT[i],UT[i]],pfeile[i],laengen[i],mitLSG=False) for i in range(n)]
    zahlenstrahleMitLSG=[zahlenstrahlBruchzahlenTikz([HT[i],UT[i]],pfeile[i],laengen[i],mitLSG=True) for i in range(n)]
    return [zahlenstrahleOhneLSG,zahlenstrahleMitLSG]



def erzeugeZahlenstrahleNatuerlicheZahlen():
#Diese Funktion erzeugt 8 Listen der Form
#		[Startwert,Endwert,Schrittweite]
#if True:
#1.)#Zufaellige Liste mit drei unterschiedlichen Startzahlen für die ersten 4 Tabellen
    rechenwerte=[random.sample(range(0, 101,2), 4)]
#2.)#Zufaellige Liste mit drei Einteilungen
    rechenwerte.append(random.sample(range(2, 11,2), 4))
#3.)#Zufaellige Liste mit drei Multiplikatoren für den zweiten Wert
    rechenwerte.append(random.sample(range(1, 5), 4))
    zahlenstrahl=[]
    for i in range(len(rechenwerte[0])):
         zahlenstrahl.append([rechenwerte[0][i],rechenwerte[0][i]+rechenwerte[1][i]*rechenwerte[2][i],rechenwerte[1][i]])
#Wie Oben, nur größere Werte
    rechenwerte=[random.sample(range(100, 10001,10), 4)]  #Zufaellige Liste mit drei unterschiedlichen Startzahlen für die ersten 4 Tabellen
    rechenwerte.append(random.sample(range(2, 11,2), 4))  #Zufaellige Liste mit drei Einteilungen
    rechenwerte.append(random.sample(range(10, 100,10), 4))  #Zufaellige Liste mit drei Multiplikatoren für den zweiten Wert
    for i in range(len(rechenwerte[0])):
         zahlenstrahl.append([rechenwerte[0][i],rechenwerte[0][i]+rechenwerte[1][i]*rechenwerte[2][i],rechenwerte[1][i]])
    return zahlenstrahl
