"""
File: Assignment1
Name: Annby
-------------------------

"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

vx = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
click_count = 0
mouse_enable = True
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(click_the_ball)

    ball.filled = True
    ball.fill_color = "skyblue"
    ball.color = "skyblue"
    window.add(ball)


def click_the_ball(mouse):
    global START_X,START_Y, click_count, mouse_enable, vx, ball

    if mouse_enable and click_count < 3:
        vy = 0
        mouse_enable = False
        while True:
            vy += GRAVITY
            ball.move(vx, vy)  # Move the ball to a new location
            pause(DELAY)  # Simulates the continuity of ball movement on the screen
            if ball.y + SIZE >= window.height:  # Check if the ball touches the bottom border of the window.
                vy *= -REDUCE  # The vertical velocity of the ball takes a negative value
                ball.move(vx, vy)
            if ball.x + SIZE >= window.width:
                window.remove(ball)
                break
        ball.x = START_X
        ball.y = START_Y
        window.add(ball)
        click_count += 1
        mouse_enable = True


if __name__ == "__main__":
    main()
