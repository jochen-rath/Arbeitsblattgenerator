#!/usr/bin/env python
# coding: utf8


#Aufruf:
#       exec(open("Funktionen/funktionenErzeugeGeometrieAufgaben.py").read())
#Diese Skript stellte verschiedene Figuren bereit, die Zeichnungen mit dem Latex-Paket Tikz erzeugen
#       exec(open("Funktionen/funktionen.py").read())

def dreieckWinkelBer(schwierigkeit="einfach",anzSpalten=2,mitText=True):
    a,b,c=100,100,100
    while a>5 or b>5 or c>5 or a<1.5 or b<1.5 or c<1.5:
        if schwierigkeit=="einfach":
            alpha=random.randint(2,13)*10
            beta=random.randint(2,18-int(alpha/10)-2)*10
        elif schwierigkeit=="normal":
            alpha=random.randint(4,26)*5
            beta=random.randint(4,18-int(alpha/10)-2)*5
        else:
            alpha=random.randint(20,130)
            beta=random.randint(20,180-alpha-20)
        gamma=180-alpha-beta
        c=random.randint(2,5)
        a=c*math.sin(alpha*math.pi/180)/math.sin(gamma*math.pi/180)
        b=c*math.sin(beta*math.pi/180)/math.sin(gamma*math.pi/180)
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
        gamma=180-alpha-beta
    A=[a,alpha,"A","a","$\\alpha$"]
    B=[b,beta,"B","b","$\\beta$"]
    C=[c,gamma,"C","c","$\\gamma$"]
    A=[a,alpha,"","",int(round(alpha))]
    B=[b,beta,"","",int(round(beta))]
    C=[c,gamma,"","",int(round(gamma))]
#Ich habe Probleme bei Kommata in der \pic Umgebung.Darum keine Dezi
    dreieckLsg=dreieckSWScBetaa(A=A,B=B,C=C)
    entf=random.choice(['A','B','C'])
    exec(F'{entf}[4]=""')
    dreieckAfg=dreieckSWScBetaa(A=A,B=B,C=C)
    aufg=['Bestimme den fehlenden Winkel: \\\\']
    afg=['\\pbox{\\linewidth}{']+(aufg if mitText else [])+ dreieckAfg+['}']
    lsg=dreieckLsg
    return [afg,lsg,[]]