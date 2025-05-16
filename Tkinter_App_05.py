import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to My Python App!")
label.pack(pady=20)

root.mainloop()
