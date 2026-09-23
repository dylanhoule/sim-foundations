import random
import tkinter as tk
from noise import pnoise1
t = 0;
W, H = 400,400
STEP = 0.02
root = tk.Tk()
canvas = tk.Canvas(root, width=W,height=H, bg="white")
canvas.pack()

def draw_circle(canvas, x, y, r, **kwargs):
    """Draws a circle given center (x, y) and radius r."""
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, **kwargs)


def tick(t):
	num = pnoise1(t * STEP, octaves=4)
	y = H / 2 + num * (H/2)
	x = t % W
	draw_circle(canvas, x, y, 3, fill="black")
	t += 1

	root.after(60,tick, t + 1)

tick(0)
root.mainloop()
