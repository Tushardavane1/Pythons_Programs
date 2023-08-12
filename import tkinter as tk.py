import tkinter as tk

def change_color():
    colors = ["red", "green", "blue", "yellow", "orange"]
    color = colors[counter % len(colors)]
    counter += 1
    label.config(text=f"Selected Color: {color}", fg=color)

counter = 1

root = tk.Tk()
root.title("Colorful GUI")
root.geometry("300x200")

label = tk.Label(root, text="Selected Color:", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Change Color", font=("Arial", 14), command=change_color)
button.pack()

root.mainloop()
