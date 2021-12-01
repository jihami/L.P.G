from tkinter import *
import tkinter.ttk
import sqlite3

def main():
    root = Tk()
    root.title("Loading Python Game")
    root.geometry("480x640")
    root.configure(bg="black")
    label = Label(root, text="Loading Python Game", fg="white", bg="black", font=("font", 30, "bold"))
    label.place(x=30, y=60)

    conS = sqlite3.connect("snowScore.db")
    curS = conS.cursor()
    curS.execute('select * from snowScore')
    arrS = list()
    rs = curS.fetchall()
    for point in rs:
        arrS.append(point)
    conS.close()

    conB = sqlite3.connect("brickScore.db")
    curB = conB.cursor()
    curB.execute('select * from brickScore')
    arrB = list()
    rsb = curB.fetchall()
    for point in rsb:
        arrB.append(point)
    conB.close()


    treeview = tkinter.ttk.Treeview(root, columns=["snow","brick"], displaycolumns=["snow","brick"],height=20)
    treeview.place(x=180/2,y=150)
    treeview.column("#0",width=100,anchor="center")
    treeview.heading("#0", text="index", anchor="center")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("snow", text="Avoid Snow", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("brick", text="Brick Breaker", anchor="center")

    treeview.insert('', 'end', text="최고점수", values=(max(arrS), max(arrB)))
    if len(arrS) > len(arrB):
        while True:
            if len(arrS) == len(arrB):
                break
            else:
                arrB.append("")
    for i in range(len(arrS)):
        treeview.insert('', 'end', text=i+1, values=(arrS[i],arrB[i]))
    print(len(arrS))
    print(len(arrB))
    print(arrB)

    root.mainloop()

if __name__ == "__main__":
    main()
