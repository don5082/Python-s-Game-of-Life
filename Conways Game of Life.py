import copy
import time
from posixpath import split
from time import sleep


def print_g(grid):
    print("  ",end=" ")
    for i in range(len(grid)):
        print(i, end=" ")
    print()

    for i in range(len(grid)):
        if i <= 9:
            print(f" {i}", end=" ")
        else:
            print(i, end=" ")

        for j in range(len(grid)):
            if j >= 10:
                print(grid[i][j], end="  ")
            else:
                print(grid[i][j], end=" ")

        print()

def init(starting_values):
    size = 15
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    for item in starting_values:

        if item[0] >= size or item[1] >= size:
            continue

        grid[item[0]][item[1]] = '*'

    return grid

def get_living_neighbors(cell, grid):
    living_neighbors = []
    for i in range(cell[0] - 1, cell[0] + 2):
        if i < 0 or i >= len(grid):
            continue
        for j in range(cell[1] - 1, cell[1] + 2):
            if j < 0 or j >= len(grid) or (i == cell[0] and j == cell[1]):
                continue
            if grid[i][j] == '*':
                living_neighbors.append((i,j))



    return living_neighbors

def run(grid):
    grid_cpy = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid)):
            num_neighbs = len(get_living_neighbors((i,j),grid_cpy))
            if grid_cpy[i][j] == "*" and 2 > num_neighbs or 3 < num_neighbs:
                grid[i][j] = " "
            if grid_cpy[i][j] == " " and num_neighbs == 3:
                grid[i][j] = "*"


    return grid

def main():
    grid = init([])
    print_g(grid)
    print("Enter starting values in form of y,x press enter after each entry")

    values_lst = []
    while True:
        inp = input()
        if len(inp) == 0 :
            break

        starting_values = inp.strip().split(',')
        values_lst.append((int(starting_values[0]),int(starting_values[1])))




    grid = init(values_lst)
    print_g(grid)

    num_iters = int(input("how many iterations would you like?"))
    for i in range(num_iters):
        grid = run(grid)
        print_g(grid)
        time.sleep(.5)

main()