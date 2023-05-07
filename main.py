import tkinter as tk
from typing import Any


def fahrenheit_to_celsius() -> Any:
    temperature = float(entry.get()) if not(entry.get() == '') else 0
    lbl["text"] = f"temperature: {(temperature - 32) * (5 / 9)}°C" if not(temperature == 0) else "temperature"


def celsius_to_fahrenheit() -> Any:
    temperature = float(entry.get()) if not (entry.get() == '') else 0
    lbl["text"] = f"temperature: {(temperature * 9 / 5) + 32}°F" if not (temperature == 0) else "temperature"

window = tk.Tk()
window.title("Temperature converter")
window.geometry("800x600")
window.update()
frame = tk.Frame(
    master=window,
    bg="cyan"
)
frame.pack(fill=tk.X)

lbl = tk.Label(
    master=frame,
    fg="magenta",
    text="convert to celsius or fahrenheit",
    font=("Arial bold", 20)
)
lbl.pack(padx=20, pady=40)

input_frame = tk.Frame(
    master=window,
    height=220,
    bg="darkcyan"
)
input_frame.pack(fill=tk.BOTH, pady=20, expand=True)

lbl = tk.Label(
    master=input_frame,
    font=("Arial bold", 30),
    text="temperature:",
    fg="white",
    background="darkcyan"
)
lbl.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

entry = tk.Entry(
    master=input_frame,
    fg="black",
    font=("Arial bold", 30),
    bg="white",
    width=10
)
entry.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

celsius_btn = tk.Button(
    master=input_frame,
    fg="wheat",
    background="green",
    font=("Arial bold",20),
    text="convert to celsius",
    command=fahrenheit_to_celsius
)
celsius_btn.place(relx=0, rely=1, anchor=tk.SW)
fahrenheit_btn = tk.Button(
master=input_frame,
    fg="wheat",
    background="green",
    font=("Arial bold",20),
    text="convert to fahrenheit",
    command=celsius_to_fahrenheit
)
fahrenheit_btn.place(relx=1, rely=1, anchor=tk.SE)

window.mainloop()