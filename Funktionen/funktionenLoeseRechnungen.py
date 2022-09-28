#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionenLoeseRechnungen.py").read())

buchstaben="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()+"a b c d e f g h i j k l m n o p q e s t u w x y z".split()

malZeichen='·';


def loese10minRechnung(rechnungen):
    loesung=[]
    for nr,r,typ in rechnungen:
        if typ =='ggT':
            zahlen=re.findall(r'\d+',r)
            teiler=[]
            for z in zahlen:
                t=[]
                for i in range(1,int(z)+1):
                    if int(z)%i==0:
                        t.append(i)
                teiler.append(t)
            lsgText=['\pbox{20cm}{']
            lsgText=lsgText+[r+'='+str(ggt(int(zahlen[0]),int(zahlen[1])))+'\\\\']
            lsgText=lsgText+['T('+zahlen[0]+'): '+','.join(list(map(str,teiler[0])))+'\\\\']
            lsgText=lsgText+['T('+zahlen[1]+'): '+','.join(list(map(str,teiler[1])))+'\\\\']
            loesung.append([nr,lsgText+['}']]) 
        if typ =='kgV':
            zahlen=re.findall(r'\d+',r)
            viel=[[int(zahlen[0])],[int(zahlen[1])]]
            i=2
            while viel[0][-1] not in viel[1] and viel[1][-1] not in viel[0]:
                viel[0].append(viel[0][0]*i)
                viel[1].append(viel[1][0]*i)
                i=i+1
            lsgText=['\pbox{20cm}{']
            lsgText=lsgText+[r+'='+str(min([viel[0][-1],viel[1][-1]]))+'\\\\']
            lsgText=lsgText+['V('+zahlen[0]+'): '+','.join(list(map(str,viel[0])))+'\\\\']
            lsgText=lsgText+['V('+zahlen[1]+'): '+','.join(list(map(str,viel[1])))+'\\\\']
            loesung.append([nr,lsgText+['}']]) 
        if typ =='erweitern':
            zaehlerErweitert=str(int(r[0])*int(r[1]))
            nennerErweitert=str(int(r[0])*int(r[2]))
            l=[]
            l.append(nr)   
            l.append('$\\frac{'+r[1]+'}{'+r[2]+'}=\\frac{'+zaehlerErweitert+'}{'+nennerErweitert+'}$')  
            loesung.append(l)  
        if typ =='kuerzen':
            teiler=ggt(int(r[0]),int(r[1]))
            l=[]
            l.append(nr)        
            l.append('$\\frac{'+r[0]+'}{'+r[1]+'}=\\frac{'+schreibIntIfFloatIsInt(int(r[0])/teiler)+'}{'+schreibIntIfFloatIsInt(int(r[1])/teiler)+'}$')  
            loesung.append(l)  
        if typ =='kuerzenMitTeiler':
            teiler=int(r[0])
            l=[]
            l.append(nr)        
            l.append('$\\frac{'+r[1]+'}{'+r[2]+'}=\\frac{'+str(schreibIntIfFloatIsInt(r[1])/teiler)+'}{'+str(schreibIntIfFloatIsInt(r[2])/teiler)+'}$')  
            loesung.append(l)
        if typ =='reihe':
            d=re.findall(r'{.*}{.*}',r)
            bruch=re.findall(r'{\d+}{\d+}',r)
            zaehler=int(re.findall(r'\d+',bruch[0])[0])
            nenner=int(re.findall(r'\d+',bruch[0])[1])
            luecken=re.findall(r'{}{\d+}',r)
            l=['\\frac'+bruch[0]]
            for lueck in luecken:
                faktor=int(int(lueck[3:-1])/nenner)
                l.append('\\frac{'+str(zaehler*faktor)+'}{'+str(nenner*faktor)+'}')
            loesung.append([nr,'Fülle die Lücken: $'+'='.join(l)+'$'])
        if typ =='reihePosZufaellig':
            bruch=re.findall(r'{\d+}{\d+}',r)
            zaehler=int(re.findall(r'\d+',bruch[0])[0])
            nenner=int(re.findall(r'\d+',bruch[0])[1])
            nennerGesamt=[int(re.findall(r'\d+',x)[0]) for x in re.findall(r'{}{\d+}',r)] + [nenner]
            nennerGesamt.sort()
            faktor=[(1.0*x)/nenner for x in nennerGesamt]
            zaehlerGesamt=[x*zaehler for x in faktor]
            for i in range(len(nennerGesamt)):
                l.append('\\frac{'+str(int(zaehlerGesamt[i]*faktor[i]))+'}{'+str(int(nennerGesamt[i]*faktor[i]))+'}')
            loesung.append([nr,'$'+'='.join(l)+'$'])
        if typ == 'bruchVergleichen':
            loesung.append([nr,zeichneBruchVergleichen(r[0],r[1])]) 
        if typ == 'Bruchteil':
            lsgText=['\pbox{20cm}{']
            lsgText=lsgText+['$\\frac{'+r[1]+'}{'+r[2]+'}$ von '+r[0]+' m sind '+r[3]+' m\\\\']
            loesung.append([nr,lsgText+zeichneBruchteilBerechnen(int(r[0]),[int(r[1]),int(r[2])],r[4])+['}']]) 
        if typ == 'GanzesBerechnen':
            lsgText=['\pbox{20cm}{']
            lsgText=lsgText+['$\\frac{'+r[1]+'}{'+r[2]+'}$ von '+r[0]+' '+r[4]+' sind '+r[3]+' '+r[4]+'\\\\']
            loesung.append([nr,lsgText+zeichneGanzesBerechnen(int(r[3]),[int(r[1]),int(r[2])],r[4])+['}']]) 
        if 'BruchAddSub' in typ:
            r1=[[str(int(y)) for y in x] if isinstance(x,list) else x for x in r]
            zwischen='' if r1[0][1]==r1[2][1] else '\\frac{'+r1[4][0]+'}{'+r1[4][1]+'}'+r1[1]+'\\frac{'+r1[5][0]+'}{'+r1[5][1]+'}='
            ergGemZahl=int(r[3][0]/r[3][1])
            gemZahl='' if r[3][0] < r[3][1] else ('' if r[3][0]-ergGemZahl*r[3][1]==0 else ('='+str(ergGemZahl)+frac(r[3][0]-ergGemZahl*r[3][1],r[3][1])))
            gekuerzt='' #if len(r1[6])==0 else ('='+schreibeGemZahl(int(r1[6][0]),int(r1[6][1])))
            loesung.append([nr,'$'+'\\frac{'+r1[0][0]+'}{'+r1[0][1]+'}'+r1[1]+'\\frac{'+r1[2][0]+'}{'+r1[2][1]+'}='+zwischen+'\\frac{'+r1[3][0]+'}{'+r1[3][1]+'}'+gemZahl+gekuerzt+'$'])
        if 'BruchPfeilMethAddSub' in typ:
            r1=[[str(int(y)) for y in x] if isinstance(x,list) else x for x in r]
            if r1[0][1]==r1[2][1]:
                gemZahl=schreibeGemZahl(r[3][0],r[3][1])
                print(r1)
                loesung.append([nr,'$'+frac(r1[0][0],r1[0][1])+r1[1]+frac(r1[2][0],r1[2][1])+'='+frac(r1[3][0],r1[3][1])+'='+gemZahl+'$'])
            else:
                r1=[[y for y in x] if isinstance(x,list) else x for x in r]
                loesung.append([nr,ungleicheBruecheAddierenSubtrahierenTikz(r1[0],r1[2],r1[1])]) 
        if typ == 'GemischteZahlzuBruch':
            loesung.append([nr,'$'+r[2]+'\\frac{'+r[3]+'}{'+r[4]+'}=\\frac{'+r[0]+'}{'+r[1]+'}$'])
        if typ == 'BruchzuGemischteZahl':
            loesung.append([nr,'$\\frac{'+r[0]+'}{'+r[1]+'}='+r[2]+'\\frac{'+r[3]+'}{'+r[4]+'}$'])
        if typ == 'rechneQuadrateEinheitenUm' or typ=='rechneLaengenEinheitenUm':
            loesung.append([nr,r[1]])
        if typ == 'UmfangMessen':
#            loesung.append([nr,'Der Umfang ist '+str(2*(r[1]+r[2]))+' cm'])
            loesung.append([nr,['\pbox{20cm}{U=2·(a+b)='+str(2*(r[1]+r[2]))+' $cm$\\\\']+rechteckTikz(r[1],r[2],beschrSeiten=True,texta='a='+str(r[1])+' cm',textb='b='+str(r[2])+' cm')+['}']])
        if typ == 'FlaecheMessen':
            loesung.append([nr,['\pbox{20cm}{A=a·b='+str(r[1]*r[2])+' $cm^2$\\\\']+rechteckTikz(r[1],r[2],beschrSeiten=True,texta='a='+str(r[1])+' cm',textb='b='+str(r[2])+' cm')+['}']])
        if typ == 'FlaecheUmfang':
            loesung.append([nr,['\pbox{20cm}{A=a·b='+str(r[1]*r[2])+' $cm^2$, U=2·(a+b)='+str(2*(r[1]+r[2]))+' $cm$\\\\']+rechteckTikz(r[1],r[2],beschrSeiten=True,texta='a='+str(r[1])+' cm',textb='b='+str(r[2])+' cm')+['}']])
        if typ == 'ZusGesetztFl':
            lsgText=['\pbox{20cm}{']
            flaeche=''
            A=0
            for i,pkt in enumerate(r):
                flaeche=flaeche+'$A_'+str(i+1)+'='+str(pkt[0])+'·'+str(pkt[1])+'='+str(pkt[0]*pkt[1])+' cm^2$, '
                if i%2==1:
                    flaeche=flaeche+'\\\\'
                A=A+pkt[0]*pkt[1]
            flaeche=flaeche+'$A='+str(A)+' cm^2$\\\\'
#            flaeche='$A='+str(A)+' cm^2$\\\\'
            lsgText.append(flaeche)
            loesung.append([nr,lsgText+zusammengesetzteRechtecke(r,mitLsg=True)+['}']]) 
#            loesung.append([nr,lsgText+['}']])
        if typ == 'ZusGesetztFlSchwer':
            lsgText=['\pbox{20cm}{']
            flaeche=''
            A=0
            for i,pkt in enumerate(r):
                flaeche=flaeche+'$A_'+str(i+1)+'='+str(pkt[1][0]-pkt[0][0])+'·'+str(pkt[1][1]-pkt[0][1])+'='+str((pkt[1][0]-pkt[0][0])*(pkt[1][1]-pkt[0][1]))+' cm^2$, '
                if i%2==1:
                    flaeche=flaeche+'\\\\'
                A=A+(pkt[1][0]-pkt[0][0])*(pkt[1][1]-pkt[0][1])
            flaeche=flaeche+'$A='+str(A)+' cm^2$\\\\'
#            flaeche='$A='+str(A)+' cm^2$\\\\'
            lsgText.append(flaeche)
            loesung.append([nr,lsgText+zusammengesetzteRechteckeSchwer(r,mitLsg=True)+['}']]) 
#            loesung.append([nr,lsgText+['}']]) 
        if typ =='Basis' or typ=='Kopf':
            loesung.append([nr,r+' = '+str(int(eval(r.replace(':','/'))))])
    return loesung
