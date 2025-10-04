import tkinter as tk


class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator App")
        self.root.geometry("450x600")
        self.root.resizable(width=False,height =False)
        self.root.configure(bg="#fbf8ef")

        self.entry = tk.Entry(self.root,font=("Arial",30),relief="ridge")
        self.entry.pack(fill="x", padx=20 , pady = 20)

        self.frameButton = tk.Frame(self.root,bg="#fbf8ef")
        self.frameButton.pack()

        self.clearBtn = tk.Button(self.frameButton , text="C" , font = ("Arial",20) , fg = "white" , bg="#a7aae1",width=5 , height=1,command = self.clear)
        self.clearBtn.grid(column=0 , row=0)
        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
            ]
        self.displayButtons()
    def evaluation(self,value):
        if value == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END,"Error")
                self.entry.configure(fg="#d0e2ff")
        else:
            self.entry.insert(tk.END,value)

    def clear(self):
        self.entry.delete(0,tk.END)

    def displayButtons(self):
        for i,row in enumerate(self.buttons):
            for j , label in enumerate(row):
                btn = tk.Button(self.frameButton , text = label , font = ("Arial",18),width=5,height=2 , relief="flat",bg="#a7aae1",fg="#696fc7",command=lambda val=label: self.evaluation(val))
                btn.grid(row=i+1,column=j,padx=5,pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
    