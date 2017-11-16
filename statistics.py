import numpy as np
import matplotlib.pyplot as plt

from sudokusolvermultiple import easy_completion_time, hard_completion_time

easy = easy_completion_time
easy.sort()
easy_length = len(easy)
easy_mean = np.mean(easy)
easy_median = np.median(easy)
easy_stdev = np.std(easy)
easy_uq = np.percentile(easy, 75)
easy_lq = np.percentile(easy, 25)
easy_max = easy[-1]
easy_min = easy[0]
easy_difference = easy_max - easy_min

hard = hard_completion_time
hard.sort()
hard_length = len(hard)
hard_mean = np.mean(hard)
hard_median = np.median(hard)
hard_stdev = np.std(hard)
hard_uq = np.percentile(hard, 75)
hard_lq = np.percentile(hard, 25)
hard_max = hard[-1]
hard_min = hard[0]
hard_difference = hard_max - hard_min

compare_mean = (hard_mean/easy_mean)
compare_median = (hard_median/easy_median)
compare_stdev = (hard_stdev/easy_stdev)
compare_max = (hard_max - easy_max)

if __name__ == '__main__':
    print('Easy sudoku stats:')
    print('Number of easy sudokus: ' + str(easy_length))
    print('Mean time to complete of the easy sudokus: ' + str(easy_mean))
    print('Median time to complete of the easy sudokus: ' + str(easy_median))
    print('Standard deviation of time to complete of the easy sudokus: ' + str(easy_stdev))
    print('Upper quartile time to complete of the easy sudokus: ' + str(easy_uq))
    print('Lower quartile time to complete of the easy sudokus: ' + str(easy_lq))
    print('Max time taken to solve by an easy sudoku: ' + str(easy_max))
    print('Minimum time taken to solve by an easy sudoku: ' + str(easy_min))
    print('Difference between max and min time to solve easy sudokus: ' + str(easy_difference))
    print()
    print('Hard sudoku stats:')
    print('Number of hard sudokus: ' + str(hard_length))
    print('Mean time to complete of the hard sudokus: ' + str(hard_mean))
    print('Median time to complete of the hard sudokus: ' + str(hard_median))
    print('Standard deviation of time to complete of the hard sudokus: ' + str(hard_stdev))
    print('Upper quartile time to complete of the hard sudokus: ' + str(hard_uq))
    print('Lower quartile time to complete of the hard sudokus: ' + str(hard_lq))
    print('Max time taken to solve by an hard sudoku: ' + str(hard_max))
    print('Minimum time taken to solve by an hard sudoku: ' + str(hard_min))
    print('Difference between max and min time to solve hard sudokus: ' + str(hard_difference))
    print()
    print('Comparing the hard and easy stats:')

    # compare how many of the hard ones are past a certain percentile of the easy distribution
    print('Time to complete mean hard sudokus compared to mean easy sudoku: ' + str(compare_mean) + 'x')
    print('Time to complete median hard sudokus compared to median easy sudoku: ' + str(compare_median) + 'x')
    print('Comparing standard deviation of hard sudokus compared to easy sudoku: ' + str(compare_stdev) + 'x')
    print('Comparing the max time taken by a hard sudoku puzzles vs easy sudoku puzzles: ' + str(compare_max))

# box plots and normal distributions to compare the easy and hard sets
