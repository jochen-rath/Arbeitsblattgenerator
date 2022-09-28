#!/usr/bin/env python
# coding: utf8

#Die Funktion in diesem Skript vereint die Würfel, Stäbe und Scheiben Bilder zu der Zahl,
#die der Funktion übergeben wird. Gespeichert wird das Ergebnis unter "test.png"
#Aufruf:
#       exec(open("Funktionen/funktionen.py").read())


def plotteStreckenKlasse5(strecken,file=[]):
    plt.rcParams.update({'font.size': 18})
    dimSeite=[19*1.5,27*1.5]
    xMax=max([x[0] for sublist in strecken for x in sublist])
    yMax=max([x[1] for sublist in strecken for x in sublist])
    print([xMax,yMax])
    dimSeite[0],dimSeite[1]=(dimSeite[1],dimSeite[0]) if xMax > 19 and yMax < 19 else (dimSeite[0],dimSeite[1])
    fig = plt.figure(figsize=cm2inch(dimSeite[0],dimSeite[1]))
    ax = fig.add_subplot(1, 1, 1)
    for strecke in strecken:
        lines=ax.plot([x[0] for x in strecke],[x[1] for x in strecke],'-o',color='k')
#Achsen definieren.
    if True:
        ax.set_xlim((0,xMax+1))
        ax.set_ylim((0,yMax+1))
        ax.set_xlabel('X', fontsize = 18)
        ax.xaxis.set_label_coords(1.00, -0.03)
        ylabel=ax.set_ylabel('Y', fontsize = 18)
        ax.yaxis.set_label_coords(-0.02, 0.98)
        major_ticksX = np.arange(0,xMax+1, 1)
        minor_ticksX = np.arange(0,xMax+1, 0.5)
        major_ticksY = np.arange(0,yMax+1, 1)
        minor_ticksY = np.arange(0,yMax+1, 0.5)
        ax.set_xticks(major_ticksX)
        ax.set_xticks(minor_ticksX, minor=True)
        ax.set_yticks(major_ticksY)
        ax.set_yticks(minor_ticksY, minor=True)
        # Or if you want different settings for the grids:
        ax.grid(which='minor', alpha=0.4)
        ax.grid(which='major', alpha=0.7)
        line=plt.arrow(0, 0, xMax+0.5, 0, head_width=0.5, head_length=0.5, fc='k', ec='k')
        line.set_clip_on(False)
        line=plt.arrow(0, 0, 0, yMax+0.5, head_width=0.5, head_length=0.5, fc='k', ec='k')
        line.set_clip_on(False)
        plt.axis('scaled')
    if len(file)==0:
	    plt.show()
    else:
        fig.savefig(file,bbox_inches='tight')