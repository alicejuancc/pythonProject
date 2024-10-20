"""
File: babygraphics.py
Name: Alice
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """

    return GRAPH_MARGIN_SIZE + (width-GRAPH_MARGIN_SIZE*2) // len(YEARS) * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    for year_index in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), 0, get_x_coordinate(CANVAS_WIDTH, year_index),
                           CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    color_index = 0
    for name in lookup_names:
        if name in name_data:
            x1, y1 = 0, 0
            x2, y2 = 0, 0
            for year_index in range(len(YEARS)):
                if str(YEARS[year_index]) in name_data[name]:  # 名字有該年資料（在該年的1000名內）
                    int_rank = int(name_data[name][str(YEARS[year_index])])
                    unit = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2) / 1000
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                       GRAPH_MARGIN_SIZE + unit * int_rank,
                                       text=f'{name} {name_data[name][str(YEARS[year_index])]}',
                                       anchor=tkinter.SW, fill=f'{COLORS[color_index]}')
                    x = get_x_coordinate(CANVAS_WIDTH, year_index)
                    y = GRAPH_MARGIN_SIZE + unit * int_rank
                else:  # 名字無該年資料
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index) + TEXT_DX,
                                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                       text=f'{name} *',
                                       anchor=tkinter.SW, fill=f'{COLORS[color_index]}')
                    x = get_x_coordinate(CANVAS_WIDTH, year_index)
                    y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

                if x1 == 0 and y1 == 0:
                    x1 = x
                    y1 = y
                else:
                    x2 = x
                    y2 = y

                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=f'{COLORS[color_index]}')
                    x1 = x2
                    y1 = y2

            color_index += 1
            color_index %= len(COLORS)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
