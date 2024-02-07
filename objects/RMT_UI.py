from tkinter import *
from objects.Mode import Mode
from utils.rmt_utils import *

LOW_THRESHOLD_MODE = Mode.getValues()[0]
HIGH_THRESHOLD_MODE = Mode.getValues()[len(Mode.getValues())-1]

LOW_THRESHOLD = 0
HIGH_THRESHOLD = 9

STOPPED = 0
RUNNING = 1

FONT_SIZE = 10
PAD_SIZE = 2


class RMT_UI(object):

    def __init__(self, model):
        self.input = None
        self.mode = model.getMode()
        self.speed = model.getSpeed()
        self.spin = model.getSpin()
        self.status = model.getRunning()
        self.initRoot()
        children = list(self.root.children.values())
        print(children[1])
        # self.root.update()


    def updateView(self, model):
        self.mode = model.getMode()
        self.speed = model.getSpeed()
        self.spin = model.getSpin()
        self.status = model.getRunning()
        children = self.root.children.values()
        print(children)
        self.root.update()


    def getRoot(self):
        return self.root


    def initRoot(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        empty_image = PhotoImage()

        screen_width = self.root.winfo_screenmmwidth()-8*PAD_SIZE
        screen_height = self.root.winfo_screenmmheight()

        BUTTON_WIDTH = screen_width/4
        BUTTON_HEIGHT = screen_height/3

        m1 = PanedWindow(bg="black")
        m1.pack(fill = BOTH, expand = 1)

        mode_frame = Frame(self.root, bg="black")
        mode_frame.pack()
        m1.add(mode_frame)

        mode_label = Button(mode_frame, image=empty_image, compound="center", text="Mode", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        mode_label.pack()
        mode_value_label = Button(mode_frame, image=empty_image, compound="center", text=Mode.getModeString(self.mode), height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        mode_value_label.pack()
        increase_button = Button(mode_frame, image=empty_image, compound="center", text="Next", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.increment_mode, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        increase_button.pack()
        decrease_button = Button(mode_frame, image=empty_image, compound="center", text="Previous", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.decrement_mode, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        decrease_button.pack()

        speed_frame = Frame(self.root, bg="black")
        speed_frame.pack()
        m1.add(speed_frame)

        speed_label = Button(speed_frame, image=empty_image, compound="center", text="Speed", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        speed_label.pack()
        speed_value_label = Button(speed_frame, image=empty_image, compound="center", text=self.speed, height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        speed_value_label.pack()
        increase_button = Button(speed_frame, image=empty_image, compound="center", text="+", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.increase_speed, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        increase_button.pack()
        decrease_button = Button(speed_frame, image=empty_image, compound="center", text="-", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.decrease_speed, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        decrease_button.pack()

        spin_frame = Frame(self.root, bg="black")
        spin_frame.pack()
        m1.add(spin_frame)

        spin_label = Button(spin_frame, image=empty_image, compound="center", text="Spin", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        spin_label.pack()
        spin_value_label = Button(spin_frame, image=empty_image, compound="center", text=self.spin, height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        spin_value_label.pack()
        increase_button = Button(spin_frame, image=empty_image, compound="center", text="+", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.increase_spin, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        increase_button.pack()
        decrease_button = Button(spin_frame, image=empty_image, compound="center", text="-", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.decrease_spin, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        decrease_button.pack()

        status_frame = Frame(self.root, bg="black")
        status_frame.pack()
        m1.add(status_frame)

        status_label = Button(status_frame, image=empty_image, compound="center", text="Status", height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        status_label.pack()
        status_value_label = Button(status_frame, image=empty_image, compound="center", text=self.status, height=f"{BUTTON_HEIGHT/2}m", width=f"{BUTTON_WIDTH}m", bg='green', font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        status_value_label.pack()
        play_button = Button(status_frame, image=empty_image, compound="center", text="Start", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.set_start, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        play_button.pack()
        pause_button = Button(status_frame, image=empty_image, compound="center", text="Stop", height=f"{BUTTON_HEIGHT}m", width=f"{BUTTON_WIDTH}m", command=self.set_stop, font=('Arial', FONT_SIZE), padx=f"{PAD_SIZE}m", pady=f"{PAD_SIZE}m")
        pause_button.pack()

    
    def increase_speed(self):
        print("Setting Increase Speed")
        self.input = INCREASE_SPEED

    def decrease_speed(self):
        self.input = DECREASE_SPEED

    def increase_spin(self):
        self.input = INCREASE_SPIN

    def decrease_spin(self):
        self.input = DECREASE_SPIN

    def increment_mode(self):
        self.input = INCREMENT_MODE

    def decrement_mode(self):
        self.input = DECREMENT_MODE

    def set_start(self):
        self.input = START_MODE

    def set_stop(self):
        self.input = STOP_MODE

    def getInput(self):
        return self.input
