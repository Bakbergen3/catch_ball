import tkinter as tk
from random import randrange as rnd, choice
import math as math

WIDTH = 400
HEIGHT = 300


def new_ball():
    """
    Creates a new ball.
    """
    global x, y, r, ball_id
    canv.delete('all')

    r = rnd(30, 50)
    x = rnd(30, WIDTH - r)
    y = rnd(30, HEIGHT - r)
    ball_id = canv.create_oval(x - r, y - r, x + r, y + r,
                    fill=choice(colors), width=0)
    root.after(3000, new_ball)


def move_ball(dx=4, dy=4):
    """
    Moves the ball with certain speed.
    Params:
        dx: speed on x-axis
        dy: speed on y-axis
    """
    global x, y
    x += dx
    y += dy
    if x + r > WIDTH or x - r <= 0:
        dx = -dx
    if y + r > HEIGHT or y - r <= 0:
        dy = -dy

    canv.move(ball_id, dx, dy)
    root.after(49, move_ball)


def click(event):
    """
    Initializes an event upon left-mouse click.
    Event: Upon click, prints the result
    """
    global score
    print(x, y)
    print(event.x, event.y)

    distance = math.sqrt((x - event.x)**2 + (y - event.y)**2)
    if distance <= r:
        print('You hit the ball! \nYour score: ', score)
        score += 1
        canv.create_text(35, 10, fill='black', font="Times 16 bold", \
                    text=f'Score: {score}')
        canv.update()
    else:
        print('Miss shot')


def main():
    global root, canv
    global score, colors
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))

    canv = tk.Canvas(root, bg='white')
    canv.pack(fill='both', expand=1)

    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    score = 0
    canv.bind('<Button-1>', click)

    new_ball()
    move_ball()

    root.mainloop()


if __name__ == "__main__":
    main()
