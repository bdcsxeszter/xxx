from tkinter import*
import time
import random

class Ball:
    def __init__(self, canvasactual, paddleactual, color):
        self.canvasproperty=canvasactual
        self.paddleproperty=paddleactual
        self.id=canvasactual.create_oval(10,10,25,25,fill=color)
        self.canvasproperty.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvastul_height=self.canvasproperty.winfo_height()
        self.canvastul_width=self.canvasproperty.winfo_width()
        self.hit_bottom=False
        self.start=False
        self.canvasproperty.bind_all('<Button-1>',self.start_game)
    def hit_paddle(self, pos):
        paddletul_pos=self.canvasproperty.coords(self.paddleproperty.id)
        if pos[2]>=paddletul_pos[0] and pos[0]<=paddletul_pos[2]:
            if pos[3]>=paddletul_pos[1] and pos[3]<=paddletul_pos[3]:
                return True
        return False
    def draw(self):
        self.canvasproperty.move(self.id,self.x,self.y)
        pos=self.canvasproperty.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvastul_height:
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvastul_width:
            self.x=-3
    def start_game(self,evt):
        self.start=True

class Paddle:
    def __init__(self, canvasact, color):
        self.canvasprop=canvasact
        self.id=canvasact.create_rectangle(0,0,100,10,fill=color)
        self.canvasprop.move(self.id,200,700)
        self.x=0
        self.canvas_width=self.canvasprop.winfo_width()
        self.canvasprop.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvasprop.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvasprop.move(self.id,self.x,0)
        pos=self.canvasprop.coords(self.id)
        self.x=0
    def turn_left(self,evt):
        pos=self.canvasprop.coords(self.id)
        if pos[0]<=0:
            self.x=0
        else:
            self.x=-2
    def turn_right(self,evt):
        pos=self.canvasprop.coords(self.id)
        if pos[2]>=self.canvas_width:
            self.x=0
        else:
            self.x=2

tk=Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost', 1)
canvascreated=Canvas(tk, width=500, height=730, bd=0, highlightthickness=0)
canvascreated.pack()
tk.update()

paddle=Paddle(canvascreated, 'blue')
ball=Ball(canvascreated, paddle, 'red')

time.sleep(1)

while 1:
    if ball.hit_bottom==False and ball.start==True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

