import tkinter as tk
from random import randrange as rnd, choice
import math as math
import time


def new_ball():
    """
    Creates a new ball.
    """
    global x, y, r
    canv.delete('all')

    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r,
                    fill=choice(colors), width=0)
    root.after(1000, new_ball)

def click(event):
    """
    Initializes an event upon left-mouse click.
    Event: Upon click, prints the result
    """
    global score

    distance = math.sqrt((x - event.x)**2 + (y - event.y)**2)
    if distance <= r:
        print('You hit the ball! \nYour score: ', score)
        score += 1
    else:
        print('Miss shot')

def main():
    global root, canv
    global score, colors
    root = tk.Tk()
    root.geometry('800x600')

    canv = tk.Canvas(root, bg='white')
    canv.pack(fill='both', expand=1)

    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    score = 0
    new_ball()
    canv.bind('<Button-1>', click)
    root.mainloop()

if __name__ == "__main__":
    main()
