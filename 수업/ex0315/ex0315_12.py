from random import *


#1.리스트 생성
randNum = []
#2.리스트에 1-25까지 입력
for i in range(25):
    randNum.append(i+1)

print('섞기 전 리스트: ', randNum)


#3.랜덤 섞기
for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno] = randNum[rno], randNum[0]
print('섞은 후 리스트 : ',randNum)

arrs = []
#4. randNum에 있는 데이터를 arrs에 list를 만들어 추가
for i in range(0,5):
    arr2 = [randNum[5*i+j] for j in range(0,5)]
    arrs.append(arr2)
    
while True:
    for arr in arrs:
        for a in arr:
            print('{:2s}' .format(str(a)),end=' ')
        print()
    #원하는 숫자를 input1에 입력.
    input1 = int(input('1~25중 원하는 숫자를 입력하시오>>'))
    
    for i,arr in enumerate(arrs):
        if input1 in arr:
            arr[i][arr.index(input1)]='X'
        
