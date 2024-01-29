from tkinter import *
from tkinter import messagebox
from objects.Mode import Mode

LOW_THRESHOLD_MODE = Mode.getValues()[0]
HIGH_THRESHOLD_MODE = Mode.getValues()[len(Mode.getValues())-1]

LOW_THRESHOLD = 0
HIGH_THRESHOLD = 9

STOPPED = 0
RUNNING = 1

FONT_SIZE = 10
PAD_SIZE = 2

def increase_mode():
    global mode, mode_value_label
    if mode < HIGH_THRESHOLD_MODE:
        mode += 1
        mode_value_label.configure(text=Mode.getModeString(mode))


def decrease_mode():
    global mode, mode_value_label
    if mode > LOW_THRESHOLD_MODE:
        mode -= 1
        mode_value_label.configure(text=Mode.getModeString(mode))


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


def set_start():
    global status, status_value_label
    status = RUNNING
    status_value_label.configure(text=get_status(status), bg='red')


def set_stop():
    global status, status_value_label
    status = STOPPED
    status_value_label.configure(text=get_status(status), bg='green')


def get_status(status):
    if status == RUNNING:
        return "Running"
    else:
        return "Stopped"


root = Tk()
root.attributes("-fullscreen", True)
mode = 0
speed = 0
spin = 0
status = "Stopped"
empty_image = PhotoImage()
running = True

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
mode_value_label = Button(mode_frame, image=empty_image, compound="center", text=Mode.getModeString(mode), height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
mode_value_label.pack()
increase_button = Button(mode_frame, image=empty_image, compound="center", text="Next", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=increase_mode, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
increase_button.pack()
decrease_button = Button(mode_frame, image=empty_image, compound="center", text="Previous", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=decrease_mode, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
decrease_button.pack()

speed_frame = Frame(root, bg="black")
speed_frame.pack()
m1.add(speed_frame)

speed_label = Button(speed_frame, image=empty_image, compound="center", text="Speed", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
speed_label.pack()
speed_value_label = Button(speed_frame, image=empty_image, compound="center", text=speed, height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
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
spin_value_label = Button(spin_frame, image=empty_image, compound="center", text=spin, height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
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
status_value_label = Button(status_frame, image=empty_image, compound="center", text=status, height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", bg='green', font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
status_value_label.pack()
play_button = Button(status_frame, image=empty_image, compound="center", text="Start", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=set_start, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
play_button.pack()
pause_button = Button(status_frame, image=empty_image, compound="center", text="Stop", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=set_stop, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
pause_button.pack()

root.mainloop()
