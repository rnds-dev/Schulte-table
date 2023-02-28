from tkinter import *
from random import randint
from time import time
bg, btng, fg_btn = '#f3f3f3', '#fefefe', '#333333'
green = '#6ecf6f'
red = '#e06c75'
sbtn = 80
offset = 10

window = Tk()
window.title("Schulte table")
window.resizable(width=False, height=False)
window.geometry(str(offset*2-2+5*sbtn)+'x'+str(int(sbtn*(5+4/3)+offset)))
window.configure(background=bg)


def info(txt, x1, clr):
	Label(window, text=txt, bg=bg, fg=clr, font=('Alata', 14)).place(
		x=offset+x1*sbtn*2.5-2, y=offset+sbtn*(5+2/3), width=sbtn*2.5-2, height=sbtn/1.5)


def ans(num):
	global n, t1, err
	if n > 24:
		info('Time: ' + str(round(time()-t1, 1)) + 's', 0, green)
		info('Mistakes: '+str(err), 1, red)
	elif num == n:
		n += 1
	else:
		err += 1
		info('Mistakes: '+str(err), 1, red)


def btn1(x1, y1, num):
	btn = Button(window, text=str(num), bg=btng, fg=fg_btn, font=('Alata', 14), borderwidth=0,
	             activebackground=bg, activeforeground=fg_btn, command=lambda: ans(num))
	btn.place(x=x1, y=y1, width=sbtn-2, height=sbtn-2)


def render():
	global n, err, t1
	n, err, t1 = 1, 0, time()
	lst = []
	while len(lst) < 25:
		x = randint(1, 25)
		if x not in lst:
			lst.append(x)
	for y in range(5):
		for x in range(5):
			btn1(offset+x*sbtn, offset+y*sbtn, lst[y*5+x])


render()
restart = Button(window, text=str('RESTART'), bg=btng, fg=fg_btn, font=(
	'Alata', 14), borderwidth=0, activebackground=bg, activeforeground=fg_btn, command=render)
restart.place(x=offset, y=offset+5*sbtn, width=sbtn*5-2, height=sbtn/1.5)
window.mainloop()
