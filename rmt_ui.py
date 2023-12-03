from tkinter import *

LOW_THRESHOLD = 0
HIGH_THRESHOLD = 9

BUTTON_HEIGHT = 4
BUTTON_WIDTH = 10

LABEL_HEIGHT = 2
LABEL_WIDTH = 10

VALUE_HEIGHT = 2
VALUE_WIDTH = 10

PAUSED = 0
PLAYING = 1

def increase_mode():
    global mode, mode_value_label
    if mode < HIGH_THRESHOLD:
        mode += 1
        mode_value_label.configure(text=mode)


def decrease_mode():
    global mode, mode_value_label
    if mode > LOW_THRESHOLD:
        mode -= 1
        mode_value_label.configure(text=mode)


def increase_speed():
    global speed, speed_value_label
    if speed < HIGH_THRESHOLD:
        speed += 1
        speed_value_label.configure(text=speed)


def decrease_speed():
    global speed, speed_value_label
    if speed > LOW_THRESHOLD:
        speed -= 1
        speed_value_label.configure(text=speed)


def increase_spin():
    global spin, spin_value_label
    if spin < HIGH_THRESHOLD:
        spin += 1
        spin_value_label.configure(text=spin)


def decrease_spin():
    global spin, spin_value_label
    if spin > LOW_THRESHOLD:
        spin -= 1
        spin_value_label.configure(text=spin)


def set_play():
    global status, status_value_label
    status = PLAYING
    status_value_label.configure(text=get_status(status))


def set_pause():
    global status, status_value_label
    status = PAUSED
    status_value_label.configure(text=get_status(status))


def get_status(status):
    if status == PLAYING:
        return "Playing"
    else:
        return "Paused"


root = Tk()
mode = 0
speed = 0
spin = 0
status = "Paused"

m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 1)

mode_frame = Frame(root)
mode_frame.pack()
m1.add(mode_frame)

mode_label = Label(mode_frame, text="Mode", height=LABEL_HEIGHT, width=LABEL_WIDTH)
mode_label.pack()
mode_value_label = Label(mode_frame, text=mode, height=VALUE_HEIGHT, width=VALUE_WIDTH)
mode_value_label.pack()
increase_button = Button(mode_frame, text="+", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=increase_mode)
increase_button.pack()
decrease_button = Button(mode_frame, text="-", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=decrease_mode)
decrease_button.pack()

speed_frame = Frame(root)
speed_frame.pack()
m1.add(speed_frame)

speed_label = Label(speed_frame, text="Speed", height=LABEL_HEIGHT, width=LABEL_WIDTH)
speed_label.pack()
speed_value_label = Label(speed_frame, text=speed, height=VALUE_HEIGHT, width=VALUE_WIDTH)
speed_value_label.pack()
increase_button = Button(speed_frame, text="+", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=increase_speed)
increase_button.pack()
decrease_button = Button(speed_frame, text="-", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=decrease_speed)
decrease_button.pack()

spin_frame = Frame(root)
spin_frame.pack()
m1.add(spin_frame)

spin_label = Label(spin_frame, text="Spin", height=LABEL_HEIGHT, width=LABEL_WIDTH)
spin_label.pack()
spin_value_label = Label(spin_frame, text=spin, height=VALUE_HEIGHT, width=VALUE_WIDTH)
spin_value_label.pack()
increase_button = Button(spin_frame, text="+", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=increase_spin)
increase_button.pack()
decrease_button = Button(spin_frame, text="-", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=decrease_spin)
decrease_button.pack()

status_frame = Frame(root)
status_frame.pack()
m1.add(status_frame)

status_label = Label(status_frame, text="Status", height=LABEL_HEIGHT, width=LABEL_WIDTH)
status_label.pack()
status_value_label = Label(status_frame, text=status, height=VALUE_HEIGHT, width=VALUE_WIDTH)
status_value_label.pack()
play_button = Button(status_frame, text="Play", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=set_play)
play_button.pack()
pause_button = Button(status_frame, text="Pause", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, command=set_pause)
pause_button.pack()

root.mainloop()
