"""
"play one" in Taiwanese sounds like "play with me" !
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

# Constants for the game
BRICK_SPACING = 5
BRICK_WIDTH = 40
BRICK_HEIGHT = 15
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_OFFSET = 50
BALL_RADIUS = 10
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 15
PADDLE_OFFSET = 50
INITIAL_Y_SPEED = 7
MAX_X_SPEED = 5
FRAME_RATE = 10
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Playone'):

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
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius*2)/2, y=(window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.ball.fill_color = "orange"
        self.ball.color = "orange"
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Create a score label
        self.score = 0
        self.score_label = GLabel(f"Score: {self.score}")
        self.score_label.font = "SansSerif-18"
        self.window.add(self.score_label, 5, window_height - 5)

        # Initialize lives display
        self.lives = NUM_LIVES
        self.lives_images = []
        self.init_lives_display()

        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_moving)

        green_colors = [
            "#008200", "#009900", "#0ab00a", "#28c828", "#46d046",
            "#64d864", "#83e083", "#a2e8a2", "#c1f0c1", "#e0f8e0"
        ]
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = col * (brick_width + brick_spacing)
                y = brick_offset + row * (brick_height + brick_spacing)
                brick_color = green_colors[row % len(green_colors)]
                brick = GRect(brick_width, brick_height, x=x, y=y)
                brick.filled = True
                brick.fill_color = brick_color
                brick.color = brick_color
                self.window.add(brick)

        self.num_bricks = brick_rows * brick_cols
        self.is_ball_moving = False

        # Perform countdown
        self.countdown()

    def countdown(self):
        countdown_labels = ["3", "2", "1", "Game start!"]
        for label_text in countdown_labels:
            label = GLabel(label_text)
            label.font = "SansSerif-36"
            self.window.add(label, (self.window.width-label.width)/2, (self.window.height - label.height)/1.5)
            pause(1000)
            self.window.remove(label)

    def update_score(self, points):
        self.score += points
        self.score_label.text = f"Score: {self.score}"

    def init_lives_display(self):
        heart_radius = 10
        for i in range(NUM_LIVES):
            heart = GOval(heart_radius * 2, heart_radius * 2)
            heart.filled = True
            heart.fill_color = "red"
            heart.color = "red"
            self.window.add(heart, self.window.width - (i + 1) * heart.width - 5, self.window.height - heart.height - 5)
            self.lives_images.append(heart)

    def update_lives_display(self):
        if self.lives_images:
            self.window.remove(self.lives_images.pop())

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
                self.__dx = -self.__dx
            self.is_ball_moving = True

    def get_dx(self):
        return self.__dx

    def set_dx(self, dx):
        self.__dx = dx

    def get_dy(self):
        return self.__dy

    def set_dy(self, dy):
        self.__dy = dy

    def reset_ball(self):
        self.ball.x = self.window.width / 2 - self.ball.width / 2
        self.ball.y = self.window.height / 2 - self.ball.height / 2
        self.is_ball_moving = False

    def check_collision(self):
        points = [
            (self.ball.x, self.ball.y),  # top-left
            (self.ball.x, self.ball.y),  # top-right
            (self.ball.x + self.ball.width, self.ball.y),  # bottom-left
            (self.ball.x + self.ball.width, self.ball.y + self.ball.width)  # bottom-right
        ]
        for point in points:
            obj_point = self.window.get_object_at(point[0], point[1])
            if obj_point is not None:
                if obj_point is self.paddle:
                    return 'paddle'
                return obj_point
        return None

    def show_label(self, text):
        label = GLabel(text)
        label.font = "SansSerif-36"
        self.window.add(label, (self.window.width - label.width) / 2, (self.window.height - label.height) / 2)


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    game_over = False

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)

        while True:
            pause(FRAME_RATE)
            if not game_over:
                if graphics.is_ball_moving:
                    graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        graphics.set_dx(-graphics.get_dx())
                    if graphics.ball.y <= 0:
                        graphics.set_dy(-graphics.get_dy())
                    elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                        lives -= 1
                        graphics.update_lives_display()
                        if graphics.num_bricks > 0:
                            graphics.reset_ball()
                        if lives == 0:
                            graphics.show_label("BAD PLAYER !")
                            game_over = True  # Set game over flag
                            break

                    collision = graphics.check_collision()
                    if collision == 'paddle':
                        # Adjust the ball's y position to be above the paddle
                        graphics.ball.y = graphics.paddle.y - graphics.ball.height
                        graphics.set_dy(-graphics.get_dy())
                    elif isinstance(collision, GRect):
                        graphics.window.remove(collision)
                        graphics.num_bricks -= 1
                        graphics.set_dy(-graphics.get_dy())
                        graphics.update_score(1)

                    # Check for win condition
                    if graphics.num_bricks == 0:
                        graphics.show_label("U WIN !")
                        game_over = True
                        break


if __name__ == '__main__':
    main()













