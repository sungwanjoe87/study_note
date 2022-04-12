from random import *

randNum =[]


for i in range(25):
    randNum.append(i+1)
    
    
for i in range(500):
    rno = randint(0,24)
    randNum[0], randNum[rno] = randNum[rno], randNum[0]
    
    
arrs= []

for i in range(0,5):
    temparr = [randNum[5*i+j] for j in range(0,5)]
    arrs.append(temparr)
    
    
    
while True:
    
    
    for arr in arrs:
        for a in arr:
            print('{:2s}' .format(str(a)), end='   ')
        print()
    
    input1 = int(input('1~25숫자 중 빙고가 된 숫자를 입력하세요>>'))
    
        
    for i,arr in enumerate(arrs):
        if input1 in arr:
            arrs[i][arr.index(input1)]='X'