import time
from Tkinter import *
import tkFont

import comm_c
import text_to_audio

from PIL import Image, ImageTk


'''
COMM_C Class:
have fuction sent_photo_get_reco(num), need photo index, return recommadation
'''
myclient = comm_c.COMM_C()

win = Tk()
win.title("GUI")
win.configure(background='black')
win.attributes("-fullscreen", True)
label = Label(win,text = 'Okay',fg = 'White',bg = 'Black',
				width = 60,height = 60,font=("Courier", 30),wraplength = 480,
				justify = 'left')

imglabel = Label(win,bg = 'Black')

texture = "Start!"
showtime = 0
staytime = 0
leavetime = 100
reco = ""

im = Image.open("0.png")
im = im.resize((250, 250),Image.ANTIALIAS)
im = ImageTk.PhotoImage(im)

def load_pic(num):
	global im
	im = Image.open(repr(num)+".png")
	im = im.resize((250, 250),Image.ANTIALIAS)
	im = ImageTk.PhotoImage(im)

def recursion():
	global texture
	global showtime
	global staytime
	global reco
	global im
	global leavetime
	dist = input()
	if(dist<60):
		leavetime = 0
		staytime = staytime + 1
		if(staytime==3):
			showtime = 2
			texture = "Let me think~"
		elif(staytime==4):
			print "reco,buy:"
			reco = raw_input()
			buy = input()
			if(reco != ""):
				texture = reco
				showtime = 1000
				load_pic(buy)
				#imglabel.configure(image=im).pack()
				#label.configure(text = reco)
			else:
				texture = "Baby I didn't see your face :("
				reco = "Baby I didn't see your face"
				showtime = 3
				staytime = 0
				load_pic(0)
			text_to_audio.speak(reco)
		'''
		elif(staytime==5):
			text_to_audio.speak(reco)
		'''
	else:
		staytime = 0
		leavetime = leavetime + 1

	if(showtime>0 and leavetime<3):
		showtime = showtime - 1
	else:
		texture = repr(dist)
		text_to_audio.stopmusic()
		load_pic(0)

	imglabel.configure(image = im)
	imglabel.pack()
	label.configure(text = texture)
	label.after(1000,recursion)
	label.pack()

if __name__ == '__main__':
	label.after(1000,recursion)
	win.mainloop()
