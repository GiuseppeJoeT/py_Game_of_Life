def neighbours_of_(cell):
    x, y = cell
    return [
        (x-1,y-1), (x,y-1), (x+1,y-1),
        (x-1,y),            (x+1,y),
        (x-1,y+1), (x,y+1), (x+1,y+1)
    ]

def number_of_living_neighbours(cells,cell):
    return len(set(neighbours_of_(cell)).intersection(cells))

def cell_survives(cells, cell):
    neighbours = number_of_living_neighbours(cells, cell)
    return neighbours == 2 or neighbours == 3

# The next generation contains cells that survive, or come to life
def next(cells):
    return survivors(cells) + come_to_life(cells)

def survivors(cells):
    return [cell for cell in cells
            if cell_survives(cells, cell)]

# Cells That Are Not Alive That Come To Life
def come_to_life(last_generation):
    candidates = might_come_to_life(last_generation)
    return [cell for cell in candidates if cell_comes_to_life(last_generation, cell)]

def might_come_to_life(last_generation):
    neighbours_of_each_cell = [neighbours_of(cell) for cell in last_generation]
    touching_live_cells = []
    for neighbours in neighbours_of_each_cell:
        touching_live_cells += neighbours

    return set(touching_live_cells).difference(last_generation)



print next([(0,0), (0,1), (1,0), (1,1)])

