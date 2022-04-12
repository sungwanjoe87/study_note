#lotto 리스트에 6개의 랜덤 숫자를 넣으시오.
#중복 제거
#숫자 6개를 입력 받으세요.

from random import *

lotto_my_List = []
lotto = []


for i in range(6):
    a= int(input("숫자를 넣으세요>>"))
    lotto_my_List.append(a)
print(lotto_my_List)

for i in range(6):
    b = randint(1,45)
    while b in lotto:
        b= randint(1,45)
    lotto.append(b)
    
print(lotto)