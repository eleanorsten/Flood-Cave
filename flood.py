"""Flood-fill to count chambers in a cave.
CS 210 project.
Eleanor Stenberg, 10/29/24
"""
import doctest
import cave
import config
import cave_view
from tracer import trace

@trace()
def pour(cavern: list[list[str]], row_i: int, col_i: int):
    """Pour water into cell at row_i, col_i"""
    if cavern[row_i][col_i] == config.AIR and (0 <= col_i < len(cavern[0]) and 0 <= row_i < len(cavern)):
        cavern[row_i][col_i] = config.WATER
        cave_view.fill_cell(row_i, col_i)
        pour(cavern, row_i-1, col_i)
        pour(cavern, row_i+1, col_i)
        pour(cavern, row_i, col_i-1)
        pour(cavern, row_i, col_i+1)
    

def scan_cave(cavern: list[list[str]]) -> int:
    """Scan the cave for air pockets.  Return the number of
    air pockets encountered.

    >>> cavern_1 = cave.read_cave("data/tiny-cave.txt")
    >>> scan_cave(cavern_1)
    1
    >>> cavern_2 = cave.read_cave("data/cave.txt")
    >>> scan_cave(cavern_2)
    3
    """
    air_pockets = 0
    for row_i in range(len(cavern)):
        for col_i in range(len(cavern[0])):
            if cavern[row_i][col_i] == config.AIR:
                air_pockets += 1
                pour(cavern, row_i, col_i)
                cave_view.change_water()
    return air_pockets

        
def main():
    doctest.testmod()
    cavern = cave.read_cave(config.CAVE_PATH)
    cave_view.display(cavern,config.WIN_WIDTH, config.WIN_HEIGHT)
    chambers = scan_cave(cavern)
    print(f"Found {chambers} chambers")
    cave_view.redisplay(cavern)
    cave_view.prompt_to_close()


if __name__ == "__main__":
    main()