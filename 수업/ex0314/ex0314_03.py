#1부터100까지 있는 상태에서 홀수만 출력하시오.

# ch = 0


# while ch <=100:
#     if ch%2==1:
#         print(ch)
    
#     ch += 1 #증감식이 if 밖으로 while에 걸리도록 빼야 한다.
i=1

while i<=9:
    if i%3==0:
        i +=1
        continue #break:해당 반복문 완전히 빠져나옴, continue:한번만 빠져나옴.
    print('2 * {}= {} ' .format(i,i*2))
    i +=1