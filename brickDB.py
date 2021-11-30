import sqlite3
'''https://www.youtube.com/watch?v=AKSXM2BTwfY'''
# 테이블 만들기
# def createTable():
#     con = sqlite3.connect("brickScore.db")
#     cur = con.cursor()
#     cur.execute('''
#         create table brickScore(
#         date text,
#         point integer)
#     ''')
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     createTable()

# insert
# def insert():
#     con = sqlite3.connect("brickScore.db")
#     cur = con.cursor()
#     cur.execute("insert into brickScore values('21/08/21',100)")
#     con.commit()
#     con.close()
# if __name__ == '__main__':
#     insert()

# 출력
# def printS():
#     con = sqlite3.connect("brickScore.db")
#     cur = con.cursor()
#     cur.execute('select * from brickScore')
#     print('[1] 전체 데이터 출력')
#     rs = cur.fetchall()
#     for point in rs:
#         print(point)
#     con.close()
# if __name__ == '__main__':
#     printS()