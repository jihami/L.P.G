from tkinter import *


def main():
    root = Tk()
    root.title("Loading Python Game")
    root.geometry("480x640")
    # root.option_add("*Font","맑은고딕 25")
    root.configure(bg="black")

    label = Label(root, text="Loading Python Game", fg="white", bg="black", font=("font", 30, "bold"))
    label.place(x=30, y=90)

    btn1 = Button(root, text="Avoid Snow", fg="black", bg="white", font=("font", 20, "bold"),command=advoidSnow)
    btn2 = Button(root, text="Brick Breaker", fg="black", bg="white", font=("font", 20, "bold"),command=brickBreaker)
    btn3 = Button(root, text="Record", fg="black", bg="white", font=("font", 20, "bold"),command=record)

    btn1.place(x=150, y=230)
    btn2.place(x=140, y=330)
    btn3.place(x=180, y=430)
    root.mainloop()
def advoidSnow():
    import avoidSnow
    avoidSnow
def brickBreaker():
    # import brickBreaker
    # brickBreaker
    pass
def record():
    pass
if __name__ == "__main__":
    main()



