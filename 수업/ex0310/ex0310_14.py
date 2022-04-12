# input1 = int(input('숫자를 입력하세요'))

# if input1>100:
#     print('100보다 큰수를 입력하셨습니다.')
# else:
#     print('100보다 작은수를 입력하셨습니다.')

from random import *

count = 1

num1 = randint(1,45)

while True:
    if count<=5:
        input1 =int(input('{}번쨰 도전! 숫자를 입력하세요.>>'.format(count)))

        if num1==input1:
            print('숫자가 일치합니다.\n입력한 숫자 :{}\n 랜덤숫자 :{}'.format\
                (input1,num1))
            break #while문을 빠져나옴.
        else:
            print('숫자가 불일치 합니다.\n입력한 숫자 :{}\n' .format\
                (num1))
            count += 1
    else:
        print('5번을 실행하였습니다. 프로그램을 종료합니다.')
        print('랜덤숫자 정답 :{}' .format(num1))
        break        