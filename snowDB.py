import sqlite3
'''https://www.youtube.com/watch?v=AKSXM2BTwfY'''
# 테이블 만들기
# def createTable():
#     con = sqlite3.connect("snowScore.db")
#     cur = con.cursor()
#     cur.execute('''
#         create table snowScore(
#         point integer)
#     ''')
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     createTable()

# insert
def insert():
    con = sqlite3.connect("snowScore.db")
    cur = con.cursor()
    cur.execute("insert into snowScore values(5)")
    con.commit()
    con.close()
if __name__ == '__main__':
    insert()

# 출력
# def printS():
#     con = sqlite3.connect("snowScore.db")
#     cur = con.cursor()
#     cur.execute('select * from snowScore')
#     print('[1] 전체 데이터 출력')
#     rs = cur.fetchall()
#     for point in rs:
#         print(point)
#     con.close()
# if __name__ == '__main__':
#     printS()