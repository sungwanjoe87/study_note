# 1. lotto 맟추기.
# 2. 학생 성적입력프로그램.


#.번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수 - 10명의 학생입력 공간 생성
stusave = []
stusaves =[]
#.학생인원 확인 count
sCount = 0
while True:
    print ('[학생성적 프로그램]')
    print ('_'*25)
    print ('1.학생성적입력')
    print ('2.학생성적수정')
    print ('3.학생성적삭제')
    print ('4.학생성적전체출력')
    print ('5.학생성적검색')
    print ('0.프로그램종료')
    
    print ('-'*25)
    choice =int(input ('원하는 번호를 입력하세요>>'))
    
    if choice==1:
        print('학생성적 입력을 선택하셨습니다.')
        print('--{}번째 학생등록--' .format(sCount+1))
        sName = input('학생이름을 입력하세요>>')
        kor = int(input('국어점수를 입력하세요>>'))
        eng = int(input('영어점수를 입력하세요>>'))
        math = int(input('수학점수를 입력하세요>>'))
        stusave[sCount][0] = sCount+1 #학생번호 입력.
        stusave[sCount][1] = sName
        stusave[sCount][2] = kor
        stusave[sCount][3] = eng
        stusave[sCount][4] = math
        stusave[sCount][5] = kor+eng+math
        stusave[sCount][6] = (kor+eng)/3 #float
        sCount +=1 #학생인원 1명 증가.
        stusaves.append(stusave)
        print(stusaves)
        print('학생성적이 저장되었습니다.')
    elif choice==2:
        print('학생성적 수정을 선택하셨습니다.')
    elif choice==3:
        print('학생성적 삭제를 선택하셨습니다.')
        a=int(print('삭제할 학생의 번호를 입력하세요'))
    elif choice==4:
        print('학생성적 전체 출력을 선택하셨습니다.')
        print(stusaves)
    elif choice==5:
        print('학생성적 검색을 선택하셨습니다.')
        a= int(input('원하는 번호를 선택하세요'))
        if a in 3[0]:
            pass
    elif choice==0:
        print('프로그램을 종료합니다...')
        break