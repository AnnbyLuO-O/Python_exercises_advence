"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Annby
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GRect

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)

        if graphics.is_ball_moving:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-graphics.get_dx())
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.set_dy(-graphics.get_dy())

            collision = graphics.check_collision()
            if collision == 'paddle':
                # Adjust the ball's y position to be above the paddle
                graphics.ball.y = graphics.paddle.y - graphics.ball.height
                graphics.set_dy(-graphics.get_dy())
            elif isinstance(collision, GRect):
                graphics.window.remove(collision)
                graphics.num_bricks -= 1
                graphics.set_dy(-graphics.get_dy())

            # Check for the ball going out of the bottom of the window
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                if lives == 0:
                    print("Game Over")
                    break

                # Check for win condition
            if graphics.num_bricks == 0:
                print("Win!")
                break




if __name__ == '__main__':
    main()
