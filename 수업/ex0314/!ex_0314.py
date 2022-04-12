from random import*

my_num = []
lotto = []
ok_num = []
count = 0
lcount = 0

for i in range(6):
    a= int(input('{}번째 숫자를 입력하세요.' .format(i+1)))
    my_num.append(a)
    

while True:
    if count <= 5:
        temp = randint(1,45)
        if temp not in lotto:
            lotto.append(temp)
            count +=1
    else:
        print('{}개의 숫자가 뽑혔습니다.' .format(count))
        break
    
for i in range(6):
    if my_num[i] in lotto:
        ok_num.append(my_num[i])
        lcount += 1
        
print('내가 뽑은 숫자:', my_num)
lotto.sort()
print('이번 로또 번호:', lotto)
print('내가 맟춘 번호 갯수:', lcount)
print('내가 맟춘 숫자:', ok_num)


        