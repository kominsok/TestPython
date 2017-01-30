import tkinter as tk

banana = r"banana.gif"
bodercolor = [('aliceblue', '#F0F8FF'), ('blue', '#0000FF'), ('beige', '#F5F5DC'),
              ('cornsilk', '#FFF8DC'), ('red', '#ff0000'), ('lightgreen', '#90EE90'),
              ]


class BgChange:
    def __init__(self,label,color):
        self.label=label
        self.color=color

    def __call__(self, event=None):
        self.label.configure(bg=self.color)


class MyWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('select bordercolor')
        f_button = tk.Frame(self)
        f_button.pack(side=tk.LEFT, padx=5, pady=1)
        self.banana = tk.PhotoImage(file="banana.gif")
        label = tk.Label(self, image=self.banana,
                         relief=tk.RAISED, bd=6)
        label.pack(side=tk.RIGHT, padx=7)

        for name, code in bodercolor:
            b = tk.Button(f_button, text=name,
                          bg=code,
                          command=BgChange(label,code)
                          )
            b.pack(fill=tk.X)

if __name__ == '__main__':
    root =tk.Tk()
    frame=MyWindow(root)
    frame.pack()
    frame.mainloop()
