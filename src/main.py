#!/usr/bin/env python3
import sys

from game import Board

def main(argv):
    board = Board()
    board.print()
    print(board.get_current_score())


if __name__ == '__main__':
    main(sys.argv)