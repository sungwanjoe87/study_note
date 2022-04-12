from random import *
# # 0~1이전까지의 랜덤한 숫자를 출력.
# #랜덤함수로 1부터 10까지의 숫자를 출력하는 방법.
# print(int(random()*10)+1) # 0+1<= x <10+1
# #랜덤인트 함수로 1부터 10까지 숫자를 출력하는 방법.
# randint(1,10)

lotto =[i+1 for i in range(0,45)]
# print(lotto)

#자신이 입력한 6개의 숫자와 자동 로또당첨번호 6개를 비교해서 몇개를 맞췄는지 출력하는 프로그램.
#당첨번호 : 6개 (나오게)
#입력한번호 : 6개 (나오게)
#당첨갯수 : X개 (당첨과 입력번호 맞은거 숫자)
#당첨번호는 : 0
#당첨금액은 @

#6개 모두 100억
#5개 50억
#4개 1억
count =0 #6자리 제한사항
lcount =0 #맞을때 마다 올라가는 숫자 (맞은 숫자)
lotto =[] #로또 번호
inputNum=[] #내가 넣은 번호
Cnum =[]
while True:
    if count <=5:
        temp = randrange(0,45)
        if temp not in lotto:
            lotto.append(temp)
            count +=1
    else:
        print('{}개의 숫자가 생성되었습니다.'.format(count))
        break
#print(lotto) #로또번호를 6개 받음. (확인체크)

for i in range(6):
    a = int(input("{}번째숫자를 입력하세요>>" .format(i+1))) #i+1번째 숫자를 {}안에
    a = int(input('{}번째 입력한 번호는 {}입니다.'.format(i+1,a)))
    inputNum.append(a)
print('입력번호는:',inputNum)

for i in range(6): #맞는 번호를 확인하는 방법.
    if inputNum in lotto:
        lcount +=1
        Cnum.append(inputNum)
    

lotto.sort()
print('당첨번호는 {} 입니다.'.format(lotto))
print('맞은 갯수는 {}개 입니다.' .format(lcount))
print('맞은 숫자는 {} 입니다.' .format(Cnum))

while True: #lcount 숫자에 따라 당첨금 출력.
    if lcount ==6:
        print('당첨금은 100억 입니다.')
    elif lcount ==5:
        print('당첨금은 50억 입니다.')
    elif lcount ==4:
        print('당첨금은 1억 입니다.')
    elif lcount ==3:
        print('당첨금은 5000만원 입니다.')
    elif lcount ==2:
        print('당첨금은 500만원 입니다.')
    elif lcount ==1:
        print('당첨금은 1천원 입니다.')
    else:
        print('꽝입니다!')
        break

randNum = []

for i in range(45):
    randNum.append(i+1)
    
for i in range(500):
    rno = randint(1,46)
    randNum[0], randNum[rno] = randNum[rno], randNum[0]
    

arrs =[]

for i in range(0,6):
    arr2 = [randNum[5*i+j] for j in range(0,6)]
    arrs.append(arr2)

print(arrs)

while True:
    
    
    for arr in arrs:
        for a in arr:
            print('{:2s}'.format(str(a)),end='   ')
        print()
        
        
    input1 = int(input('1~25 중 맞은 숫자를 입력하세요.'))
    
    for i,arr in enumerate(arrs):
        if input1 in arr:
            arrs[i][arr.index(input1)]='X'


# shuffle(lotto)
# print(lotto)
# print(sample(lotto,6))


# for i in range(500):
#     rno = randint(0,44)
#     lotto[0],lotto[rno]=lotto[rno],lotto[0]

# print(lotto[0:6])


# count=0
# lottonum = []
# while True:
#     if count<6:
#         rno = randint(0,44)
#         if not lotto[rno] in lottonum:
#             lottonum.append(lotto[rno])
#         count +=1
#     else:
#         break
# print(lottonum)
# lotto =[i+1 for i in range(0,45)]
# print(lotto)

# lotto1 = range(1,46)
# print(list(lotto))
# print(type(lotto1))