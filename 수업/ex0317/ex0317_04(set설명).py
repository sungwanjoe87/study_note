

#3.set에 추가, 삭제

# myset = {1,2,3}
# myset.add(4)
# #삭제
# print(myset)
# myset.remove(2)
# print(myset)
# #세트 완전 삭제
# myset.clear

#4.set 2개를 합집합. 교집합, 차집합, 대칭집합

adic = {1,2,3,4,5}
bdic = {3,4,5,6,7}

print (adic|bdic)#합집합
print (adic&bdic)#교집합
print (adic-bdic)#차집합 a것만
print (bdic-adic)#차집합 b것만
print (adic^bdic)#교집합 빼고 대칭집합

#set은 key만 가지고 있는 딕셔너리 이다.
#set은 디폴트 값으로 중복되는 값을 자동으로 없애준다.
#set은 정렬도 자동으로 한다.
# myset = {1,2,3,4,5,5}
# #세트는 중복 값은 무조건 없어짐 (디폴트)
# print(myset)

# mylist = [9,12,3,4,4,5,5,1,2,6,7,8]
# #리스트를 세트로 타입변경
# myset = set(mylist)
# print(myset)
# #리스트로 타입 변경.
# mylist = list(myset)
# print(mylist)




# saleList = ['삼각김밥', '바나나', '도시락', '삼각김밥', '도시락','오뎅', '바나나']
# print(type(set(saleList)))
# saledic =set(saleList)

# a={1,2,4}



# zipcode1 = {66012,66017,660075,66013,66019}#10만개
# zipcode2 = {66012,66017,660075,66015,66018} #10만개

# print(zipcode1 | zipcode2)

# numdic ={1,2,33,3,3,5,1,9,2,3}
# numdic2 ={2,3,4,5,2,3,9,10,11,13}
# print('numdic:',numdic)
# print('numdic2:',numdic2)
# print('numdic | numdic2(합집합):', numdic | numdic2)
# print('numdic & numdic2(교집합):',numdic & numdic2)
# print('numdic - numdic2(1-2차집합):', numdic - numdic2)
# print('numdic2 - numdic(2-1차집합):', numdic2 - numdic)

# adic = {1:'aaa',2:'bbb',3:'ccc',1:'ddd'}
# print(adic)




# nlist1 = [1,2,5,4,8]
# nlist2 = [3,4,5,8,2]
# print(nlist1+nlist2)

# count = 0 



# #정렬

# tdic = {'pig':'돼지','tiger':'호랑이','lion':'사자','dog':'개'}
# print(tdic)
# dtuple = list(tdic.items())

# #소트 된 것은 아직 list.
# dtuple.sort()


# print(dict(dtuple))