#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeKgv():
#Erzeugt eine Aufgabe zur Berechnung des kleinsten gemeinsamen Vielfachens
#Aufruf: [afg,lsg,[a,b]]=erzeugeKgv()
    a=random.randint(5,12)
    b=random.randint(2,a)
    erg=kgV(a,b)
    afg='kgV('+strNW(a)+','+strNW(b)+')='
    vielfache=[[a],[b]]
    i=2
    while vielfache[0][-1] <erg or vielfache[1][-1] < erg:
        vielfache[0].append(vielfache[0][0]*i)
        vielfache[1].append(vielfache[1][0]*i)
        i=i+1
    lsg='\pbox{20cm}{'+afg+strNW(erg)+'\\\\'
    lsg=lsg+'V('+strNW(a)+'): '+','.join(list(map(strNW,vielfache[0])))+'\\\\'
    lsg=lsg+'V('+strNW(b)+'): '+','.join(list(map(strNW,vielfache[1])))+'\\\\'+'}'
    return [afg,lsg,[a,b]]

def erzeugeGgt():
#Erzeugt eine Aufgabe zur Berechnung des größten gemeinsamen Teilers.
#Aufruf: [afg,lsg,[a,b]]=erzeugeGgt()
#if True:
    a=random.randint(8,50)
    b=random.randint(2,50)
    i=0
    while ggt(a,b)<3 or i<1:
        a=random.randint(8,50)
        b=random.randint(2,50)
        i=i+1
    erg=ggt(a,b)
    afg='ggT('+strNW(a)+','+strNW(b)+')='
    teiler=[]
    for z in [a,b]:
        t=[]
        for i in range(1,int(z)+1):
            if int(z)%i==0:
                t.append(i)
        teiler.append(t)
    lsg='\pbox{20cm}{'+afg+strNW(erg)+'\\\\'
    lsg=lsg+'T('+strNW(a)+'): '+','.join(list(map(strNW,teiler[0])))+'\\\\'
    lsg=lsg+'T('+strNW(b)+'): '+','.join(list(map(strNW,teiler[1])))+'\\\\'+'}'
    return [afg,lsg,[a,b]]

def BruchMitNatuerlicherZahlMultiPfeildarstellung():
#Diese Funktion erzeugt eine Aufgabe, in der die SuS erkennen sollen, welche Multiplikationsaufgabe dargestellt wird.
    n=random.randint(2,8)
    z=random.randint(1,n-1)
    faktor=random.randint(2,10)
    afg=zeichneBruchMultiNZahlPfeile([z,n],faktor)
    afg.append('\\newline')
    afg=afg+zahlenstrahlMitEinteilung(0,math.ceil(z/n*faktor),n)
    lsg=zeichneBruchMultiNZahlPfeile([z,n],faktor,mitLSG=True)
    lsg.append('\\newline')
    lsg=lsg+zeichneBruchMultiNZahlPfeile([z*faktor,n],1,mitLSG=True)
    lsg.append('\\newline')
    zahlen=[]
    return [afg,lsg,zahlen]

def BruchMitNatuerlicherZahlMulti():
#Diese Funktion erstellt eine Aufgabe, in der ein Bruch mit einer natürlichen Zahl multipliziert werden soll.
#Ausgabe: [[Aufgabe],[Loesung]]
#          Aufgabe=[z1,z2,n,'*',faktor]
    z=random.randint(1,12)
    n=random.randint(2,15)
    faktor=random.randint(1,12)
    if random.randint(1,2)==2:
        afg='$'+strNW(faktor)+'\\cdot'+frac(z,n)+'=$'
        lsg='$'+strNW(faktor)+'\\cdot'+frac(z,n)+'='+'\\frac{'+str(faktor)+'\\cdot'+str(z)+'}{'+str(n)+'}='
    else:
        afg='$'+frac(z,n)+'\\cdot'+strNW(faktor)+'=$'
        lsg='$'+frac(z,n)+'\\cdot'+strNW(faktor)+'='+'\\frac{'+str(z)+'\\cdot'+str(faktor)+'}{'+str(n)+'}='
    teiler=ggt(faktor*z,n)
    lsg=lsg+frac(faktor*z,n)+('' if teiler==1 else ('='+frac(faktor*z/teiler,n/teiler)))+(('='+schreibeGemZahl(faktor*z/teiler,n/teiler)) if (faktor*z>n) else '')+'$'
    zahlen=[faktor,[z,n],[z*faktor,n]]
    return [afg,lsg,zahlen]

def zweiBruecheMulti(werte=[]):
#Diese Funktion erstellt eine Aufgabe, in der zwei Brüche multipliziert werden sollen
#Ausgabe: [[Aufgabe],[Loesung],[Zahlen]]
    z1,n1,z2,n2=[0,0,0,0]
    while z1==n1 or z2==n2:
        z1,n1,z2,n2=[random.randint(2,12) for i in range(4)] if len(werte)==0 else werte
    afg='$'+frac(z1,n1)+'\\cdot'+frac(z2,n2)+'=$'
    teiler=ggt(z1*z2,n1*n2)
    lsg='$'+frac(z1,n1)+'\\cdot'+frac(z2,n2)+'='+'\\frac{'+str(z1)+'\\cdot'+str(z2)+'}{'+str(n1)+'\\cdot'+str(n2)+'}='+frac(z1*z2,n2*n1)
    lsg=lsg+('' if teiler==1 else ('='+frac(z1*z2/teiler,n2*n1/teiler)))+(('='+schreibeGemZahl(z1*z2/teiler,n2*n1/teiler)) if (z1*z2>n2*n1) else '')+'$'
    zahlen=[z1,n1,z2,n2]
    return [afg,lsg,zahlen]


def zweiBruecheDividieren():
#Diese Funktion erstellt eine Aufgabe, in der zwei Brüche multipliziert werden sollen
#Ausgabe: [[Aufgabe],[Loesung],[Zahlen]]
    z1,n1,z2,n2=[0,0,0,0]
    while z1==n1 or z2==n2:
        z1,z2=[random.randint(1,12) for i in range(2)]
        n1,n2=[random.randint(2,12) for i in range(2)]
    afg='$'+frac(z1,n1)+':'+frac(z2,n2)+'=$'
    lsg='$'+frac(z1,n1)+':'+frac(z2,n2)+'='
#Man kann hier die Loesung von zwei Bruechen multiplizieren nutzen. Reduziert schreibarbeit
    a,l,d=zweiBruecheMulti([z1,n1,n2,z2])
    lsg=lsg+l[1:] #l[0]='$', das haben wir schon
    zahlen=[z1,n1,z2,n2]
    return [afg,lsg,zahlen]

def erzeugeBruchAddition(gleichnamig=True,operator='+'):
#Diese Funktion erstellt eine Aufgabe zur Addition oder Subtraktion gleichnamiger oder ungleichnamiger Brüche
#Ausgabe: [afg,lsg,zahlen]=erzeugeBruchAddition(gleichnamig=False,operator='-')
    erg=-1
    n1,z1,n2,z2=1,1,1,1
    while erg<1 or z1%n1==0 or z2%n2==0:
        n1=random.randint(2,10)
        z1=random.randint(1,12)
        n2=n1 if gleichnamig else random.randint(2,10)
        z2=random.randint(1,20)
        viel=kgV(n1,n2)
        z1V=1.0*(viel/n1)*z1
        z2V=1.0*(viel/n2)*z2
        erg=eval(str(z1V)+operator+str(z2V))
        teiler=ggt(erg,viel)
    zahlen=[[z1,n1],operator,[z2,n2],[erg,viel],[z1V,viel],[z2V,viel],[erg/teiler,viel/teiler] if teiler>1 else []]
    afg='$'+frac(z1,n1)+operator+frac(z2,n2)+'=$'
    lsgMitPfeilmethode=True
    if lsgMitPfeilmethode:
        if n1==n2:
            gemZahl=schreibeGemZahl(erg,viel)
            lsg='$'+frac(z1,n1)+operator+frac(z2,n2)+'='+frac(erg,viel)+'='+gemZahl+'$'
        else:
            lsg='\n'.join(ungleicheBruecheAddierenSubtrahierenTikz(zahlen[0],zahlen[2],zahlen[1]))
    else:
        zwischen='' if n1==n2 else frac(z1V,viel)+operator+frac(z2V,viel)+'='
        ergGemZahl=int(erg/viel)
        gemZahl='' if erg < viel else ('' if erg-ergGemZahl*erg==0 else ('='+str(ergGemZahl)+frac(erg-ergGemZahl*viel,viel)))
        gekuerzt='' #if len(zahlen[6])==0 else ('='+schreibeGemZahl(int(zahlen[6][0]),int(zahlen[6][1])))
        lsg='$'+frac(z1,n1)+operator+frac(z2,n2)+'='+zwischen+frac(erg,viel)+gemZahl+gekuerzt+'$'
    return [afg,lsg,zahlen]
            
def erzeugeKuerzen(mitTeiler=False):
#Diese Funktion erzeugt eine Aufgabe, zum kürzen von Brüchen.
#       [afg,lsg,[a,b,f]]=erzeugeKuerzen()
#       [afg,lsg,[a,b,f]]=erzeugeKuerzen(mitTeiler=True)
#Im zweiten Fall wird der Teiler, mit dem die SuS erweitern sollen, in die Aufgabe geschrieben.
    teiler=random.randint(2,5)
    a=teiler*random.randint(1,9)
    b=teiler*random.randint(2,15)
    while a>=b:
        b=teiler*random.randint(2,20)
    maxTeiler=ggt(a,b)
    if mitTeiler:
        afg='Kürze den Bruch $'+frac(a,b)+'$ mit dem Teiler '+strNW(maxTeiler)+'.' 
    else:
        afg='Kürze soweit wie möglich: $'+frac(a,b)+'$'
    lsg='$'+frac(a,b)+'=\\frac{'+strNW(a)+':'+strNW(maxTeiler)+'}{'+strNW(b)+':'+strNW(maxTeiler)+'}='+frac(a/maxTeiler,b/maxTeiler)+'$'  
    return [afg,lsg,[a,b,maxTeiler]]

def erzeugeErweitern():
#Diese Funktion erzeugt eine Aufgabe, zum Erweitern von Brüchen.
#       [afg,lsg,[a,b,f]]=erzeugeErweitern()
    a=random.randint(1,12)
    b=random.randint(a+1,20)
    f=random.randint(2,10)
    afg='Erweiter den Bruch $'+frac(a,b)+'$ mit dem Faktor '+strNW(f)+'.' 
    lsg='$'+frac(a,b)+'=\\frac{'+strNW(a)+'\cdot'+strNW(f)+'}{'+strNW(b)+'\cdot'+strNW(f)+'}='+frac(a*f,b*f)+'$'  
    return [afg,lsg,[a,b,f]]

def erzeugeBruchteileBerechnen():
#Diese Funktion erzeugt eine Aufgabe zum berechnen von Bruchteilen.. 
#      [afg,lsg,[bruch,teil,ganzes]]=erzeugeBruchteileBerechnen()
    einheit=random.choice(['m','kg','mm','l','ml','g','dm','T','km','cm','dl','cl'])
    bruch=erzeugeBrueche(1)[0]
    teil=bruch[0]*random.randint(2,8)
    ganzes=teil/bruch[0]*bruch[1]
    afg='Berechne $'+frac(bruch[0],bruch[1])+'$ von '+strNW(ganzes)  +' '+einheit
    lsg='\pbox{5cm}{'
    lsg=lsg+'$'+frac(bruch[0],bruch[1])+'$ von '+strNW(ganzes)+' '+einheit+' sind '+strNW(teil)+' '+einheit+'\\\\'
    lsg=lsg+'\n'.join(zeichneBruchteilBerechnen(ganzes,bruch,einheit))+'}'
    return [afg,lsg,[bruch,teil,ganzes]]

def erzeugeGanzesBerechnen():
#Diese Funktion erzeugt eine Aufgabe zum berechnen von Bruchteilen.. 
#      [afg,lsg,[bruch,teil,ganzes]]=erzeugeBruchteileBerechnen()
    einheit=random.choice(['m','kg','mm','l','ml','g','dm','T','km','cm','dl','cl'])
    bruch=erzeugeBrueche(1)[0]
    teil=bruch[0]*random.randint(2,8)
    ganzes=teil/bruch[0]*bruch[1]
    afg='Bestimme $'+frac(bruch[0],bruch[1])+'$ von \\rule{2cm}{0.4pt} sind '+strNW(teil)  +' '+einheit
    lsg='\pbox{5cm}{'
    lsg=lsg+'$'+frac(bruch[0],bruch[1])+'$ von '+strNW(ganzes)+' '+einheit+' sind '+strNW(teil)+' '+einheit+'\\\\'
    lsg=lsg+'\n'.join(zeichneGanzesBerechnen(teil,bruch,einheit))+'}'
    return [afg,lsg,[bruch,teil,ganzes]]

def erzeugeBruchVergleichen():
#Diese Funktion erzeugt eine Aufgabe zum vergleichen von Brüchen. 
#      [afg,lsg,brueche]=erzeugeBruchVergleichen()
#Die Lösung enthält eine Tikz- Zeichnung, wenn die Brüche ungleichnamig sind.
    brueche=erzeugeBrueche(n=2)
    afg='Vergleiche $'+frac(brueche[0][0],brueche[0][1])+'$ mit  $'+frac(brueche[1][0],brueche[1][1])+'$'
    lsg=zeichneBruchVergleichen(brueche[0],brueche[1])
    return [afg,lsg,brueche]

def erzeugeBrueche(n=2,echt=True,gross=False):
    brueche=[]
    for i in range(n):
        zaehler=random.randint(1,30 if gross else 12)
        nenner=random.randint(zaehler+1 if echt else 1,100 if gross else 20)
        brueche.append([zaehler,nenner])
    return brueche

def erzeugeBruchzuGemischteZahl():
#Diese Funktion erzeugt eine Aufgabe zur Bestimmung einer gemischten Zahl aus einem Bruch.
#      [afg,lsg,[bruch,zahl]]=erzeugeBruchzuGemischteZahl()
    bruch=erzeugeBrueche(1)[0]
    zahl=random.randint(1,10)
    afg='\pbox{5cm}{Schreibe als gemischte Zahl:\\\\'
    afg=afg+'$'+frac(bruch[0]+bruch[1]*zahl,bruch[1])+'$'+'}'
    lsg='$'+frac(bruch[0]+bruch[1]*zahl,bruch[1])+'='+frac(bruch[1]*zahl,bruch[1])+'+'+frac(bruch[0],bruch[1])+'='+strNW(zahl)+frac(bruch[0],bruch[1])+'$'
    return [afg,lsg,[bruch,zahl]]

def erzeugeGemischteZahlZuBruch():
#Diese Funktion erzeugt eine Aufgabe zur Bestimmung einer gemischten Zahl aus einem Bruch.
#      [afg,lsg,[bruch,zahl]]=erzeugeBruchzuGemischteZahl()
    bruch=erzeugeBrueche(1)[0]
    zahl=random.randint(1,10)
    afg='\pbox{20cm}{Schreibe als Bruch:\\\\'
    afg=afg+'$'+strNW(zahl)+frac(bruch[0],bruch[1])+'$'+'}'
    lsg='$'+strNW(zahl)+frac(bruch[0],bruch[1])+'='+frac(bruch[1]*zahl,bruch[1])+'+'+frac(bruch[0],bruch[1])+'='+frac(bruch[0]+bruch[1]*zahl,bruch[1])
    lsg=lsg+'='+frac(bruch[0]+bruch[1]*zahl,bruch[1])+'$'
    return [afg,lsg,[bruch,zahl]]

def erzeugeBruechGemischte(anzahl=30, proReihe=3):
#Erzeuge eine Aufgabe mit gemischten Zahlen:
#Rechnung=[[zaehler,nenner,gemische Zahl Wert,gemische Zahl Zaehler, gemische Zahl Nenner],...]
    brueche=[]
    for i in range(int(anzahl/proReihe)):
        reihe=[]
        for j in range(proReihe):
            z2=''
            while z2=='':
                nenner=random.randint(2,10)
                zaehler=random.randint(nenner,nenner*6)
                zahl='' if nenner>zaehler else str(int(1.0*zaehler/nenner))
                z2='' if zaehler%nenner==0 else str(zaehler%nenner)
                n2='' if zaehler%nenner==0 else str(nenner)
            z1=str(zaehler)
            n1=str(nenner)
            zlen1=max(map(len,[z1,n1]))
            zlen2=max(map(len,[z2,n2]))
            reihe.append([' '*(zlen1-len(z1))+z1,' '*(zlen1-len(n1))+n1,zahl,' '*(zlen2-len(z2))+z2,' '*(zlen2-len(n2))+n2])
        brueche.append(reihe)
    return brueche


def BruchReiheAufgabe(position=None,faktorenBeliebig=False):
#Diese Funktion erzeugt eine Aufgabe zur Bestimmung von fehlenden Zählern in einer Gleichheitsreihe von Brüchen. Genutzt wird die Funktion erzeugeBruchReihe()
#      [afg,lsg,reihe]=BruchReiheAufgabe()
    reihe=erzeugeBruchReihe(position,faktorenBeliebig)
    afg='\pbox{7cm}{Schreibe die fehlenden Zähler auf:\\\\ '
    afg=afg+'$'+'='.join([frac(x[0],x[1]) for x in reihe])+'$'+'}'
    ind=[i for i,x in enumerate(reihe) if len(x[0])>0][0]
    lsg='$'+'='.join([frac(1.0*int(x[1])/int(reihe[ind][1])*int(reihe[ind][0]),x[1]) for x in reihe])+'$'
    return [afg,lsg,reihe]

def erzeugeBruchReihe(position=None,faktorenBeliebig=False):
#Diese Funktion erzeugt eine Aufgabe in Form von
#   []/4=[]/8=4/16=[]/64
#Die SuS sollen die fehlenden Zahlen eintragen.
#Die Faktoren können beliebig sein, oder aufeinander aufbauen. Z.B.:
#           f[0]=2; f[1]=f[0]*3; f[2]=f[1]*2 usw.
# Ausgabe: [['',2],['',4],[4,8],['',16]]=erzeugeBruchReihe()
    nenner=[10000000]
    zaehler=[1]
    while int(nenner[-1])>1000:
    #Der Letzte Nenner soll nicht größer als 1000 sein.
        zaehlerStart=random.randint(1,4)
        nennerStart=random.randint(zaehlerStart+1,10)
        while ggt(zaehlerStart,nennerStart)>1:
        #Der erste Bruch soll nichtmehr teilbar sein.
            zaehlerStart=random.randint(1,5)
            nennerStart=random.randint(zaehlerStart+1,10)
        faktoren=[1]*5
        for i in range(1,len(faktoren)):
        #Die Faktoren sollen untereinander mal genommen werden können.
            faktoren[i]=faktoren[i-1]*random.randint(2,4)
        faktoren=random.sample(range(2, 15), 5) if faktorenBeliebig==True else faktoren
        zaehler=[str(x*zaehlerStart) for x in faktoren]
        nenner=[str(x*nennerStart) for x in faktoren]
    indexBehalten=random.randint(0,len(nenner)-1) if position==None else position
    return [[zaehler[i],x] if i==indexBehalten else ['',x] for i,x in enumerate(nenner)]

def erzeugeBruecheVergleichen(art,gesamt=20,proReihe=2):
#Diese Funktion erzeugt "gesamt" Anzahl an Brüchen, die mit <,>,= vergliechen werden sollen.
#        art=='GleicherNenner' --> Die Nenner zweier Brüche sind gleich
#        art=='GleicherZaehler' --> Die Zähler zweier Brüche sind gleich
#Die Ausgabe erfolgt in Stringformat und zwar so formatiert, dass Nenner und Zähler
#Die gleiche Anzahl an Stringcharacktäre brauchen. Dies werden mit Leerzeichen aufgefüllt:
#		 ausgabe =[[['z1','n1'],'>',['z2','n2'],....]...
#        beispiel=[[[' 7','12'],'<',[' 8','12'],...],[[['9','9'],'>',[' 1','9'],...
#Ausgabe: 
    tabelle=[]
    count=0
    for j in range(gesamt/proReihe):
        zeile=[]
        for i in range(proReihe):
#Erzeuge zwei Brüche
            z1=random.randint(1,10)
            z2=random.randint(1,10)
            n1=random.randint(z1+1,12)
            n2=random.randint(z2+1,12)
            if art=='GleicherNenner':
                n2=n1
                z2=random.randint(1,n1)
            if art=='GleicherZaehler':
                z2=z1
                n2=random.randint(z2+1,20)
#Bestimme das vorzeichen
            vZ='>' if (1.0*z1/n1)>(1.0*z2/n2) else ('<' if (1.0*z1/n1)<(1.0*z2/n2) else '=')    #Vergleichszeichen
            if n1==n2 or z1==z2:
                b1=[str(z1),str(n1)]
                zlen=max(map(len,b1))
                b1=[' '*(zlen-len(b1[0]))+b1[0],' '*(zlen-len(b1[1]))+b1[1]]
                b2=[str(z2),str(n2)]
                zlen=max(map(len,b2))
                b2=[' '*(zlen-len(b2[0]))+b2[0],' '*(zlen-len(b2[1]))+b2[1]]
            else:
                vielF=kgV(n1,n2)
                b1=[str(z1),str(n1),str(z1*vielF/n1),str(vielF)]
                zlen1=max(map(len,b1[:2]))
                zlen2=max(map(len,b1[2:]))
                b1=[' '*(zlen1-len(b1[0]))+b1[0],' '*(zlen1-len(b1[1]))+b1[1],' '*(zlen2-len(b1[2]))+b1[2],' '*(zlen2-len(b1[3]))+b1[3]]
                b2=[str(z2),str(n2),str(z2*vielF/n2),str(vielF)]
                zlen1=max(map(len,b2[:2]))
                zlen2=max(map(len,b2[2:]))
                b2=[' '*(zlen1-len(b2[0]))+b2[0],' '*(zlen1-len(b2[1]))+b2[1],' '*(zlen2-len(b2[2]))+b2[2],' '*(zlen2-len(b2[3]))+b2[3]]
            zeile=zeile+[[buchstaben[26+count]+')',b1,vZ,b2]]
            count=count+1
        tabelle.append(zeile)
    return tabelle
