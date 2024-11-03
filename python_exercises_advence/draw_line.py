"""
File: Assignment1
Name: Annby
-------------------------

"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
click_count = 0
last_click = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    global click_count, last_click, hole
    if click_count % 2 == 0:
        hole = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(hole)
        last_click = mouse  # Store the coordinates of the last click
    else:
        line = GLine(last_click.x, last_click.y, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
        window.add(line)
        window.remove(hole)
    click_count += 1  # Determine whether to perform the first or second click


if __name__ == "__main__":
    main()
