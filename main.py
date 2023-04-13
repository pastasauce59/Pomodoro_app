from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If its the 1st/3rd/5th/7th rep:
    if reps % 2 !=  0:
        count_down(work_sec)
    # #If its the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
    # #if its the 2nd/4th/6th rep:
    if reps % 2 == 0:
        count_down(short_break_sec)
    

    print(reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'


    if count > 0:
        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(bg=YELLOW, fg=GREEN)
timer_label.config(text='Timer', font=(FONT_NAME, 35, 'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(highlightbackground=YELLOW, command=start_timer)
start_button.config(text='Start')
start_button.grid(column=0, row=2)

reset_button = Button(highlightbackground=YELLOW)
reset_button.config(text='Reset')
reset_button.grid(column=2, row=2)

checkmark_label = Label(bg=YELLOW)
checkmark_label.config(text='✅')
checkmark_label.grid(column=1, row=3)

window.mainloop()