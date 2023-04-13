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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minute = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'


    if count > 0:
        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
        window.after(1000, count_down, count - 1)

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