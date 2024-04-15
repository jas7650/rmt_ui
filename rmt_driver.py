from objects.Model import Model
from tkinter import *

FONT_SIZE = 10
PAD_SIZE = 2

def increment_mode():
    global rmt_model, mode_value_label
    rmt_model.increment_mode()
    mode_value_label.configure(text=rmt_model.getMode())


def decrement_mode():
    global rmt_model, mode_value_label
    rmt_model.decrement_mode()
    mode_value_label.configure(text=rmt_model.getMode())


def increase_speed():
    global rmt_model, speed_value_label
    rmt_model.increase_speed()
    speed_value_label.configure(text=rmt_model.getSpeed())


def decrease_speed():
    global rmt_model, speed_value_label
    rmt_model.decrease_speed()
    speed_value_label.configure(text=rmt_model.getSpeed())


def increase_spin():
    global rmt_model, spin_value_label
    rmt_model.increase_spin()
    spin_value_label.configure(text=rmt_model.getSpin())


def decrease_spin():
    global rmt_model, spin_value_label
    rmt_model.decrease_spin()
    spin_value_label.configure(text=rmt_model.getSpin())


def set_start():
    global rmt_model, status_value_label
    rmt_model.set_start()
    status_value_label.configure(text=rmt_model.getRunning(), bg='red')


def set_stop():
    global rmt_model, status_value_label
    rmt_model.set_stop()
    status_value_label.configure(text=rmt_model.getRunning(), bg='green')


def print_status():
    rmt_model.print_status()


rmt_model = Model(15, 15)
root = Tk()
root.attributes("-fullscreen", True)
empty_image = PhotoImage()

screen_width = root.winfo_screenmmwidth()-8*PAD_SIZE
screen_height = root.winfo_screenmmheight()

BUTTON_WIDTH = screen_width/4
BUTTON_HEIGHT = screen_height/3

m1 = PanedWindow(bg="black")
m1.pack(fill = BOTH, expand = 1)

mode_frame = Frame(root, bg="black")
mode_frame.pack()
m1.add(mode_frame)

mode_label = Button(mode_frame, image=empty_image, compound="center", text="Mode", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
mode_label.pack()
mode_value_label = Button(mode_frame, image=empty_image, compound="center", text=rmt_model.getMode(), height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
mode_value_label.pack()
increase_button = Button(mode_frame, image=empty_image, compound="center", text="Next", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=increment_mode, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
increase_button.pack()
decrease_button = Button(mode_frame, image=empty_image, compound="center", text="Previous", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=decrement_mode, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
decrease_button.pack()

speed_frame = Frame(root, bg="black")
speed_frame.pack()
m1.add(speed_frame)

speed_label = Button(speed_frame, image=empty_image, compound="center", text="Speed", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
speed_label.pack()
speed_value_label = Button(speed_frame, image=empty_image, compound="center", text=rmt_model.getSpeed(), height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
speed_value_label.pack()
increase_button = Button(speed_frame, image=empty_image, compound="center", text="+", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=increase_speed, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
increase_button.pack()
decrease_button = Button(speed_frame, image=empty_image, compound="center", text="-", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=decrease_speed, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
decrease_button.pack()

spin_frame = Frame(root, bg="black")
spin_frame.pack()
m1.add(spin_frame)

spin_label = Button(spin_frame, image=empty_image, compound="center", text="Spin", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
spin_label.pack()
spin_value_label = Button(spin_frame, image=empty_image, compound="center", text=rmt_model.getSpin(), height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
spin_value_label.pack()
increase_button = Button(spin_frame, image=empty_image, compound="center", text="+", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=increase_spin, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
increase_button.pack()
decrease_button = Button(spin_frame, image=empty_image, compound="center", text="-", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=decrease_spin, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
decrease_button.pack()

status_frame = Frame(root, bg="black")
status_frame.pack()
m1.add(status_frame)

status_label = Button(status_frame, image=empty_image, compound="center", text="Status", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
status_label.pack()
status_value_label = Button(status_frame, image=empty_image, compound="center", text=rmt_model.getRunning(), height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", bg='green', font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
status_value_label.pack()
play_button = Button(status_frame, image=empty_image, compound="center", text="Start", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=set_start, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
play_button.pack()
pause_button = Button(status_frame, image=empty_image, compound="center", text="Stop", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=set_stop, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
pause_button.pack()

root.mainloop()
