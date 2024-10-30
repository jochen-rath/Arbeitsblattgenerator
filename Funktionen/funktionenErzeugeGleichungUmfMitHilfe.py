#!/usr/bin/env python
# coding: utf8

#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def erzeugeSehrEinfacheGleichungenMitHilfe(variabel='x',mitText=True,nurPlusMinus=False,PlusMinusVariImTerm2=False,PlusMinusVariRechtsImTerm1=False,nurMalGeteilt=False,MalUndPlusMinus=False,MalUndPlusMinusAufgeteilt=False,einfKlammer=False):
    G=F'3*{variabel}-5=10'
    if nurPlusMinus:
        G = F'{variabel}{random.choice(["+", "-"])}{random.randint(1, 50)} = {random.randint(1, 50)}'
    if PlusMinusVariImTerm2:
        G = F'{random.randint(1, 50)}={variabel}{random.choice(["+", "-"])}{random.randint(1, 50)}'
    if nurMalGeteilt:
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        G = F'{a}*{variabel}={a * b}' if bool(random.getrandbits(1)) else F'{variabel}/{a}={b}'
    if MalUndPlusMinus:
        x = random.randint(2, 12)
        b = random.randint(2, 20)
        a = random.randint(2, 10)
        c = a*x-b
        G=F"{a}*{variabel}-{b}={c}"
    if MalUndPlusMinusAufgeteilt:
        x = random.randint(2, 12)
        b = random.randint(2, 20)
        a = random.randint(2, 10)
        c = a*x-b
        op1=random.choice(['+','-'])
        op2=random.choice(['+','-'])
        #a=a1 +/- a2
        a2=random.randint(1,a-1)
        a1=eval(F'{a}{ {"+":"-","-":"+"}[op1] }{a2}')
        # b=b1 +/- b2
        b2=random.randint(1,b-1)
        b1=eval(F'{b}{ {"+":"-","-":"+"}[op2] }{b2}')
        werte=[F'+{a1}*{variabel}',F'{op1}{a2}*{variabel}',F'-{b1}',F'{ {"+":"-","-":"+"}[op2] }{b2}']
        random.shuffle(werte)
        G=F'{"".join([werte[0].replace("+","")]+werte[1:])}={c}'
    if PlusMinusVariRechtsImTerm1:
        G = F'{random.randint(1, 50)}{random.choice(["+", "-"])}{variabel}={random.randint(1, 50)}'
    if einfKlammer:
        variabel=random.choice(['a','b','x','y','z'])
        werte={}
        op=random.choice(['+','-'])
        for i in variabel,'h','i','j':
            werte[i]=random.randint(2,8)
        klammer=F"{werte['h']}*({werte['i']}*{variabel}{op}{werte['j']})"
        G= F'{klammer} = {eval(klammer.replace(variabel,str(werte[variabel])))}'
    afg = F'{"Berechne die Variable $" if mitText else ""}${G.replace("**", "^").replace("*", "&&cdot ").replace("/", ":")}${"$" if mitText else ""}'.replace("&&","\\")
    lsg = loeseGleichungEinfachMitEinerVariabel(G=G, variable=variabel, mitProbe=True)
    return [afg, lsg, G]


def erstelleHilfeFuerEinfacheGleichungsLsg(G='2*x+5=19',opHilfe=True,variable='x',mitTikzUmrandung=True,mitProbe=False):
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
            operator=F'/(-{operator})' if Lsplit[0][0]=='-' else F'/{operator}'  #'/('+Lsplit[0][0]+operator+')'
        operator=F'\\underline{{\\phantom{{{operator}}}}}'
        print(operator)
#Manchmal erzeugt simplify beim Umwandeln eine Klammer. Diese muß vor dem Aufschreiben wieder entfernt werden.
        if '(' in L+'='+R:
            L,R=klammernEntfernen(L),klammernEntfernen(R)
            L,R=L if not L[0]=='+' else L[1:], R if not R[0]=='+' else R[1:]
        latexcommand.append(ersetzePlatzhalterMitSymbolen(L.replace('.',',')) + ' &=' + ersetzePlatzhalterMitSymbolen(R.replace('.',',')) + '& & ' + ('' if operator == '+0' else ('\\mid ' + ersetzePlatzhalterMitSymbolen(operator.replace('.',','),operator=True))) + '\\\\')
        L=str(sympy.simplify('('+L+')'+operator))
        R=str(sympy.simplify('('+R+')'+operator))
#simplify reduziert nicht "1.0*x" weiter
        L=L[4:] if L.startswith('1.0*') else L
        loopCounter=loopCounter+1
    zaeR=0 if not '/' in R else int(R.split('/')[0])
    nenR=0 if not '/' in R else int(R.split('/')[1])
    if loopCounter<10:
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
    return latexcommand 
