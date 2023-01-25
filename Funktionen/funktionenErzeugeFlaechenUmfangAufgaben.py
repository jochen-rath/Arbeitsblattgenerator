#!/usr/bin/env python
# coding: utf8
import random


#Aufruf:
#       exec(open("Funktionen/funktionErzeugeFlaechenUmfangAufgaben.py").read())
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeRechteck():
    a=random.randint(1,4)
    b=random.randint(1,4)
    return [rechteckTikz(a,b),a,b]

def erzeugeUmfangFlaechenBerechnung(maxA=4,maxB=4,breitePbox='6',mitText=True):
#Diese Funktion erzeugt eine Aufgabe zur Berechnung des Umfangs eines Rechtecks.
#Ausgabe: [Aufgabe,Lösungen,[a,b]]=erzeugeUmfangRechnung(maxA,maxB)
    a=random.randint(1,maxA)
    b=random.randint(1,maxB)
    afg=('\\pbox{'+breitePbox+'cm}{Bestimme den Umfang und die Fläche von: \\\\') if mitText else ''
    afg=afg+'\n'.join(rechteckTikz(a,b))+('}' if mitText else '')
    lsg='\\pbox{'+breitePbox+'cm}{$U=2\cdot a+2\cdot b$ \\\\ $U=2\cdot'+strNW(a)+'cm+2\cdot'+strNW(b)+'cm='+strNW(2*a+2*b)+'cm$ \\\\'
    lsg=lsg+'$A=a\cdot b$ \\\\ $A='+strNW(a)+'\cdot'+strNW(b)+'='+strNW(a*b)+'cm^2$ \\\\'
    lsg=lsg+'\n'.join(rechteckTikz(a,b,beschrSeiten=True,texta='a='+strNW(a)+'cm',textb='b='+strNW(b)+'cm'))+'}'
    return [afg,lsg,[a,b]]
    
def erzeugeUmfangRechnung(maxA=4,maxB=4,breitePbox='6',mitText=True):
#Diese Funktion erzeugt eine Aufgabe zur Berechnung des Umfangs eine Rechtecks.
#Ausgabe: [Aufgabe,Lösungen,[a,b]]=erzeugeUmfangRechnung(maxA,maxB)
    a=random.randint(1,maxA)
    b=random.randint(1,maxB)
    afg=('\\pbox{'+breitePbox+'cm}{Bestimme den Umfang von: \\\\') if mitText else ''
    afg=afg+'\n'.join(rechteckTikz(a,b))+('}' if mitText else '')
    lsg='\\pbox{'+breitePbox+'cm}{$U=2\cdot a+2\cdot b$ \\\\ $U=2\cdot'+strNW(a)+'cm+2\cdot'+strNW(b)+'cm='+strNW(2*a+2*b)+'cm$ \\\\'
    lsg=lsg+'\n'.join(rechteckTikz(a,b,beschrSeiten=True,texta='a='+strNW(a)+'cm',textb='b='+strNW(b)+'cm'))+'}'
    return [afg,lsg,[a,b]]

def erzeugeFlaechenberechnung(maxA=4,maxB=4,breitePbox='6',mitText=True):
#Diese Funktion erzeugt eine Aufgabe zur Berechnung der Fläche eine Rechtecks.
#Ausgabe: [Aufgabe,Lösungen,[a,b]]=erzeugeUmfangRechnung(maxA,maxB)
    a=random.randint(1,maxA)
    b=random.randint(1,maxB)
    afg=('\\pbox{'+breitePbox+'cm}{Bestimme die Fläche von: \\\\') if mitText else ''
    afg=afg+'\n'.join(rechteckTikz(a,b))+('}' if mitText else '')
    lsg='\\pbox{'+breitePbox+'cm}{$A=a\cdot b$ \\\\ $a='+strNW(a)+'cm\cdot'+strNW(b)+'cm='+strNW(a*b)+'cm^2$ \\\\'
    lsg=lsg+'\n'.join(rechteckTikz(a,b,beschrSeiten=True,texta='a='+strNW(a)+'cm',textb='b='+strNW(b)+'cm'))+'}'
    return [afg,lsg,[a,b]]

def erzeugeZusammengesetzRechtecke(n=3,gesamtlaenge=5,hoehe=8,mitText=True):
    punkte=[]
    endlaenge=gesamtlaenge
    for i in range(n):
        if endlaenge>0:
#            punkte.append([random.randint(1,endlaenge if endlaenge<int(endlaenge/2+0.5) else int(endlaenge/2+0.5)),random.randint(1,hoehe)])
            pkt=[random.randint(1,int(1.0*endlaenge/(n-i))+1),random.randint(1,hoehe)]
            if len(punkte)>0:
                while pkt[1]==punkte[-1][1]:
                    pkt=[random.randint(1,int(1.0*endlaenge/(n-i))+1),random.randint(1,hoehe)]
            punkte.append(pkt)
#            punkte.append([random.randint(1,endlaenge),random.randint(1,hoehe)])
            endlaenge=endlaenge-punkte[-1][0]
    afg=['\pbox{'+str(gesamtlaenge)+'cm}{']
    if mitText:
        afg.append('Berechne die Fläche von')
    afg.append('\n'.join(zusammengesetzteRechtecke(punkte,mitLsg=False)))
    afg.append('}') 
    lsg=['\pbox{'+str(gesamtlaenge)+'cm}{']
    flaeche=''
    A_str='$A='
    A=0
    for i,pkt in enumerate(punkte):
        A_str=A_str+' A_'+str(i+1)+('+' if i<len(punkte)-1 else '')
        flaeche=flaeche+'$A_'+str(i+1)+'='+str(pkt[0])+'·'+str(pkt[1])+'='+str(pkt[0]*pkt[1])+' cm^2$, '
        if i%2==1:
            flaeche=flaeche+'\\\\'
        A=A+pkt[0]*pkt[1]
    flaeche=flaeche+A_str+'='+str(A)+' cm^2$\\\\'
    lsg.append(flaeche)
    lsg.append('\n'.join(zusammengesetzteRechtecke(punkte,mitLsg=True)))
    lsg.append('}') 
    print(lsg)
    return [afg,lsg,punkte]
    
def erzeugeZusammengesetzRechteckeSchwer(n=3,gesamtlaenge=5,maxHoehe=8,mitText=True):#Beispiel:
#Jedes Rechteck wird von zwei Punkte aufgespannt: 
#           rechtecke=[punkte1,punkte2,...
#           punkte1=[[x_0,y_0],[x_1,y_1]] usw.
#Soll das Rechteck über die Gesamte Seitebreite gezeichnet werden,  nutze 17 cm. In einer Tabelle z.B. 7 cm oder 8 cm.
#Das erste Rechteck soll Maximal Gesamtbreite/(Anzahl Rechtecke) breit sein. Damit genügend Platz für alle ist.
    hoehe1=random.randint(1,int(maxHoehe/2))
    hoehe2=random.randint(hoehe1+1,maxHoehe)
    rechtecke=[[[0,hoehe1],[random.randint(1,int(1.0*gesamtlaenge/n)+1),hoehe2]]]
    endlaenge=gesamtlaenge
    for i in range(1,n):
        if endlaenge>0:
            hoehe1=random.randint(1,rechtecke[-1][1][1]-1)
            hoehe2=random.randint(max(hoehe1,rechtecke[-1][0][1])+1,maxHoehe)
            breite=random.randint(1,int(1.0*endlaenge/(n-i))+1)
            rechtecke.append([[rechtecke[-1][1][0],hoehe1],[rechtecke[-1][1][0]+breite,hoehe2]])
            endlaenge=endlaenge-rechtecke[-1][1][0]
    afg=['\pbox{'+str(gesamtlaenge)+'cm}{']
    if mitText:
        afg.append('Berechne die Fläche von')
    afg.append('\n'.join(zusammengesetzteRechteckeSchwer(rechtecke,mitLsg=False)))
    afg.append('}')             
    lsg=['\pbox{'+str(gesamtlaenge)+'cm}{']
    flaeche=''
    A=0
    for i,pkt in enumerate(rechtecke):
        flaeche=flaeche+'$A_'+str(i+1)+'='+str(pkt[1][0]-pkt[0][0])+'·'+str(pkt[1][1]-pkt[0][1])+'='+str((pkt[1][0]-pkt[0][0])*(pkt[1][1]-pkt[0][1]))+' cm^2$, '
        if i%2==1:
            flaeche=flaeche+'\\\\'
        A=A+(pkt[1][0]-pkt[0][0])*(pkt[1][1]-pkt[0][1])
    flaeche=flaeche+'$A='+str(A)+' cm^2$\\\\'
    lsg.append(flaeche)
    lsg.append('\n'.join(zusammengesetzteRechteckeSchwer(rechtecke,mitLsg=True)))
    lsg.append('}')    
    return [afg,lsg,rechtecke]

def erzeugeFlaechenDreieckAufgabe(mitText=True,mitBeschr=True):
    g=random.randint(20,50)/10
    h=random.randint(20,50)/10
    drehung=random.randint(0,360)
    dx=random.randint(0,int(g)+2)-g
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+dreieckFuerFlaechenBer(g=g,h=h,drehung=drehung,dx=dx,mitBeschr=mitBeschr)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg=lsg+[F'A&=g\cdot \\frac{{h}}{{2}} \\\\']
    lsg=lsg+[F'&={strNW(g)}\cdot \\frac{{{strNW(h)}}}{{2}}={strNW(g*h/2,2)}~cm^2']
    lsg=lsg+[F'\\end{{aligned}}$']
    lsg=lsg+dreieckFuerFlaechenBer(g=g,h=h,drehung=drehung,dx=dx,mitBeschr=True)
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeFlaechenParallelogrammAufgabe(mitText=True,mitBeschr=True):
    g=random.randint(20,50)/10
    h=random.randint(20,50)/10
    drehung=random.randint(0,360)
    dx=random.randint(0,30)/10
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+parallogrammFuerFlaechenBer(g=g,h=h,dx=dx,drehung=drehung,mitBeschr=mitBeschr)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg=lsg+[F'A&=g\cdot h \\\\']
    lsg=lsg+[F'&={strNW(g)}\cdot {strNW(h)}={strNW(g*h,2)}~cm^2']
    lsg=lsg+[F'\\end{{aligned}}$']
    lsg=lsg+parallogrammFuerFlaechenBer(g=g,h=h,dx=dx,drehung=drehung,mitBeschr=True)
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeFlaechenDrachenAufgabe(mitText=True,mitBeschr=True,mitEundF=True,istRaute=False):
    e=random.randint(20,50)/10
    f=random.randint(20,50)/10
    drehung=random.randint(0,360)
    dx=e/2 if istRaute else random.randint(5,int(e*10))/10
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+dracheFuerFlaechenBer(e=e,f=f,dx=dx,drehung=drehung,mitBeschr=mitBeschr,mitEundF=mitEundF)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg=lsg+[F'A&=\\frac{{1}}{{2}}\\cdot e\\cdot f \\\\']
    lsg=lsg+[F'&=\\frac{{1}}{{2}}\\cdot{strNW(e)}\cdot {strNW(f)}={strNW(0.5*e*f,2)}~cm^2']
    lsg=lsg+[F'\\end{{aligned}}$']
    lsg=lsg+dracheFuerFlaechenBer(e=e,f=f,dx=dx,drehung=drehung,mitBeschr=mitBeschr)
    lsg=lsg+['}']
    return [afg,lsg,[]]