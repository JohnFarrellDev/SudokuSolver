import time  # for measuring how long it takes to solve a sudoku
import sys  # for taking arguments from the terminal
import re  # regex for assert testing


def grid(c, d):
    return [a+b for a in c for b in d]


if sys.argv.__len__() == 2:
    user_input = sys.argv[1]
    grid1 = user_input  # this is the unfinished sudoku inserted via terminal
else:
    grid1 = '...............9..97.3......1..6.5....47.8..2.....2..6.31..4......8..167.87......'

start_grid = list(grid1)

digits = '123456789'
rows = 'ABCDEFGHI'
cols = '123456789'  # recreate instead of using digits for later clarity

squares = grid(rows, cols)  # produces 9x9 grid from A1 to I9

'''Implement the 3 rules of sudoku'''

columns = [grid(rows, c) for c in cols]
rows = [grid(r, cols) for r in rows]
sub_grids = [grid(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

rules = columns + rows + sub_grids  # store all 3 rules within one list

'''for each square in the 9x9 grid determine which other squares it can not have the same value as'''

units = dict((s, [u for u in rules if s in u]) for s in squares)
# creates a dictionary in which every square is mapped to all squares it can not share the same value as

peers = dict((s, set(sum(units[s], [])) - {s}) for s in squares)
# alters the dictionary so that each square does not include itself as a square it cannot share the same value as


def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or return False if a contradiction is detected."""
    values = dict((s, digits) for s in squares)  # initially assign each square a possible value from 1-9
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False  # (Fail if we can't assign d to square s.)
    return values


def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    return dict(zip(squares, chars))


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values  # Already eliminated
    values[s] = values[s].replace(d, '')
    # (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False  # Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    # (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False  # Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values


def solve(board):
    return search(parse_grid(board))


def search(values):
    """Using depth-first search and propagation, try all possible values"""
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values  # Solved!
    # Chose the unfilled square s with the fewest possibilities
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def some(seq):
    """Return some element of seq that is true."""
    for e in seq:
        if e:
            return e
    return False


'''cosmetics from here and below'''


def line(numb, squ):
    temp_list = squ[(numb-9):numb]
    print('#{}#{}#{}#'.format(temp_list[0:3], temp_list[3:6], temp_list[6:9]), flush=True)


def hashline():
    print('#################################################')


def grid_display(squ):
    hashline()
    for i in range(9, 90, 9):
        if i == 36 or i == 63:
            hashline()
        line(i, squ)
    hashline()


def make_final_sudoku():
    x = solve(grid1)
    for k, v in x.items():
        location = squares.index(k)
        squares[location] = v


def print_grids():
    print()  # to separate grids with a blank line
    print('initial sudoku')
    grid_display(start_grid)
    print()  # to separate grids with a blank line
    print('completed sudoku')
    grid_display(squares)
    print()  # to separate grids with a blank line
    print("--------- %s seconds ----------" % (time.time() - start_time))


def tests():
    assert len(grid1) == 81, 'Make sure your sudoku input is exactly 81 characters long'
    assert len(start_grid) == 81
    assert len(squares) == 81
    assert len(columns) == 9
    assert len(rows) == 9
    assert len(sub_grids) == 9
    assert len(rules) == 27
    assert len(peers['A1']) == 20
    assert re.match("^[0-9.]*$", grid1), \
        'Make sure your sudoku only contains digits or ".", pelase use a "0" or a "." for any unknown values.'


start_time = time.time()
make_final_sudoku()

if __name__ == "__main__":
    print_grids()


tests()
