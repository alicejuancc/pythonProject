"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 13			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    graphics.set_live(NUM_LIVES)
    graphics.life_board.text = f'Lives:{graphics.live}'
    win = False
    # Add the animation loop here!
    while True:
        if graphics.live == 0:
            graphics.show_result(win)
            break
        if win:
            graphics.show_result(win)
            break

        if graphics.start:
            dy = graphics.get_dy()
            dx = graphics.get_dx()
            while True:
                # --Update--
                graphics.ball.move(dx, dy)

                # --Check--
                # touching left and right
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                # touching top
                if graphics.ball.y <= 0:
                    dy = -dy
                # dropping to floor
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.reset_ball()
                    graphics.live -= 1
                    graphics.life_board.text = f'Lives:{graphics.live}'
                    graphics.start = False
                    break

                # --Pause--
                pause(FRAME_RATE)

                obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                     graphics.ball.y + graphics.ball.height)

                if obj1 is not None:
                    if obj1 is graphics.paddle:
                        if dy > 0:
                            dy = -dy
                    elif obj1 is not graphics.score_board and obj1 is not graphics.life_board:
                        graphics.window.remove(obj1)
                        dy = -dy
                        graphics.score += 1
                        graphics.score_board.text = f"Score: {graphics.score}"
                elif obj2 is not None:
                    if obj2 is graphics.paddle:
                        if dy > 0:
                            dy = -dy
                    elif obj2 is not graphics.score_board and obj2 is not graphics.life_board:
                        graphics.window.remove(obj2)
                        dy = -dy
                        graphics.score += 1
                        graphics.score_board.text = f"Score: {graphics.score}"
                elif obj3 is not None:
                    if obj3 is graphics.paddle:
                        if dy > 0:
                            dy = -dy
                    elif obj3 is not graphics.score_board and obj3 is not graphics.life_board:
                        graphics.window.remove(obj3)
                        dy = -dy
                        graphics.score += 1
                        graphics.score_board.text = f"Score: {graphics.score}"
                elif obj4 is not None:
                    if obj4 is graphics.paddle:
                        if dy > 0:
                            dy = -dy
                    elif obj4 is not graphics.score_board and obj4 is not graphics.life_board:
                        graphics.window.remove(obj4)
                        dy = -dy
                        graphics.score += 1
                        graphics.score_board.text = f"Score: {graphics.score}"
                if graphics.score == graphics.brick_amount:
                    graphics.reset_ball()
                    win = True
                    break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
