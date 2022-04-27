from tkinter import*
from gpiozero import LED
import RPi.GPIO

red=LED(14)
yellow =LED(23)
green = LED(24)

win=Tk()
def toogleRed():
    if red.is_lit:
        red.off
    else:
        red.on()
    yellow.off()
    green.off()

def toogleYellow():
    if yellow.is_lit:
        yellow.off
    else:
        yellow.on()
    red.off()
    green.off()

def toogleGreen():
    if green.is_lit:
        green.off
    else:
        green.on()
    red.off()
    yellow.off()

def close():
    RPi.GPIO.cleanup()
    win.destroy()

v = StringVar(win, "red")
red.on()
Radiobutton(win, text="Red LED", variable =v, command=toogleRed, value='red').pack(side=TOP, ipady=5)
Radiobutton(win, text="Yellow LED", variable =v, command=toogleYellow, value='yellow').pack(side=TOP, ipady=5)
Radiobutton(win, text="Green LED", variable =v, command=toogleGreen, value='Green').pack(side=TOP, ipady=5)

exitButton =Button(win, text="exit", command=close).pack(side=TOP, ipady=3)
win.mainloop()