import time  # for measuring how long it takes to solve a sudoku

def grid(c, d):
    return [a+b for a in c for b in d]


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


hard_completion_time = []
easy_completion_time = []

hard = open('2365hardpuzzles.txt', 'r')
easy = open('1011easypuzzles.txt', 'r')


for line in hard:
    grid1 = line

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
    start_time = time.time()
    solve(grid1)
    final_time = time.time() - start_time
    hard_completion_time.append(final_time)

for line in easy:
    grid1 = line

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
    start_time = time.time()
    solve(grid1)
    final_time = time.time() - start_time
    easy_completion_time.append(final_time)

