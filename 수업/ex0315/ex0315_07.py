aa =[1,2,3333,4,555,6,77,8,9]
print('1:' ,aa)


bb=aa
#얕은 복사 - 수정은 전혀 불가능하고 주소값만 받아 넣어 놓는다. 타입도 None이다.
aa[0] = 500
print('aa list[aa[0]=500을 넣음]: ', aa)
print('bb list에는 넣지 않음: ', bb)

#aa만 데이터를 추가했지만, 같은 주소를 바라보고 있는 bb도 데이터가 추가된 것 처럼 보인다. 이는 추가가 아니라 주소가 같아서 그렇다.
#깊은 복사, aa와 다른 주소를 가지는 새로운 cc라는 리스트를 만들어 준다.

cc= aa.copy()
print()

# #주소만 복사해서 쓴다.
# bb=aa.sort()
# print('2:' ,bb)

# cc = sorted(aa)
# print('3: ',cc)

# aa[0] = 500

# print('4:', aa)
# print('5:', cc)


#뒤에 리스트를 늘려줌.
# aa.extend([1,2,3])
# print(aa)



# #찾는 데이터의 위치를 알려줌
# idx= aa.index(77)
# print(idx)

# #찾고자 하는 데이터의 갯수를 알려줌
# print(aa.count(6))



# if 77 in aa:
#     print('77이 aa에 있습니다.')

# #앞은 자리 숫자, 뒤는 데이터 , 특정 ((),에 ()를) 넣는다.
# aa.insert(2,3)
# print(aa)

# #제일 뒤에 데이터 추가
# aa.append(44)
# print(aa)

# #역순정렬.
# aa.sort(reverse=True)
# print(aa)


#순차정렬
# aa.sort()
# print(aa)


# #기본적으로 마지막 것을 삭제한다.
# #안에 해당 데이터를 넣으면 해당 데이터를 삭제한다.
# aa.pop()
# print(aa)



#aa리스트에서 3333데이터를 검색해서 해당하는 첫번째 데이터를 삭제
# aa.remove(3333)


# #aa안에 5라는 데이터가 있을시 몽땅 지우는 방법
# for i in range(len(aa)):
#     if 5 in aa:
#         aa.remove(5)
        
# #aa=[] 와 같다.        
# aa.clear

#삭제
# aa[1:4]=[]
# print(aa)

# #1.aa에 빈공간을 덮어 씌우기 타입은 남아있음.
# #리스트인 타입은 살아있음
# aa = []
# print(aa)
# print(type(aa))


# #2.aa라는 변수만 존재하게 함. 타입도 삭제
# #모두 삭제 (타입까지)
# aa = None
# print(aa)
# print(type(aa))

# #3.삭제방법3 aa라는 변수까지도 사라짐.
# del(aa)



