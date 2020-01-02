import tkinter as tk
from random import randrange as rnd, choice
import math as math

WIDTH = 400
HEIGHT = 300


class Ball:
    def __init__(self):
        """
        Initializes
            r - radius
            x - point on x-axis
            y - point on y-axis
            ball_id - id of initialized ball
            dx - speed of movement on x-axis
            dy - speed of movement on y-axis
        """
        self.r = rnd(30, 50)
        self.x = rnd(30, WIDTH - self.r)
        self.y = rnd(30, HEIGHT - self.r)
        self.dx, self.dy = +2, +3
        self.ball_id = canvas.create_oval(self.x - self.r, self.y - self.r,
                                        self.x + self.r, self.y + self.r,
                                        fill=choice(colors), width=0)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > WIDTH or self.x - self.r <= 0:
            self.dx = -self.dx
        if self.y + self.r > HEIGHT or self.y - self.r <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def controller():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, controller)


def new_ball():
    """
    Creates a new ball.
    """
    canvas.delete('all')
    root.after(3000, new_ball)


def move_ball(dx=4, dy=4):
    """
    Moves the ball with certain speed.
    Params:
        dx: speed on x-axis
        dy: speed on y-axis
    """
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
        canvas.create_text(35, 10, fill='black', font="Times 16 bold", \
                    text=f'Score: {score}')
        canvas.update()
    else:
        print('Miss shot')


def main():
    global root, canvas
    global score, colors, balls
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))

    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill='both', expand=1)

    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    score = 0
    canvas.bind('<Button-1>', click)

    balls = [Ball() for i in range(5)]
    controller()

    root.mainloop()


if __name__ == "__main__":
    main()
