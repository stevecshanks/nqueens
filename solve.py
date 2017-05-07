#!/usr/bin/env python3
import sys
import getopt
from nqueens.chessboard import Chessboard
from nqueens.printer import Printer
from nqueens.solver import Solver


def main():
    try:
        n = parse_command_line()
    except ValueError as e:
        print("Error: " + str(e))
        print("Usage: nqueens.py <n>")
        sys.exit(1)
    solution = solve_for(n)
    if solution is None:
        print("No solution found")
    else:
        print_solution(solution)


def parse_command_line():
    try:
        _, args = getopt.getopt(sys.argv[1:], "", [])
    except getopt.GetoptError:
        raise ValueError("Could not parse command line")
    if len(args) == 0:
        raise ValueError("No arguments supplied")
    if len(args) > 1:
        raise ValueError("Too many arguments supplied")
    n = args[0]
    if not n.isdigit() or int(n) < 1:
        raise ValueError("n must be a positive number")
    return int(n)


def solve_for(n):
    board = Chessboard.create(n)
    solver = Solver.create(board)
    return solver.solve()


def print_solution(solution):
    printer = Printer.create(solution)
    printer.printBoard()


if __name__ == '__main__':
    sys.exit(main())
