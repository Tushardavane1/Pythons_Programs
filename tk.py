import tkinter

class MyApp:
    def __init__(self, parent):
        self.root = parent
        self.root.geometry("400x400")
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        self.root.after(3000, self.delayed)
        tkinter.Button(padx=20,pady=20,text="fetch")
    def delayed(self):
        print('I was delayed')

if __name__ == "__main__":
    root = tkinter.Tk()
    app = MyApp(root)
    root.mainloop()