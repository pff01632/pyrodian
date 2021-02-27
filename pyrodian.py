import tkinter as tk

def create_frame():
    frame = tk.Tk()
    frame.title("Parodian by python3: Pyrodian V1.00")
    frame.geometry("480x640")
    frame.resizable(False, False)
    return  frame

def main():
    root = create_frame()
    root.mainloop()

if __name__ == "__main__":
    main()
