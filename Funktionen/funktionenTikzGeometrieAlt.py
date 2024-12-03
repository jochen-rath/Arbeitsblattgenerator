
def erzeugeDreieckSWSKonstruktion(mitText=True,anzSpalten=[2,2]):
    auswahl=random.randint(0,2)
    winkelBez=['alpha','beta','gamma']
    seitenBez=[['c','b'],['a','c'],['b','a']]
    l1,l2=random.randint(20,60)/10,random.randint(20,60)/10
    winkel=random.randint(20,140)
    groesse='{17 cm}' if anzSpalten[1] == 1 else '{7 cm}'
    afg=[f'\\pbox{groesse}{{']
    afg=afg+([F'Konstruiere das Dreieck aus folgenden Werten:\\\\']  if mitText else [])
    afg=afg+[F'$\\begin{{aligned}}']
    afg=afg+[F'{seitenBez[auswahl][0]}&={strNW(l1)}~cm \\\\']
    afg=afg+[F'\\{winkelBez[auswahl]}&={winkel}^\\circ \\\\']
    afg=afg+[F'{seitenBez[auswahl][1]}&={strNW(l2)}~cm \\\\']
    afg=afg+[F'\\end{{aligned}}$']
    afg=afg+['}']
    lsg=dreieckSWSKonstruktion(l1=l1,winkel=winkel,l2=l2,winkelBei=winkelBez[auswahl])
    return [afg,lsg,[]]

    
def dreieckSWSKonstruktion(l1=4,winkel=55,l2=3,winkelBei='alpha'):
    l3=(l1**2+l2**2-2*l1*l2*math.cos(winkel*math.pi/180))**0.5
    if winkelBei not in ['alpha','beta','gamma']:
        return []
    if winkelBei=='alpha':
        alpha=winkel
        a,b,c=l3,l2,l1
        beta=math.acos((b**2-a**2-c**2)/(-2*a*c))*180/math.pi
        gamma=180-alpha-beta
    if winkelBei=='beta':
        beta=winkel
        a,b,c=l1,l3,l2
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
        gamma=180-alpha-beta
    if winkelBei=='gamma':
        gamma=winkel
        a,b,c=l2,l1,l3
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
        beta=180-alpha-gamma
    bogenR=0.75
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    if winkelBei=='alpha':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{{strNW(c)} cm}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{{strNW(b)} cm}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{alpha}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({alpha/2}:{bogenR*0.75}) {{${alpha}^\\circ$}} ;')
    if winkelBei=='beta':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{{strNW(c)} cm}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  -- node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{{strNW(a)} cm}} ({alpha}:{b}) ;')
        x=c+bogenR*0.75*math.cos((180-beta/2)*math.pi/180)
        y=0+bogenR*0.75*math.sin((180-beta/2)*math.pi/180)
        tikzcommand.append(F'\\draw[thick,red] ({c-bogenR},0) arc (180:{180-beta}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({x},{y}) {{${beta}^\\circ$}} ;')
    if winkelBei=='gamma':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{{strNW(b)} cm}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{{strNW(a)} cm}} ({alpha}:{b}) ;')
        xBogen=(b-bogenR)*math.cos(alpha*math.pi/180)
        yBogen=(b-bogenR)*math.sin(alpha*math.pi/180)
        tikzcommand.append(F'\\draw[thick,red] ({xBogen},{yBogen}) arc ({180+alpha}:{180+alpha+gamma}:{bogenR} cm) ;')
        xZahl=b*math.cos(math.radians(alpha))+bogenR*0.75*math.cos((180+alpha+gamma/2)*math.pi/180)
        yZahl=b*math.sin(math.radians(alpha))+bogenR*0.75*math.sin((180+alpha+gamma/2)*math.pi/180)
        tikzcommand.append(F'\\node[red] at ({xZahl},{yZahl}) {{${gamma}^\\circ$}} ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand



def erzeugeDreieckWSWKonstruktion(mitText=True,anzSpalten=[2,2]):
    auswahl=random.randint(0,2)
    seiten=['a','b','c']
    winkelBez=[['beta','gamma'],['gamma','alpha'],['alpha','beta']]
    w1,w2=100,100
    while w1+w2>140:
        w1,w2=random.randint(20,140),random.randint(20,140)
    if random.randint(0,9)<1:
        w1=random.randint(80,110)
        w2=(180-w1)+random.randint(5,30)
    l=random.randint(20,60)/10
    groesse='{17 cm}' if anzSpalten[1] == 1 else '{7 cm}'
    afg=[f'\\pbox{groesse}{{']
    afg=afg+([F'Konstruiere das Dreieck aus folgenden Werten:\\\\']  if mitText else [])
    afg=afg+[F'$\\begin{{aligned}}']
    afg.append(f'\\{winkelBez[auswahl][0]}&={strNW(w1)}^\\circ \\\\')
    afg=afg+[F'{seiten[auswahl]}&={strNW(l)}~cm\\\\']
    afg=afg+[F'\\{winkelBez[auswahl][1]}&={strNW(w2)}^\\circ  \\\\']
    afg=afg+[F'\\end{{aligned}}$']
    afg=afg+['}']
    lsg=dreieckWSWKonstruktion(w1=w1,l=l,w2=w2,seite=seiten[auswahl])
    return [afg,lsg,[]]


def dreieckSSSKonstruktion(a=2,b=3,c=4):
    if abs((a**2-b**2-c**2)/(-2*b*c))>1:
        alpha=-1
    else:
        alpha=math.acos((a**2-b**2-c**2)/(-2*b*c))*180/math.pi
    winkelStartUmA=-10
    winkelEndUmA=190 if alpha > 90 or alpha <0 else 100
    winkelStartUmB=-10 if b>c and alpha<45 else 80
    winkelEndUmB=190
    x=c+a*math.cos(winkelStartUmB*math.pi/180)
    y=0+a*math.sin(winkelStartUmB*math.pi/180)
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
    if alpha>0:
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b});')
    tikzcommand.append(F'\\draw[thick,red] ({winkelStartUmA}:{b}) arc ({winkelStartUmA}:{winkelEndUmA}:{b} cm);')
    tikzcommand.append(F'\\draw[thick,red] ({x},{y}) arc ({winkelStartUmB}:{winkelEndUmB}:{a} cm);')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand




def dreieckWSWKonstruktion(w1=40,l=5,w2=110,seite='c'):
    bogenR=0.75
    if seite not in ['a','b','c']:
        return []
    if w1+w2>180:
        x=l+l*math.cos(math.radians(180-w2))
        y=0+l*math.sin(math.radians(180-w2))
        tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
        tikzcommand.append('\\begin{tikzpicture}[show background grid]')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  -- node[below]{{{l} cm}}({l},0) ;')
        tikzcommand.append(F'\\draw[thick,black] (0,0)--({w1}:{l}) ;')
        tikzcommand.append(F'\\draw[thick,black] ({l},0) --({x},{y}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{w1}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({w1/2}:{bogenR*0.75}) {{${w1}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({l-bogenR},0) arc ({180}:{180-w2}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({l+bogenR*0.75*math.cos(math.radians(180-w2/2))},{bogenR*0.75*math.sin(math.radians(180-w2/2))}) {{${w2}^\\circ$}} ;')
        tikzcommand.append('\\end{tikzpicture}')
        return tikzcommand
    if seite=='a':
        a=l
        beta=w1
        gamma=w2
        alpha=180-beta-gamma
        b=a/math.sin(math.radians(alpha))*math.sin(math.radians(beta))
        c=a/math.sin(math.radians(alpha))*math.sin(math.radians(gamma))
    if seite=='b':
        b=l
        gamma=w1
        alpha=w2
        beta=180-alpha-gamma
        a=b/math.sin(math.radians(beta))*math.sin(math.radians(alpha))
        c=b/math.sin(math.radians(beta))*math.sin(math.radians(gamma))
    if seite=='c':
        c=l
        alpha=w1
        beta=w2
        gamma=180-alpha-beta
        a=c/math.sin(math.radians(gamma))*math.sin(math.radians(alpha))
        b=c/math.sin(math.radians(gamma))*math.sin(math.radians(beta))
    tikzcommand=['\\tikzstyle{background grid}=[draw, black!15,step=.5cm]']
    tikzcommand.append('\\begin{tikzpicture}[show background grid]')
    x=c+bogenR*0.75*math.cos((180-beta/2)*math.pi/180)
    y=0+bogenR*0.75*math.sin((180-beta/2)*math.pi/180)
    xBogen=(b-bogenR)*math.cos(alpha*math.pi/180)
    yBogen=(b-bogenR)*math.sin(alpha*math.pi/180)
    xZahl=b*math.cos(math.radians(alpha))+bogenR*0.75*math.cos((180+alpha+gamma/2)*math.pi/180)
    yZahl=b*math.sin(math.radians(alpha))+bogenR*0.75*math.sin((180+alpha+gamma/2)*math.pi/180)
    if seite=='c':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{{strNW(c)} cm}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{alpha}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({alpha/2}:{bogenR*0.75}) {{${alpha}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({c-bogenR},0) arc (180:{180-beta}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({x},{y}) {{${beta}^\\circ$}} ;')
    if seite=='a':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  -- node[left]{{b}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{{strNW(a)} cm}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({c-bogenR},0) arc (180:{180-beta}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({x},{y}) {{${beta}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({xBogen},{yBogen}) arc ({180+alpha}:{180+alpha+gamma}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({xZahl},{yZahl}) {{${gamma}^\\circ$}} ;')
    if seite=='b':
        tikzcommand.append(F'\\draw[thick,black] (0,0) node[left]{{A}} --node[below]{{c}} ({c},0) node[right]{{B}};')
        tikzcommand.append(F'\\draw[thick,black] (0,0)  --node[left]{{{strNW(b)} cm}} ({alpha}:{b}) node[above]{{C}};')
        tikzcommand.append(F'\\draw[thick,black] ({c},0)  --node[right]{{a}} ({alpha}:{b}) ;')
        tikzcommand.append(F'\\draw[thick,red] ({xBogen},{yBogen}) arc ({180+alpha}:{180+alpha+gamma}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({xZahl},{yZahl}) {{${gamma}^\\circ$}} ;')
        tikzcommand.append(F'\\draw[thick,red] ({bogenR},0) arc (0:{alpha}:{bogenR} cm) ;')
        tikzcommand.append(F'\\node[red] at ({alpha/2}:{bogenR*0.75}) {{${alpha}^\\circ$}} ;')
    tikzcommand.append('\\end{tikzpicture}')
    return tikzcommand