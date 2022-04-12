# 번호,이름,국어,영어,합계,평균,등수 - 10명의 학생입력공간 생성

# stuSave = [[0]*7 for i in range(0)]
stuSave = []
# print(stuSave)
# 학생가입인원 확인count
sCount = 0

while True:
    print('[ 학생성적프로그램 ]')
    print('-'*25)
    print('1. 학생성적입력') # 완료
    print('2. 학생성적수정') # 완료
    print('3. 학생성적삭제') # 완료
    print('4. 학생성적전체출력') #완료
    print('5. 학생검색출력') #완료
    print('6. 등수처리')    #완료
    print('0. 프로그램종료')     #완료
    print('-'*25)
    # 숫자만 받는데, 문자를 입력하면 에러
    # 숫자만 받도록 변경
    choice = input('원하는 번호를 입력하세요.>>')
    
    # isdigit() 숫자인지아닌지 확인함수
    if not choice.isdigit():  # 숫자
        print('숫자만 입력가능합니다.!!')
        continue
    # int형 변경
    choice = int(choice)
    count=0 #학생검색이 되었는지 체크
    if choice==1:
        print('-- {}번째 학생등록 -- '.format(sCount+1))
        sName = input('학생이름을 입력하세요.>>')
        kor = int(input('국어 점수를 입력하세요.>>'))
        eng = int(input('영어 점수를 입력하세요.>>')) 
        # 리스트 추가
        temp ={'stuno':sCount+1,'stuname':sName,'kor':kor,'eng':eng,\
            'total':kor+eng,'avg':(kor+eng)/2,'rank':0}
        stuSave.append(temp)#딕셔너리를 append
        sCount += 1 #학생인원 count 1증가
        print('학생성적이 저장되었습니다.')
        #print(stuSave)
    
    elif choice==2:
        print('[ 학생성적 수정페이지 ]')
        print('='*50)
        searchName = input('수정할 이름을 검색하세요>>')
        count = 0 #원하는 학생이름이 검색이 되었는지 확인하는 변수
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('{} 학생이 검색되었습니다.'.format(searchName))
                print('점수 수정')
                print('[1.국어점수 수정]')
                print('[2.영어점수 수정]')
                print('[0.상위메뉴로 이동]')
                searchNo=int(input('수정할 과목 번호를 입력하세요>>'))
                
                if searchNo ==1: #국어점수 수정
                    print('현재 국어 점수:',stu['kor'])
                    score = int(input('변경할 국어점수를 입력하세요.>>'))
                    stu['kor'] = score #현재국어점수 = 변경국어점수
                    #합계, 평균 점수 변경
                    stu['total'] =stu['kor']+stu['eng']
                    stu['avg'] =stu['total']/2
                    
                    print('국어점수 변경되었습니다.')
                elif searchNo ==2: #영어점수 수정
                    print('현재 영어 점수:',stu['eng'])
                    scroe = int(input('변경할 영어점수를 입력하세요>>'))
                    stu['eng'] =score #현재영어점수 = 변경영어점수
                    #합계, 평균 점수 변경
                    stu['total'] =stu['kor']+stu['eng']
                    stu['avg'] =stu['total']/2
                elif searchNo ==0: #상위메뉴로 이동
                    print('상위메뉴로 이동합니다.')               
                count=+1 #학생이 검색됨.
                break
                                

        if count ==0:
            print('{}학생이 없습니다.'.format(searchName))                                 
            
    elif choice==3:
        print('학생성적 삭제를 선택하셨습니다.')
        
        searchName = input('이름을 검색하세요>>')
        count = 0
        for i,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('{} 학생이 이 있습니다.'.format(searchName))
                del(stuSave[i])
                print('{}학생이 삭제되었습니다.'.format(searchName))
                count =+1
                break
        if count ==0:
            print('{}학생이 없습니다.'.format(searchName))
            
    elif choice==4:
        print('번호','이름','국어','영어','합계','평균','등수',sep='\t')  
        print('-'*60)
        # [[1,홍길동,100,100,200,100.0,0]]
        for stu in stuSave:
            for k,v in stu.items():
               print('{}\t'.format(v),end='') 
            print() #줄바꿈
            
            
    elif choice ==5:
        print('학생 검색 출력을 선택하셨습니다.')
        print('='*40)
        searchName =input('검색을 원하시는 학생의 이름을 입력하세요>>')
        print('+'*40)
        count =0 #이름이 검색되었는지 확인하는 count
        for idx,stu in enumerate(stuSave):
            if searchName in stu.values():
                print('{}학생의 성적은 다음과 같습니다.'.format(searchName))
                print('='*60)
                print('번호','이름','국어','영어','합계','평균','등수',sep='\t')
                print('-'*60)
                print(stu['stuno'],stu['stuname'],stu['kor'],stu['eng'],stu['total'],stu['avg'],stu['rank'],sep='\t')
                count =1
                break                
            
        if count ==0:
            print('검색에 해당하는 {}학생이 없습니다.'.format(searchName))
    
    elif choice ==6:
        print('등수처리를 선택하셨습니다.')
        for stu in stuSave:
            rcount =1
            for stu2 in stuSave:
                if stu['total'] < stu2['total']: #total점수 비교
                    rcount +=1 #stu2가 더 클 경우에만 1 증가.
            stu['rank'] = rcount  #등수 입력.
        print('등수처리가 완료되었습니다.')
                
    elif choice==0:
        print('프로그램을 종료합니다.')
        break
    