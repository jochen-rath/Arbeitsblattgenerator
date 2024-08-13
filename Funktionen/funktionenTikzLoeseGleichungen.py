#!/usr/bin/env python
# coding: utf8

#Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

#Aufruf:
#      exec(open("Funktionen/funktionen.py").read())

def loeseEinfacheMalGeteiltAufg(G='1.564=8.56+2.33*variStrh_k',vari='variStrh_k'):
    werte={}
    drehen=False
    L,R=G.split('=')[0],G.split('=')[1]
    if vari in R:
        L,R=R,L
        drehen=True
    werte['R']=float(R)
    if '+' in L or '-' in L:
        LL,LR=G.split('*')[0],L.split('*')[1]
    op=''
    for pm in '+','-':
        if pm in R:
            op=pm+R.split(pm)[0] if not list(ges.keys())[0] in op.split(pm)[0]  else op.split(pm)[1]
    lsg.append(F'{formelStrNw.split("=")[0]}&={formelStrNw.split("=")[1]} & & {F"& & §§mid~{op}" if len(op)>0 else ""}\\\\')
    return glLsg


def klammernEntfernen(S):
    Ssplit=spliteSeiteAddSub(S)
    Ssplit=[str(sympy.expand(sympy.simplify(x))) for x in Ssplit]
    #Vor dem Join muss ein Pluszeichen eingefügt werden, falls kein Plus- oder Minuszeichen vorhanden ist.
    Ssplit=['+'+x if not (x[0]=='+' or x[0]=='-') else x for x in Ssplit]
    return ''.join(Ssplit)

def probeGleichungLoesen(G="2*x+6=3*x-2",variable='x',erg='8',mitTikzUmrandung=True):
    latexcommand=[]
    if mitTikzUmrandung:
        latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')
        latexcommand.append('\\begin{tikzpicture}[show background grid]')
        latexcommand.append('\\node[below right] at (0,0.1) {')
        latexcommand.append('$\\begin{aligned}')
    L,R=G.split('=')
    latexcommand.append('\\mbox{Probe:}\\qquad '+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(L))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'& &  \\\\')
    linkeSeite=L.replace(variable, F'({erg})')
    rechteSeite=R.replace(variable,  F'({erg})')
    latexcommand.append(ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(linkeSeite))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(rechteSeite))+'& &  \\\\')
    linkeSeite=klammernEntfernen(linkeSeite)
    rechteSeite=klammernEntfernen(rechteSeite)
    latexcommand.append(ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(linkeSeite))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(rechteSeite))+'& &  \\\\')
    latexcommand.append(ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(strNW(eval(linkeSeite),True)))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(strNW(eval(rechteSeite),True)))+'& &  \\\\')
    if mitTikzUmrandung:
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')
        latexcommand.append('\\endgroup')
    return latexcommand

def loeseGleichungEinfachMitEinerVariabel(G="2*x+6=3*x-2",variable='x',mitTikzUmrandung=True,mitProbe=False,latexAusgabe=True,fracAmEnde=True):
#Diese Funktion löst ein einfaches Gleichungssystem mit x oder x**2 am Ende
#Das Gleichungssystem darf nur aus einer Variabel bestehen, ansonsten eine Kombination aus zahlen und Faktoren und Variabel. Beispiel:
#
#Beispiel:         4*(4+x)+5*x-6=x-5-7*(4*x+3)
#Das geht nicht:   W=G*p:100 nach G auflösen
#
#Aufruf:   loesung=loeseGleichungEinfach(G,variabel)
#
#mit G=Gleichung
#    variabel=Variabel, nach der Aufgelöst wird
    latexcommand=[]
    nurLsg=''
    if mitTikzUmrandung:
        latexcommand.append('\\begingroup\\setlength{\\jot}{-0.03cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[below right] at (0,0.1) {')  
        latexcommand.append('$\\begin{aligned}')  
    L,R=G.split('=')
    print(L+'='+R)
#Wenn Klammern in der Gleichung ist, löse diese:
    if '(' in G:
#        latexcommand.append(L.replace('**','^').replace('*','\\cdot ')+' &='+R.replace('**','^').replace('*','\\cdot ')+'& & \\\\')
        latexcommand.append(erzeugeLatexFracAusdruck(ersetzePlatzhalterMitSymbolen(L))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'& & \\\\ ')
        L,R=klammernEntfernen(L),klammernEntfernen(R)
#Wenn die Terme nicht Reduziert sind, reduziere sie.
#sympy.simplify erzeugt Leerzeichen zur besseren Lesbarkeit, die stören aber beim Vergleichen.
    if not(L.replace(' ','')==str(sympy.simplify(L)).replace(' ','') and  R.replace(' ','')==str(sympy.simplify(R)).replace(' ','')):
        #Entferne für die Ausgabe das führende Pluszeichen
        L=L if not L[0]=='+' else L[1:]
        R=R if not R[0]=='+' else R[1:]
#        latexcommand.append(L.replace('**','^').replace('*','\\cdot ')+' &='+R.replace('**','^').replace('*','\\cdot ')+'& & \\\\')
#        print(F'Not {L=}=={str(sympy.simplify(L))=}')
        latexcommand.append(erzeugeLatexFracAusdruck(ersetzePlatzhalterMitSymbolen(L.replace('.',',')))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R.replace('.',',')))+'& & \\mid~\\mbox{Vereinfachen}  \\\\')
        L=str(sympy.simplify(L))
        R=str(sympy.simplify(R))
    operator='+0'
#Solange Links nicht nur die Variabel steht, soll umgeformt werden.
    loopCounter=0
    while (not (L==variable or L==variable+'**2') or (variable in R)) and loopCounter<10:
        print(L+'='+R)
        Lsplit,Rsplit=spliteSeiteAddSub(L),spliteSeiteAddSub(R)
#1. Überprüfen ob Links noch eine reine Zahl steht. Achtung, wenn die Zahl nurnoch Null ist, entsteht eine Dauerschleife
        if (True in [isfloat(x.replace(' ','')) and (not (x=='+0' or x=='-0'  or x=='0')) for x in Lsplit]):
            floatPos=[i for i in range(len(Lsplit)) if isfloat(Lsplit[i].replace(' ',''))][0]
            operator=('-' if Lsplit[floatPos][0]=='+' else '+')+Lsplit[floatPos][1:]
#2. Überprüfen ob Rechts noch eine Variabel vorhanden ist:
        elif True in [variable in x for x in Rsplit]:
            variablePos=[i for i in range(len(Rsplit)) if variable in Rsplit[i]][-1]
            operator=('-' if Rsplit[variablePos][0]=='+' else '+')+Rsplit[variablePos][1:]
#3. Wird auf der Linken Seite noch durch eine Zahl geteilt?
        elif True in ['/' in x for x in Lsplit]: 
            variablePos=[i for i in range(len(Lsplit)) if '/' in Lsplit[i]][-1]
            operator='*'+Lsplit[variablePos].split('/')[1]
#4. Rechts steht keine variable, Links nur noch Zahl mal x oder Zahl mal x^2
        else:
            regex=r'\d+\.\d+' if '.' in Lsplit[0].split('**')[0] else r'\d+'
            result=re.search(regex, Lsplit[0].split('**')[0])
            if result:
                operator=result.group(0)
            else:
                operator='1'
#            operator='1' if (re.search(regex, Lsplit[0].split('**')[0]) is None) else re.search(regex, Lsplit[0].split('**')[0]).group(0)
#            operator='1' if (re.search(r'\d+', Lsplit[0].split('**')[0]) is None) else re.search(r'\d+', Lsplit[0].split('**')[0])[0]
            operator=F'/(-{operator})' if Lsplit[0][0]=='-' else F'/{operator}'  #'/('+Lsplit[0][0]+operator+')'
#Manchmal erzeugt simplify beim Umwandeln eine Klammer. Diese muß vor dem Aufschreiben wieder entfernt werden.
        if '(' in L+'='+R:
            L,R=klammernEntfernen(L),klammernEntfernen(R)
            L,R=L if not L[0]=='+' else L[1:], R if not R[0]=='+' else R[1:]
#        latexcommand.append(L.replace('**','^').replace('*','\\cdot ')+' &='+R.replace('**','^').replace('*','\\cdot ')+'& & \\mid '+operator.replace('/',':').replace('**','^').replace('*','\\cdot ')+'\\\\')
        latexcommand.append(ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(L.replace('.',','))) + ' &=' + ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R.replace('.',','))) + '& & ' + ('' if operator == '+0' else ('\\mid ' + ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(operator.replace('.',','),operator=True)))) + '\\\\')
        L=str(sympy.simplify('('+L+')'+operator))
        R=str(sympy.simplify('('+R+')'+operator))
#simplify reduziert nicht "1.0*x" weiter
        L=L[4:] if L.startswith('1.0*') else L
        loopCounter=loopCounter+1
    zaeR=0 if not '/' in R else int(R.split('/')[0])
    nenR=0 if not '/' in R else int(R.split('/')[1])
    if loopCounter<10:
        if fracAmEnde:
            latexcommand.append(erzeugeLatexFracAusdruck(ersetzePlatzhalterMitSymbolen(L))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'& & ')
        else:
#            latexcommand.append(L.replace('**','^').replace('*','\\cdot ')+' &='+ ((R) if not '/' in R else(frac(zaeR,nenR)+('' if abs(zaeR)< nenR else ('='+schreibeGemZahl(zaeR,nenR)))))+'& &')
            latexcommand.append(F'{ersetzePlatzhalterMitSymbolen(L)}&={strNW(eval(R),2)} & &')
        nurLsg=L+'='+R
    else:
        return 'Error'
#Zum Schluss gibt es zwei Und-Zeichen, da bei der aligned Umgebung die Inhalte Abwechselnd Rechts- und Linksseitig angeordnet werden
    if mitProbe:
        latexcommand=latexcommand+['\\\\']*2+probeGleichungLoesen(G=G,variable=variable,erg=R,mitTikzUmrandung=False)
    if mitTikzUmrandung:
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
        latexcommand.append('\\endgroup')
    return latexcommand if latexAusgabe else nurLsg


def formeEinfacheFormelNachVorgabenUm(G="p/100=W/G",gesucht='W',mitTikzUmrandung=True,latexAusgabe=True):
#Diese Funktion formt eine Formel nach der gesuchte Variabel um.
#Es können nur einfache Formeln umgewandelt werden, bei der die gesucht Variabel nur auf einer Seite steht und es dürfen keine KLammern vorkommen.
#
#Beispiel:         p/100=W/G
#Geht nicht:       U=2*(a+b)
#Aufruf:   loesung=formeFormelNachVorgabenUm(G,gesucht)
#
#mit G=Gleichung
#    variabel=Variabel, nach der Aufgelöst wird
    latexcommand=[] 
    if mitTikzUmrandung:
#        latexcommand.append('\\begingroup\\setlength{\\jot}{0.13cm}')
        latexcommand.append('\\tikzstyle{background grid}=[draw, black!15,step=.5cm]')  
        latexcommand.append('\\begin{tikzpicture}[show background grid]')  
        latexcommand.append('\\node[below right] at (0,0.1) {')  
        latexcommand.append('$\\begin{aligned}')  
    L,R=G.split('=')
    operator='+0'
    latexcommand.append(ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(L))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'& & '+'\\\\')
#Solange Links nicht nur die Variabel steht, soll umgeformt werden.
    loopCounter=0
    endFormel=G
    while not (L==gesucht) and loopCounter<10:
        print(L+'='+R)
        umdrehen=False
#1. Überprüfen ob die gesuchte Variabel links steht. Wenn nicht, Verstausche die Seiten.
        if gesucht in R:
            Ls=R
            R=L
            L=Ls
            Lneu,Rneu=L,R
            umdrehen=True
#2. Gibt es ein '+' oder '-'
        elif (('+' in L) or ('-' in L)) and not L[0]=='-':
            Lsplit=spliteSeiteAddSub(L)
            gesTerm=[x for x in Lsplit if not gesucht in x][0]
            operator=('-' if gesTerm[0]=='+' else '+')+gesTerm[1:]
            Lneu,Rneu=L,R
#3. Gibt es ein '/' Zeichen in L, dann Kehrbruch oder Mulitplikation
        elif '/' in L:
            Ldiv=L.split('/')
            if gesucht in Ldiv[1]:
                operator=' \\mbox{Kehrbruch}'
                Lneu=Ldiv[1]+'/'+Ldiv[0]
                if '/' not in R:
                    R='('+R+')'+'/1'
                Rdiv=R.split('/')
                Rneu=Rdiv[1]+'/'+Rdiv[0]
            else:
                operator='*('+Ldiv[1]+')'
                Lneu,Rneu=L,R
#4. Gibt es ein '*' Zeichen in L, dann Division
        elif '*' in L:
            Lmult=L.split('*')
            gesTerm=[x for x in Lmult if not gesucht in x][0]
            operator='/'+'('+gesTerm+')'
            Lneu,Rneu=L,R
        else:
            Lsplit=spliteSeiteAddSub(L)
            operator='1' if (re.search(r'\d+', Lsplit[0].split('**')[0]) is None) else re.search(r'\d+', Lsplit[0].split('**')[0])[0]
            operator='/('+Lsplit[0][0]+operator+')'
            Lneu,Rneu=L,R
#Manchmal erzeugt simplify beim Umwandeln eine Klammer. Diese muß vor dem Aufschreiben wieder entfernt werden.
        if '(' in L+'='+R:
            L,R=klammernEntfernen(L),klammernEntfernen(R)
            L,R=L if not L[0]=='+' else L[1:], R if not R[0]=='+' else R[1:]
        if not umdrehen:
            latexcommand.append(ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(L))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'& & '+('' if operator=='+0' else ('\\mid '+ersetzePlatzhalterMitSymbolen(operator)))+'\\\\')
        print(L+'='+R+' | '+operator)
        print(Lneu+'='+Rneu+' | '+operator)
        L=str(sympy.simplify('('+Lneu+')'+('' if 'Kehrbruch' in operator else operator)))
        R=str(sympy.simplify('('+Rneu+')'+('' if 'Kehrbruch' in operator else operator)))
        print(L+'='+R)
        loopCounter=loopCounter+1
        endFormel=L+'='+R
    if loopCounter<10:
        latexcommand.append(erzeugeLatexFracAusdruck(ersetzePlatzhalterMitSymbolen(L))+' &='+ersetzePlatzhalterMitSymbolen(erzeugeLatexFracAusdruck(R))+'& & ')
    else:
        return 'Error'
#Zum Schluss gibt es zwei Und-Zeichen, da bei der aligned Umgebung die Inhalte Abwechselnd Rechts- und Linksseitig angeordnet werden
    if mitTikzUmrandung:
        latexcommand.append('\\end{aligned}$};')
        latexcommand.append('\\end{tikzpicture}')   
#        latexcommand.append('\\endgroup')
    return latexcommand if latexAusgabe else endFormel
    
