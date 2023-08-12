import tkinter as tk
import random

class GunGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gun Game")
        self.master.geometry("400x300")

        self.target = random.randint(1, 10)
        self.bullets = 6

        self.title_label = tk.Label(self.master, text="Gun Shooting Game")
        self.title_label.pack()

        self.target_label = tk.Label(self.master, text="Target: -")
        self.target_label.pack()

        self.bullets_label = tk.Label(self.master, text="Bullets: -")
        self.bullets_label.pack()

        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack()

        self.guess_label = tk.Label(self.input_frame, text="Guess:")
        self.guess_label.pack(side=tk.LEFT)

        self.guess_entry = tk.Entry(self.input_frame)
        self.guess_entry.pack(side=tk.LEFT)

        self.shoot_button = tk.Button(self.master, text="Shoot", command=self.shoot)
        self.shoot_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.update_labels()

    def shoot(self):
        guess = self.guess_entry.get()
        if guess.isdigit():
            guess = int(guess)
            if guess < 1 or guess > 10:
                self.result_label.configure(text="Please enter a number between 1 and 10.")
            else:
                if guess == self.target:
                    self.result_label.configure(text="Congratulations! You shot the target!")
                elif self.bullets == 0:
                    self.result_label.configure(text="Oops! You ran out of bullets. Game over!")
                else:
                    self.result_label.configure(text="Missed the target!")
                    self.bullets -= 1

                self.update_labels()
        else:
            self.result_label.configure(text="Please enter a valid number.")

    def update_labels(self):
        self.target_label.configure(text=f"Target: {self.target}")
        self.bullets_label.configure(text=f"Bullets: {self.bullets}")

def main():
    root = tk.Tk()
    game_gui = GunGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
