"""
File: draw_line.py
Name: Alice
-------------------------
TODO:
This is a program of drawing straight lines. When Users click the mouse first time,
the first clicking position will appear a circle.
When users click mouse second times, the clicking position of first and second time will be linked as a line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 10  # size of circle

# Global Variable
window = GWindow()
switch = False
start_x = 0
start_y = 0
oval = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(m):
    """
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    global switch, start_x, start_y, oval
    if not switch:
        window.add(oval, x=m.x-SIZE/2, y=m.y-SIZE/2)
        start_x = m.x
        start_y = m.y
        switch = True
    else:
        window.remove(oval)
        line = GLine(start_x, start_y, m.x, m.y)
        window.add(line)
        switch = False


if __name__ == "__main__":
    main()
