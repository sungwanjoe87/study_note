s=[1, '홍길동']
s.append(100)

#딕셔너리 선언
stu1 ={'stu_no':1,'name':'홍길동','major':'컴퓨터학과'}

#딕셔너리 추가
stu1['tel']='010-0000-0000'



#딕셔너리 삭제 (해당하는 값 삭제)
del(stu1['tel'])

print(stu1['name'])
print(stu1.get('name'))

#get은 에러를 뿌리지 않는다! 프로그램이 다운 되지 않게 하는 것으로 중요.
print(stu1.get('tel'))

#키 값 전체 출력
print(stu1.keys())

#밸류 값 전체 출력
print(stu1.values())
print(type(stu1.values()))

#밸류 값 전체를 리스트로 뽑는다.
print(list(stu1.values()))

#키 값 전체를 리스트로 뽑는다
print(list(stu1.keys()))

#튜플 형태로 뽑는다.
print(stu1.items())

#stu1에 name이 있으면 True를 반환.
print('name' in stu1)

#aa라는 list에 11 데이터가 있는지 확인.
aa=[1,2,3,4,7,11,44,77]
if 11 in aa:
    print('11이 있습니다.')

if 'name' in stu1:
    print('name value 값:' ,stu1['name'])
    print('name 키가 있습니다.')
else:
    print('name 키가 없습니다.')
# print(s)
# print(stu1['major'])
# print(stu1['stu_no'])
# print(stu1)
#stuNo   변수 or stu_no   *낙타봉 방식 or _ 분할 방식.
#stu_No() 함수
#Stu_no   클래스 (개발 약속.)



# stu= [1,'홍길동',100,100,200,100.0,0]
# aa= {'no':1,'name':'홍길동','kor':100,'eng':100,'total':100}
# print(stu[1])
# print(aa['no'])
# aa=[
#     [1,2,3,4]
#     [5,6]
#     [7,8,9]
#     ]
# #print(aa.index(13))
# #13의 주소값

# for a2 in aa:
#     for a in a2:
#         print(a)