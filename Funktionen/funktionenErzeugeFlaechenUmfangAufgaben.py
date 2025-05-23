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
#    lsg='\\pbox{'+breitePbox+'cm}{$A=a\cdot b$ \\\\ $a='+strNW(a)+'cm\cdot'+strNW(b)+'cm='+strNW(a*b)+'cm^2$ \\\\'
#    lsg=lsg+'\n'.join(rechteckTikz(a,b,beschrSeiten=True,texta='a='+strNW(a)+'cm',textb='b='+strNW(b)+'cm'))+'}'
    lsg=['\\pbox{5cm}{']
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg.append(F'geg.: a&={strNW(a)} cm \\\\')
    lsg.append(F'   b&={strNW(b)} cm \\\\')
    lsg.append(F'ges.: A&=? \\\\')
    lsg.append(F'A&=a\\cdot b \\\\')
    lsg=lsg+[F'&={strNW(a)}\\cdot {strNW(b)} \\\\']
    lsg=lsg+[F'A&={strNW(a*b,2)}~cm^2']
    lsg.insert(-1, F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg=lsg+[F'\\end{{aligned}}$']
    lsg=lsg+rechteckTikz(a,b,beschrSeiten=True,texta='a='+strNW(a)+'cm',textb='b='+strNW(b)+'cm')
    lsg=lsg+['}']
    return [afg,lsg,[a,b]]

def erzeugeZusammengesetzRechtecke(n=3,gesamtlaenge=5,hoehe=8,mitText=True):
    punkte=[]
    endlaenge=gesamtlaenge
#Erzeuge die Eckpunkte oben Rechts, z.B: punkte=[[1, 3], [2, 5], [1, 3]]
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
    drehung=random.randint(-90,90)
    dx=random.randint(0,int(g)+2)-g
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+dreieckFuerFlaechenBer(g=g,h=h,drehung=drehung,dx=dx,mitBeschr=mitBeschr)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg.append(F'geg.: g&={strNW(g)} cm \\\\')
    lsg.append(F'   h&={strNW(h)} cm \\\\')
    lsg.append(F'ges.: A&=? \\\\')
    lsg=lsg+[F'A&=\\frac{{g \\cdot h}}{{2}} \\\\']
    lsg=lsg+[F'&={strNW(g)} \\cdot \\frac{{{strNW(h)}}}{{2}}\\\\']
    lsg=lsg+[F'A&={strNW(g*h/2,2)}~cm^2']
    lsg.insert(-1, F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg=lsg+[F'\\end{{aligned}}$']
    lsg=lsg+dreieckFuerFlaechenBer(g=g,h=h,drehung=drehung,dx=dx,mitBeschr=True)
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeFlaechenParallelogrammAufgabe(mitText=True,mitBeschr=True):
    g=random.randint(20,50)/10
    h=random.randint(20,50)/10
    drehung=random.randint(-90,90)
    dx=random.randint(0,30)/10
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+parallogrammFuerFlaechenBer(g=g,h=h,dx=dx,drehung=drehung,mitBeschr=mitBeschr)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg.append(F'geg.: g&={strNW(g)} cm \\\\')
    lsg.append(F'   h&={strNW(h)} cm \\\\')
    lsg.append(F'ges.: A&=? \\\\')
    lsg.append(F'A&=g\\cdot h \\\\')
    lsg=lsg+[F'&={strNW(g)}\cdot {strNW(h)} \\\\']
    lsg=lsg+[F'A&={strNW(g*h,2)}~cm^2']
    lsg.insert(-1, F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg=lsg+[F'\\end{{aligned}}$']
    lsg=lsg+parallogrammFuerFlaechenBer(g=g,h=h,dx=dx,drehung=drehung,mitBeschr=True)
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeFlaechenDrachenAufgabe(mitText=True,mitBeschr=True,mitEundF=True,istRaute=False):
    e=random.randint(20,50)/10
    f=random.randint(20,50)/10
    drehung=random.randint(-90,90)
    dx=e/2 if istRaute else random.randint(5,int(e*10))/10
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+dracheFuerFlaechenBer(e=e,f=f,dx=dx,drehung=drehung,mitBeschr=mitBeschr,mitEundF=mitEundF)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+dracheFuerFlaechenBer(e=e,f=f,dx=dx,drehung=drehung,mitBeschr=True,mitEundF=True)
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg.append(F'geg.: e&={strNW(e)} cm \\\\')
    lsg.append(F'   f&={strNW(f)} cm \\\\')
    lsg.append(F'ges.: A&=? \\\\')
    lsg.append(F'A&=\\frac{{1}}{{2}}\\cdot e\\cdot f \\\\')
    lsg.append(F'&=\\frac{{1}}{{2}}\\cdot{strNW(e)}\cdot {strNW(f)}\\\\')
    lsg.append(F'A&={strNW(0.5*e*f,2)}~cm^2')
    lsg.insert(-1, F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append(F'\\end{{aligned}}$')
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugeFlaechenTrapezAufgabe(mitText=True,mitBeschr=True):
    a=random.randint(20,50)/10
    c=random.randint(10,int(a)*10)/10
    h=random.randint(20,50)/10
    drehung= random.randint(-90,90)
    dx=random.randint(0,int((a-c)*10))/10
    afg=['\\pbox{5cm}{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+trapezFuerFlaechenBer(a=a,c=c,h=h,dx=dx,drehung=drehung,mitBeschr=mitBeschr)
    afg=afg+['}']
    lsg=['\\pbox{5cm}{']
    lsg=lsg+trapezFuerFlaechenBer(a=a,c=c,h=h,dx=dx,drehung=drehung,mitBeschr=True)
    lsg=lsg+[F'$\\begin{{aligned}}']
    lsg.append(F'geg.: a&={strNW(a)} cm \\\\')
    lsg.append(F'   c&={strNW(c)} cm \\\\')
    lsg.append(F'   h&={strNW(h)} cm \\\\')
    lsg.append(F'ges.: A&=? \\\\')
    lsg.append(F'A&=\\frac{{a+c}}{{2}}\\cdot h \\\\')
    lsg.append(F'&=\\frac{{{strNW(a)}+{strNW(c)}}}{{2}}\\cdot{strNW(h)}\\\\')
    lsg.append(F'A&={strNW(0.5*(a+c)*h,2)}~cm^2')
    lsg.insert(-1, F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append(F'\\end{{aligned}}$')
    lsg=lsg+['}']
    return [afg,lsg,[]]

def erzeugePfeilFlaechenBerechnung(anzSpalten=2,mitText=True):
    a=random.randint(10,60 if anzSpalten<2 else 40)/10;
    b=random.randint(10,30)/10;
    z=random.randint(10,20)/10;
    g=b+2*z
    if anzSpalten>1:
        h=random.randint(10,(50-a*10))/10;
    else:
        h=random.randint(10,50)/10;
    afg=[F'\\pbox{{{15 if anzSpalten==1 else 5}cm}}{{']
    afg=afg+([F'Berechne den Flächeninhalt von:\\\\']  if mitText else [])
    afg=afg+pfeilFlaechenBer(a=a,b=b,g=g,h=h,z=z,lsg=False)
    afg=afg+['}']
    lsg = ['\\pbox{7cm}{']
    lsg= lsg + pfeilFlaechenBer(a=a,b=b,g=g,h=h,z=z,lsg=True)+['\\\\']
    lsg=lsg+['$\\begin{aligned}']
    lsg.append(F'geg.: a &={strNW(a)}~cm& & \\\\')
    lsg.append(F'  b &={strNW(b)}~cm& & \\\\')
    lsg.append(F'  g &={strNW(g)}~cm& & \\\\')
    lsg.append(F'  h &={strNW(h)}~cm& & \\\\')
    lsg.append(F'ges.: A_G &=?~cm^2& & \\\\')
    lsg.append(F'& & & \\\\')
    lsg.append(F'A_G&= A_R+A_D & & \\\\')
    lsg.append(F'A_R&= a \\cdot b & & \\\\')
    lsg.append(F'A_R&= {strNW(a)} \\cdot {strNW(b)}={strNW(a*b)}cm^2 & & \\\\')
    lsg.insert(-1,F'\\makebox[0pt][l]{{\\uline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append(F'A_D&= \\frac{{g\\cdot h}}{{2}} & & \\\\')
    lsg.append(F'A_D&= \\frac{{{strNW(g)}\\cdot {strNW(h)}}}{{2}} ={strNW(g*h/2)} cm^2& & \\\\')
    lsg.insert(-1,F'\\makebox(0pt,-0.25cm)[l]{{\\uline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append(F'A_G&= A_R+A_D={strNW(a*b)}+{strNW(g*h/2)}={strNW(a*b+g*h/2)} cm ^2& & \\\\')
    lsg.insert(-1,F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append('\\end{aligned}$')
    lsg.append('}')
    return [afg,lsg,[]]

def trapezGruenBlauGroesserAufgabe(anzSpalten=2,mitText=True):
    R=random.randint(50,65)
    h=random.randint(20,30)
    dR=int(h/(0.75**0.5))
    h1=int(0.75**0.5*R)
    gesamtHoehe=2*(int(0.75**0.5*R)+h)
    afg=[F'\\pbox{{{15 if anzSpalten==1 else 5}cm}}{{']
    afg=afg+([F'Welche Fläche ist größer, grün oder Blau?\\\\']  if mitText else [])
    afg=afg+trapezMitTrapezenUmrandet(R=R,h=h)
    afg=afg+['}']
    lsg = ['\\pbox{7cm}{']
    lsg=lsg+trapezMitTrapezenUmrandet(R=R,h=h,LSG=True)
    lsg=lsg+['$\\begin{aligned}']
    lsg.append(F'geg.: a_1 &={strNW(2*R)}~cm& & \\\\')
    lsg.append(F'  c_1 &={strNW(R)}~cm& & \\\\')
    lsg.append(F'  h_1 &={int(gesamtHoehe)}:2-{h}={strNW(int(h1))}~cm& & \\\\')
    lsg.append(F'  a_2 &={strNW(int(R+dR))}~cm& & \\\\')
    lsg.append(F'  c_2 &={strNW(R)}~cm& & \\\\')
    lsg.append(F'  h_2 &={int(h)}~cm & \\\\')
    lsg.append(F'ges.: A_{{Gruen}} &=?~cm^2& & \\\\')
    lsg.append(F' A_{{Blau}} &=?~cm^2& & \\\\')
    lsg.append(F'& & & \\\\')
    lsg.append(F'A_{{Gruen}}&= 2\\cdot (\\frac{1}2(a_1+c_1)\\cdot h_1) & & \\\\')
    lsg.append(F'&= 2\\cdot (\\frac{1}2({strNW(2*R)}+{strNW(R)})\\cdot {strNW(h1,True)}) & & \\\\')
    lsg.append(F'A_{{Gruen}}&={strNW(2*(2*R+R)*h1*0.5,True)}~cm^2 & & \\\\')
    lsg.insert(-1,F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append(F'& & & \\\\')
    lsg.append(F'A_{{blau}}&= 6\\cdot (\\frac{1}2(a_2+c_2)\\cdot h_2) & & \\\\')
    lsg.append(F'&= 6\\cdot (\\frac{1}2({strNW(int(R+dR))}+{strNW(R)})\\cdot {strNW(h,True)}) & & \\\\')
    lsg.append(F'A_{{blau}}&={strNW(6*(R+dR+R)*h*0.5,True)}~cm^2 & & \\\\')
    lsg.insert(-1,F'\\makebox[0pt][l]{{\\uuline{{\\phantom{{${lsg[-1].replace("&", "")}$}} }} }}')
    lsg.append('\\end{aligned}$')
    lsg.append(F'Die {"grüne" if 2*(2*R+R)*h1*0.5>6*(R+dR+R)*h*0.5 else "blaue"} Fläche ist größer.')
    lsg.append('}')
    return [afg, lsg, []]