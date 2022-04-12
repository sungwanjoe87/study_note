# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성

# stuSave = [[0]*7 for i in range(0)]



stuSave = []
# print(stuSave)
# 학생가입인원 확인count
sCount = 0
while True:
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력') 
    print('5. 학생검색출력') 
    print('6. 등수처리')    
    print('0. 프로그램종료')     
    print('-'*25)

    choice = input('원하는 번호를 선택하세요>>')
    
    if not choice.isdigit(): #choice가 숫자가 맞는지 확인 하는 문법
        print('숫자만 가능합니다.')
        continue
    
    choice = int(choice)
    
    count =0
    if choice ==1:
        print('1.학생성적 입력을 선택하셨습니다.')
        print('--{}번째 학생 등록---'.format(sCount+1))
        sname = input('이름을 입력하세요>>')
        kor = int(input('국어 점수를 입력하세요>>'))
        eng = int(input('영어 점수를 입력하세요>>'))
        total = kor+eng
        avg = total/2
        rank = 0
        temp = {'stuno':sCount, 'name':sname, 'kor':kor,'eng':eng, 'total':total, 'avg':avg, 'rank':rank}
        stuSave.append(temp) #stuSave
        sCount +=1
        
    elif choice ==2:
        print('학생성적 수정 페이지.')
        count =0
        searchName = input('수정할 학생의 이름을 입력하세요...')
        for i,stu in enumerate(stuSave):
            if searchName in stu.values:
                print('학생의 이름이 있습니다.')
                print('1. 국어점수')
                print('2. 영어점수')
                print('0. 상위메뉴로 이동')
                searchNo = input('수정을 원하는 과목을 입력하세요')
                if searchNo ==1:
                    korin=int('1.국어 점수를 수정하겠습니다. 수정할 점수를 넣으세요...')
                    stu['kor'] = korin #기존 국어 점수를 korin으로 치환
                    stu['total'] = kor+eng
                    stu['avg'] = kor+eng/2
                    
                    print('국어점수가 변경되었습니다.')
                    
                elif searchNo ==2:
                    engin=int('2.영어 점수를 수정하겠습니다. 수정할 점수를 넣으세요...')
                    stu['eng'] = engin
                    stu['total'] = kor+eng
                    stu['avg'] = kor+eng/2
                
                    print('영어점수가 변경되었습니다.')
                    
                elif searchNo ==0:
                    print('0을 선택하여 상위메뉴로 돌아갑니다.')
                count =1
                    
    elif choice ==3:
        print('학생성적 삭제을 선택하셨습니다.')
        input1= input('삭제할 학생의 이름을 입력하세요...')
        chcount = 0
        for i,stu in enumerate(stuSave):
            if input1 in stu.values:
                print('{} 학생이 검색되었습니다.' .format(input1))
                del(stuSave[i])
                print('{} 학생이 삭제되었습니다.'.format(input1))
                chcount =1
            else:
                print('입력한 학생이 없습니다.')
                chcount =0
                break
            
                
    elif choice ==4:
        print('학생성적 전체출력을 선택하셨습니다.')
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
        print('-'*50)
        for stu in stuSave:
            for keys,values in stu.items():
                print( '{}\t'.format(values),end='')
            print()
    
    
    elif choice ==5:
        print('학생성적 검색출력을 선택하셨습니다..')
        search_stu = ('찾으시는 학생의 이름을 입력하세요')
        
        for i,stu in enumerate(stuSave):
            if search_stu in stu:
                print('번호', '이름', '국어', '합계', '평균', '등수')
        
    elif choice ==0:
        print('프로그램을 종료합니다...')
        break
        
            