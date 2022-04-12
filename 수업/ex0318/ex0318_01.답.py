from random import *
mark_lotto=[i+1 for i in range(45)] #로또 카드 형태를 만드는 리스트
in_num = []     #입력될 칸의 리스트
in_lotto = []   #당첨된 번호
lotto =[]       #당첨번호 리스트
lottonum = [i+1 for i in range(45)] #로또 카드에 번호를 입력하는 리스트 
reward = ['꽝','1천원','5백만원','5천만원','1억원','50억원','100억원'] #상금 출력 리스트

###1.로또당첨번호 생성.
for i in range(500):
    rno = randint(0,44)
    lottonum[0], lottonum[rno] = lottonum[rno], lottonum[0]
lotto = lottonum[:6]


##2.로또번호 입력
for i in range(6):    
    count =0 #45까지 출력되도록 출력하는 변수
    print('[ LOTTO CARD ]')
    for i in range(5):
        for j in range(10):
            if count <45:
                print('{:2s}'.format(str(mark_lotto[10*i+j])),end=' ')
                count+=1
            else:
                break
        print()
    temp=int(input('로또번호를 입력하세요>>'))
    in_num.append(temp) #입력한 숫자 입력리스트에 추가
    mark_lotto[temp-1]='X'
print('입력번호는 {}입니다.'.format(in_num))

    
###3.당첨확인
for num in in_num: #(idex와 데이터 값)
    if num in lotto:
        in_lotto.append(num)
        

print('당첨번호',lotto)
print('당첨 갯수는:{} , 당첨번호:{}'.format(len(in_lotto),in_lotto))
print('당첨금액 :',reward[len(in_lotto)])        


