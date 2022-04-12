#화면구성
#1.학생성적입력
#2.학생성적수정
#3.학생성적삭제
#0.프로그램종료

#1.학생성적입력
# [번호,학생이름,국어성적,영어성적,수학성적,합계,평균,등수]

stusave = []
sCount = 0

while True:
    print('[학생성적 프로그램]')
    print('='*25)
    print('1.학생성적입력')
    print('2.학생성적수정')
    print('3.학생성적삭제')
    print('4.학생성적전체출력')
    print('5.학생성적검색')
    print('0.프로그램종료')
    print('='*25)
    
    choice = int(input('원하는 번호를 입력하세요.'))
    
    if choice == 1:
        for i in range(3):
            print('1.학생성적 입력을 선택하셨습니다')
            print('---{}번 학생의 성적을 등록합니다.---' .format(sCount+1))
            sName = input('학생의 이름을 입력하세요>>')
            kor = int(input('국어성적을 입력하세요>>'))
            eng = int(input('영어성적을 입력하세요>>'))
            math =int(input('수학성적을 입력하세요>>'))
            sum = kor+eng+math
            evg = sum/3
            rank = 0
            # stusave[sCount][0] = sCount+1 #학생번호 입력.
            # stusave[sCount][1] = sName
            # stusave[sCount][2] = kor
            # stusave[sCount][3] = eng
            # stusave[sCount][4] = math
            # stusave[sCount][5] = sum
            # stusave[sCount][6] = evg #float
            # stusave[sCount][7] = rank
            temp = [sCount+1,sName,kor,eng,math,sum,evg,rank]
            stusave.append(temp)
            sCount +=1
            print('{}개의 학생 성적이 저장되었습니다. ' .format(sCount))
            print(stusave)
        else:
            continue
    elif choice == 2:
        print('2.학생성적 수정을 선택하셨습니다.')
        
    elif choice == 3:
        print('3.학생성적 삭제를 선택하셨습니다.')
        
    elif choice == 4:
        print('4.학생성적 전체 출력을 선택하셨습니다.')
        print(stusave)
    elif choice == 5:
        print('5.학생성적 검색을 선택하셨습니다.')    
    
    elif choice == 0:
        print('프로그램을 종료합니다...')
    
        break