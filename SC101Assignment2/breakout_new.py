"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
1. 優化前後端同步dx, dy，採取set_dx/set_dy作法
2. click不只打開開關，也拿到新速度值
3. attribute start只在後端做修改
4. graphics放到global，新增分數系統
"""

from campy.gui.events.timer import pause
from breakoutgraphics_new import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 13			# Number of attempts

graphics = BreakoutGraphics()


def main():
    graphics.set_live(NUM_LIVES)
    graphics.life_board.text = f'Lives:{graphics.live}'
    win = False
    hit = 0
    # Add the animation loop here!
    while True:
        if graphics.live == 0:
            graphics.show_result(win)
            break
        if win:
            graphics.show_result(win)
            break

        if graphics.start:
            while True:
                # --Update--
                dy = graphics.get_dy()
                dx = graphics.get_dx()
                graphics.ball.move(dx, dy)

                # --Check--
                # touching left and right
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_dx(-dx)
                # touching top
                if graphics.ball.y <= 0:
                    graphics.set_dy(-dy)
                # dropping to floor
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.reset_ball()
                    graphics.live -= 1
                    graphics.life_board.text = f'Lives:{graphics.live}'
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
                            graphics.set_dy(-dy)
                    elif obj1 is not graphics.score_board and obj1 is not graphics.life_board:
                        score_sys()
                        graphics.window.remove(obj1)
                        hit += 1
                        graphics.set_dy(-dy)
                        graphics.score_board.text = f"Score: {graphics.score}"
                elif obj2 is not None:
                    if obj2 is graphics.paddle:
                        if dy > 0:
                            graphics.set_dy(-dy)
                    elif obj2 is not graphics.score_board and obj2 is not graphics.life_board:
                        score_sys()
                        graphics.window.remove(obj2)
                        hit += 1
                        graphics.set_dy(-dy)
                        graphics.score_board.text = f"Score: {graphics.score}"
                elif obj3 is not None:
                    if obj3 is graphics.paddle:
                        if dy > 0:
                            graphics.set_dy(-dy)
                    elif obj3 is not graphics.score_board and obj3 is not graphics.life_board:
                        score_sys()
                        graphics.window.remove(obj3)
                        hit += 1
                        graphics.set_dy(-dy)
                        graphics.score_board.text = f"Score: {graphics.score}"
                elif obj4 is not None:
                    if obj4 is graphics.paddle:
                        if dy > 0:
                            graphics.set_dy(-dy)
                    elif obj4 is not graphics.score_board and obj4 is not graphics.life_board:
                        score_sys()
                        graphics.window.remove(obj4)
                        hit += 1
                        graphics.set_dy(-dy)
                        graphics.score_board.text = f"Score: {graphics.score}"
                if hit == graphics.brick_amount:
                    graphics.reset_ball()
                    win = True
                    break
        pause(FRAME_RATE)


def score_sys():
    if graphics.ball.y <= (graphics.window.height - graphics.brick_offset) // 3 + graphics.brick_offset:
        if graphics.ball.y >= (graphics.window.height - graphics.brick_offset) // 3 + \
                graphics.brick_offset - (graphics.brick_spacing + graphics.brick_height) * 2:
            graphics.score += 1
        elif graphics.ball.y >= (graphics.window.height - graphics.brick_offset) // 3 + \
                graphics.brick_offset - (graphics.brick_spacing + graphics.brick_height) * 4:
            graphics.score += 10
        elif graphics.ball.y >= (graphics.window.height - graphics.brick_offset) // 3 + \
                graphics.brick_offset - (graphics.brick_spacing + graphics.brick_height) * 6:
            graphics.score += 100
        elif graphics.ball.y >= (graphics.window.height - graphics.brick_offset) // 3 + \
                graphics.brick_offset - (graphics.brick_spacing + graphics.brick_height) * 5:
            graphics.score += 1000
        else:
            graphics.score += 10000


if __name__ == '__main__':
    main()
