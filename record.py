from tkinter import *
import sqlite3

def main():
    root = Tk()
    root.title("Loading Python Game")
    root.geometry("480x640")
    # root.option_add("*Font","맑은고딕 25")
    root.configure(bg="black")
    label = Label(root, text="Loading Python Game", fg="white", bg="black", font=("font", 30, "bold"))
    label.place(x=30, y=30)
    root.mainloop()
def database():
    arr = list()
    con = sqlite3.connect("snowScore.db")
    cur = con.cursor()
    cur.execute('select * from snowScore')
    rs = cur.fetchall()
    for point in rs:
        arr.append(point)
    con.close()
    print(arr)
if __name__ == "__main__":
    main()



