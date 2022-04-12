# a = 1
# b = 2
# c = a


# a = 2

# print (a,b,c)



# a = [1]
# b = [2]
# c = a #주소가 복사 된다.

# print(a,b,c)

# a[0] = 10
# print(a)
# print(c)
#깊은 복사 (새로운 공간을 만들어서 생성)
list1 = [[0]*2 for _ in range(5)]
#[[0]*2]*5 (얕은 복사 동일한 공산을 만들어서 생성)
tno=0
while True:
    print(list1)
    if tno<len(list1):
        no1 = int(input('첫번째 수를 입력하세요>>'))
        no2 = int(input('두번째 수를 입력하세요>>'))
        list1[tno][0] = no1
        print()
                
    