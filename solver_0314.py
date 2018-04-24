import numpy as np
import sys
import csv
import pandas as pd

def import_puzzle(i=1):
    """
    This function is to import the puzzle saved in suduku.csv
    i: the number of puzzles. range in 1 to 1,000,000.
    """
    with open('sudoku.csv','rt', encoding='utf-8') as f1:
        reader=csv.reader(f1)
        rows=list(reader)
#     print(rows[i])
    quiz = rows[i][0]
    solution = rows[i][1]
    return quiz, solution

user_input = input("Please enter the number of puzzle (1-1,000,000): ")
(q,s) = import_puzzle(int(user_input))
print(q)
print(s)

q_list = []
for i in range(9):
    q_list.append(tuple(q)[i*9:(i+1)*9])
# print(q_list)
q_pd = pd.DataFrame.from_records(q_list, columns=list('ABCDEFGHI'))
q_pd


q2 = q_pd.replace({'0':'123456789'})
q2


def row_opt(q2):
    for i in range(9):
        for j in range(9):
            if len(list(q2.iloc[i][j])) == 1:
                value = q2.iloc[i][j]
    #             print(value)
                for k in [x for x in range(9) if x != j]:
                    new = q2.loc[i][k].replace(value,'')
                    q2.loc[i][k] = new
    return q2

# Not finished.