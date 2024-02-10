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
   count_min = math.floor(count / 60)
   count_sec = count % 60
   if count_sec < 10:
       count_sec = f"0{count_sec}"

   canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
   if count > 0:
       window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
label_timer = Label(text="TİMER", font=("bold", 25), foreground=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

tomato = PhotoImage(file="tomato.png")
canvas.create_image((100, 112), image=tomato)
timer_text = canvas.create_text((100, 130), text="00:00", font=("bold", 25), fill="white")
canvas.grid(row=1, column=1)


check_marks = Label(text="✔", bg=YELLOW, fg=GREEN, font=25)
check_marks.grid(row=3, column=1)

def action():
    pass


button_start = Button(text="Start", command=start_timer, font=("bold", 13))
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=action, font=("bold", 13))
button_reset.grid(row=2, column=2)

window.mainloop()