from random import *

#rendNum=[i+1 for i in range(25)]
#rendNum=[1,2,3,4......25] 같음

randNum=[]

for i in range(25):
    randNum.append(i+1)
print('섞기 전 리스트 :',randNum)
#rendNum=[1,2,3,4......25] 입력

#랜덤 섞기
for i in range(500):
    rno = randint(0,24)
    randNum[0],randNum[rno] = randNum[rno],randNum[0]
    

arrs = []
#randNum에 있는 데이터를 arrs에 list를 만들어 추가
for i in range(0,5):
    # i = 0,1,2,3,4 j=0,1,2,3,4
    arr2 = [randNum[5*i+j] for j in range(0,5)]    
    #i = 0
    arrs.append(arr2)
#2차원리스트에 1부터~25까지의 숫자를 입력.
# for i in range(0,5): #0,1,2,3,4   
#     #5*0,1,2,3,4     1,2,3,4,5
#     arr2=[5*i+j for j in range(1,6)]
#     arrs.append(arr2)  
# print(arrs)


# #0으로 채워진 5*5의 배열을 생성하시오.
while True:

    for arr in arrs:
        for a in arr:
            print('{:2s}' .format(str(a)), end='   ')
        print()


    # print('1부터 25의 숫자를 입력하세요.>>')
    input1 =int(input('1~25중 X를 넣기 원하는 자리의 숫자를 넣으세요>>'))
    #input1에 받은 숫자에 X가 나타나도록 입력되도록 구현

        
    for i,arr in enumerate(arrs):
        if input1 in arr:
            #[1,2,3,4,5] 3의 자리를 찾는 것은 arr,index(3) ->2
            arrs[i][arr.index(input1)]='X'

        print(arrs)
        break
        
    
    
               
# list1 = []
# for i in range(5):
#     list2=[0 for j in range(1,6)]
#     list1.append(list2)
# print(list1)