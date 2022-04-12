#프로그램 할때의 순서식을 세워라.
#1.웹 스크래핑
#2.네이버에서 주식 정보
#3.가지고 옴.
#4.데이터 분석
#2.그래프의 형태로 추출한다.
#와 같은 일련의 순서도

#리스트 생성 #리스트에 1부터 25까지 있는 숫자 입력.
from random import * #랜덤 함수 가지고 오기
randNum = [i+1 for i in range(25)]

#print(randNum) ->확인

#랜덤 섞기.
for i in range(200):
    rno = randrange(0,25) #randint(0,24)
    randNum[0], randNum[rno] = randNum[rno], randNum[0]
#print(randNum)->확인

#1차원 배열 리스트 생성arrs = []
#2차원리스트에 추가
arrs= []
for i in range(0,5):
    #arr2 = [5*i+j for j in range(1,6)] #순차로 넣고 싶을때
    arr2 = [randNum[5*i+j] for j in range(0,5)]
    arrs.append(arr2)
#print(arrs) ->확인
    

#2차원에 출력.
#무한 루프에 2차원 배열 출력하여 
while True:
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end='   ')
        print()


    print('-'*40)
    
#원하는 숫자를 입력 받고
    input1 = int(input('1~25중 원하는 값을 입력하세요>>(프로그램 종료시는 0 입력)'))
    
#0이 입력되면 프로그램을 종료    
    if input1 ==0:
        print('프로그램 종료')
        break
    
#arrs 안에 있는 arr안의 input1의 데이터 주소 값을 X로 변경.
    for i,arr in enumerate(arrs):
        if input1 in arr:
            arrs[i][arr.index(input1)]='X'
    