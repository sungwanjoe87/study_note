from random import *

count = 1
#num1 = randint(1,45)
# numbers=[]
# for i in range(1,6):
#     number=randint(1,45)
#     numbers.append(number)
numbers=[]
while True:
    
    number=randint(1,45)
    numbers.append(number)
    input1 =int(input('{}번쨰 도전! 숫자를 입력하세요.>>'.format(count)))

    if number==input1:
        print('숫자가 일치합니다.\n입력한 숫자 :{}\n 랜덤숫자 :{}'.format\
            (input1,number))
        break #while문을 빠져나옴. if문에는 break가 없음.
    else:
        print('숫자가 불일치 합니다.\n입력한 숫자 :{}\n' .format\
            (input1,number))
        count += 1
    if count ==10:
        print('{}번째 모두 실패하셨습니다.\n입력한 숫자 :{}\n 랜덤숫자 :{}' .format\
            (count,input1,numbers))
        break