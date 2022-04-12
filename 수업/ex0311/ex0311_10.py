#리스트 1,45 까지의 숫자를 집어넣어보세요.
from random import *
numbers = []
# for i in range(1,46):
#     numbers.append(i)
# print(numbers)


#lotto 번호 부여 1~45
numbers[0] = numbers[range(0,46)]
#lotto 번호 섞음
for i in range(500):
    ran_num =randint(0,44)
    numbers[0],numbers[ran_num] = numbers[ran_num],numbers[0]

print(numbers)


# numbers2 = [i for i in range(1,46)]
# print(numbers2)

