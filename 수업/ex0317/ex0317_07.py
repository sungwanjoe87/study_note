# 주민번호 뒷자리를 입력받아 남자, 여자 출력하시오.
# 7자리가 아니면 다시 받기
#
innum=str('990101-1105555')
print(len(innum))
# while True:
#     innum = input('주민번호를 입력하세요')
#     if len(innum[7:-1])!=7:
#         print('주민번호가 아닙니다. 다시 입력하세요')
#         continue
#     temp = innum[7:-1]
#     if temp=='1'or temp=='3':
#             print('남자입니다.')
#     elif temp=='2'or temp=='4':
#             print('여자입니다.')
        

#문자열 슬라이싱
# str1 = '안녕하세요. 파이썬입니다.'
# print(str1[7:])
# print(str1[2])
#str - len()함수
# alist = [123,45,3456,483,1,50,111,33333,9,1000000]
# numlist = ['짝수','홀수']
# for i in alist:
#         print('{}[{}자리]:{}'.format(i,len(str(i)),numlist[i%2]))




# a = '안녕하세요. 파이썬 수업에 오신 것을 환영합니다.'

# alist = [1,2,3,4,5]
# print(alist[0])

# print(a[0])

# print(a[0:2])

# print(len(a))