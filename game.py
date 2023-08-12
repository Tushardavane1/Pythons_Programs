import tkinter as tk

def change_color(color):
    root.configure(bg=color)

def main():
    global root
    root = tk.Tk()
    root.title("Color Screen")
    root.geometry("400x300")

    red_button = tk.Button(root, text="Red", command=lambda: change_color("red"))
    red_button.pack(side=tk.LEFT)

    green_button = tk.Button(root, text="Green", command=lambda: change_color("green"))
    green_button.pack(side=tk.LEFT)

    blue_button = tk.Button(root, text="Blue", command=lambda: change_color("blue"))
    blue_button.pack(side=tk.LEFT)

    root.mainloop()

if __name__ == "__main__":
    main()
