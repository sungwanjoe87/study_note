# 1. 찾는 사람 검색
# 2. 찾는 사람 삭제


students=[ 
          [1,'홍길동',100,100,200,100,100.0,0],
          [2,'이순신',100,100,200,100,100.0,0],
          [3,'유관순',100,100,200,100,100.0,0],
          [4,'김유신',100,100,200,100,100.0,0],
          [5,'김구',100,100,200,100,100.0,0]
          ]




while True:
    print('1번: 찾는 사람 검색')
    print('2번: 찾는 사람 삭제')
    
    choice = int(input('원하는 숫자를 입력하세요'))
    chk=0
    
    if choice ==1:
        chkName = input('찾는 학생의 이름을 입력하세요>>')
        for stu in students: #리스트 형태임
            if chkName in stu:     
                print(stu)
                print()
                chk=1   
                break
        if chk==0:
            print('찾는 학생이 없습니다. 다시 입력해 주세요')         
        
                           
    elif choice ==2:     
        chkname = input('삭제할 이름을 입력하세요>>')
        for idx,stu in enumerate(students):
            if chkname in stu:
                del(students[idx])       
                print(students)
                chk=1
                break
        if chk==0:
            print('삭제하라는 학생이 없습니다. 다시 입력하세요.')