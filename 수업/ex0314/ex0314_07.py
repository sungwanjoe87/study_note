from random import *
#1,100까지의 랜덤숫자 생성
#정답이 출력될때, 지금까지 입력한 숫자를 출력하세요.
my_num = []
temp = randint(1,100)
count = 0
while count <3:
    input1 = int(input('1-100까지의 원하는 번호를 입력하세요>>'))

    if temp == input1:
            print('정답입니다. 정답수자는: {}' .format(input1))
            break
    elif temp>=input1:
            print('입력한 {}숫자가 보다 작습니다. 더 큰수를 입력하세요' .format(input1))
    else:
            print('입력한 {}숫자가 더 큽니다. 작은 수를 입력하세요'.format(input1))
    count +=1
    my_num.append(input1)
    
    if count==3:
        print('{}번째 까지 입력하셨습니다. 모두 틀렸습니다. 맞는 숫자는 {}였습니다.' .format(count,temp))
        my_num.sort(reverse=True)
        print('입력했던 숫자는:', (my_num))