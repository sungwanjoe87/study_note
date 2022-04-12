list1 = ['주바다','공유진','김샛별','송선유','양홍욱','윤상운','이한구']

while True:
    search = input('이름을 입력하세요>>')
    if search in list1:
        print('출석했습니다.')
    else:
        print('출석 전 입니다.')






# list1 = [i for i in range(0,10)]
# #list1 은 list타입.
# print (type(list1))

# for i in range(0,10):
#     print(i) # i는 int형
#     print(type(i))


# idx = 1
# list1 = ['주바다','공유진','김샛별','송선유','양홍욱']
# for idx,i in enumerate(list1):  #이뮬레이트 사용
#     print('{}.{}' .format(idx+1,i))
    
# for i in list1:  #인덱스 방법
#     print('{}.{}' .format(idx,i))
#     idx+=1

# for i in range(len(list1)):
    # print('{}.{}' .format(i+1,list1[i]))
    


# 구구단
# print('[1단] \t[2단] \t[3단]\t[4단]\t[5단]\t[6단]\t[7단]\t[8단]\t[9단]')
# for p in range(2,10):
#     print('[{:4d}단  ]'.format(p),end='   ')
# print()
# for i in range(1,10): #단부분 1번째 for문은 단부분
#     for j in range(2,10): #뒷 부분에 해당
#         print ('{} X {} = {:2d}' .format(j,i, i*j), end='   ')
#     print()