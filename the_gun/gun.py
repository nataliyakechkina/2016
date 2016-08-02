from tkinter import *
from random import choice, randint

screen_width=400
screen_height=300
timer_delay=100

class Ball:
    initial_number=100
    min_radius=15
    max_radius=40
    available_colors=['green', 'blue', 'red']

    def __init__(self):
        """Создаю шарик в случайном положении на холсте"""
        R=randint(Ball.min_radius, Ball.max_radius)
        x=randint(0, screen_width-1-2*R)
        y=randint(0, screen_height-1-2*R)
        self._R=R
        self._x=x
        self._y=y
        fillcolor=choice(Ball.available_colors)
        self._avatar=canvas.create_oval(x,y,x+2*R, y+2*R,
                                        width=1, fill=fillcolor,
                                        outline=fillcolor)
        self._Vx=randint(-2,+2)
        self._Vy=randint(-2,+2)

    def fly(self):
        self._x+=self._Vx
        self._y+=self._Vy
        if self._x<0:
            self._x=0
            self._Vx=-self._Vx
        elif self._x+2*self._R>=screen_width:
            self._x=screen_width-self._R-1
            self._Vx=-self._Vx
        if self._y<0:
            self._y=0
            self._Vy=-self._Vy
        elif self._y+2*self._R>=screen_height:
            self._y=screen_height-self._R-1
            self._Vy=-self._Vy
        canvas.coords(self._avatar, self._x, self._y,
                      self._x+2*self._R, self._y+2*self._R)

class Gun:
    def __init__(self):
        self._x=0
        self._y=screen_height-1
        self._lx=30
        self._ly=-30
        self._vavtar=canvas.create_line(self._x, self._y,
                                        self._x+self._lx, self._y+self._ly)
    def shoot(self):
        shell=Ball()
        shell.x=self._x+self._lx
        shell.y=self._y+self._ly
        shell.Vx=self._lx/10
        shell.Vy=self._ly/10
        shell._R=5
        shell.fly()
        return shell


def init_game():
    global balls, gun, shells_on_fly
    balls=[Ball() for i in range(Ball.initial_number)]
    shells_on_fly=[]
    gun=Gun()


def init_main_window():
    global root, canvas, scores_text, scores_value
    root=Tk()
    balls=[Ball() for i in range(Ball.initial_number)]
    scores_value = IntVar()
    canvas=Canvas(root, width=screen_width, height=screen_height, bg='white' )
    canvas.pack()
    scores_text=Entry(root, textvariable=scores_value)
    #scores_text.grid(row=0,column=2)
    scores_text.pack()
    canvas.bind('<Button-1>', click_event)

def timer_event(event):
    print ('New time tike')
    for ball in balls:
        ball.fly()
    canvas.after(timer_delay, timer_event)
    for shell in shells_on_fly:
        shell.fly()
    canvas.after(timer_delay, timer_event, event)

def click_event():
    global shells_on_fly
    shell=gun.shoot()
    shells_on_fly.append(shell)


if __name__ == "__main__":
    init_main_window()
    init_game()
    canvas.after(2000, timer_event)
    root.mainloop()
