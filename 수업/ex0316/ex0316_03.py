aa=[1,'홍길동',100,100,200,100.0,0]

for i in range(len(aa)):
    print('{} : {} '.format(i,aa[i]))
    print(type(aa))

stu1 = {'no':1, 'name':'홍길동', 'kor': 100, 'eng': 100, 'total':200,\
    'avg':100.0, 'rank':0}

#딕셔너리 전체 출력 for문
for key in stu1:
    print('{} : {}'.format (key,stu1[key]))
    print(type(stu1))


# while True:
#     search = input('키 값을 입력하세요>>')
#     
#     if search in stu1:
#         print(stu1[search])
#     else:
#         print('키 값이 없습니다. 다시 입력하세요>>')
#         print()

