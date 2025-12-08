from tkinter import *
from tkinter import messagebox
import random
import winsound

root = Tk()
root.title("Starter")
root.geometry("250x120")

# --------------------------------------------
# FUNCTIONS FOR SPECIAL EFFECTS
# --------------------------------------------

def shake_window(win):
    """Shake effect (small movements)."""
    def shake():
        try:
            x = win.winfo_x()
            y = win.winfo_y()
            win.geometry(f"+{x + random.randint(-5, 5)}+{y + random.randint(-5, 5)}")
            win.after(10, shake)
        except:
            pass
    shake()

def bounce_window(win):
    """Bounce effect around the screen."""
    xs, ys = random.choice([3, -3]), random.choice([3, -3])

    def move():
        nonlocal xs, ys
        try:
            x, y = win.winfo_x(), win.winfo_y()
            w, h = 200, 100
            sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()

            if x <= 0 or x + w >= sw: xs = -xs
            if y <= 0 or y + h >= sh: ys = -ys

            win.geometry(f"+{x + xs}+{y + ys}")
            win.after(5, move)
        except:
            pass
    move()

def random_color(win):
    """Change BG color randomly forever."""
    def change():
        try:
            colors = ["red", "yellow", "orange", "purple", "green", "blue", "pink"]
            win.config(bg=random.choice(colors))
            win.after(10, change)
        except:
            pass
    change()

# --------------------------------------------
# SPAWN WINDOWS ONE BY ONE
# --------------------------------------------

def spawn_window(i):
    """Spawn one special window with random effects."""
    win = Toplevel()
    win.title("Error!")
    win.geometry("200x100")

    # random starting position
    x = random.randint(0, root.winfo_screenwidth() - 200)
    y = random.randint(0, root.winfo_screenheight() - 100)
    win.geometry(f"200x100+{x}+{y}")

    # Play Windows beep
    winsound.MessageBeep()

    # Label + close button
    Label(win, text="Something went wrong!",
          fg="red", bg=win["bg"],
          font=("Arial", 12)).pack(pady=10)

    Button(win, text="Close", command=win.destroy).pack()

    # Randomly choose effects
    effects = []
    if random.random() < 0.4: effects.append("shake")
    if random.random() < 0.4: effects.append("bounce")
    if random.random() < 0.4: effects.append("color")

    # Apply chosen effects
    if "shake" in effects: shake_window(win)
    if "bounce" in effects: bounce_window(win)
    if "color" in effects: random_color(win)

def spawn_slowly(count=5, delay=600):
    """Spawn several windows one by one with delay."""
    for i in range(count):
        root.after(i * delay, lambda i=i: spawn_window(i))

# --------------------------------------------
# MAIN BUTTON
# --------------------------------------------

def go():
    answer = messagebox.askyesno("Confirm", "Continue?")
    if answer:
        spawn_slowly(50, 10)  # 5 windows, 700ms delay

Button(root, text="Click Me", font=("Arial", 14), command=go).pack(expand=True)

root.mainloop()
