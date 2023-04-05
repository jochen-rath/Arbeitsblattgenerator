#!/usr/bin/env python
# coding: utf8
import random



# Diese Datei enthält verschiedene Funktionen, zur Erzeugung von Aufgaben zur Prozentrechnung

# Aufruf:
#       exec(open("/home/jochen/funktionenErzeugeLabyrinth.py").read())

# Create a maze using the depth-first algorithm described at
# https://scipython.com/blog/making-a-maze/
# Christian Hill, April 2017.

# MazeSolver:
# https://thecleverprogrammer.com/2021/01/26/maze-solver-with-python/
#Der Solver läuft rekursiv durch das Labyrinth und schaut, ob Wände da sind oder nicht. Ist keine Wand
#da, geht er den Weg weiter. Wenn nur Wände da sind ist es eine Sackgasse und der Weg wird gelöscht.

def erzeugeLabyrinthAufgabe(hoehe=5,anzSpalten=2):
    breite=5 if anzSpalten==2 else 15
    maze=Maze(breite*2, hoehe*2, 0, 0)
    maze.make_maze()
    maze.escape()
    while len(maze.loeseWeg)<3:
        maze=Maze(breite*2, hoehe*2, 0, 0)
        maze.make_maze()
        maze.escape()
    afg=maze.writeTikz(mitLsg=False)
    lsg=maze.writeTikz(mitLsg=True)
    return [afg,lsg,[]]

class Cell:
    """A cell in the maze.
    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.
    """
    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs={'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""
        self.x, self.y=x, y
        self.walls={'N': True, 'S': True, 'E': True, 'W': True}
    def has_all_walls(self):
        """Does this cell still have all its walls?"""
        return all(self.walls.values())
    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""
        self.walls[wall]=False
        other.walls[Cell.wall_pairs[wall]]=False
class Maze:
    """A Maze, represented as a grid of cells."""
    def __init__(self, nx, ny, ix=0, iy=0):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).
        """
        self.nx, self.ny=nx, ny
        self.ix, self.iy=ix, iy
        self.maze_map=[[Cell(x, y) for y in range(ny)] for x in range(nx)]
    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""
        return self.maze_map[x][y]
    def escape(self, nach='N'):
        printLaby=False
        current_cell=self.loeseWeg[-1]
        if printLaby:
            self.aktpos=[current_cell.x, current_cell.y]
            print(F'fx={self.finish.x},fy={self.finish.y}, cx={current_cell.x},cy={current_cell.y}')
            print(self)
            time.sleep(0.3)
        ichKommeVon=current_cell.wall_pairs[nach]
        if current_cell==self.finish:
            return
        delta=[('W', (-1, 0)), ('E', (1, 0)), ('S', (0, 1)), ('N', (0, -1))]
        # Entferne die Richtung, aus der ich komme.
        del delta[[i for i in range(len(delta)) if ichKommeVon in delta[i]][0]]
        for direction, (dx, dy) in delta:
            if not current_cell.walls[direction]:
                x2, y2=current_cell.x+dx, current_cell.y+dy
                if (0<=x2<self.nx) and (0<=y2<self.ny):
                    self.loeseWeg.append(self.cell_at(x2, y2))
                    self.escape(nach=direction)
        # If we get here, this means that we made a wrong decision, so we need to
        # backtrack
        current_cell=self.loeseWeg[-1]
        if current_cell!=self.finish:
            cell_to_remove=self.loeseWeg.pop()
        return

    def findeZusammenhaengendeWaende(self, wandListe):
        alleTrue=[i for i, x in enumerate(wandListe) if x]
        if len(alleTrue)==0:
            return []
        startEndpunkte=[[alleTrue[0]]]
        for i, x in enumerate(alleTrue[1:]):
            if not x==alleTrue[i]+1:
                startEndpunkte[-1].append(alleTrue[i])
                startEndpunkte.append([x])
        startEndpunkte[-1].append(alleTrue[-1])
        return startEndpunkte

    def writeTikz(self,mitLsg=False):
        tikzcommand=[]
        tikzcommand.append('\\begin{tikzpicture}')
        tikzcommand.append('\\node at (0,0.25) {};')
        # Zeichne die horizontalen Linien
        for j in range(self.ny):
            oben=[self.maze_map[x][j].walls['N'] for x in range(self.nx)]
            startEndpunkte=self.findeZusammenhaengendeWaende(oben)
            tikzcommand=tikzcommand+[F'\\draw ({x*0.5},-{j*0.5}) -- ({y*0.5+0.5},-{j*0.5});' for x, y in startEndpunkte]
        unten=[self.maze_map[x][-1].walls['S'] for x in range(self.nx)]
        startEndpunkte=self.findeZusammenhaengendeWaende(unten)
        tikzcommand=tikzcommand+[F'\\draw ({x*0.5},-{(j+1)*0.5}) -- ({y*0.5+0.5},-{(j+1)*0.5});' for x, y in
                                 startEndpunkte]
        # Zeichne die vertikalen Linien
        for i in range(self.nx):
            links=[self.maze_map[i][y].walls['W'] for y in range(self.ny)]
            startEndpunkte=self.findeZusammenhaengendeWaende(links)
            tikzcommand=tikzcommand+[F'\\draw ({i*0.5},-{x*0.5}) -- ({i*0.5},-{y*0.5+0.5});' for x, y in startEndpunkte]
        rechts=[self.maze_map[-1][y].walls['E'] for y in range(self.ny)]
        startEndpunkte=self.findeZusammenhaengendeWaende(rechts)
        tikzcommand=tikzcommand+[F'\\draw ({(i+1)*0.5},-{x*0.5}) -- ({(i+1)*0.5},-{y*0.5+0.5});' for x, y in
                                 startEndpunkte]
        if mitLsg:
            if len(self.loeseWeg)<3:
                self.escape()
            tikzcommand.append(F'\\draw[red] ({self.start.x*0.5+0.25},-{self.start.y*0.5-0.25}) -- ({self.start.x*0.5+0.25},-{self.start.y*0.5+0.25});')
            for i,weg in enumerate(self.loeseWeg[1:]):
                tikzcommand.append(F'\\draw[red] ({self.loeseWeg[i].x*0.5+0.25},-{self.loeseWeg[i].y*0.5+0.25}) -- ({weg.x*0.5+0.25},-{weg.y*0.5+0.25});')
#                tikzcommand.append(F'\\node[red] at ({weg.x*0.5+0.25},-{weg.y*0.5+0.25}) {{o}};')
            tikzcommand.append(F'\\draw[red] ({self.finish.x*0.5+0.25},-{self.finish.y*0.5+0.25}) -- ({self.finish.x*0.5+0.25},-{self.finish.y*0.5+0.75});')
        tikzcommand.append('\\end{tikzpicture}')
        return tikzcommand

    def __str__(self):
        """Return a (crude) string representation of the maze."""
        maze_rows=[]
        maze_row=['|']
        for x in range(self.nx):
            if self.maze_map[x][0].walls['N']:
                maze_row.append('-+')
            else:
                maze_row.append(' +')
        maze_rows.append(''.join(maze_row))
        for y in range(self.ny):
            maze_row=['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
                if self.aktpos[0]==x and self.aktpos[1]==y:
                    maze_row[-1]='X'
            maze_rows.append(''.join(maze_row))
            maze_row=['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def find_valid_neighbours(self, cell):
        """Return a list of unvisited neighbours to cell."""

        delta=[('W', (-1, 0)),
               ('E', (1, 0)),
               ('S', (0, 1)),
               ('N', (0, -1))]
        neighbours=[]
        for direction, (dx, dy) in delta:
            x2, y2=cell.x+dx, cell.y+dy
            if (0<=x2<self.nx) and (0<=y2<self.ny):
                neighbour=self.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze(self):
        # Total number of cells.
        n=self.nx*self.ny
        cell_stack=[]
        current_cell=self.cell_at(self.ix, self.iy)
        # Total number of visited cells during maze construction.
        nv=1

        while nv<n:
            neighbours=self.find_valid_neighbours(current_cell)

            if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell=cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell=random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            cell_stack.append(current_cell)
            current_cell=next_cell
            nv+=1
        # Erzeuge Eingang- Ausgangspunkt:
        self.startIntX=random.randint(0, self.nx-1)
        self.finishIntX=random.randint(0, self.nx-1)
        self.start=self.cell_at(self.startIntX, 0)
        self.finish=self.cell_at(self.finishIntX, self.ny-1)
        self.start.walls['N']=False
        self.finish.walls['S']=False
        self.loeseWeg=[self.start]
        self.aktpos=[self.startIntX, 0]