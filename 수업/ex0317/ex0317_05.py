foods=['떡볶이','짜장면','라면','피자','맥주']
sides=['오뎅','단무지','김치','피클','땅콩']


#복사할 때는 copy 명령어 사용
#1개의 주소값은 foods2와 foods 가 같이 사용함.
# foods2 = foods.copy()
foods2 = foods[:]
foods2[0] = '안팔어'
print(foods)


#튜플형태의 list 타입으로 변경.
#2개의 list를 dic타입으로 변경.
# tulist =list(zip(foods,sides))
# print(type(tulist))
# print(type(dict(tulist)))
# print(dict(tulist))



#리스트에서 min은 최소값을 max는 최대 값을 리턴
# idx = min(len(foods),len(sides))
# for i in range(idx):
#     print(foods[i],':',sides[i])

# if len(foods)<len(sides):
#     idx = len(foods)
# else:
#     idx = len(sides)
# for i in range(idx):
#     print(foods[i]:sides[i])
  


# for foods,sides in zip(foods,sides):
#     print('{}:{}'.format(food,side))

#for문의 종류

# #기본 for 문
# alist = []

# for i in range(0,10):
#     alist.append(i)
    
# print(alist)

# blist = [ i for i in range(0,10)]
# print(blist)

# #1~20까지 3의 배수
# clist= []
# #기본 for문
# for i in range(1,21):
#     if i%3 ==0:
#         clist.append(i)
# print(clist)

# dlist =[i for i in range(1,21) if i%3==0]
# print(dlist)

