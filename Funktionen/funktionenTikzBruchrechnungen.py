

def zeichneBruchMultiNZahlPfeile(bruch,faktor,mitLSG=False):
#Diese Funktion zeichnet einen Zahlenstrahl von 0 bis ...
#Darüber zeichnet diese Funktion faktor mal Pfeile in Länge des Bruchs
    laenge=10
    endwert=math.ceil(bruch[0]/bruch[1]*faktor)
    l=bruch[0]/bruch[1]*passeLaengenAnZahlenstrahlAn(0,endwert,bruch[1],laenge=10)
    tikzcommand=['\\begin{tikzpicture}[baseline=0]']
    tikzcommand=tikzcommand+zahlenstrahlMitEinteilung(0,endwert,bruch[1],laenge=10,mitBeginEnd=False)
    for i in range(faktor):
        tikzcommand.append('\\draw[-latex] ('+str(i*l)+'cm,0.5cm) -- ('+str((i+1)*l)+'cm,0.5cm) ;')
    tikzcommand.append('\draw[black] (11cm,0.25cm) --'+(('node[above]{$'+((strNW(faktor)+'\\cdot') if faktor>1 else '')+frac(bruch[0],bruch[1])+'$}') if mitLSG else '' )+' (12cm,0.25cm) ;')
    tikzcommand.append('\end{tikzpicture}')
    return tikzcommand


def zeichneBruchteilBerechnen(vonZahl,bruch,einheit='m'):
#Diese Funktion zeichnet die Lösung einer Bruchteil Berechnungsaufgabe in der Pfeildarstellung:
#
#    
    pfeilLaenge=1.2
    tikzcommand=['\\begin{tikzpicture}[baseline=0]']
    tikzcommand.append('\\draw[black] (0cm,0.1cm) node[left] {$'+schreibIntIfFloatIsInt(vonZahl)+'$ '+einheit+'} ;')
    tikzcommand.append('\\draw[-latex] (0cm,0.1cm) -- ('+str(pfeilLaenge)+'cm,0.1cm) ;')
    tikzcommand.append('\\draw ('+str(pfeilLaenge*0.5)+'cm,0.1cm) node[above] {$:'+schreibIntIfFloatIsInt(bruch[1])+'$} ;')
    tikzcommand.append('\\draw ('+str(pfeilLaenge)+'cm,0.1cm) node[right] {$'+schreibIntIfFloatIsInt(vonZahl/bruch[1])+'$ '+einheit+'} ;')
    abstand=0.3*(len(schreibIntIfFloatIsInt(vonZahl/bruch[1])+einheit)+2)
    tikzcommand.append('\\draw[-latex] ('+str(abstand+pfeilLaenge)+'cm,0.1cm) -- ('+str(abstand+2*pfeilLaenge)+'cm,0.1cm) ;')
    tikzcommand.append('\\draw ('+str(abstand+1.5*pfeilLaenge)+'cm,0.1cm) node[above] {$\\cdot'+schreibIntIfFloatIsInt(bruch[0])+'$} ;')
    tikzcommand.append('\\draw ('+str(abstand+2*pfeilLaenge)+'cm,0.1cm) node[right] {$'+schreibIntIfFloatIsInt(vonZahl/bruch[1]*bruch[0])+'$ '+einheit+'} ;')
#    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\end{tikzpicture}')
    return tikzcommand

def zeichneGanzesBerechnen(teil,bruch,einheit='m'):
    pfeilLaenge=1.2
    tikzcommand=['\\begin{tikzpicture}[baseline=0]']
    tikzcommand.append('\\draw[black] (0cm,0.1cm) node[left] {$'+schreibIntIfFloatIsInt(teil)+'$ '+einheit+'} ;')
    tikzcommand.append('\\draw[-latex] (0cm,0.1cm) -- ('+str(pfeilLaenge)+'cm,0.1cm) ;')
    tikzcommand.append('\\draw ('+str(pfeilLaenge*0.5)+'cm,0.1cm) node[above] {$:'+schreibIntIfFloatIsInt(bruch[0])+'$} ;')
    tikzcommand.append('\\draw ('+str(pfeilLaenge)+'cm,0.1cm) node[right] {$'+schreibIntIfFloatIsInt(teil/bruch[0])+'$ '+einheit+'} ;')
    abstand=0.3*(len(schreibIntIfFloatIsInt(teil/bruch[0])+einheit)+2)
    tikzcommand.append('\\draw[-latex] ('+str(abstand+pfeilLaenge)+'cm,0.1cm) -- ('+str(abstand+2*pfeilLaenge)+'cm,0.1cm) ;')
    tikzcommand.append('\\draw ('+str(abstand+1.5*pfeilLaenge)+'cm,0.1cm) node[above] {$\\cdot'+schreibIntIfFloatIsInt(bruch[1])+'$} ;')
    tikzcommand.append('\\draw ('+str(abstand+2*pfeilLaenge)+'cm,0.1cm) node[right] {$'+schreibIntIfFloatIsInt(teil/bruch[0]*bruch[1])+'$ '+einheit+'} ;')
#    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\end{tikzpicture}')
    return tikzcommand



def zeichneBruchVergleichen(bruch1,bruch2):
    z1=1.0*bruch1[0]/bruch1[1]
    z2=1.0*bruch2[0]/bruch2[1]
    zeichen= ('=') if z1==z2 else ('<' if z1 < z2 else '>')
    tikzcommand=['\\begin{tikzpicture}[baseline=0]']
    tikzcommand.append('\draw[black] (0cm,0.0cm) node {$\\frac{'+str(bruch1[0])+'}{'+str(bruch1[1])+'}$} ;')
    tikzcommand.append('\draw[black] (0.6cm,0.0cm) node {$'+zeichen+'$} ;')
    tikzcommand.append('\draw[black] (1.2cm,0.0cm) node {$\\frac{'+str(bruch2[0])+'}{'+str(bruch2[1])+'}$} ;')
    if not (bruch1[0] == bruch2[0] or bruch1[1]==bruch2[1]):
        tikzcommand.append('\draw[-latex] (0.0cm,-0.3cm) -- (0.0cm,-1.0cm) ;')
        tikzcommand.append('\draw[black] (0cm,-0.65cm) node[left] {e$'+str(bruch2[1])+'$} ;')
        tikzcommand.append('\draw[-latex] (1.2cm,-0.3cm) -- (1.2cm,-1.0cm) ;')
        tikzcommand.append('\draw[black] (1.2cm,-0.65cm) node[right] {e$'+str(bruch1[1])+'$} ;')
        tikzcommand.append('\draw[black] (0cm,-1.3cm) node {$\\frac{'+str(bruch1[0]*bruch2[1])+'}{'+str(bruch1[1]*bruch2[1])+'}$} ;')
        tikzcommand.append('\draw[black] (0.6cm,-1.3cm) node {$'+zeichen+'$} ;')
        tikzcommand.append('\draw[black] (1.2cm,-1.3cm) node {$\\frac{'+str(bruch2[0]*bruch1[1])+'}{'+str(bruch2[1]*bruch1[1])+'}$} ;')
#    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\end{tikzpicture}')
    return tikzcommand

def ungleicheBruecheAddierenSubtrahierenTikz(bruch1,bruch2,op='+',mitKgv=True):
    tikzcommand=['\\begin{tikzpicture}[baseline=0]']
    tikzcommand.append('\draw[black] (0cm,0.0cm) node {$\\frac{'+strNW(bruch1[0])+'}{'+strNW(bruch1[1])+'}$} ;')
    tikzcommand.append('\draw[black] (0.6cm,0.0cm) node {$'+op+'$} ;')
    tikzcommand.append('\draw[black] (1.2cm,0.0cm) node {$\\frac{'+strNW(bruch2[0])+'}{'+strNW(bruch2[1])+'}$} ;')
    tikzcommand.append('\draw[-latex] (0.0cm,-0.3cm) -- (0.0cm,-1.0cm) ;')
    if mitKgv:
        e1=kgV(bruch1[1],bruch2[1])/bruch1[1]
        e2=kgV(bruch1[1],bruch2[1])/bruch2[1]
    else:
        e1=bruch2[1]
        e2=bruch1[1]
    tikzcommand.append('\draw[black] (0cm,-0.65cm) node[left] {e$'+strNW(e1)+'$} ;')
    tikzcommand.append('\draw[-latex] (1.2cm,-0.3cm) -- (1.2cm,-1.0cm) ;')
    tikzcommand.append('\draw[black] (1.2cm,-0.65cm) node[right] {e$'+strNW(e2)+'$} ;')
    tikzcommand.append('\draw[black] (0cm,-1.3cm) node {$\\frac{'+strNW(bruch1[0]*e1)+'}{'+strNW(bruch1[1]*e1)+'}$} ;')
    tikzcommand.append('\draw[black] (0.6cm,-1.3cm) node {$'+op+'$} ;')
    tikzcommand.append('\draw[black] (1.2cm,-1.3cm) node {$\\frac{'+strNW(bruch2[0]*e2)+'}{'+strNW(bruch2[1]*e2)+'}$} ;')
    zNeu=eval(str(bruch1[0])+'*'+str(e1)+op+str(bruch2[0])+'*'+str(e2))
    nNeu=e1*bruch1[1]
    teiler=ggt(zNeu,nNeu)
    gemZahl=schreibeGemZahl(zNeu/teiler,nNeu/teiler)
    print(gemZahl)
    tikzcommand.append('\draw[black] (1.4cm,-1.3cm) node[right] {$='+frac(zNeu,nNeu)+('' if teiler==1 else ('='+frac(zNeu/teiler,nNeu/teiler)))+(('='+gemZahl) if not gemZahl[0]=='\\' else '' )+'$} ;')
        
#    tikzcommand.append('\\addvmargin{1mm}')
    tikzcommand.append('\end{tikzpicture}')
    return tikzcommand