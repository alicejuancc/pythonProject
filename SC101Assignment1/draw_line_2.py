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

# Global variable
window = GWindow()
origin_x = 0
origin_y = 0
stroke = GOval(SIZE, SIZE)


def main():
    onmouseclicked(punch)


def punch(m):
    global origin_x, origin_y, stroke
    if origin_x == 0 and origin_y == 0:
        stroke = GOval(SIZE, SIZE, x=m.x - (SIZE / 2), y=m.y - (SIZE / 2))
        window.add(stroke)
        origin_x = m.x
        origin_y = m.y
    else:
        line = GLine(m.x, m.y, origin_x, origin_y)
        window.remove(stroke)
        window.add(line)
        origin_x = 0
        origin_y = 0


if __name__ == "__main__":
    main()