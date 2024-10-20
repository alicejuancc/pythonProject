"""
File: bouncing_ball.py
Name: Alice
-------------------------
TODO:
Once the user clicks the mouse, the ball will start bouncing to right way several times.
When the ball leave at the right of the window, it will appear again at the initial position.
This action can be executed three times. After that, clicking mouse can't trigger the action anymore.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3  # 球的水平移動速度
DELAY = 10  # 動畫停格多少毫秒
GRAVITY = 1  # 模擬重力加速度。每一圈 while loop 垂直速度要加上的數值
SIZE = 20  # 球的直徑
REDUCE = 0.9  # 每一次反彈，球垂直速度所剩的比例


# The initial position of the ball
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball_2')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
time = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(punch)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)


def punch(m):
    global time
    maybe_object = window.get_object_at(START_X + SIZE/2, START_Y + SIZE/2)
    if maybe_object is not None:
        if time > 0:
            time -= 1
            all_gravity = 0
            while True:

                all_gravity += GRAVITY
                ball.move(VX, all_gravity)
                pause(DELAY)
                if ball.y + SIZE >= window.height:
                    if all_gravity > 0:
                        all_gravity = -all_gravity * REDUCE
                if ball.x + SIZE >= window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    break


if __name__ == "__main__":
    main()