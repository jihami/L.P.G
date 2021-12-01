import sqlite3
# 테이블 만들기
# def createTable():
#     con = sqlite3.connect("brickScore.db")
#     cur = con.cursor()
#     cur.execute('''
#         create table brickScore(
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
#     cur.execute("insert into brickScore values(100)")
#     cur.execute("insert into brickScore values(?)", (score,)) #변수 하나 입력
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