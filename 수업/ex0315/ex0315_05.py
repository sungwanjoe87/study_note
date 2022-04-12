#학생검색 삭제

students=[ 
          [1,'홍길동',100,100,200,100,100.0,0],
          [2,'이순신',100,100,200,100,100.0,0],
          [3,'유관순',100,100,200,100,100.0,0],
          [4,'김유신',100,100,200,100,100.0,0],
          [5,'김구',100,100,200,100,100.0,0]
          ]

while True:
    chkName = input('삭제할 학생의 이름을 입력하세요>>')
    #리스트안에 있는 학생의 각 
    for idx,stu in enumerate(students): #리스트 형태임 idx는 0부터 시작함!
        if chkName in stu:
            del(students[idx])
            break
    print(students)