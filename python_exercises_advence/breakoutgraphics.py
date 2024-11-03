"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Annby
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
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
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2-paddle_width/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "skyblue"
        self.paddle.color = "skyblue"
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(window_width-ball_radius*2)/2,
                          y=(window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_moving)

        # Draw bricks
        self.colors = ["red","orange","yellow","green","blue"]
        self.color_index = 0
        for row in range(brick_rows):
            for col in range(brick_cols):
                self.x = col * (brick_width + brick_spacing)
                self.y = brick_offset + row * (brick_height + brick_spacing)
                self.brick_color = self.colors[self.color_index]
                self.brick = GRect(brick_width, brick_height, x=self.x, y=self.y)
                self.brick.filled = True
                self.brick.fill_color = self.brick_color
                self.brick.color = self.brick_color
                self.window.add(self.brick)
            # Change color every two rows
            if row % 2 == 1:
                self.color_index = (self.color_index+1) % len(self.colors)

        self.num_bricks = brick_rows * brick_cols
        self.is_ball_moving = False  # Ball is initially not moving

    def paddle_moving(self, event):
        paddle_new_x = event.x - self.paddle.width/2
        if paddle_new_x < 0:  # beyond left border
            paddle_new_x = 0
        elif paddle_new_x > self.window.width - self.paddle.width:
            paddle_new_x = self.window.width - self.paddle.width
        self.paddle.x = paddle_new_x

    def set_ball_velocity(self, event):
        if not self.is_ball_moving:  # Only set the velocity if the ball is not already moving
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx  # Randomize direction
            self.is_ball_moving = True

    def get_dx(self):
        return self.__dx

    def set_dx(self, dx):
        self.__dx = dx

    def get_dy(self):
        return self.__dy

    def set_dy(self, dy):
        self.__dy = dy

    # Reset ball to the center of the window and stop its movement
    def reset_ball(self):
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2
        self.is_ball_moving = False

    # Check for collisions with the paddle or bricks at the ball's corners
    def check_collision(self):
        points = [
            (self.ball.x, self.ball.y),  # top-left
            (self.ball.x, self.ball.y),  # top-right
            (self.ball.x + self.ball.width, self.ball.y),  # bottom-left
            (self.ball.x + self.ball.width, self.ball.y + self.ball.width)  # bottom-right
        ]
        for point in points:  # for loop for four coordinates
            obj_point = self.window.get_object_at(point[0], point[1])  # (x,y) of obj_point
            if obj_point is not None:  # means ball hits something
                if obj_point is self.paddle:  # Indicates that the ball hits the board
                    return 'paddle'
                return obj_point  # hits the bricks
        return None  # no collision occurred














