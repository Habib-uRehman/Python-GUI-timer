# from tkinter import *
#
# window = Tk()
# window.title("GUI Interface")
# window.minsize(width=500, height=300)
#
# my_label = Label(text="this is text", font = ("New Times Roman",24))
# my_label.pack()
#
# #Button
# def on_click():
#     # my_label["text"] ="I am clicked"
#     t = input.get()
#     my_label.config(text=t)
# bt = Button(text="Click",command=on_click)
# bt.pack()
#
# # Entry (used to print text feild)
#
# input = Entry(width=15)
# input.pack()
#
#
#
#
#
#
#
#
# window.mainloop()

# Day 28

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    my_label2.config(text="")
    my_label.config(text="Timer")
    canvas.itemconfig(canvas_text,text="00:00")
    global reps

# ---------------------------- TIMER MECHANISM ------------------------------- #
def time_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED, font=(FONT_NAME, 20, "normal"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK, font=(FONT_NAME,20,"normal"))
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN, font=(FONT_NAME,20,"normal"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer= window.after(1000,count_down,count-1)
    else:
        time_start()
        tick = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            tick += "✔"
        my_label2.config(text=tick)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx = 100, pady= 100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness = 0)
t_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=t_image)

canvas_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,25,"bold"))


start_bt = Button(text="Start",highlightthickness=0, command=time_start)
end_bt = Button(text="Reset",highlightthickness=0, command=reset_time)

canvas.grid(column = 2, row=2)

my_label = Label(text="Timer", bg=YELLOW,fg= GREEN,font=(FONT_NAME,30,"normal"))
my_label.grid(column=2, row=1)
my_label2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,"bold"))
my_label2.grid(column=2, row=4)
start_bt.grid(column = 0, row=3)
end_bt.grid(column = 3, row=3)






window.mainloop()