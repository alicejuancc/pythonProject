"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gimage import GImage
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width)/2,y=self.window.height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width/2 - ball_radius, y=self.window.height/2 - ball_radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.start = False

        # Initialize our mouse listeners
        onmousemoved(self.move)
        onmouseclicked(self.click)

        # Draw bricks
        self.brick_amount = brick_rows * brick_cols
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=j * (brick_width + brick_spacing), y=brick_offset +
                                i * (brick_height + brick_spacing))

        # Create a score board
        self.score = 0
        self.score_board = GLabel(f"Score:{self.score}")
        self.score_board.font = "-30"
        self.window.add(self.score_board, x=0, y=self.window.height)

        # Create a life board
        self.live = 100
        self.life_board = GLabel(f'Lives:{self.live}')
        self.life_board.font = '-30'
        self.window.add(self.life_board, x=self.window.width-self.life_board.width, y=self.window.height)

        #
        # for score system use
        self.brick_offset = brick_offset
        self.brick_rows = brick_rows
        self.brick_spacing = brick_spacing
        self.brick_height = brick_height
        # for animation use
        self.first_click = True

        # Create a cover
        self.bg = GRect(window_width, window_height)
        self.bg.filled = True
        self.bg.fill_color = 'white'
        self.window.add(self.bg)
        self.bg_word = GLabel(f'Click to Start')
        self.bg_word.font = '-50'
        self.window.add(self.bg_word, x=(self.window.width-self.bg_word.width)/2, y=self.window.height/2)

    def reset_ball(self):
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.__dx = 0
        self.__dy = 0
        self.start = False

    def move(self, m):
        self.paddle.x = m.x - self.paddle.width/2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def click(self, m):
        if self.first_click:
            self.window.remove(self.bg)
            self.window.remove(self.bg_word)
            self.first_click = False
        elif not self.start:
            self.start = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def set_live(self, num):
        self.live = num

    def show_result(self, result):
        if result:
            result_word = GLabel("VICTORY ;)")
            result_word.font = '-40'
            result_word.color = 'blue'
            self.window.add(result_word, x=(self.window.width-result_word.width)/2, y=self.window.height/2)
        else:
            result_word = GLabel("LOSE :(")
            result_word.font = '-40'
            result_word.color = 'red'
            self.window.add(result_word, x=(self.window.width-result_word.width)/2, y=self.window.height/2)
